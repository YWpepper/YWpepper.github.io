---
title: 'how_to_use_remoteSSH'
lang: zh-CN
date: 2025-03-11
permalink: /posts/2025/03/how_to_use_remoteSSH/
tags:
  - ssh
  - sever
---
这篇博客介绍了如何在Ubuntu系统和路由器的局域网连接中，配置路由器的端口转发服务。

## 1. 配置路由器的端口转发服务

1. 首先ubuntu和路由器有一个局域的连接，路由器是大的，ubuntu电脑插到路由器上面，大的路由器会分配一个小的ip给到ubuntu，一般开头都是`192.168.xx.xx`,如果我在实验室里，因为全部都是在路由器的局域网下面，所以可以通过`192.168`来访问，但是由于学校又是一个再大一点的局域网，下面包裹着我的路由器，所以我在图书馆访问的时候就要访问路由器的`58.xx`开头的那个ip。
2. 打开 华为路由的ip：` http://192.168.3.1/` 这个应该每个人都一样，输入的密码就是wifi密码

<p align="center">
  <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029348.png" style="zoom:23%;" />
</p>




   3. 查看自己的终端信息：此处展示的只是有线连接，其实可以看到wifi连接的设备

      <p align="center">
      	<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111029748.png" alt="image-20250311102945687" style="zoom:30%;" />
      </p>



4. 在这里可以设置端口转发服务，我的理解是，把路由器下设备1的端口1，暴露出来作为路由器本身的端口2来访问，因为设备1无法在学校wifi下检索到，但是路由器归属学校wifi管理。我也不是很懂这里有端口映射和端口触发，反正我是全部配置了一下。

   

   <p align="center">
     <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031263.png" alt="image-20250311103113189" alt="Image 1" width="400" style="display: inline-block; margin-right: 10px;">
     <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031402.png" alt="image-20250311103124337"  alt="Image 2" width="500" style="display: inline-block;">
   </p>
   

5. 详细编辑信息如下

    `注意打开自己电脑的3389端口或者22端口
   `

   `主要是ubuntu需要在防火墙打开这个端口，不然一直报错都不知道是什么原因`

   

   <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111031182.png" alt="image-20250311103153133" style="zoom:20%;" />

### 1.1 有趣的端口开放

- 模型训练的时候为了查看tensorboard的可视化效果，由于ubuntu打开的是localhost:6006

   - 方法1 ： 如果只是同一个路由器的wifi下面，我可以直接使用命令行： 

     ​	 `tensorboard --logdir libcity/ --host 0.0.0.0`

      此处访问192.168.xxx即可

     <p align="center">
     <img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503122135974.png" alt="image-20250312213516786" style="zoom:35%;" />
     </p>

   - 方法2: 如果我在图书馆，即我只是在学校的大wifi下面，我还是需要在路由器上面映射端口6006出来

     此处我就可以访问 59.xxx开头的ip进行访问啦！

     <p align="center">
       	<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503122128505.png" alt="image-20250312212834388" style="zoom: 25%;" />
     </p>
     
     

## 2. vscode里面远程仓库环境

1. 需要注意远程用户的读写权利，不然尽管远程了都没办法写入文件。

2. Vscode 下载插件remote-ssh服务，然后需要先将远程环境的信息写入config文件中：
   1. 在 SSH 配置文件 (~/.ssh/config) 中添加端口信息
      - 这里需要注意就是config文件，不是config.txt也不是config文件夹，直接用`touch config` 或者` vim config` 。 其中下面的hostname是电脑ip，user是登陆名字，这里注意权限问题就好。因为我是局域网暴露了路由器下的用户端口，所以需要额外指定为路由器的端口，比如8001、8002。

        ```shell
        Host 59.xx.xx.xx
                HostName 59.xx.xx.xxx
                User root
                Port xxxx                    
        ```

<img src="https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202503111032822.png" alt="image" style="display: block; margin: 0 auto; zoom:30%;" />
