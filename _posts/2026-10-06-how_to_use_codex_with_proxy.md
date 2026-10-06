---
layout: post
title: "工具-Codex 对接第三方中转配置指南"
lang: zh-CN
date: 2026-10-06
author: pepper
tags: [codex, openai, api, tool]
comments: true
toc: true
pinned: false
---

记录从 401 到跑通：记一次让 Codex 对接第三方中转的全过程

> 折腾了整整两天，踩遍了几类典型坑，最后通过本地协议代理彻底解决。这篇博客完整复盘整个过程，希望能帮到同样被 Codex 的 `wire_api = "responses"` 卡住的人。

<!-- more -->

## 一、背景：为什么 Codex 这么难伺候

OpenAI 的 Codex 客户端（桌面版）和我们平时用的 API 客户端有个本质区别：**它底层硬编码强制走 `/v1/responses` 协议**（WebSocket 长连接），而不是传统的 `/v1/chat/completions`。

这带来两个连锁影响：

1. `config.toml` 里的 `wire_api` 字段**只允许填 `responses`**，填其他值直接报配置解析错误：
   
   ```
   unknown variant `chat_completions`, expected `responses`
   ```
2. 大量第三方中转服务商只实现了老的 `chat/completions` 接口，根本不认 Codex 发出的 Responses 请求体。

这两点叠加，就注定了 Codex 不能像普通客户端那样"填个中转地址就完事"。

## 二、踩坑实录：一步步定位问题

### 坑 1：YAML 类型校验 —— `disable_response_storage` 要字符串

最开始创建任务就报错：
```
invalid configuration: invalid type: boolean `true`, expected a string
```
<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062108495.png" alt="image-20261006210807302" style="zoom:50%;" />

原因是 `disable_response_storage` 这个字段在 schema 里要求**字符串类型**，但 YAML 里写 `true` 会被解析成布尔值。修复方式是加引号：

```toml
shell_environment_policy.set.disable_response_storage = "true"
```

> 这个字段只在 `wire_api = "responses"` 时才生效，后来我改用协议代理后，这个配置直接不再参与请求，问题自然消失🥹。

### 坑 2：401 invalid_api_key —— 鉴权方式不匹配

接着遇到经典报错：
```
401 Unauthorized: Incorrect API key provided
auth error code: invalid_api_key
```

一开始我以为只是密钥失效，重新生成、检查空格、测试 base_url……折腾半天。直到我直接用 curl 测试上游才发现真相：

```bash
curl https://us.gpt.ge/v1/models -H "Authorization: Bearer sk-xxx"
# 返回：{"error":{"message":"未提供令牌"}}
```

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062110262.png" alt="image-20261006211013214" style="zoom:50%;" />

关键点浮出水面：

- **`us.gpt.ge` 这个服务商根本不读 `Authorization: Bearer` 头**
- 它要的是自定义请求头 `V-API-Key`
- 但 Codex 的 responses 模式**只发标准 Bearer 鉴权**，没法直接指定自定义头

换句话说：**上游鉴权方式和 Codex 的鉴权方式不兼容**，即使密钥完全正确也过不了。

### 坑 3：协议不匹配 —— 强制 responses 是硬约束

我还试过把 `wire_api` 改成 `chat_completions`，结果直接炸配置。这也彻底确认了一件事：**当前版本 Codex 只支持 responses，无法在配置层面绕过。**

## 三、破局：用 CC-Switch 做本地协议代理

既然 Codex 改不了、上游也不兼容，那就**在中间加一层翻译**。

### 链路设计

```
Codex（发 /v1/responses，Bearer 鉴权）
      ↓
CC-Switch（本地代理，端口 15721）
      ↓ ① 协议转换：Responses → Chat Completions
      ↓ ② 鉴权替换：Bearer → V-API-Key
      ↓
us.gpt.ge（/v1/chat/completions，V-API-Key 鉴权）
```

### 部署步骤

**1. 安装 CC-Switch**

macOS 用 Homebrew 一键安装：
```bash
brew install --cask cc-switch
```
启动后，确认打开了【本地路由接管】总开关。

**2. 在 CC-Switch 添加供应商**

- 供应商类型：**自定义 OpenAI 兼容**（注意别选 Anthropic 系列）

  <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062113806.png" alt="image-20261006211317776" style="zoom:50%;" />

- API 请求地址：`https://us.gpt.ge/v1`（**必须带 `/v1`**，也可以自己选择其他请求地址，这个有免费0.5元测试🤪我要是能收它广告费就好了）

- 上游协议：**Chat Completions**（这是协议转换的开关❣️【重要】高级选项）

  <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062115980.png" alt="image-20261006211500935" style="zoom:50%;" />

- Header 覆盖配置成：
  ```json
  { "V-API-Key": "${apiKey}" }
  ```
  `${apiKey}` 是 CC-Switch 内置变量，自动引用表单里填的密钥，用来替换掉默认的 Bearer 头。
  
  <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062116445.png" alt="image-20261006211634354" style="zoom:50%;" />
  
- 模型映射：添加 `gpt-5.1`（和 Codex 配置一致）

**3. 修改 Codex 的 config.toml**

把上游指向本地代理：
```toml
[model_providers.vapi]
name = "VAPI"
base_url = "http://127.0.0.1:15721/v1"
wire_api = "responses"          # 保留不动，Codex 硬性要求
query_params = {}
request_max_retries = 3
stream_max_retries = 6
```

Codex 界面里 API Key 随便填个占位字符串即可，真正鉴权由 CC-Switch 完成。

**4. 验证链路**

先测本地代理连通性：
```bash
curl http://127.0.0.1:15721/v1/models -H "Authorization: Bearer dummy"
```
返回模型列表（哪怕 `{"models":[]}` 也代表端口通了）。再用一次完整对话请求验证：

```bash
curl http://127.0.0.1:15721/v1/responses \
  -H "Authorization: Bearer dummy" \
  -X POST -H "Content-Type: application/json" \
  -d '{"model":"gpt-5.1","input":"你好"}'
```

能返回文字即整条链路跑通。

## 四、过程中那些容易卡住的细节

**1. 端口对不上**
CC-Switch 默认本地服务地址是 `http://127.0.0.1:15721`，我一度用错端口导致 `Connection refused`。记住：Codex 的 base_url 和 CC-Switch 的服务端口必须完全一致。

**2. 「需要路由」≠「路由已启动」**
CC-Switch 里每个供应商要**单独点击小火箭图标启动路由**，不是加完供应商就自动监听端口。没启动路由，端口不会打开，curl 直接拒绝连接。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062118855.png" alt="image-20261006211811807" style="zoom: 33%;" />

**3. 模型名要对上**
`gpt-5.1` 是服务商自定义的模型代号，必须和上游平台实际支持的模型名一致，否则上游会报模型不存在。

**4. 冗余参数要清理**
Codex 默认会带上 `model_reasoning_effort`、`model_max_output_tokens` 等 Responses 专属参数，很多中转服务商不识别，会直接报 400。建议在 Codex 配置里注释掉这些参数。

## 五、写在最后

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062120189.png" alt="image-20261006212025137" style="zoom:35%;" />

这次排错最大的收获是理解了一个通用思路：**当"客户端协议"和"上游服务能力"不匹配，又无法改任何一方时，引入一层本地代理做协议转换是最干净的解法。**

CC-Switch 的价值正在于此——它不只是个"中转"工具，更像一个协议翻译器，让只认 Responses 的 Codex 也能吃上各种 chat/completions 中转服务。

整个排查链路可以浓缩成一句话：**401 未必是密钥错，先确认鉴权头是否匹配；连不上先看端口和路由是否真正启动；协议不合，就让代理在中间翻译。**

---

*如果你也遇到 Codex 对接中转服务卡在 401 / 协议不兼容，希望这篇记录能帮你少走一些弯路。*

---

参考资料：
知乎1: https://zhuanlan.zhihu.com/p/2057392064011276681

中转1: https://gpt.ge/panel/log

![image-20261006212236415](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062122462.png)

中转2: https://doc.openlux.ai/



ps： 博主的mac OS是12.10的就系统，甚至codex的版本是 26.715.72359，之前忘记是通过啥操作安转的了，不然总让我升级MacOS-13。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202610062157949.png" alt="image-20261006215712836" style="zoom:50%;" />
