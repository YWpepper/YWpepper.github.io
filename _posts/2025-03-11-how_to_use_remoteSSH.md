---
title: '服务器-远程SSH配置与端口转发'
lang: zh-CN
date: 2025-03-11
author: pepper
tags: [ssh, server]
pinned: false
toc: true
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

## 3. 常见报错

### 3.1 wsl与windows无法镜像

【自我描述问题版本：】 正常情况下，比如`ssh`运行在`wsl`内部的`2222`端口，`win`应该是和`wsl`是镜像模式，但是不知道什么原因导致他们不是镜像了。我在路由器管理页面配置了`win`的`2222`端口映射到路由器上的`10022`端口，但是我还是无法通过路由器`ip -p100022`,因为`win`的端口`2222`根本不是`wsl`中的`ssh`服务。

【官方ai总结问题版本：】用户在 `.wslconfig` 中配置了 `networkingMode=mirrored`（镜像网络模式），预期 `WSL` 内部监听的 `2222` 端口应自动映射至 `Windows` 宿主机的 `2222` 端口。然而，实际测试发现 `Windows `侧并未同步监听该端口，导致路由器即便配置了“公网 `10022 -> Win 2222`”的转发规则，流量也无法到达 `WSL` 内部的 `SSH` 服务。

### 3.1 问题解决：

#### 1. WSL 内部环境准备 (Ubuntu)

确保 WSL 内部的 SSH 服务正常运行，并监听指定端口。

- **修改配置**：`sudo nano /etc/ssh/sshd_config`
  - `Port 2222` (建议避开默认 22 端口)
  - `ListenAddress 0.0.0.0`
  - `PasswordAuthentication yes`
- **安装工具**：`sudo apt update && sudo apt install net-tools -y`
- **启动服务**：`sudo service ssh restart`
- **检查监听**：`sudo netstat -tlnp | grep 2222`
  - _预期输出：`0.0.0.0:2222 LISTEN`_

---

#### 2. Windows 宿主机“接力”配置

由于 WSL2 架构原因，外部流量到达 Windows 后需要手动映射。

##### A. 端口转发 (Port Proxy)

在 **Windows PowerShell (管理员)** 执行，建立 Windows 与 WSL 之间的桥梁：

```powershell
# 建立转发：将 Windows 的 11126 端口流量传给 WSL 的 2222
netsh interface portproxy add v4tov4 listenport=10022 listenaddress=0.0.0.0 connectport=2222 connectaddress=127.0.0.1

## 记得然后去路由器的控制面板设置:
   # win的10022转发到路由器上的10022

# 检查当前转发规则
netsh interface portproxy show all

# 如果你刚刚设定的端口还是没有被监听，那就换一个端口，或者再检查一下错误

# 如果需要重置所有规则
netsh interface portproxy reset
```

##### B. 防火墙放行

必须手动允许外部端口入站：

```bash
New-NetFirewallRule -DisplayName "WSL_SSH_External" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 10022
```

#### 3. 官方wsl镜像排查

核心原因： `.wslconfig` 镜像配置可能未生效，或者被系统层面的防火墙/其他服务占用了端口，导致自动映射“断层”。

修复步骤：

- 验证 `.wslconfig`：确保文件位于 `%UserProfile%\.wslconfig `且格式正确：

```bash
Ini, TOML
[wsl2]
networkingMode=mirrored
```

- 强制重启：`PowerShell` 执行 `wsl --shutdown`。

#### 4. 完整链路检查清单

- 客户端 `->` 识别真实公网 `IP` (非 198.18 段)。

- 路由器 `->` 转发 外部端口 至 `Windows`局域网`IP:`内部端口。

- `Windows -> netsh` 转发 内部端口 至 `127.0.0.1:2222`。

- `WSL -> sshd` 服务在 `2222` 正常工作。

---
