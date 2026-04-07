---
layout: post
title: "how_to_manageLLM"
date: 2026-04-05
author: pepper
tags: [server]
comments: true
toc: true
pinned: false
---

这篇博客介绍了如何管理本地的LLM，本文将详细梳理使用xinference管理LLM模型的常用命令，以及通过vllm部署LLM模型的核心操作步骤与命令示例，帮助读者快速掌握本地LLM的管理与部署流程。

<!-- more -->

### 一、xinference管理LLM模型常用命令

#### 1. 安装xinference

注意版本不要太高，详细安装和配置可以参考官网文档：
目前本人使用的版本是 `xinference ==1.13.0` 以及`torch==2.3.1+cu121` 和`transformers==4.57.1`

#### 2. 设置xinference为服务

找到目标脚本`xinference/run.sh`，先给它执行权限：

```bash
chmod +x ~/xinference/run.sh
```

创建systemd服务文件：

```bash
sudo nano /etc/systemd/system/xinference.service
```

在文件中添加以下内容：

```ini
[Unit]
Description=Xinference Service
After=network.target

[Service]
Type=simple
User=yw
WorkingDirectory=/home/yw/xinference
ExecStart=/home/yw/xinference/run.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

保存并退出后，执行以下命令启用服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable xinference
sudo systemctl start xinference

# 查看服务状态
sudo systemctl status xinference
```
