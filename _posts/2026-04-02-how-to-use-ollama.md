---
layout: post
title: "how_to_useOllama"
date: 2026-04-02
author: pepper
tags: [server]
comments: true
toc: true
pinned: false
---

这篇博客介绍了Ollama 常用命令笔记（Ubuntu 终端专用）

<!-- more -->



# Ollama 常用命令笔记（Ubuntu 终端专用）
全部为 Ubuntu 下直接可执行的命令，简洁可复制保存。

## 1. 安装与服务
```bash
# 安装 Ollama（官方一键脚本）
curl -fsSL https://ollama.com/install.sh | sh

# 查看 Ollama 服务状态
systemctl status ollama

# 启动/停止/重启服务
sudo systemctl start ollama
sudo systemctl stop ollama
sudo systemctl restart ollama

# 设置开机自启
sudo systemctl enable ollama
```

## 2. 基础命令
```bash
# 查看版本
ollama --version

# 查看已安装模型
ollama list

# 查看正在运行的模型
ollama ps

# 停止所有运行中的模型
ollama stop
```

## 3. 模型下载、运行、删除
```bash
# 下载模型
ollama pull qwen2.5:7b
ollama pull llama3.2:3b
ollama pull gemma2:2b

# 运行并进入对话
ollama run qwen2.5:7b

# 后台运行（供 API 调用）
ollama run qwen2.5:7b --now

# 删除模型
ollama rm qwen2.5:7b

# 复制/重命名模型
ollama cp 原模型名 新模型名

# 查看模型信息
ollama show qwen2.5:7b
```

## 4. 交互模式内命令（对话中使用）
```
/bye        退出
/help       帮助
/system     设置系统提示词
/set        设置参数
/show       查看当前模型信息
```

## 5. 日志与排查
```bash
# 查看 Ollama 日志
journalctl -u ollama -f

# 查看占用端口（默认 11434）
ss -tulpn | grep ollama
```

## 6. 卸载 Ollama（如需）
```bash
sudo systemctl stop ollama
sudo rm /usr/local/bin/ollama
sudo rm -rf /usr/share/ollama
rm -rf ~/.ollama
```





