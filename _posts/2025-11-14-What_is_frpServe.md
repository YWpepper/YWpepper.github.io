---
layout: post
title: 'How_to_make_frpServe'
date: 2025-11-14
author: pepper
tags: [server]
comments: true
toc: true
pinned: false
---
这篇博客介绍了在Ubuntu22.04上部署frp-0.48.0内网穿透服务。
<!-- more -->

内网穿透允许我们在公共网络中安全地访问位于私有网络中的设备。其中一种常用的实现方式是使用frp（Fast Reverse Proxy）工具。frp是一个开源的内网穿透工具，它提供了简单而强大的功能，可以帮助我们轻松地实现内网穿透，让我们能够方便地访问内网资源。


## 服务端（公网IP服务器）
1. 下载frp
    frp-0.48.0的下载地址为：[fatedier/frp/releases/tag/vv0.65.0](https://link.zhihu.com/?target=https%3A//github.com/fatedier/frp/releases/tag/vv0.65.0)

    ```bash
    #直接使用weget命令，使用github加速镜像
    wget https://ghfast.top/https://github.com/fatedier/frp/releases/download/v0.48.0/frp_0.48.0_linux_amd64.tar.gz
    ```
    <img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763220029393-aee9343c-ee15-4ae6-b9dd-b857a5773f8b.png" width="100%" alt="FinRpt Framework Diagram"/>

2. 将文件上传至服务器
    
    将下载的frp的.tar.gz文件传到服务器中(建议使用xftp)

    ```bash
    # 在服务器中使用下面的命令解压.tar.gz文件
    tar -zxvf frp_0.65.0_linux_amd64.tar.gz
    ```

    将解压后的文件夹移动到/root/目录下

    ```bash
    # 移动到root目录下
    sudo mv frp_0.48.0_linux_amd64/ /root/frp
    
    # 将文件夹以及其子文件权限设置为仅root可读可写
    sudo chmod -R 700 frp
    
    # 将文件夹与其子文件的拥有者设置为root用户
    sudo chown -R root:root frp
    ```


3. frps配置

    为了方便起见，以下配置需要切换到root用户，用sudo也可行。

    ```shell
    # 进入到frp目录
    cd /root/frp
    # 编辑frps的配置文件
    nano frps.ini
    ```

    下面是frps服务器端的配置文件的参考，虚线中间的**端口**、**用户名**及**密码**请根据自己的需求更改

    ```shell

    [common]
    # --------------------------------------------------------------------------------------
    # bind_port为frps和frpc通信的端口，需要在防火墙中放行该端口
    bind_port = 80001
    # dashboard_port 网页界面的端口，在网页中输入ip:dashboard_port，可以查看frpc的连接情况
    dashboard_port = 80002
    # frps的连接密码,这里需要和frpc.ini文件中的token保持一致
    token = password

    # 80002端口下的dashboard网页用户名密码，用来作为管理界面
    dashboard_user = user
    dashboard_pwd = password
    # --------------------------------------------------------------------------------------

    max_pool_count = 50
    log_file = /root/frp/logs/frps.log
    log_level = info
    log_max_days = 10
    # 我这里打开了tls加密，根据个人情况决定是否要开
    tls_only = true
    ```
4. 设置开机自启动

   ```bash
    # 先打开服务文件
    cd /etc/systemd/system/
    nano frps.service

    # 将下面内容写入到frps.service
    [Unit]
    Description=Frp Server Service
    After=network.target

    [Service]
    Type=simple
    User=root
    Restart=on-failure
    RestartSec=5s
    ExecStart=/root/frp/frps -c /root/frp/frps.ini
    ExecReload=/root/frp/frps -c /root/frp/frps.ini
    LimitNOFILE=1048576

    [Install]
    WantedBy=multi-user.target
   ```
5. 保存后执行下面命令启动开机自启动
    ```bash
    # 修改完一次配置文件，就需要reload一下
    systemctl daemon-reload
    # 打开服务
    systemctl start frps.service
    # 暂停服务
    systemctl stop frps.service
    # 设置开机自启动
    systemctl enable frps.service
    ## 最后一定要检查一下服务是否打开
    systemctl status frps.service
    ```





## 客户端（windows/ubuntu）
1. 安装frp文件同上

2. 切换到root用户，编辑frpc的配置文件,这里修改client的配置
    ```bash
    # 进入到frp目录
    cd /root/frp
    # 编辑frpc的配置文件
    nano frpc.ini
    ```

3. 编辑frpc的配置文件。

    ```bash
    [common]
    # 比如域名baidu.com / 它对应ip 180.101.49.11 
    server_addr = 你的服务器的IP地址（如果是动态IP，使用ddns的域名也行）
    # server_port和frps中的bind_port对应
    # 即由于服务器上在端口80001开启了服务，所以你需要请求80001
    server_port = 80001
    # 与frps配置文件中的token对应，这个用来校验身份
    token =  password
    tls_enable = true

    # 第一个服务类型为tcp的ssh远程连接
    [ssh]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 22
    # 下面的remote_port端口需要在部署frps的服务器中放行该端口
    # 即我本地的22端口映射到公网服务器上的remote端口，服务器要打开这个端口，区分上面的服务端口80001
    remote_port = 2222

    # 第二个服务类型为udp的windows远程桌面连接,可以注释掉
    [windows_remote]
    type = udp
    # 穿透的主机不仅局限于本机，这个地方我还不太明白
    local_ip = 192.168.123.100
    local_port = 3389
    # 需要在部署frps的服务器中放行3389端口
    remote_port = 3389 
    ```
4. 客户端启动frpc服务
    ```bash
    
    cd /etc/systemd/system/
    nano frpc.service
    ```

    将下面的内容写入到frpc.service
    ```shell
    [Unit]
    Description=Frp Client Service
    After=network.target

    [Service]
    Type=simple
    User=root
    Restart=on-failure
    RestartSec=5s
    ExecStart=/root/frp/frpc -c /root/frp/frpc.ini
    ExecReload=/root/frp/frpc -c /root/frp/frpc.ini
    LimitNOFILE=1048576

    [Install]
    WantedBy=multi-user.target
    ```
5. 保存后执行下面命令启动开机自启动
    ```bash
    systemctl daemon-reload
    systemctl start frpc.service
    systemctl enable frpc.service

    # 注意最后检查是否与服务器实现通信
    systemctl status frpc.service
    ```
    <img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763219783004-bc1961bf-e64d-4e02-a62c-241b7cf1aa04.png" width="100%" alt="FinRpt Framework Diagram"/>


至此完成所有步骤.


