---
title: '工具-GitHub-Pages与Jekyll搭建'
lang: zh-CN
date: 2025-02-07
author: pepper
permalink: /posts/2025/02/how_to_make_GitubwithJekyll_in_windows/
toc: true
pinned: false
tags: [jekyll, github]
---

这篇博客介绍了如何在gitubPage上的学术网站（个人学术页面）。
<!-- more -->

## github页面注意事项

**1. 创建了一个地图统计**
开源项目的地址为: [地址](https://mapmyvisitors.com/profile)
创建过程：
    - A. 如果你更喜欢静态的、简约的平面地图，可以使用 ClustrMaps：
    - B. 前往 ClustrMaps 官网。
    - C.输入你的博客地址 https://ywpepper.github.io。
    - D.它会生成一段类似 `<script...>` 的代码。
    - E. 将该代码直接粘贴在 about.md 的最下方。

**2. 创建一个访客统计**
- A. 方案一：使用 HITS (样式简洁，支持多种配色) 
这是目前 GitHub 开源项目中最常用的访问量统计插件。

- B. 代码模板： 将以下代码复制到你的 about.md 最下方：

```html
![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FYWpepper%2FHomeNotebook&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)
```
    
`url=:` 后面接你仓库的地址（需要经过 URL 编码，上面代码中已经帮你替换为你的仓库名）。

`count_bg=:` 右侧数字框的颜色。

`title_bg=:` 左侧标题框的颜色。


## 如何部署
1. 在 GitHub 上创建一个新的仓库，命名为 `yourusername.github.io`，其中 `yourusername` 是你的 GitHub 用户名。

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1766303759895-68854205-4e4c-4026-882c-375e0c6946ee.png?x-oss-process=image%2Fformat%2Cwebp" width="80%" alt="FinRpt Framework Diagram"/>

1. 克隆该仓库到本地计算机。
2. 修改右侧website的配置文件 `_config.yml`，根据你的需求进行调整。
3. 将你的 Jekyll 网站文件添加到仓库中。
<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1766303789252-529bc406-9fe5-49bb-8395-b8fee6195f77.png?x-oss-process=image%2Fformat%2Cwebp" width="80%" alt="FinRpt Framework Diagram"/>

1. 更重要的是那个conig文件
    ```yaml
    utteranc:
    repo: ywpepper/ywpepper.github.io # 替换为你的 GitHub 仓库名
    issue-term: title
    label: comment
    theme: github-dark
    crossorigin: anonymous
    ```


## Ruby+Jekylls
**前言：** 当初学习这方面的知识主要是因为涉及到gitubPage上的学术网站（个人学术页面），发现gitub可以自动渲染出来，但是在**本地想要渲染就需要自己搭建开发环境**，经过这次学习对于**不同开发语言需要的环境编译器**能有更深的认识，因为所有的编译都是需要一个编译库，我们需要在官网下载对应的编译库，同时由于现在已经一键配置了PATH的开发环境，所以可以在终端直接使用ruby语言，ruby和python也比较类似，小众和大流的区别。

Ruby类似脚本语言，而Jekyll，作为Ruby的明星项目之一，是一款静态网站生成器，它允许用户使用纯文本格式编写内容，并通过模板引擎生成结构化的静态网站。两者结合，为开发者提供了一种高效、灵活的网站构建方式。

* **Ruby + Jekylls 的应用场景**

  1. **个人博客**：利用Jekyll的博客功能和Ruby的灵活性，快速搭建个人博客，展示个人作品和分享知识。

  2. **项目文档**：通过Markdown编写项目文档，使用Jekyll生成静态网站，方便团队成员和用户查阅。

  3. **公司官网**：结合Ruby的后端开发能力 и Jekyll的静态生成优势，打造高性能、易维护的公司官网。

  4. **开源项目展示**：利用Jekyll的插件系统，集成GitHub等开源平台，展示开源项目和个人贡献。

## 上手步骤

1. 下载ruby+devkit

2. Ruby 版本稳定后，就可以安裝 Jekyll 了
  
    ```bash
    gem install jekyll 
    ```

3. 安装bundler

    ```bash
    gem install bundler
    ```

4. 安装配置文件的需要

    ```bash
     bundle install
    ```

5. 直接运行

    ```bash
    bundle exec jekyll server
    ```

## 官网资源

  1. 下载Ruby [官网link](https://rubyinstaller.org/) [下载link](https://rubyinstaller.org/downloads/) DevKit 是一个为 Windows 平台提供编译功能的工具集

     这是我下载的版本 \

    <Center>
    <img src='/images/blog/01/1.png' style='zoom:50%'>
    </Center>

  2. Ruby的函数打包下载器叫做 Gem,类似python和conda中的pip，或者一些叫做npm，apt-get等等。 <https://rubygems.org/> 以及镜像 <https://index.ruby-china.com/>

## 常见命令

* 更新 Ruby 和 Bundler

    ```bash
    gem update --system
    gem install bundle
    ```

* 清除 Bundler 缓存

    ```bash
    bundle clean --force
    ```

* 查看 Jekyll 日志

    ```bash
    jekyll build --trace
    ```

* 检查 Gemfile 和 Gemfile.lock

    ```bash
    ## 确保 Gemfile 和 Gemfile.lock 文件没有冲突。
    ## 如果需要，可以尝试删除 Gemfile.lock 并重新运行 bundle install：
    rm Gemfile.lock
    bundle install
    ```

* 强制删除下载失败的安装包，需要打开cmd的管理员模式

    ```bash
    # 自己更换路径
    rd /s /q E:\Ruby31\lib\ruby\gems\3.1.0\gems\nokogiri-1.18.2
    ```

* 修改编译器标志

    ```bash
    # 有时，编译器标志可能会导致这些问题。
    # 您可以尝试在安装 gem 时添加编译器标志来忽略某些警告。例如：
    gem install wdm -- --with-cflags="-Wno-error=implicit-function-declaration"
    ```

* 启动Ruby安装程序

    ```bash
    # 似乎可以用来更新某些安装包        
    ridk install
    ```

    <Center>
    <img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873049879-14808f28-9a50-4ee6-91c8-6ebdcdb39a3a.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
    </Center>

### Debug报错

现在才发现这个仓库的**配置文件更新**了，呜呜，之前自己一直有一个包安不上去
    <Center>
    <img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873066326-bf0a17d3-50aa-4341-b2a7-5c227d32fae3.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
    </Center>

无法安装的包如下，报错如下：
    <Center>
    <img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873095186-b69af19e-a559-4306-9c66-c9915b8d87d9.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
    </Center>

配置文件原本如下:
    <Center>
    <img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873168809-8a4d0723-158d-49ea-889f-ec17ab5cf60b.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
    </Center>

通过我全部这个配置文件，然后一个一个的加入报错的需要，就避开了那个魔法包:
    <Center>
    <img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873188694-21fe1da0-4181-48f3-9465-1ddae6476f83.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
    </Center>

修改后的配置文件:

``` bash
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

ruby镜像地址：<https://index.ruby-china.com/>

```bash
bundle config mirror.https://rubygems.org https://gems.ruby-china.com/
## 或者清华镜像
bundle config mirror.https://rubygems.org https://mirrors.tuna.tsinghua.edu.cn/rubygems/
```

设置完成后，可以运行以下命令来验证是否已成功更改镜像源：

``` bash
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
<img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873258271-5310cc62-5963-429a-b1a6-662280f57cd3.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
</Center>

**国外的Ruby大会** [link](https://rubycommunityconference.konfeo.com/en/groups)
<center>
<img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873271153-b2fc1ac3-b7f7-47f9-a448-34e16e7d10bc.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
<img src='https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762873289115-bba3d649-7104-41e5-af9f-47d2040942ab.png?x-oss-process=image%2Fformat%2Cwebp' style='zoom:50%'>
</center>

---
