---
title: 'ssh&remote'
lang: zh-CN
date: 2025-03-11
permalink: /posts/2025/03/remoteSSH/
tags:
  - ssh
  - sever
---
这篇博客介绍了如何在Ubuntu系统和路由器的局域网连接中，配置路由器的端口转发服务。

## 1. 配置路由器的端口转发服务

1. 首先ubuntu和路由器有一个局域的连接，路由器是大的，ubuntu电脑插到路由器上面，大的路由器会分配一个小的ip给到ubuntu，一般开头都是`192.168.xx.xx`,如果我在实验室里，因为全部都是在路由器的局域网下面，所以可以通过`192.168`来访问，但是由于学校又是一个再大一点的局域网，下面包裹着我的路由器，所以我在图书馆访问的时候就要访问路由器的`58.xx`开头的那个ip。

2. 打开 华为路由的ip：` http://192.168.3.1/` 这个应该每个人都一样，输入的密码就是wifi密码

   ![](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029348.png)

   3. 查看自己的终端信息：此处展示的只是有线连接，其实可以看到wifi连接的设备

![image-20250311102945687](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029748.png)



4. 在这里可以设置端口转发服务，我的理解是，把路由器下设备1的端口1，暴露出来作为路由器本身的端口2来访问，因为设备1无法在学校wifi下检索到，但是路由器归属学校wifi管理。我也不是很懂这里有端口映射和端口触发，反正我是全部配置了一下。

   ![image-20250311103113189](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031263.png)

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031402.png" alt="image-20250311103124337" style="zoom:60%;" />



5. 详细编辑信息如下（ `注意打开自己电脑的3389端口或者22端口，主要是ubuntu需要在防火墙打开这个端口，不然一直报错都不知道是什么原因` ） 

   ![image-20250311103153133](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031182.png)



1. ## vscode里面远程仓库环境

1. 需要注意远程用户的读写权利，不然尽管远程了都没办法写入文件。
2. Vscode 下载插件remote-ssh服务，然后需要先将远程环境的信息写入config文件中：
   1. 在 SSH 配置文件 (~/.ssh/config) 中添加端口信息
      -   这里需要注意就是config文件，不是config.txt也不是config文件夹，直接用`touch config` 或者` vim config` 。 其中下面的hostname是电脑ip，user是登陆名字，这里注意权限问题就好。因为我是局域网暴露了路由器下的用户端口，所以需要额外指定为路由器的端口，比如8001、8002。

      - ```Shell
        Host 59.xx.xx.xx
                HostName 59.xx.xx.xxx
                User root
                Port xxxx
        ~                       
        ```

![image](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111032822.png)
