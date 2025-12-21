---
title: 'How_to_useUbuntu'
lang: zh-CN
date: 2024-02-07
author: pepper
permalink: /posts/2024/02/how_to_use_ubuntu/
toc: true
pinned: false
tags:
  - Server
  - Command
---
这篇笔记汇总了在 Ubuntu 下常用的快速命令与进程/服务管理方法，包含文件/目录操作、显卡查看、后台进程管理（nohup、systemd、tmux）及自检与故障排查常用命令。便于快速查阅与实际操作参考。
<!-- more -->

## 常见基本命令（快速参考）
- 更新与安装软件
  ```bash
  sudo apt update           # 更新软件源
  sudo apt upgrade -y        # 更新已安装软件
  sudo apt install <package> -y  # 安装软件包
  sudo apt install ./debfile.deb -y     # 本地deb包安装
  ```
- 文件/目录：查看、复制、移动、删除、权限
  ```bash
  ls -lah         # 列出详细信息
  cd /path/to/dir   
  mkdir -p newdir
  cp -r src dst   # src源头复制到 dst 目标
  mv oldname newname  # 重命名或移动
  rm file.txt
  rm -rf directory/
  chmod 644 file.txt # 修改权限 644 rw-r--r-- 777 rwxrwxrwx 最高权限是 777
  chmod +x script.sh # 添加可执行权限 
  chown user:group file # 修改文件所有者和用户组
  ```
- 查找与内容搜索
  ```bash
  find /path -name "pattern" # 按名称查找文件 
  grep -RIn "keyword" /path # 递归搜索关键词，显示行号 
  sudo lsof -i :8080 # 查找端口是否被人使用 
  locate filename         # 需先 sudo updatedb
  ```
- 磁盘与空间
  ```bash
  df -h                  # 挂载点磁盘空间
  du -sh /path           # 目录大小
  du -sh *               # 当前目录下各文件/目录大小
  lsblk                  # 块设备信息
  ```
- 网络与端口
  ```bash
  ip addr show
  ss -tuln               # 监听端口
  sudo lsof -i :8080
  grep -RIn "main.py" /etc/systemd/system/ # 查找main.py 运行在哪个端口
  curl -I https://example.com
  ```

## 文件和目录操作（建议与常用场景）
- 递归复制并保留权限：
  ```bash
  cp -a src_dir/ dest_dir/
  ```
- 批量重命名（示例）：
  ```bash
  for f in *.txt; do mv "$f" "${f%.txt}.bak"; done
  ```
- 查找大文件：
  ```bash
  find / -type f -size +100M -exec ls -lh {} \;
  ```

## 显卡动态查看（常见 NVIDIA）
- 实时查看 GPU 使用情况：
  ```bash
  nvidia-smi
  watch -n 2 nvidia-smi    # 每2秒刷新
  ```
- 查看显卡详细信息：
  ```bash
  sudo lshw -C display
  nvidia-smi --query-gpu=name,memory.total,memory.used,utilization.gpu --format=csv
  ```
- NVIDIA 设置 GUI：
  ```bash
  nvidia-settings
  ```
- 如果使用 CUDA/驱动出问题，检查内核驱动与日志：
  ```bash
  dmesg | grep -i nvidia
  journalctl -k | grep -i nvidia
  ```

## 进程管理（查看与定位）
- 查看进程列表与资源占用：
  ```bash
  ps aux | grep process_name
  top
  htop             # 更友好的交互式工具（需安装）
  ```
- 根据名称查进程 ID：
  ```bash
  pgrep -fl "python run_script.py"
  ps aux | grep "[p]ython run_script.py"
  ```
- 文件/端口被哪个进程占用：
  ```bash
  sudo lsof -i :PORT
  sudo lsof /path/to/file
  ```

## 后台进程管理方案（开发到生产）
以下根据复杂度与可靠性由低到高排列。

### 1) 使用 nohup（简单、快速）
优点：无需额外配置，适合短期任务。
```bash
nohup python -u run_script.py > script.log 2>&1 &
# 说明：
# nohup: 忽略挂断信号，使进程在登出后继续运行
# -u (Python): 禁用输出缓冲，适合实时日志
# > script.log 2>&1: 标准输出与错误输出合并到文件
# &: 后台运行
```
查看与终止：
```bash
ps aux | grep "python run_script.py"
tail -f script.log
pkill -f "python run_script.py"     # 优雅结束
kill -9 <pid>                       # 强制结束（谨慎）
```

### 2) 使用 tmux（会话管理）
优点：交互式控制，方便重连和调试。
```bash
sudo apt install tmux -y
tmux new -s model_train
# 在会话中运行：
python run_script.py
# 分离：
Ctrl+B 然后 D
# 重连：
tmux attach -t model_train
# 列出现有会话：
tmux ls
```
提示：tmux 可以配合日志重定向使用，或在会话内启动监控工具（htop、nvidia-smi -l 2 等）。

### 3) 使用 systemd（生产环境推荐）
优点：开机自启、故障自动重启、日志集中（journalctl）。
- 创建服务文件（命名示例：/etc/systemd/system/model.service）
  ```ini
  [Unit]
  Description=Model Training Service
  After=network.target

  [Service]
  User=root
  WorkingDirectory=/root/PDFormer
  ExecStart=/root/miniconda3/envs/base/bin/python run_script.py
  Restart=always
  RestartSec=5
  StandardOutput=file:/var/log/model.log
  StandardError=file:/var/log/model_error.log
  Environment=PYTHONUNBUFFERED=1

  [Install]
  WantedBy=multi-user.target
  ```
- 启用并管理服务：
  ```bash
  sudo systemctl daemon-reload
  sudo systemctl enable model
  sudo systemctl start model
  sudo systemctl status model
  sudo systemctl stop model
  ```
- 查看日志：
  ```bash
  sudo journalctl -u model -f
  # 如果使用 StandardOutput=file: 也可直接 tail -f /var/log/model.log
  ```

## 其他工具与建议
- 使用 supervisor / pm2（针对 Python 或 Node 应用）也可管理进程并提供 Web 管理界面。
- 使用虚拟环境或 conda 管理 Python 依赖，避免系统级冲突。
- 使用 logrotate 管理日志文件大小：
  - 为 /var/log/model.log 添加 logrotate 配置，防止磁盘被日志占满。
- 安全与权限：
  - 尽量避免以 root 运行业务进程，创建专用用户并赋予最小权限。

## 常见排查命令
- 查看系统日志：
  ```bash
  sudo journalctl -xe
  ```
- 查看最近内核/驱动消息：
  ```bash
  dmesg | tail -n 50
  ```
- 检查磁盘使用导致的问题：
  ```bash
  df -h
  sudo du -sh /var/log
  ```

## 小结
- 开发时：nohup 或 tmux 快速起步，便于调试与观察日志。
- 生产时：使用 systemd（或 supervisor/pm2）以保证服务可管理、可重启与开机自启，并结合 journalctl/logrotate 做日志管理。
- 常备命令：nvidia-smi、top/htop、ps/pgrep、lsof、journalctl、ss。掌握这些可应对大多数日常维护与排障场景。
