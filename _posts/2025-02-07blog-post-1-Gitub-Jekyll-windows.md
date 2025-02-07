---
title: 'Gitub + Jekyll + windows指南'
lang: zh-CN
date: 2025-02-07
permalink: /posts/2025/02/blog-post-1-Gitub-Jekyll-windows/
tags:
  - cool posts
  - category1
  - category2
---

**前言：** 当初学习这方面的知识主要是因为涉及到gitubPage上的学术网站（个人学术页面），发现gitub可以自动渲染出来，但是在**本地想要渲染就需要自己搭建开发环境**，经过这次学习对于**不同开发语言需要的环境编译器**能有更深的认识，因为所有的编译都是需要一个编译库，我们需要在官网下载对应的编译库，同时由于现在已经一键配置了PATH的开发环境，所以可以在终端直接使用ruby语言，ruby和python也比较类似，小众和大流的区别。

## Ruby+Jekylls

Ruby类似脚本语言，而Jekyll，作为Ruby的明星项目之一，是一款静态网站生成器，它允许用户使用纯文本格式编写内容，并通过模板引擎生成结构化的静态网站。两者结合，为开发者提供了一种高效、灵活的网站构建方式。

* **Ruby + Jekylls 的应用场景**

  1. **个人博客**：利用Jekyll的博客功能和Ruby的灵活性，快速搭建个人博客，展示个人作品和分享知识。

  2. **项目文档**：通过Markdown编写项目文档，使用Jekyll生成静态网站，方便团队成员和用户查阅。

  3. **公司官网**：结合Ruby的后端开发能力 и Jekyll的静态生成优势，打造高性能、易维护的公司官网。

  4. **开源项目展示**：利用Jekyll的插件系统，集成GitHub等开源平台，展示开源项目和个人贡献。



## **上手步骤**

1. 下载ruby+devkit

2. Ruby 版本稳定后，就可以安裝 Jekyll 了
  
    ```plain&#x20;text
    gem install jekyll 
    ```

3. 安装bundler

    ```plain&#x20;text
    gem install bundler
    ```

4. 安装配置文件的需要

    ```plain&#x20;text
     bundle install
    ```

5. 直接运行

    ```plain&#x20;text
    bundle exec jekyll server
    ```

## **官网资源**

  1. 下载Ruby [官网link](https://rubyinstaller.org/) [下载link](https://rubyinstaller.org/downloads/) DevKit 是一个为 Windows 平台提供编译功能的工具集

     这是我下载的版本 \
    <Center>
    <img src='/images/blog/01/1.png' style='zoom:50%'>
    </Center>


  2. Ruby的函数打包下载器叫做 Gem,类似python和conda中的pip，或者一些叫做npm，apt-get等等。 https://rubygems.org/ 以及镜像 https://index.ruby-china.com/



## **常见命令**

  * 更新 Ruby 和 Bundler

    ```plain&#x20;text
    gem update --system
    gem install bundle
    ```

  * 清除 Bundler 缓存

    ```plain&#x20;text
    bundle clean --force
    ```

  * 查看 Jekyll 日志

    ```plain&#x20;text
    jekyll build --trace
    ```

  * 检查 Gemfile 和 Gemfile.lock

    ```plain&#x20;text
    ## 确保 Gemfile 和 Gemfile.lock 文件没有冲突。
    ## 如果需要，可以尝试删除 Gemfile.lock 并重新运行 bundle install：
    rm Gemfile.lock
    bundle install
    ```

  * 强制删除下载失败的安装包，需要打开cmd的管理员模式

    ```plain&#x20;text
    # 自己更换路径
    rd /s /q E:\Ruby31\lib\ruby\gems\3.1.0\gems\nokogiri-1.18.2
    ```

  * 修改编译器标志

      ```plain&#x20;text
      ## 有时，编译器标志可能会导致这些问题。
      ## 您可以尝试在安装 gem 时添加编译器标志来忽略某些警告。例如：
      gem install wdm -- --with-cflags="-Wno-error=implicit-function-declaration"
      ```

  * 启动Ruby安装程序

      ```plain&#x20;text
      # 似乎可以用来更新某些安装包        
      ridk install
      ```
    <Center>
    <img src='/images/blog/01/2.png' style='zoom:50%'>
    </Center>

### Debug报错
现在才发现这个仓库的**配置文件更新**了，呜呜，之前自己一直有一个包安不上去
    <Center>
    <img src='/images/blog/01/3.png' style='zoom:50%'>
    </Center>

无法安装的包如下，报错如下：
    <Center>
    <img src='/images/blog/01/4.png' style='zoom:50%'>
    </Center>

配置文件原本如下:
    <Center>
    <img src='/images/blog/01/5.png' style='zoom:50%'>
    </Center>

通过我全部这个配置文件，然后一个一个的加入报错的需要，就避开了那个魔法包:
    <Center>
    <img src='/images/blog/01/6.png' style='zoom:50%'>
    </Center>

修改后的配置文件:
  
``` plain&#x20;text
    source "https://rubygems.org"
    gem 'tzinfo'
    gem 'tzinfo-data'
    gem 'jekyll-paginate'
    gem 'jekyll-sitemap'
    gem 'jekyll-gist'
    gem 'jekyll-feed'
    gem 'jekyll-redirect-from'
    gem 'jekyll', '~> 4.4.1'
    # ... 其他依赖 ...
  ```


### Tipss&#x20;

**设置镜像**

选择一个国内的RubyGems镜像源，例如Ruby China的镜像源。

ruby镜像地址：https://index.ruby-china.com/

```plain&#x20;text
bundle config mirror.https://rubygems.org https://gems.ruby-china.com/
## 或者清华镜像
bundle config mirror.https://rubygems.org https://mirrors.tuna.tsinghua.edu.cn/rubygems/
```

设置完成后，可以运行以下命令来验证是否已成功更改镜像源：

``` plain&#x20;text
bundle config
```



### Others

看了一下ruby的官网有一些会议举办非常有意思记录一下，比较类似小众的爱好，感觉国外的讨论风格还是很有意思的，一种不孤独的研究。

**女性交流** [link](https://dcn8hodqlmqo.feishu.cn/wiki/NPmXwubu8iPaDMkR7WUcJTaMn8g?fromScene=spaceOverview#share-VFLNdLaqooXdsHxgAUUcwh1FnZg)
<Center>
<img src='/images/blog/01/7.png' style='zoom:50%'>
</Center>

**中国的交流会** [link](https://groups.google.com/g/shanghaionrails?pli=1)
一个google群组，第一次发现还有如此好玩的东西
<Center>
<img src='/images/blog/01/8.png' style='zoom:50%'>
</Center>

**国外的Ruby大会** [link](https://rubycommunityconference.konfeo.com/en/groups)
<center>
<img src='/images/blog/01/9.png' style='zoom:50%'>
<img src='/images/blog/01/10.png' style='zoom:50%'>
</center>

------
