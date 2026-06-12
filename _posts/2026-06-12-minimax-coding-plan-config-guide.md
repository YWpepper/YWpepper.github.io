---
layout: post
title: "MiniMax Coding Plan 配置操作指南"
date: 2026-06-12
author: pepper
tags: [tool]
comments: true
toc: true
pinned: false
---

这篇博客介绍了 MiniMax Coding Plan 的配置在vscode copilot 里的操作指南。

<!-- more -->

## 概述

MiniMax Coding Plan 是 MiniMax 提供的一项编程辅助服务，旨在帮助开发者更高效地进行代码编写和调试。本指南将详细介绍如何配置和使用该服务。

## 配置步骤

### 🤖 Assistant

在配置 MiniMax **Coding Plan**（编程订阅套餐，非普通按量付费）时，有一个至关重要的底层逻辑：**MiniMax 的 Coding Plan 秘钥原生走的是 Anthropic 兼容协议（提供 M3 / M2.7 等模型且支持 thinking 思维链展示）**。
因此，如果你在 VS Code 中直接修改内置的 `chatLanguageModels.json` 用 `chat-completions`（OpenAI协议）强行调用，会导致额度扣除异常、404 或者无法展示思考过程。
目前在 VS Code 的 Copilot 聊天框架中完美配置并使用 MiniMax Coding Plan，主要有两种业界标准方法：

### 方法一：使用 VS Code 专属扩展（推荐，最完美）

VS Code 插件市场中已经有开发者专门针对 **GitHub Copilot + MiniMax Coding Plan** 开发了语言模型桥接扩展，比如 **MiniMax (coding)** 或 **Minimax VScode Copilot**。

#### 1. 安装扩展

在 VS Code 插件市场搜索并安装：

- **MiniMax (coding)** (作者: Denizhan Dakılır)

#### 2. 配置专属 API Key

1. 登录 MiniMax 开放平台，进入 **Coding Plan** 页面，复制以 `sk-` 开头的 **Coding Plan 专属秘钥**（注意：不是普通 API 的 Key）。
2. 在 VS Code 中按下 `Ctrl + Shift + P`（Mac: `Cmd + Shift + P`）打开命令面板。
3. 输入并选择 `MiniMax: Set API Key`（或类似命令），将你的 Coding Plan 秘钥粘贴进去。

#### 3. 切换模型

打开 VS Code 的 **Copilot Chat（聊天面板）**，点击输入框上方的**模型下拉选择器**，你会直接看到 `MiniMax-M3` 或 `MiniMax 2.7`。选中它，Copilot 就会直接走你的 Coding Plan 5小时限次额度，并且支持原生的 `thinking` 思考块输出。

### 方法二：通过内置 `chatLanguageModels.json` 强行配置

1. 首先在copilot添加自定义的模型

![](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260612103149833.png)

2. 配置的信息主要是key token，配置完之后就打开 `chatLanguageModels.json` 文件，添加如下配置：
   ![](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260612102922850.png)

如果你不想安装第三方插件，执意通过 VS Code 内置的 `customendpoint` 覆盖（即你前几次提问尝试的方法），请注意：**MiniMax 国际站和国内站的网关在 Coding Plan 下极为挑剔**。
由于国内站限制，如果你在**中国大陆**使用，必须通过其 Anthropic 兼容网关，且协议必须是 `messages`。
请按下 `Ctrl + Shift + P` 打开 `Preferences: Open User Settings (JSON)`，找到或新建 `chatLanguageModels.json` 块，**严格按照以下格式修改**：

```json
[
  {
    "name": "Copilot",
    "vendor": "copilot",
    "settings": {
      "gpt-5-mini": {
        "reasoningEffort": "low"
      }
    }
  },
  {
    "name": "minimax-coding",
    "vendor": "customendpoint",
    "apiKey": "${input:chat.lm.secret.c3262}",
    "apiType": "messages",
    "models": [
      {
        "id": "MiniMax-M3",
        "name": "MiniMax M3",
        "url": "https://api.minimaxi.com/anthropic",
        "toolCalling": true,
        "vision": true,
        "maxInputTokens": 128000,
        "maxOutputTokens": 16000
      }
    ]
  }
]
```

⚠️ 重点避坑注意：URL 必须精准：如果你在国内，用 [https://api.minimaxi.com/anthropic](https://api.minimaxi.com/anthropic)；如果在海外，用 [https://api.minimax.io/anthropic](https://api.minimax.io/anthropic)。不要在尾部加 /v1 或 /v1/messages，因为 VS Code 当 apiType 为 "messages" 时，会自动隐式拼接路由，多加会导致 404。密码存储：${input:chat.lm.secret.c3262} 对应的这个 Secret 变量里，必须确保你存入的是 Coding Plan 控制台里生成的 Key。

### 💡 为什么首推方法一（装插件）？

因为 VS Code 的内置 `customendpoint` 功能对 Anthropic 协议（`messages` 类型）的兼容性经常随着 VS Code 版本的更新而变化，容易产生由于路径拼接导致的 `404 page not found` 或非标协议报错。
而专用的桥接插件会帮你在本地把 Copilot 的请求精准转换为 MiniMax Coding Plan 所需的格式，用起来最稳定。
