---
layout: post
title: '开发-十一月Bug排查记录'
date: 2025-11-11
author: pepper
tags: [bug, springboot]
comments: true
toc: true
pinned: false
---

记录11月有价值的bug。
<!-- more -->
### 语雀的图片

语雀的图片在 GitHub 页面上无法显示的原因主要有以下几点：

1. 跨域（CORS）限制 🔒
语雀的图片服务器配置了 CORS 策略，限制了来自其他域名（如 GitHub Pages）的访问请求。浏览器出于安全考虑会阻止这些跨域请求。

2. 防盗链机制 🛡️
语雀可能实施了防盗链措施，检查 HTTP 请求头中的 Referer 字段。当从 GitHub Pages 访问图片时，Referer 不是语雺域名，请求会被拒绝。

3. 域名白名单 ✅
语雀的服务器只允许特定域名访问其资源，GitHub Pages 的域名不在白名单中。

方案一：下载图片到本地仓库（推荐）

方案二：使用图片代理服务，使用免费的图片代理服务绕过限制：

```bash
<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/..." width="70%">
```

方案三：使用 GitHub 提供的 CDN

```bash
<img src="https://raw.githubusercontent.com/YWpepper/HomePage/master/images/image-name.png" width="70%">
```
### github加速镜像


下载的 Release 文件（二进制压缩包），应主要使用“GitHub 文件加速”或“GitHub Proxy”服务。

原链接：`https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz`

##### 方案一：使用文件加速/代理服务（最推荐）

这些服务通常通过 CDN 缓存文件或作为国内高速代理。您只需将原链接作为参数输入或替换域名。

| 加速域名/服务 | 使用方式 | 对应的 `wget` 命令 |
| :--- | :--- | :--- |
| **`ghproxy.link`** | 替换 `github.com` | `wget https://ghproxy.link/https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz` |
| **`ghfast.top`** | 替换 `github.com` | `wget https://ghfast.top/https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz` |
| **`github.fxxk.dedyn.io`** | 作为前缀/代理 | `wget https://github.fxxk.dedyn.io/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz` |


<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763192246006-8ce1b00a-ca27-4166-b657-28644537bc24.png" width="100%" alt="FinRpt Framework Diagram"/>




### ubuntu 部分命令积累

1. 进入其他人的文件夹
```bash 
    sudo -iu root
```
---
