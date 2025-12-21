---
title: 'how_to_install_latex'
lang: zh-CN
date: 2025-11-02
author: pepper
pinned: false
toc: true
tags:
  - ssh
  - sever
---
这篇博客介绍了安装和配置VSCode+LaTeX(含环境变量_配置_详细过程)
<!-- more -->


[安装和_配置_VSCode+_LaTeX_(含环境变量_配置_详细过程)](https://zhuanlan.zhihu.com/p/637046509)

## Windows

### 1. 下载TeX Live

清华镜像：

| 镜像源 | 链接 |
|--------|------|
| 清华大学 | [https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/) |
| 镜像2 | [https://mirror-hk.koddos.net/CTAN/systems/texlive/Images/](https://mirror-hk.koddos.net/CTAN/systems/texlive/Images/) |
| 镜像3 | [https://mirrors.aliyun.com/CTAN/systems/texlive/Images/?userCode=okjhlpr5](https://mirrors.aliyun.com/CTAN/systems/texlive/Images/?userCode=okjhlpr5) |

推荐使用清华大学开源软件镜像站：[Index of /CTAN/systems/texlive/Images/](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)

![选择版本](https://pic3.zhimg.com/v2-ba9e4144613807cc8060928e3b797460_1440w.jpg)

下载开始，过程有些慢。（可以把链接复制到迅雷里会快一些）

---

---

### 2. 安装texlive
2.1 双击(或者 鼠标右键->打开方式:文件任务管理器)

![](https://pica.zhimg.com/v2-ce182325403752f04fd283ac7a4161c8_1440w.jpg)

2.2 找到 `install-tl-windows.bat` 文件,双击

![](https://pic2.zhimg.com/v2-dd43f01034bec373c94396e404fbfa07_1440w.jpg)

安装

2.3 更改一些安装配置

![](https://pic4.zhimg.com/v2-62b352617f91ba6bb254b63e30f95bd1_1440w.jpg)

自定义安装

修改一些安装内容,控制内存...

记得可以自定义安装位置(我这里没截图,路径最好不要有中文),**记住路径,后面配置环境变量需要**

![](https://picx.zhimg.com/v2-68e612a066aa381759300d5350f9d33d_1440w.jpg)

控制内存

我选择删去了一些国家的语言和TexWorks editor等内容(因为我要用VSCode编辑LaTeX)

![](https://pica.zhimg.com/v2-b4ac4d1571e772e9150fb7fa0edba4d8_1440w.jpg)

最后大概的样子(Greek为希腊语,可能会用到一些符号,就没删)

![](https://pic1.zhimg.com/v2-3ff955c65cc1e898060831e512e288ae_1440w.jpg)

自定义后的截图

点击安装..过程会很慢很慢

![](https://picx.zhimg.com/v2-b86996996492f012dae91f6e3acb80f7_1440w.jpg)

安装完成

查看环境变量是否可用:

`Win + R` 打开命令面板:`tex -v` 查看环境变量是否可用.

以下截图是环境变量正确的..无需进行`2.4`操作

其实是要查看四个环境(但一个好,其他的都好了)

```bash
tex -v
latex -v
xelatex -v
pdflatex -v
```

![](https://pic3.zhimg.com/v2-f197d83ae94c670339194fee8a42055e_1440w.jpg)

2.4 配置环境变量!(<font style="color:#DF2A3F;">我是先配置了path然后才能在终端里检索到，检索到之后就没关系了</font>)

我的电脑-->属性(左上角or鼠标右键)-->高级系统设置-->环境变量-->系统变量Path-->双击Path

![](https://pic1.zhimg.com/v2-dbabd09e0641215aea06b14c59338370_1440w.jpg)

添加环境变量

![](https://pic1.zhimg.com/v2-1f92f31de257d505e2c689fc0e60d10a_1440w.jpg)

我这里出现的问题是安装时**自动配置的变量路径不对**!正确路径:`E:\texlive\2023\bin\windows` (这个路径是自己在`2.3`步骤中自定义的位置下的,可以找到那个文件夹,继续单击,知道出现`bin\win`即可,也可能是`\bin\windows`都可以)

一定要在`....\bin\win`后面

再次`Win + R`打开命令面板:`tex -v` 查看环境变量是否可用

![](https://pic3.zhimg.com/v2-f197d83ae94c670339194fee8a42055e_1440w.jpg)

环境变量可用

再次输入其他命令查看环境变量:

```shell
tex -v
latex -v
xelatex -v
pdflatex -v
```

应该都没有问题了..环境变量配置成功

---

### 3. 安装VSCode
3.1 官网下载:[Download Visual Studio Code - Mac, Linux, Windows](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/Download)

3.2 安装[LaTeX插件](https://zhida.zhihu.com/search?content_id=229697152&content_type=Article&match_order=1&q=LaTeX%E6%8F%92%E4%BB%B6&zhida_source=entity)

![](https://pica.zhimg.com/v2-1122f25968a9066f7d98ff8dac274ed8_1440w.jpg)

安装插件

3.3 写内容

文件拓展名为`.tex`,随意写一些内容

```latex
\documentclass{article} % 文档类别：文章
\usepackage{amsmath}     % 引入 amsmath 宏包，用于更高级的数学排版
\usepackage{ctex}

\title{一个简单的带公式的文档} % 标题
\author{AI 助手}             % 作者
\date{\today}             % 日期为当前日期

\begin{document} % 文档主体开始

\maketitle % 生成标题

\section{介绍} % 第一节

这是一个简单的 \LaTeX{} 文档，展示了如何插入行内公式和独立公式。

\section{数学公式} % 第二节

\subsection{行内公式} % 第二节的子节

一个简单的行内公式，例如欧拉恒等式 $e^{i\pi} + 1 = 0$，可以像这样嵌入到文本中。

\subsection{独立公式} % 第二节的另一个子节

更复杂的公式通常会独立一行并自动编号。例如，二次方程的求根公式为：
\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\label{eq:quadratic} % 给公式添加标签，方便引用
\end{equation}
我们可以通过引用 \ref{eq:quadratic} 来提及这个公式。

另一个不带编号的独立公式:
\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]

\end{document} % 文档主体结束
```

![](https://pica.zhimg.com/v2-a37254883f966aac3878d4ebaa8b9e96_1440w.jpg)

正确内容截图,注意左侧的文件栏

以上,**VSCode配置LaTeX完整!**

**附:**

1. 若出现以下问题是环境变量问题.

![](https://pica.zhimg.com/v2-438677a48643986a9107ad5d7d50201a_1440w.jpg)

环境变量导致的出错

2. 有的参考教程改了json文件.不改也行,有想法的可以参考他人的进行修改

安装好环境和插件只是一小步,这里放两个大佬的帖子,很详细(比我的强太多了,但我比他们多了环境变量的配置,算是特点吧)

1. 超强配置:[Visual Studio Code (vscode)配置LaTeX - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/166523064)

2. 补充1中反向搜索出错的问题:[VSCode中LaTeX和SumatraPDF双向搜索 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/95330916)

3. 同2:[Latex+VSCode 正向搜索和反向搜索 | Jintao Lee (jintaolee-roger.github.io)](https://link.zhihu.com/?target=https%3A//jintaolee-roger.github.io/posts/latexsearch/)

 

### 4 vscode 配置环境
```json
"latex-workshop.latex.tools": [
  {
    // 编译工具和命令
    "name": "xelatex",
    "command": "xelatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "-pdf",
      "%DOCFILE%"
    ]
  },
  {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
      "-synctex=1",
      "-interaction=nonstopmode",
      "-file-line-error",
      "%DOCFILE%"
    ]
  },
  {
    "name": "bibtex",
    "command": "bibtex",
    "args": [
      "%DOCFILE%"
    ]
  }
],
// 用于配置编译链
"latex-workshop.latex.recipes": [
  {
    "name": "xelatex",
    "tools": [
      "xelatex"
    ],
  },
  {
    "name": "pdflatex",
    "tools": [
      "pdflatex"
    ]
  },
  {
    "name": "xe->bib->xe->xe",
    "tools": [
      "xelatex",
      "bibtex",
      "xelatex",
      "xelatex"
    ]
  },
  {
    "name": "pdf->bib->pdf->pdf",
    "tools": [
      "pdflatex",
      "bibtex",
      "pdflatex",
      "pdflatex"
    ]
  }
],
```



### 5 latex测试模板
```latex
\documentclass{article} % 文档类别：文章
\usepackage{amsmath}     % 引入 amsmath 宏包，用于更高级的数学排版
\usepackage{ctex}

\title{一个简单的带公式的文档} % 标题
\author{AI 助手}             % 作者
\date{\today}             % 日期为当前日期

\begin{document} % 文档主体开始

\maketitle % 生成标题

\section{介绍} % 第一节

这是一个简单的 \LaTeX{} 文档，展示了如何插入行内公式和独立公式。

\section{数学公式} % 第二节

\subsection{行内公式} % 第二节的子节

一个简单的行内公式，例如欧拉恒等式 $e^{i\pi} + 1 = 0$，可以像这样嵌入到文本中。

\subsection{独立公式} % 第二节的另一个子节

更复杂的公式通常会独立一行并自动编号。例如，二次方程的求根公式为：
\begin{equation}
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\label{eq:quadratic} % 给公式添加标签，方便引用
\end{equation}
我们可以通过引用 \ref{eq:quadratic} 来提及这个公式。

另一个不带编号的独立公式:
\[
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
\]

\end{document} % 文档主体结束
```

## Linux


#### 1 安装linux版本 [7-zip](https://zhida.zhihu.com/search?content_id=722097146&content_type=Answer&match_order=1&q=7-zip&zhida_source=entity)
1 . 需要提前在linux中安装镜像解压器pzzip，也就是7-zip的linux版本：

```bash
 apt install p7zip-full
```

#### 2. 安装texlive

1 . 首先使用wget 安装镜像：

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive.iso
```

2 . 使用7-z进行镜像的解压

```bash
7z x texlive.iso
```

3 . 解压后进行安装

```bash
 chmod 777 install-tl && ./install-tl   
安装过程需要注意，使用B可以选择二进制的版本，linux则要安装linux对应的版本
使用D可以设置安装路径
R指令是返回
I指令是执行安装（安装过程时间较长，大概50分钟左右，如果是SSH远程连接服务器建议使用tmux来进行）
```

一般上面我不修改安装路径

4 . 安装完成texlive之后，可以进行相关环境变量的配置

```bash
vim ~/.bashrc
export PATH=your/Path/bin:$PATH 
export MANPATH=your/Path/doc/man:$MANPATH 
export INFOPATH=your/Path/doc/info:$INFOPATH
```

一般默认路径命令：

```bash
# TeX Live 2025 环境变量配置
export PATH=/usr/local/texlive/2025/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/texlive/2025/texmf-dist/doc/man:$MANPATH
export INFOPATH=/usr/local/texlive/2025/texmf-dist/doc/info:$INFOPATH
```

5 . 最后source ~/.bashrc进行使用

```bash
source ~/.bashrc
which xelatex
```

6. vscode里面下面l插件： LaTeX Workshop


```cpp
 ----------------------------------------------------------------------
Welcome to TeX Live!
See /usr/local/texlive/2025/index.html for links to documentation.

The TeX Live web site (https://tug.org/texlive/) provides all updates
and corrections. TeX Live is a joint project of the TeX user groups
around the world; please consider supporting it by joining the group
best for you. The list of groups is available on the web
at https://tug.org/usergroups.html.

Add /usr/local/texlive/2025/texmf-dist/doc/man to MANPATH.
Add /usr/local/texlive/2025/texmf-dist/doc/info to INFOPATH.
Most importantly, add /usr/local/texlive/2025/bin/x86_64-linux
to your PATH for current and future sessions.

Logfile: /usr/local/texlive/2025/install-tl.log
```




---