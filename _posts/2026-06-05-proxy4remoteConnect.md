---
layout: post
title: "开发-远程的codex无法使用代理"
date: 2026-06-04
author: pepper
tags: [ssh, ai]
comments: true
toc: true
pinned: false
---

在 Remote-SSH 远程开发环境下，AI 插件（如 Codex、Copilot）经常会出现网络超时、无法登录或流式对话中断的问题。 很多人一看到 `token_exchange_failed` 或 `stream disconnected`，第一反应是账号被封了或者 Plus 权限过期。但本质上，这往往是一个由于 **本地与远程混用 `127.0.0.1` 代理端口** 导致的典型“网络鬼打墙”事件。

<!-- more -->

## 🔍 问题核心：127.0.0.1 的“相对论”

在 VS Code Remote-SSH 架构中，本机和远程服务器是两个完全独立的网络环境，但它们很容易在配置中被混淆：

- **A 电脑（本地 Windows/Mac）**：`127.0.0.1` 指向 A 本机，Clash 端口为 `:7897`。
- **B 电脑（远程 Ubuntu 宿主机）**：`127.0.0.1` 指向 B 服务器自身，Clash 端口为 `:22545`。

### 为什么会挂掉？

当 A 本机的 VS Code 设置里配置了全局代理：

```json
"http.proxy": "[http://127.0.0.1:7897](http://127.0.0.1:7897)"
```

这个设置被 Remote-SSH 自动继承到了远程 VS Code Server 上。结果跑在 B 机器上的 Codex 插件在请求网络时，也去连接 `127.0.0.1:7897`。然而，**B 机器的 7897 端口根本没有代理服务在监听**，网络请求直接撞墙。

## 🚨 报错表现

网络环境不一致在不同阶段会表现为不同的错误：

1. **登录阶段（Auth 失败）** A 本机 CLI 登录成功了，但 Remote-SSH 下的 Codex 跑在 B 的环境里，找不到凭证，且网络不通，报错：

   ```
   token_exchange_failed
   [https://auth.openai.com/oauth/token](https://auth.openai.com/oauth/token)
   ```

2. **对话阶段（Stream 断开）** 即使在 B 上完成了登录（生成了 `/root/.codex/auth.json`），一旦开始对话，流式传输会瞬间卡死：

   ```
   stream disconnected before completion
   [https://chatgpt.com/backend-api/codex/responses](https://chatgpt.com/backend-api/codex/responses)
   ```

## 🛠 终极修复与配置方案

要彻底解决这个问题，必须做到**双端环境完全隔离**。以下是针对 **A端端口 `7897`**、**B端端口 `22545`** 的完整配置方案。

### 1\. A 电脑（本地）配置

首先修A电脑上的clash配置，修改其代理端口为`22545`,实现统一。然后，打开 A 本地的 `settings.json`（快捷键 `Ctrl+Shift+P` -\> `Open User Settings (JSON)`），利用 VS Code 的远程覆盖机制`override`进行隔离：

```
{
    // A 本地自身及本地扩展使用的代理
    "http.proxy": "http://127.0.0.1:22545",

    // 关闭全局代理支持的错误继承，防止本地代理盲目应用到远程
    "http.proxySupport": "override",

    "remote.SSH.settings": {
        "http.proxy": "http://127.0.0.1:22545"
    }
}
```

### 2\. 远程 B 机器配置

为了防止某些底层依赖绕过 VS Code 代理，我们需要在**编辑器层**和**系统底层**同时打通 `22545` 端口。

#### 💡 第一层：远程 VS Code Server 配置

连接到远程后，打开远程设置（`Ctrl+Shift+P` -\> `Open Remote Settings (JSON)`），确保覆盖生效：

```
{
    "http.proxy": "http://127.0.0.1:22545",
    "http.proxySupport": "override",
    "http.proxyStrictSSL": true
}
```

#### 💡 第二层：远程 Ubuntu 系统环境变量 (`~/.bashrc`)

由于 Codex 实际跑在 B 的 root（或指定用户）环境下，登录远程终端，修改环境变量：

```
nano ~/.bashrc
```

在文件末尾追加以下内容：

```
# 代理配置
export HTTP_PROXY = http://127.0.0.1:22545
export HTTPS_PROXY = http://127.0.0.1:22545
export ALL_PROXY = http://127.0.0.1:22545
# 过滤本地回环与局域网，防止内部通信被误代理
export NO_PROXY=localhost,127.0.0.1,::1

```

保存退出后，执行命令使其立即生效：

```
source ~/.bashrc
```

## ✅ 结果验证

在远程 B 机器的终端执行以下命令，测试代理是否彻底打通：

```
curl -I https://chatgpt.com
```

如果返回 `HTTP/2 200`，说明 B 机器的网络链路已经完全正常。此时重启一下远程 VS Code 窗口，Codex 的登录和流式对话即可纵享丝滑。

> **🎯 一句话总结**： 别盲目重装插件或折腾账号，Remote-SSH 场景下，**把 A 和 B 的代理端口隔离开**才是解题的核心。

## 注意事项总结：

1. override 模式
2. 统一代理端口一致
3. 配置ubuntu的系统配置，`#过滤本地回环与局域网，防止内部通信被误代理 export NO_PROXY=localhost,127.0.0.1,::1`
