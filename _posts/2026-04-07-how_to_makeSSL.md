---
layout: post
title: "how_to_makeSSL证书"
date: 2026-04-07
author: pepper
tags: [server]
comments: true
toc: true
pinned: false
---

这篇博客介绍了安装SSL证书，防止“裸奔”在互联网——用户信息可能被窃取，搜索引擎排名也会大打折扣。一张SSL证书，不仅能实现HTTPS加密，还能提升用户信任度！

<!-- more -->

### 一、SSL证书怎么选？


看域名数量

- 单域名：保护1个主域名（如 http://www.company.com）。

- 通配符：保护主域名+所有子域名（如 *.http://company.com）。

- 多域名：一张证书覆盖多个独立域名（如 http://company.com + http://shop.company.net）。



### 二、托管平台(不建议)

由于一开始是新手，自己不会，所以在网上找了免费签发版本。申请后五分钟内可以发放，参考 [OHTTPS](https://ohttps.com/docs/) 的免费版 HTTPS 证书 / SSL 证书。其中，OHTTPS 的免费版 HTTPS证书 / SSL 证书是由 Let's Encrypt 颁发。

#### 0. DNS授权

由于这个托管平台需要帮你管理，它需要有很多权限，其中我们按照它的指南开始操作，以下选择DNS授权验证模式，可以参考它的[指南](https://ohttps.com/docs/dns/aliyun)，但是有点旧了。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408222044022.png" alt="alt text" width="80%" />

#### 1. 新建RAM用户
访问阿里云的链接如下：`https://ram.console.aliyun.com/overview`

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408222548784.png" alt="alt text" width="80%" />

#### 2. 保存AccessKey ID和AccessKey Secret

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408222226606.png" alt="alt text" width="80%" />

阿里云中的获取方式与之前的传统不一样，在用户新建完成后，及时保存 `AccessKey ID` 和`AccessKey Secret`。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408223229155.png" alt="alt text" width="80%" />

#### 3. 为用户添加权限
选择新建的`ohttps-dns`用户，为该用户添加`[AliyunDNSFullAccess(管理云解析（DNS）的权限)]` 以及 `[AliyunYundunCertFullAccess(管理云盾证书服务的权限)]` 权限。该权限仅在申请证书时证书提供商 Let'sEncrypt 验证域名所属权使用,以及该权限仅用于上传用户在 OHTTPS 中申请的 HTTPS 证书 / SSL 证书。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408223417844.png" alt="alt text" width="80%" />

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408223614769.png" alt="alt text" width="80%" />

#### 4. 部署SSL证书

下载证书放到服务器上，或者使用平台直接托管一键操作。

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/20260408223652679.png" alt="alt text" width="80%" />


### 三、 certbot工具配置

在自己的服务器上配置 Let's Encrypt SSL 证书，最主流、最省心的方案是使用 Certbot 工具。它能自动完成域名验证、证书签发、Web 服务器配置（Nginx/Apache）、自动续期全流程。

#### 1. 安装 Certbot（官方推荐）

用 apt 安装（Ubuntu/Debian）

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx python3-certbot-apache -y
```
#### 2.申请 & 自动配置证书

Nginx 服务器（全自动，最常用）:Certbot 会自动修改 Nginx 配置、开启 HTTPS、强制 HTTP→HTTPS 重定向。
```bash
certbot --nginx -d 你的域名.com --non-interactive --agree-tos -m 你的邮箱@xxx.com
```

这条命令会：自动验证域名 /  自动签发证书 / 自动修改 Nginx 配置 / 自动开启 HTTPS / 自动把 80 重定向到 443 / 自动配置自动续期任务

> 执行后会问你 3 个问题：
    1. 输入邮箱：随便填一个你的邮箱
    2. 同意协议：输入 Y
    3. 是否共享邮箱：输入 N
    4. 最后问是否重定向：输入 2（自动 HTTP 转 HTTPS）

#### 3、交互过程（执行命令后）
成功后会提示：
- 证书路径：`/etc/letsencrypt/live/yourdomain.com/` 也可以手动指定移动到例如 `/etc/nginx/ssl/yourdomain.com`
- 关键文件：
    - fullchain.pem（证书链）
    - privkey.pem（私钥）

```bash
# 复制 Let's Encrypt 证书到这个目录（自动续期后也需要重新复制）
sudo cp /etc/letsencrypt/live/yourdomain.com/fullchain.pem /etc/nginx/ssl/yourdomain.com/
sudo cp /etc/letsencrypt/live/yourdomain.com/privkey.pem /etc/nginx/ssl/yourdomain.com/

# 设置正确权限
sudo chmod 600 /etc/nginx/ssl/yourdomain.com/*
sudo chown nginx:nginx /etc/nginx/ssl/yourdomain.com/*  # 如果是 Ubuntu 则是 www-data:www-data

```

#### 4. 配置
打开配置文件：
```bash
sudo vi /etc/nginx/conf.d/vllm-https.conf
```
把下面内容完整粘贴进去（只需要把 yourdomain.com 换成你的真实域名）：

```bash

# HTTPS 安全配置
server {
    listen 443 ssl http2;
    server_name yourdomain.com;  # 改成你的域名

    # 你要求的证书路径
    ssl_certificate /etc/nginx/ssl/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/yourdomain.com/privkey.pem;

    # 安全优化（官方推荐）
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # 这里是你的 vllm 代理配置
    location / {
        proxy_pass http://127.0.0.1:8000;  # vllm 默认端口
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 大模型接口需要长连接
        proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
    }
}

# 强制 HTTP 跳转到 HTTPS（必开）
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

```

#### 5. 测试 + 重启 Nginx

```bash
# 测试配置是否正确
sudo nginx -t

# 重启生效
sudo systemctl restart nginx
```

#### 6. 自动续期证书（必须配置）
因为你手动移动了证书，Certbot 自动续期后不会同步到 /etc/nginx/ssl，所以要加一个自动复制脚本:

```bash
sudo vi /etc/letsencrypt/renewal-hooks/deploy/copy-to-nginx-ssl.sh
```
粘贴内容：
```bash
#!/bin/bash
DOMAIN="yourdomain.com"
cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/nginx/ssl/$DOMAIN/
cp /etc/letsencrypt/live/$DOMAIN/privkey.pem /etc/nginx/ssl/$DOMAIN/
chmod 600 /etc/nginx/ssl/$DOMAIN/*
systemctl reload nginx
```

加执行权限：
```bash
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/copy-to-nginx-ssl.sh
```
