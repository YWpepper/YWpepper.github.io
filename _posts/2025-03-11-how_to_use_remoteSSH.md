---
title: 'how_to_use_remoteSSH'
lang: zh-CN
date: 2025-03-11
author: pepper
permalink: /posts/2025/03/how_to_use_remoteSSH/
pinned: false
toc: true
tags:
   - ssh
   - server
---

这篇博客介绍了如何在Ubuntu系统和路由器的局域网连接中，配置路由器的端口转发服务，实现远程SSH访问。

<!-- more -->

## 1. 配置路由器的端口转发服务

### 1.1 网络拓扑说明

Ubuntu电脑通过路由器连接到局域网,路由器会分配一个内网IP(通常是`192.168.xx.xx`)。

- **实验室内访问**: 同一路由器局域网下,可直接使用内网IP(`192.168.xx.xx`)访问
- **校园网访问**: 路由器本身也在学校更大的局域网中,需要使用路由器的公网IP(`58.xx.xx.xx`)访问

### 1.2 配置步骤

1. **登录路由器管理页面**
    - 访问华为路由器管理地址: `http://192.168.3.1/`
    - 使用WiFi密码登录

    <p align="center">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029348.png" style="zoom:23%;" />
    </p>

2. **查看终端信息**

    查看连接到路由器的设备及其内网IP地址(支持有线和WiFi设备)

    <p align="center">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029748.png" alt="终端信息" style="zoom:30%;" />
    </p>

3. **配置端口转发**

    端口转发的作用是将路由器下某个设备的指定端口映射到路由器的公网端口,使得外网可以访问内网设备。

    <p align="center">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031263.png" alt="端口映射" width="400" style="display: inline-block; margin-right: 10px;">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031402.png" alt="端口触发" width="500" style="display: inline-block;">
    </p>

4. **配置详细信息**

    **重要提示**:
    - 需要在Ubuntu防火墙中开放SSH端口(22)或远程桌面端口(3389)
    - 否则会导致连接失败

    <p align="center">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031182.png" alt="端口配置" style="zoom:20%;" />
    </p>

### 1.3 端口开放实例: TensorBoard可视化

在模型训练时,TensorBoard默认运行在`localhost:6006`,需要通过以下方式远程访问:

**方法1: 局域网内访问**

在同一路由器WiFi下,使用命令开放端口:

```bash
tensorboard --logdir libcity/ --host 0.0.0.0
```

然后通过内网IP(`192.168.xx.xx:6006`)访问

<p align="center">
   <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503122135974.png" alt="局域网访问" style="zoom:35%;" />
</p>

**方法2: 校园网访问**

在路由器管理页面配置端口映射,将内网6006端口映射到路由器公网端口,然后通过路由器公网IP(`59.xx.xx.xx:6006`)访问

<p align="center">
   <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503122128505.png" alt="校园网访问" style="zoom: 25%;" />
</p>

## 2. VSCode远程SSH配置

### 2.1 权限配置

确保远程用户具有足够的读写权限,否则无法编辑文件。

### 2.2 配置步骤

1. **安装插件**

    在VSCode中安装`Remote - SSH`插件

2. **编辑SSH配置文件**

    编辑`~/.ssh/config`文件(注意是config文件,不是config.txt):

    ```bash
    touch config  # 创建文件
    vim config    # 编辑文件
    ```

    配置内容示例:

    ```
    Host 59.xx.xx.xx
          HostName 59.xx.xx.xx
          User root
          Port 8001
    ```

    **参数说明**:
    - `Host`: 连接别名
    - `HostName`: 路由器公网IP
    - `User`: 远程用户名
    - `Port`: 映射后的路由器端口

    <p align="center">
       <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111032822.png" alt="SSH配置" style="zoom:30%;" />
    </p>

---
