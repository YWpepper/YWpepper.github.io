---
title: 'dailyResource'
lang: zh-CN
date: 2025-04-10
permalink: /posts/2025/04/dailyResource/
tags:
  - daily
---
这篇博客介绍了一些日常收集整理资料。

---

##### 常见的日常积累小技巧

1. mac 电脑外接显示屏
  对于屏幕分辨率的问题，其中较好的一个仓库软件叫做betterdisaplay，可以用来调整刷新赫兹以及分辨率，但是要注意下载符合mac的系统版本的软件；
`https://github.com/waydabber/BetterDisplay/releases?page=6`

2. 绘图的时候图例位置参数设置
```python
    # 紧凑型图例
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[:35], labels[:35], loc='upper right', 
              ncol=2, columnspacing=0.8, handletextpad=0.5)
    
    # 自动检测最佳位置
    # plt.legend(
    #     loc='best',
    #     bbox_to_anchor=(1, 0.5),  # 右侧垂直居中
    #     borderaxespad=0.5,
    #     framealpha=0.9
    # )
    
    # plt.legend(
    # loc='upper center',
    # bbox_to_anchor=(0.5, -0.15),  # 向下偏移15%
    # ncol=2,
    # frameon=True,
    # shadow=True,
    # fancybox=True
    # )
```



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

```txt
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
- 书籍
```
http://38.147.170.240:5959/c1/baidupan/222222/%E5%85%B6%E5%AE%83/EPUB
本站网址
http://103.74.192.62:1234
http://103.74.192.62
主站http://www.https.ng
http://38.147.170.240 http://38.147.170.240:5959
http://45.145.228.151
http://45.145.228.171
http://193.134.211.102:1234 http://193.134.211.108:1234
前面不要加httpS，是http
```
