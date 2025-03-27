---
title: 'dailyResource'
lang: zh-CN
date: 2025-02-10
permalink: /posts/2025/02/dailyResource/
tags:
  - daily
---
这篇博客介绍了一些日常收集整理资料。

---

**google colab**
时刻触发脚本

```
function ConnectButton(){
    console.log("Connect pushed");
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click()
}
setInterval(ConnectButton,60000);
```


#### 2. 后台进程管理方案
- 使用nohup持久运行
`nohup python -u run_script.py > script.log 2>&1 &`

- 参数说明
```
  nohup：忽略挂断信号
  -u（Python参数）：禁用输出缓冲
  > script.log：标准输出重定向
  2>&1：错误输出合并
  &：后台运行
```

- 验证进程状态
```
查看进程列表
ps aux | grep "python run_script.py"
实时监控日志
tail -f script.log
```

- 终止进程 
```
#优雅终止
pkill -f "python run_script.py"
#强制终止（无响应时）
kill -9 1708
```
- 高级管理方案（生产环境推荐）
使用systemd服务 创建服务文件：
`sudo nano /etc/systemd/model.service`

- 服务内容：
```
[Unit]
Description=Model Training Service
[Service]
User=root
WorkingDirectory=/root/PDFormer
ExecStart=/root/miniconda3/envs/base/bin/python run_script.py
Restart=always
StandardOutput=file:/var/log/model.log
StandardError=file:/var/log/model_error.log
[Install]
WantedBy=multi-user.target
```

- 启用服务：
```
sudo systemctl daemon-reload
sudo systemctl enable model
sudo systemctl start model
```

- 使用tmux会话管理
```
安装tmux
sudo apt install tmux -y
创建会话
tmux new -s model_train
在会话中运行
python run_script.py
分离会话：
Ctrl+B → D
重连会话：
tmux attach -t model_train
要打开现有的tmux会话"python_session"，请使用以下命令：
tmux attach -t python_session
```



#### markdown
- Markdown中常用的快捷键
```
Ctrl 0 到 Ctrl 6： 普通文本、一级文本~六级文本

Ctrl B： 加粗；加粗测试

Ctrl I： 斜体；斜体测试

Ctrl U： 下划线；下划线测试

Shift Alt 5： 删除线；删除线测试

Shift Ctrl ~： 行内代码块；行内代码块测试

Ctrl K： 超链接，[超链接测试；欢迎点一个大大的关注！！！](《LL》 - 博客园 (cnblogs.com))；还支持文章内锚点，按Ctrl 键点击此处 👉第一节

Ctrl T： 表格，支持拖拽移动、网页端表格复制转换

Ctrl Shift Q： 引用；

Shift Ctrl I： 插入图片；

Shift Ctrl M： 公式块；

[ ]： 任务列表(可勾选的序列)注意每一个符号之间都有空格

<sup> 内容 </sup>： 上标；上标测试

<sub> 内容 </sub>： 下标；  下标测试  

:smile:： 😄

[toc]： 展示目录

Ctrl l： 选中一行

Ctrl d： 选中内容/单词

Ctrl home： 跳转到文章开头

Ctrl end： 跳转到文章结尾

Ctrl f： 搜索

Ctrl h： 替换
```


- 美剧
Home Watch TV Show  Hacks - Season 1 - [Episode 1](https://cineb.rs/watch-tv/watch-hacks-free-69823.4805626)
