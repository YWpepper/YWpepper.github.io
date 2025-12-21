---
title: 'how_to_install_mySql'
lang: zh-CN
date: 2025-11-02
author: pepper
pinned: false
toc: true
tags:
  - ssh
  - sever
---
安装 MySQL 关系型数据库管理系统的操作指南；
<!-- more -->
## 各种数据库的端口

+ MySQL：3306
+ Redis：6379
+ MongoDB：27017
+ Django：8000
+ flask：5000

## 使用 Navicat 进行数据库管理

1. 设置实际运行的端口 3308，因为我的电脑上有 WSL 会有镜像问题

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762142013620-2eb8d811-510a-427d-a214-8313c63e73b3.png" width="70%">

## 安装报错

### 1. data 文件夹无法使用

**解决方案**：删除该文件夹，重新创建，确保其为空

```bash
C:\Windows\System32>mysqld --initialize --console
2025-11-02T15:12:33.373893Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
2025-11-02T15:12:33.383215Z 0 [System] [MY-013169] [Server] E:\MySql\mysql-8.4.7\bin\mysqld.exe (mysqld 8.4.7) initializing of server in progress as process 40892
2025-11-02T15:12:33.406661Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-11-02T15:12:33.592871Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-11-02T15:12:34.444169Z 0 [ERROR] [MY-000067] [Server] unknown variable 'default_authentication_plugin=mysql_native_password'.
2025-11-02T15:12:34.445152Z 0 [ERROR] [MY-013236] [Server] The designated data directory E:\MySql\mysql-8.4.7\data\ is unusable. You can remove all files that the server added to it.
2025-11-02T15:12:34.445232Z 0 [ERROR] [MY-010119] [Server] Aborting
2025-11-02T15:12:35.218892Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
```

### 2. 正常运行结果

临时密码：`**********`

```bash
C:\Windows\System32>mysqld --initialize --console
2025-11-03T03:48:13.155389Z 0 [System] [MY-015017] [Server] MySQL Server Initialization - start.
2025-11-03T03:48:13.158492Z 0 [System] [MY-013169] [Server] E:\MySql\bin\mysqld.exe (mysqld 9.4.0) initializing of server in progress as process 16960
2025-11-03T03:48:13.169209Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-11-03T03:48:13.358200Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-11-03T03:48:14.164476Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: **********
2025-11-03T03:48:15.693586Z 0 [System] [MY-015018] [Server] MySQL Server Initialization - end.
```

### 3. 服务无法打开

报错原因如下：

```bash
E:\MySql\bin>mysqld --console
2025-11-03T03:18:35.629807Z 0 [System] [MY-015015] [Server] MySQL Server - start.
2025-11-03T03:18:35.708375Z 0 [System] [MY-010116] [Server] E:\MySql\bin\mysqld.exe (mysqld 8.4.7) starting as process 41084
2025-11-03T03:18:35.715892Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2025-11-03T03:18:35.863177Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2025-11-03T03:18:35.938180Z 0 [ERROR] [MY-011292] [Server] Plugin mysqlx reported: 'Preparation of I/O interfaces failed, X Protocol won't be accessible'
2025-11-03T03:18:35.938305Z 0 [ERROR] [MY-011300] [Server] Plugin mysqlx reported: 'Setup of bind-address: '*' port: 33060 failed, (10013). Do you already have another mysqld server running with Mysqlx ?'
2025-11-03T03:18:35.939039Z 0 [ERROR] [MY-013597] [Server] Plugin mysqlx reported: 'Value '*' set to `Mysqlx_bind_address`, X Plugin can't bind to it. Skipping this value.'
2025-11-03T03:18:35.990818Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
2025-11-03T03:18:35.990982Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
2025-11-03T03:18:35.994040Z 0 [ERROR] [MY-010262] [Server] Can't start server: Bind on TCP/IP port: 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。
2025-11-03T03:18:35.994168Z 0 [ERROR] [MY-010257] [Server] Do you already have another mysqld server running on port: 3306 ?
2025-11-03T03:18:35.994254Z 0 [ERROR] [MY-010119] [Server] Aborting
2025-11-03T03:18:37.208184Z 0 [System] [MY-010910] [Server] E:\MySql\bin\mysqld.exe: Shutdown complete (mysqld 8.4.7) MySQL Community Server - GPL.
2025-11-03T03:18:37.208369Z 0 [System] [MY-015016] [Server] MySQL Server - end.
```

#### 错误解析：端口占用 ❌

主要的错误集中在端口绑定失败上：

**1. 传统连接端口 (Port 3306)**

+ **错误信息：** `Can't start server: Bind on TCP/IP port: 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。`
+ **错误信息：** `Do you already have another mysqld server running on port: 3306 ?`
+ **解释：** 这是最主要的错误。操作系统报告说 **MySQL 的默认端口 3306 已经被另一个进程（可能是另一个 MySQL 实例或任何其他服务）占用**。服务器无法绑定到这个端口，因此启动失败。

**2. X Protocol 端口 (Port 33060)**

+ **错误信息：** `Plugin mysqlx reported: 'Setup of bind-address: '*' port: 33060 failed, (10013). Do you already have another mysqld server running with Mysqlx ?'`
+ **解释：** MySQL 8.0+ 版本默认启用了 X Plugin，它使用 **33060 端口**。这个端口也遇到了类似的绑定失败问题，很可能是因为 **另一个进程占用了 33060 端口**，或者 **权限不足 (错误代码 10013)**，但最常见的原因仍是端口占用。

#### 修改 MySQL 的默认端口

如果 3306 端口被一个您不想或不能停止的程序占用，您可以**修改您当前要启动的 MySQL 实例使用的端口**。

1. 找到您的 MySQL 配置文件 `my.ini`（通常在 `E:\MySql` 或其子目录下）
2. 用文本编辑器打开它
3. 在 `[mysqld]` 标题下，找到或添加 `port` 配置项，将其更改为**另一个未被占用的端口**（例如 **3307** 或 **3308**）：

```ini
[mysqld]
# ... 其他配置
port=3307
# ...
```

4. **保存** `my.ini` 文件
5. **重新启动** MySQL 服务器：`E:\MySql\bin>mysqld --console`

---

## 参考指南

### 【一】各种数据库的端口

+ MySQL：3306
+ Redis：6379
+ MongoDB：27017
+ Django：8000
+ flask：5000

### 【二】MySQL 介绍

+ MySQL 是一个开源免费的关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 旗下公司。
+ MySQL 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。
+ 具有成本低、速度快、体积小且开放源代码等优点。
+ 全球数据库引擎使用排行榜：

<img src="https://pica.zhimg.com/v2-64e9d5ab42a89c506420bcf17e625d44_1440w.jpg" width="70%">

### 【三】下载 MySQL 服务端

#### （1）打开官网

+ [https://www.mysql.com](https://link.zhihu.com/?target=https%3A//www.mysql.com)

#### （2）点击 downloads

<img src="https://pic2.zhimg.com/v2-73f621867acaf68bc699326a1653537d_1440w.jpg" width="70%">

<img src="https://picx.zhimg.com/v2-41787b19ae771ba440d66b39524e2463_1440w.jpg" width="70%">

#### （3）选择 MySQL Community Server

<img src="https://pic2.zhimg.com/v2-7da1db22a0e0246216aa93a1d4bfb45b_1440w.jpg" width="70%">

#### （4）选择版本

<img src="https://pic1.zhimg.com/v2-fd39072cf256372a9259ef2ecc48bd58_1440w.jpg" width="70%">

<img src="https://pic3.zhimg.com/v2-3c90ad4e36584ed39ea6c0c28f8ffd7c_1440w.jpg" width="70%">

### 【四】安装 MySQL

#### （1）解压压缩包

+ 右键压缩包选择解压，可以改文件夹名字也可以不改

<img src="https://pic3.zhimg.com/v2-7a24844ce2598f24b3261dd0b1444a44_1440w.jpg" width="70%">

#### （2）配置环境变量

+ 打开设置搜索环境变量
+ 将 MySQL 的 bin 目录添加到环境变量中

<img src="https://pic3.zhimg.com/v2-1b1009da6e889dd87147a744b16cc97a_1440w.jpg" width="70%">

#### （3）打开终端

+ win+r
+ 以管理员身份运行

<img src="https://pic3.zhimg.com/v2-d49d26e468fd9fd84deb769abfe3205a_1440w.jpg" width="70%">

#### （4）配置 MySQL 配置文件

+ 在你的 MySQL 安装目录下新建一个文件，文件名 `my.ini`

<img src="https://pica.zhimg.com/v2-3611fbaadac1e1f556ae97c3e5f4fc54_1440w.jpg" width="70%">

+ 复制并且修改路径

```ini
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录
basedir="D:\python_studyclass\MySQL"
# 设置mysql数据库的数据的存放目录，就是前面手动创建的data目录
datadir="D:\python_studyclass\MySQL\data"
# 允许最大连接数
max_connections=200
# 允许连接失败的次数
max_connect_errors=10
# 服务端使用的字符集默认为utf8mb4
character-set-server=utf8mb4
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用"mysql_native_password"插件认证
default_authentication_plugin=mysql_native_password

[mysql]
# 设置mysql网络通信的默认字符集
default-character-set=utf8mb4

[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
# 设置mysql客户端的默认字符集
default-character-set=utf8mb4
```

<img src="https://picx.zhimg.com/v2-56210162f1ea7d9cc80a5be6ce25277b_1440w.jpg" width="70%">

+ 再创建一个 data 文件夹

<img src="https://pic1.zhimg.com/v2-e9420745dfcad84c75e0dd7247dad57a_1440w.jpg" width="70%">

#### （5）初始化 MySQL 服务端

+ 执行命令进行初始化

```bash
mysqld --initialize --console
```

+ 复制并记住临时密码：`****`

<img src="https://pic3.zhimg.com/v2-6f33a38a79b7e4ae723edf73ec84eab2_1440w.jpg" width="70%">

#### （6）注册系统服务

+ 未注册之前是没有 MySQL 服务的
+ 搜索栏里搜索服务 或者 右键我的电脑 打开计算机管理 → 服务和应用程序 → 服务

<img src="https://pic2.zhimg.com/v2-b04efc134337ad6c1b61b7e8bec42865_1440w.jpg" width="70%">

+ 执行命令注册

```bash
mysqld --install
```

<img src="https://pic4.zhimg.com/v2-b9bf9eef852fc9df22ac3dd4ddce330d_1440w.jpg" width="70%">

<img src="https://pic3.zhimg.com/v2-1ba8be270ba8d4c872783616fbb19e44_1440w.jpg" width="70%">

+ 如果后续要移除的话，cmd 中以管理员身份运行

```bash
mysqld --remove
```

刷新服务，可以看到 MySQL 服务就被移除了

#### （7）启动 MySQL 服务

**方式一：**

<img src="https://pic4.zhimg.com/v2-564797523dad3ef2a3fa502a0ab342d5_1440w.jpg" width="70%">

**方式二：** cmd 中以管理员身份运行

```bash
net start mysql  # 启动MySQL服务
```

<img src="https://pic3.zhimg.com/v2-937a6679f4fe354d48b15b4b03e31d6c_1440w.jpg" width="70%">

```bash
net stop mysql  # 停止MySQL服务
```

<img src="https://pic1.zhimg.com/v2-af17dd937ad8dab5caf21c70f69f5fb8_1440w.jpg" width="70%">

### 【五】MySQL 操作

#### （1）登入和退出

```bash
# 登录
# 方式一：直接本地登入 u：username root：用户名 -p：password
mysql -uroot -p

# 方式二：加上用户名和密码一起登入
mysql -uroot -p123456

# 链接远程服务登入
mysql -h 192.168.1.63 -P 3306 -uroot -p123456

# 在SQL语句中必须有结束符: ;
quit;
```

#### （2）修改密码

**登入客户端：**

```bash
# 先执行：
mysql -uroot -p

# 再输入临时密码：
****
```

<img src="https://pica.zhimg.com/v2-8a159a0d71e3492637e8e4cb9648ce0c_1440w.jpg" width="70%">

**修改密码：**

```sql
alter user 'root'@'localhost' identified by '****';
```

<img src="https://pic3.zhimg.com/v2-0e8397a2c714459bd74e8f0639dc197c_1440w.jpg" width="70%">

**刷新权限：**

```sql
flush privileges;
```

<img src="https://pic3.zhimg.com/v2-62485287f11618a38cfda7036c9ca484_1440w.jpg" width="70%">

**退出：**

```bash
quit;
```

#### （3）修改密码（忘记原本的密码）

+ 先关闭 MySQL 服务

```bash
net stop mysql
```

+ 执行跳表命令

```bash
mysqld --skip-grant-tables
```

+ 以无密码登入的启动模式启动 MySQL 服务端
+ 额外再用管理员身份打开一个终端
+ 执行 MySQL 登入命令 `mysql -uroot -p`
+ 输入密码的时候什么都不要输，直接 enter

<img src="https://pic2.zhimg.com/v2-2bb097e513664db57488e2a0e4ee167f_1440w.jpg" width="70%">

+ 继续修改密码，先刷新一下权限

```sql
flush privileges;
```

+ 再执行修改密码

```sql
alter user 'root'@'localhost' identified by '****';
```

+ 再刷新权限

```sql
flush privileges;
```

#### （4）跳过输入密码直接登入

+ 在 `my.ini` 配置文件中增加下述配置（在 `[mysql]` 部分）
+ 不需要每次输入验证码即可登陆

```ini
[mysql]
user="root"
password=**********
default-character-set=utf8mb4
```
