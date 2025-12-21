---
layout: post
title: 'How_to_downloadHF'
date: 2025-11-14
author: pepper
tags: [Dlenv,LLM]
comments: true
toc: true
pinned: false
---
这篇博客介绍了使用专用多线程下载器快速下载huggingface上的模型。
<!-- more -->

### 专用多线程下载器 hfd

**`hfd` 是基于 curl 和 aria2 实现的专用于huggingface 下载的命令行脚本：** [hfd.sh](https://link.zhihu.com/?target=https%3A//padeoe.com/file/hfd/hfd.sh)（[Gitst链接](https://link.zhihu.com/?target=https%3A//gist.github.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f)）。hfd 相比 `huggingface-cli` ，鲁棒性更好，此外多线程控制力度也更细，可以设置下载线程数、并行文件数。缺点是目前**仅适用于 Linux 和 Mac OS**。

其原理:
  - Step1：通过Hugging Face API获取模型/数据集仓库对应的所有文件 url；
  - Step2：利用 `aria2` 多线程下载文件。

该工具同样支持设置镜像端点的环境变量:

  ```bash
  export HF_ENDPOINT="https://hf-mirror.com"
  ```

**基本命令：**
  ```bash
  ./hfd.sh gpt2
  ```

如果没有安装 aria2，则可以改用 wget：

    ./hdf.sh bigscience/bloom-560m --tool wget

`--include` 指定下载特定文件

    # Qwen2.5-Coder下载q2_k量化版本的模型
    hfd Qwen/Qwen2.5-Coder-32B-Instruct-GGUF --include qwen2.5-coder-32b-instruct-q2_k.gguf
    # gpt2下载onnx路径下的所有json文件
    hfd gpt2 --include onnx/*.json 

`--exclude` 排除特定文件的下载

    # gpt2仓库，不下载.bin格式的模型以及onnx模型
    hfd gpt2 --exclude *.bin onnx/*

注意：语法方面，`--include a --include b` 和 `--include a b` 等价。

**完整命令格式：**

    $ ./hfd.sh --help
    用法:
      hfd <REPO_ID> [--include include_pattern1 include_pattern2 ...] [--exclude exclude_pattern1 exclude_pattern2 ...] [--hf_username username] [--hf_token token] [--tool aria2c|wget] [-x threads] [-j jobs] [--dataset] [--local-dir path]
    
    描述:
    使用提供的仓库ID从Hugging Face下载模型或数据集。
    
    参数:
    仓库ID          Hugging Face仓库ID(必需)
                    格式:'组织名/仓库名'或旧版格式(如 gpt2)
    选项:
    包含/排除模式    用于匹配文件路径的模式,支持通配符。
                     例如:'--exclude *.safetensor .md', '--include vae/*'。
    --include       (可选)指定要下载的文件包含模式(支持多个模式)。
    --exclude       (可选)指定要排除下载的文件模式(支持多个模式)。
    --hf_username   (可选)Hugging Face用户名用于认证(非邮箱)。
    --hf_token      (可选)Hugging Face令牌用于认证。
    --tool          (可选)使用的下载工具:aria2c(默认)或wget。
    -x              (可选)aria2c的下载线程数(默认:4)。
    -j              (可选)aria2c的并发下载数(默认:5)。
    --dataset       (可选)标记下载的是数据集。
    --local-dir     (可选)存储下载数据的目录路径。
                     默认下载到当前目录下以'仓库名'命名的子目录。(如果记仓库ID为'组织名/仓库名')。
    
    示例:
    hfd gpt2
    hfd bigscience/bloom-560m --exclude *.bin .msgpack onnx/
    hfd meta-llama/Llama-2-7b --hf_username myuser --hf_token mytoken -x 4
    hfd lavita/medical-qa-shared-task-v1-toy --dataset


多线程和并行下载：

hfd 在使用 aria2c 作为下载工具时，支持两种并行配置：

单文件线程数 (-x)：控制每个文件的连接数，用法：hfd gpt2 -x 8，建议值：4-8，默认：4 线程。限制最大为10，别开太多了，服务器压力太大了😂。
并发文件数 (-j)：控制同时下载的文件数，用法：hfd gpt2 -j 3，建议值：3-8，默认：5 个文件。限制最大为10，同上别开太大。
组合使用：

```bash
hfd gpt2 -x 8 -j 3  # 每个文件 8 个线程，同时下载 3 个文件
```

### 操作案例


1. 方法1 ： 获取并提供 Hugging Face 令牌

    步骤 1: 获取 Hugging Face 访问令牌 (Token)

    - 访问令牌设置页面： 前往 `https://huggingface.co/settings/tokens`
    - 创建新令牌： 点击 "New token" (新建令牌)。
    - 为令牌命名（例如 xinference-download）。
    - 选择 "Role"（角色）为 Read（读取），这是下载模型所需的最低权限。
    - 点击 "Generate a token"（生成令牌）。
    - 复制令牌： 令牌生成后只会显示一次，请务必将其复制并妥善保管。

    步骤 2: 使用令牌运行下载命令

    - 由于你的脚本提示需要传递 `--hf_username` 和 `--hf_token`，你可以修改你的下载命令，将用户名和令牌作为参数传入。  格式：

    ```shell
      ./hfd.sh 模型ID \--hf\_username 你的用户名 \--hf\_token 你的令牌 \--exclude ...
    ```

    示例（请替换为你自己的信息）：

    ```bash
     ./hfd.sh meta-llama/Llama-2-7b \--hf\_username 你的HuggingFace用户名 \--hf\_token 你复制的令牌 \--exc
    ```

2. 方法2 ：使用 `huggingface-cli login`

    如果你的 `./hfd.sh` 脚本底层是调用 `huggingface_hub` 库，那么你可以先在终端中执行登录命令，让系统记住你的凭证：

    登录： 在终端中运行以下命令：

    ```bash
    huggingface-cli login
    ```

    输入令牌： 系统会提示你输入在步骤 1 中获取的 Hugging Face 令牌。

    ```bash
    git config --global credential.helper store
    # 存储地方
    cat /home/peper/.cache/huggingface/token
    ```

    重新运行下载： 登录成功后，再次运行你的原始下载命令：

    ```bash
    # 可以手动限制下载的内容
    ./hfd.sh meta-llama/Llama-2-7b --exclude \*.bin \*.msgpack onnx/
    ```


ps： 参考[知乎指南1](https://zhuanlan.zhihu.com/p/663712983)

---