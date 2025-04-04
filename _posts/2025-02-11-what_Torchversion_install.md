---
title: 'what_Torchversion_install'
lang: zh-CN
date: 2025-02-11
permalink: /posts/2025/02/what_Torchversion_install/
tags:
  - daily
---
这篇博客介绍了如何安装和使用 PyTorch 最新版本，同时提供了旧版本的安装指南，帮助用户根据需求快速开始机器学习开发。

---
We’d prefer you install the [latest version](https://pytorch.org/get-started/locally), but old binaries and installation instructions are provided below for your convenience.

记得给conda换源，终端脚本：
```shell 
# 生成.condarc配置文件（如果不存在）
conda config --set show_channel_urls yes

# 添加清华镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

# 设置搜索时显示通道地址
conda config --set show_channel_urls yes

# 清除索引缓存
conda clean -i
```

手动操作：
```
nano ~/.condarc
# 粘贴
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
或者在指定安装源：
```
pip install ray fastdtw tslearn torch_geometric  tqdm -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install  "ray[tune]"  -i http://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com
```

## Commands for Versions >= 1.0.0[](https://pytorch.org/get-started/previous-versions/#commands-for-versions--100)

### v2.5.1[](https://pytorch.org/get-started/previous-versions/#v251)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx)

    # conda
    conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows)

    # CUDA 11.8
    conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1  pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CUDA 12.4
    conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.4 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-1)

    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-1)

    # ROCM 6.1 (Linux only)
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/rocm6.1
    # ROCM 6.2 (Linux only)
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/rocm6.2
    # CUDA 11.8
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121
    # CUDA 12.4
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124
    # CPU only
    pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
    

### v2.5.0[](https://pytorch.org/get-started/previous-versions/#v250)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-1)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-2)

    # conda
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-2)

    # CUDA 11.8
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0  pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CUDA 12.4
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 pytorch-cuda=12.4 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-1)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-3)

    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-3)

    # ROCM 6.1 (Linux only)
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/rocm6.1
    # ROCM 6.2 (Linux only)
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/rocm6.2
    # CUDA 11.8
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu121
    # CUDA 12.4
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cu124
    # CPU only
    pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 --index-url https://download.pytorch.org/whl/cpu
    

### v2.4.1[](https://pytorch.org/get-started/previous-versions/#v241)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-2)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-4)

    # conda
    conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-4)

    # CUDA 11.8
    conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1  pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CUDA 12.4
    conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-2)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-5)

    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-5)

    # ROCM 6.1 (Linux only)
    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/rocm6.1
    # CUDA 11.8
    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu121
    # CUDA 12.4
    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124
    # CPU only
    pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cpu
    

### v2.4.0[](https://pytorch.org/get-started/previous-versions/#v240)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-3)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-6)

    # conda
    conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-6)

    # CUDA 11.8
    conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0  pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CUDA 12.4
    conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.4 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-3)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-7)

    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-7)

    # ROCM 6.1 (Linux only)
    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/rocm6.1
    # CUDA 11.8
    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu121
    # CUDA 12.4
    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cu124
    # CPU only
    pip install torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cpu
    

### v2.3.1[](https://pytorch.org/get-started/previous-versions/#v231)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-4)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-8)

    # conda
    conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-8)

    # CUDA 11.8
    conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-4)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-9)

    pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-9)

    # ROCM 6.0 (Linux only)
    pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/rocm6.0
    # CUDA 11.8
    pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 --index-url https://download.pytorch.org/whl/cpu
    

### v2.3.0[](https://pytorch.org/get-started/previous-versions/#v230)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-5)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-10)

    # conda
    conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-10)

    # CUDA 11.8
    conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-5)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-11)

    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-11)

    # ROCM 6.0 (Linux only)
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/rocm6.0
    # CUDA 11.8
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cpu
    

### v2.2.2[](https://pytorch.org/get-started/previous-versions/#v222)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-6)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-12)

    # conda
    conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-12)

    # CUDA 11.8
    conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-6)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-13)

    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-13)

    # ROCM 5.7 (Linux only)
    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/rocm5.7
    # CUDA 11.8
    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
    

### v2.2.1[](https://pytorch.org/get-started/previous-versions/#v221)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-7)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-14)

    # conda
    conda install pytorch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-14)

    # CUDA 11.8
    conda install pytorch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-7)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-15)

    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-15)

    # ROCM 5.7 (Linux only)
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/rocm5.7
    # CUDA 11.8
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --index-url https://download.pytorch.org/whl/cpu
    

### v2.2.0[](https://pytorch.org/get-started/previous-versions/#v220)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-8)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-16)

    # conda
    conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-16)

    # CUDA 11.8
    conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-8)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-17)

    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-17)

    # ROCM 5.6 (Linux only)
    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/rocm5.6
    # CUDA 11.8
    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu
    

### v2.1.2[](https://pytorch.org/get-started/previous-versions/#v212)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-9)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-18)

    # conda
    conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-18)

    # CUDA 11.8
    conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-9)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-19)

    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-19)

    # ROCM 5.6 (Linux only)
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/rocm5.6
    # CUDA 11.8
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cpu
    

### v2.1.1[](https://pytorch.org/get-started/previous-versions/#v211)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-10)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-20)

    # conda
    conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-20)

    # CUDA 11.8
    conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-10)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-21)

    pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-21)

    # ROCM 5.6 (Linux only)
    pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/rocm5.6
    # CUDA 11.8
    pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cpu
    

### v2.1.0[](https://pytorch.org/get-started/previous-versions/#v210)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-11)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-22)

    # conda
    conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-22)

    # CUDA 11.8
    conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CUDA 12.1
    conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-11)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-23)

    pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-23)

    # ROCM 5.6 (Linux only)
    pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/rocm5.6
    # CUDA 11.8
    pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118
    # CUDA 12.1
    pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu121
    # CPU only
    pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu
    

### v2.0.1[](https://pytorch.org/get-started/previous-versions/#v201)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-12)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-24)

    # conda
    conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-24)

    # CUDA 11.7
    conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
    # CUDA 11.8
    conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-12)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-25)

    pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-25)

    # ROCM 5.4.2 (Linux only)
    pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/rocm5.4.2
    # CUDA 11.7
    pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
    # CUDA 11.8
    pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
    # CPU only
    pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cpu
    

### v2.0.0[](https://pytorch.org/get-started/previous-versions/#v200)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-13)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-26)

    # conda
    conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-26)

    # CUDA 11.7
    conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia
    # CUDA 11.8
    conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-13)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-27)

    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-27)

    # ROCM 5.4.2 (Linux only)
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/rocm5.4.2
    # CUDA 11.7
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1
    # CUDA 11.8
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
    # CPU only
    pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cpu
    

### v1.13.1[](https://pytorch.org/get-started/previous-versions/#v1131)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-14)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-28)

    # conda
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-28)

    # CUDA 11.6
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
    # CUDA 11.7
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-14)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-29)

    pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-29)

    # ROCM 5.2 (Linux only)
    pip install torch==1.13.1+rocm5.2 torchvision==0.14.1+rocm5.2 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/rocm5.2
    # CUDA 11.6
    pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
    # CUDA 11.7
    pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
    # CPU only
    pip install torch==1.13.1+cpu torchvision==0.14.1+cpu torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cpu
    

### v1.13.0[](https://pytorch.org/get-started/previous-versions/#v1130)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-15)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-30)

    # conda
    conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-30)

    # CUDA 11.6
    conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 pytorch-cuda=11.6 -c pytorch -c nvidia
    # CUDA 11.7
    conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 pytorch-cuda=11.7 -c pytorch -c nvidia
    # CPU Only
    conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-15)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-31)

    pip install torch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-31)

    # ROCM 5.2 (Linux only)
    pip install torch==1.13.0+rocm5.2 torchvision==0.14.0+rocm5.2 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/rocm5.2
    # CUDA 11.6
    pip install torch==1.13.0+cu116 torchvision==0.14.0+cu116 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu116
    # CUDA 11.7
    pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu117
    # CPU only
    pip install torch==1.13.0+cpu torchvision==0.14.0+cpu torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cpu
    

### v1.12.1[](https://pytorch.org/get-started/previous-versions/#v1121)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-16)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-32)

    # conda
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-32)

    # CUDA 10.2
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=10.2 -c pytorch
    # CUDA 11.3
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.3 -c pytorch
    # CUDA 11.6
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge
    # CPU Only
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-16)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-33)

    pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-33)

    # ROCM 5.1.1 (Linux only)
    pip install torch==1.12.1+rocm5.1.1 torchvision==0.13.1+rocm5.1.1 torchaudio==0.12.1 --extra-index-url  https://download.pytorch.org/whl/rocm5.1.1
    # CUDA 11.6
    pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
    # CUDA 11.3
    pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
    # CUDA 10.2
    pip install torch==1.12.1+cu102 torchvision==0.13.1+cu102 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu102
    # CPU only
    pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cpu
    

### v1.12.0[](https://pytorch.org/get-started/previous-versions/#v1120)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-17)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-34)

    # conda
    conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-34)

    # CUDA 10.2
    conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=10.2 -c pytorch
    # CUDA 11.3
    conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch
    # CUDA 11.6
    conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.6 -c pytorch -c conda-forge
    # CPU Only
    conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-17)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-35)

    pip install torch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-35)

    # ROCM 5.1.1 (Linux only)
    pip install torch==1.12.0+rocm5.1.1 torchvision==0.13.0+rocm5.1.1 torchaudio==0.12.0 --extra-index-url  https://download.pytorch.org/whl/rocm5.1.1
    # CUDA 11.6
    pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116
    # CUDA 11.3
    pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113
    # CUDA 10.2
    pip install torch==1.12.0+cu102 torchvision==0.13.0+cu102 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu102
    # CPU only
    pip install torch==1.12.0+cpu torchvision==0.13.0+cpu torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cpu
    

### v1.11.0[](https://pytorch.org/get-started/previous-versions/#v1110)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-18)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-36)

    # conda
    conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-36)

    # CUDA 10.2
    conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch
    
    # CPU Only
    conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-18)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-37)

    pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-37)

    # ROCM 4.5.2 (Linux only)
    pip install torch==1.11.0+rocm4.5.2 torchvision==0.12.0+rocm4.5.2 torchaudio==0.11.0 --extra-index-url  https://download.pytorch.org/whl/rocm4.5.2
    
    # CUDA 11.3
    pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
    
    # CUDA 10.2
    pip install torch==1.11.0+cu102 torchvision==0.12.0+cu102 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu102
    
    # CPU only
    pip install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cpu
    

### v1.10.1[](https://pytorch.org/get-started/previous-versions/#v1101)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-19)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-38)

    # conda
    conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-38)

    # CUDA 10.2
    conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-19)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-39)

    pip install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-39)

    # ROCM 4.2 (Linux only)
    pip install torch==1.10.1+rocm4.2 torchvision==0.11.2+rocm4.2 torchaudio==0.10.1 -f https://download.pytorch.org/whl/rocm4.2/torch_stable.html
    
    # ROCM 4.1 (Linux only)
    pip install torch==1.10.1+rocm4.1 torchvision==0.11.2+rocm4.1 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.0.1 (Linux only)
    pip install torch==1.10.1+rocm4.0.1 torchvision==0.10.2+rocm4.0.1 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 11.1
    pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu102/torch_stable.html
    
    # CPU only
    pip install torch==1.10.1+cpu torchvision==0.11.2+cpu torchaudio==0.10.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
    

### v1.10.0[](https://pytorch.org/get-started/previous-versions/#v1100)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-20)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-40)

    # conda
    conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-40)

    # CUDA 10.2
    conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-20)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-41)

    pip install torch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-41)

    # ROCM 4.2 (Linux only)
    pip install torch==1.10.0+rocm4.2 torchvision==0.11.0+rocm4.2 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.1 (Linux only)
    pip install torch==1.10.0+rocm4.1 torchvision==0.11.0+rocm4.1 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.0.1 (Linux only)
    pip install torch==1.10.0+rocm4.0.1 torchvision==0.10.1+rocm4.0.1 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 11.1
    pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.10.0+cu102 torchvision==0.11.0+cu102 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.10.0+cpu torchvision==0.11.0+cpu torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.9.1[](https://pytorch.org/get-started/previous-versions/#v191)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-21)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-42)

    # conda
    conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-42)

    # CUDA 10.2
    conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 cudatoolkit=11.3 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-21)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-43)

    pip install torch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-43)

    # ROCM 4.2 (Linux only)
    pip install torch==1.9.1+rocm4.2 torchvision==0.10.1+rocm4.2 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.1 (Linux only)
    pip install torch==1.9.1+rocm4.1 torchvision==0.10.1+rocm4.1 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.0.1 (Linux only)
    pip install torch==1.9.1+rocm4.0.1 torchvision==0.10.1+rocm4.0.1 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 11.1
    pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.9.1+cu102 torchvision==0.10.1+cu102 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.9.1+cpu torchvision==0.10.1+cpu torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.9.0[](https://pytorch.org/get-started/previous-versions/#v190)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-22)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-44)

    # conda
    conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-44)

    # CUDA 10.2
    conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=11.3 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-22)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-45)

    pip install torch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-45)

    # ROCM 4.2 (Linux only)
    pip install torch==1.9.0+rocm4.2 torchvision==0.10.0+rocm4.2 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.1 (Linux only)
    pip install torch==1.9.0+rocm4.1 torchvision==0.10.0+rocm4.1 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 4.0.1 (Linux only)
    pip install torch==1.9.0+rocm4.0.1 torchvision==0.10.0+rocm4.0.1 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 11.1
    pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.9.0+cpu torchvision==0.10.0+cpu torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.8.2 with LTS support[](https://pytorch.org/get-started/previous-versions/#v182-with-lts-support)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-23)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-46)

macOS is currently not supported for LTS.

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-46)

    # CUDA 10.2
    # NOTE: PyTorch LTS version 1.8.2 is only supported for Python <= 3.8.
    conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch-lts
    
    # CUDA 11.1 (Linux)
    # NOTE: 'nvidia' channel is required for cudatoolkit 11.1 <br> <b>NOTE:</b> Pytorch LTS version 1.8.2 is only supported for Python <= 3.8.
    conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c nvidia
    
    # CUDA 11.1 (Windows)
    # 'conda-forge' channel is required for cudatoolkit 11.1 <br> <b>NOTE:</b> Pytorch LTS version 1.8.2 is only supported for Python <= 3.8.
    conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c conda-forge
    
    # CPU Only
    # Pytorch LTS version 1.8.2 is only supported for Python <= 3.8.
    conda install pytorch torchvision torchaudio cpuonly -c pytorch-lts
    
    # ROCM5.x
    
    Not supported in LTS.
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-23)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-47)

macOS is currently not supported in LTS.

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-47)

    # CUDA 10.2
    pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu102
    
    # CUDA 11.1
    pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu111
    
    # CPU Only
    pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cpu
    
    # ROCM5.x
    
    Not supported in LTS.
    

### v1.8.1[](https://pytorch.org/get-started/previous-versions/#v181)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-24)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-48)

    # conda
    conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-48)

    # CUDA 10.2
    conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.3
    conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=11.3 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-24)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-49)

    pip install torch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-49)

    # ROCM 4.0.1 (Linux only)
    pip install torch==1.8.1+rocm4.0.1 torchvision==0.9.1+rocm4.0.1 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # ROCM 3.10 (Linux only)
    pip install torch==1.8.1+rocm3.10 torchvision==0.9.1+rocm3.10 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 11.1
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.1
    pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.8.0[](https://pytorch.org/get-started/previous-versions/#v180)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-25)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-50)

    # conda
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-50)

    # CUDA 10.2
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.1
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
    
    # CPU Only
    conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-25)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-51)

    pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-51)

    # RocM 4.0.1 (Linux only)
    pip install torch -f https://download.pytorch.org/whl/rocm4.0.1/torch_stable.html
    pip install ninja
    pip install 'git+https://github.com/pytorch/vision.git@v0.9.0'
    
    # CUDA 11.1
    pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
    
    # CPU only
    pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.7.1[](https://pytorch.org/get-started/previous-versions/#v171)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-26)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-52)

    # conda
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-52)

    # CUDA 9.2
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.1 -c pytorch
    
    # CUDA 10.2
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.0
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
    
    # CPU Only
    conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-26)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-53)

    pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-53)

    # CUDA 11.0
    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
    
    # CUDA 10.1
    pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 9.2
    pip install torch==1.7.1+cu92 torchvision==0.8.2+cu92 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.7.0[](https://pytorch.org/get-started/previous-versions/#v170)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-27)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-54)

    # conda
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-54)

    # CUDA 9.2
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.1 -c pytorch
    
    # CUDA 10.2
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.2 -c pytorch
    
    # CUDA 11.0
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=11.0 -c pytorch
    
    # CPU Only
    conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-27)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-55)

    pip install torch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-55)

    # CUDA 11.0
    pip install torch==1.7.0+cu110 torchvision==0.8.0+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 10.2
    pip install torch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0
    
    # CUDA 10.1
    pip install torch==1.7.0+cu101 torchvision==0.8.0+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 9.2
    pip install torch==1.7.0+cu92 torchvision==0.8.0+cu92 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.7.0+cpu torchvision==0.8.0+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.6.0[](https://pytorch.org/get-started/previous-versions/#v160)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-28)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-56)

    # conda
    conda install pytorch==1.6.0 torchvision==0.7.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-56)

    # CUDA 9.2
    conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch
    
    # CUDA 10.2
    conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.2 -c pytorch
    
    # CPU Only
    conda install pytorch==1.6.0 torchvision==0.7.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-28)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-57)

    pip install torch==1.6.0 torchvision==0.7.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-57)

    # CUDA 10.2
    pip install torch==1.6.0 torchvision==0.7.0
    
    # CUDA 10.1
    pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 9.2
    pip install torch==1.6.0+cu92 torchvision==0.7.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.5.1[](https://pytorch.org/get-started/previous-versions/#v151)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-29)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-58)

    # conda
    conda install pytorch==1.5.1 torchvision==0.6.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-58)

    # CUDA 9.2
    conda install pytorch==1.5.1 torchvision==0.6.1 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.5.1 torchvision==0.6.1 cudatoolkit=10.1 -c pytorch
    
    # CUDA 10.2
    conda install pytorch==1.5.1 torchvision==0.6.1 cudatoolkit=10.2 -c pytorch
    
    # CPU Only
    conda install pytorch==1.5.1 torchvision==0.6.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-29)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-59)

    pip install torch==1.5.1 torchvision==0.6.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-59)

    # CUDA 10.2
    pip install torch==1.5.1 torchvision==0.6.1
    
    # CUDA 10.1
    pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 9.2
    pip install torch==1.5.1+cu92 torchvision==0.6.1+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.5.0[](https://pytorch.org/get-started/previous-versions/#v150)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-30)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-60)

    # conda
    conda install pytorch==1.5.0 torchvision==0.6.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-60)

    # CUDA 9.2
    conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit=10.1 -c pytorch
    
    # CUDA 10.2
    conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit=10.2 -c pytorch
    
    # CPU Only
    conda install pytorch==1.5.0 torchvision==0.6.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-30)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-61)

    pip install torch==1.5.0 torchvision==0.6.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-61)

    # CUDA 10.2
    pip install torch==1.5.0 torchvision==0.6.0
    
    # CUDA 10.1
    pip install torch==1.5.0+cu101 torchvision==0.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CUDA 9.2
    pip install torch==1.5.0+cu92 torchvision==0.6.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.4.0[](https://pytorch.org/get-started/previous-versions/#v140)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-31)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-62)

    # conda
    conda install pytorch==1.4.0 torchvision==0.5.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-62)

    # CUDA 9.2
    conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.1
    conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch
    
    # CPU Only
    conda install pytorch==1.4.0 torchvision==0.5.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-31)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-63)

    pip install torch==1.4.0 torchvision==0.5.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-63)

    # CUDA 10.1
    pip install torch==1.4.0 torchvision==0.5.0
    
    # CUDA 9.2
    pip install torch==1.4.0+cu92 torchvision==0.5.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.2.0[](https://pytorch.org/get-started/previous-versions/#v120)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-32)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-64)

    # conda
    conda install pytorch==1.2.0 torchvision==0.4.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-64)

    # CUDA 9.2
    conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=9.2 -c pytorch
    
    # CUDA 10.0
    conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch
    
    # CPU Only
    conda install pytorch==1.2.0 torchvision==0.4.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-32)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-65)

    pip install torch==1.2.0 torchvision==0.4.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-65)

    # CUDA 10.0
    pip install torch==1.2.0 torchvision==0.4.0
    
    # CUDA 9.2
    pip install torch==1.2.0+cu92 torchvision==0.4.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
    
    # CPU only
    pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
    

### v1.1.0[](https://pytorch.org/get-started/previous-versions/#v110)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-33)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-66)

    # conda
    conda install pytorch==1.1.0 torchvision==0.3.0 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-66)

    # CUDA 9.0
    conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch
    
    # CUDA 10.0
    conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
    
    # CPU Only
    conda install pytorch-cpu==1.1.0 torchvision-cpu==0.3.0 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-33)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-67)

    pip install torch==1.1.0 torchvision==0.3.0
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-67)

    # CUDA 10.0
    Download and install wheel from https://download.pytorch.org/whl/cu100/torch_stable.html
    
    # CUDA 9.0
    Download and install wheel from https://download.pytorch.org/whl/cu90/torch_stable.html
    
    # CPU only
    Download and install wheel from https://download.pytorch.org/whl/cpu/torch_stable.html
    

### v1.0.1[](https://pytorch.org/get-started/previous-versions/#v101)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-34)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-68)

    # conda
    conda install pytorch==1.0.1 torchvision==0.2.2 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-68)

    # CUDA 9.0
    conda install pytorch==1.0.1 torchvision==0.2.2 cudatoolkit=9.0 -c pytorch
    
    # CUDA 10.0
    conda install pytorch==1.0.1 torchvision==0.2.2 cudatoolkit=10.0 -c pytorch
    
    # CPU Only
    conda install pytorch-cpu==1.0.1 torchvision-cpu==0.2.2 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-34)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-69)

    pip install torch==1.0.1 torchvision==0.2.2
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-69)

    # CUDA 10.0
    Download and install wheel from https://download.pytorch.org/whl/cu100/torch_stable.html
    
    # CUDA 9.0
    Download and install wheel from https://download.pytorch.org/whl/cu90/torch_stable.html
    
    # CPU only
    Download and install wheel from https://download.pytorch.org/whl/cpu/torch_stable.html
    

### v1.0.0[](https://pytorch.org/get-started/previous-versions/#v100)

#### Conda[](https://pytorch.org/get-started/previous-versions/#conda-35)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-70)

    # conda
    conda install pytorch==1.0.0 torchvision==0.2.1 -c pytorch
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-70)

    # CUDA 10.0
    conda install pytorch==1.0.0 torchvision==0.2.1 cuda100 -c pytorch
    
    # CUDA 9.0
    conda install pytorch==1.0.0 torchvision==0.2.1 cuda90 -c pytorch
    
    # CUDA 8.0
    conda install pytorch==1.0.0 torchvision==0.2.1 cuda80 -c pytorch
    
    # CPU Only
    conda install pytorch-cpu==1.0.0 torchvision-cpu==0.2.1 cpuonly -c pytorch
    

#### Wheel[](https://pytorch.org/get-started/previous-versions/#wheel-35)

##### OSX[](https://pytorch.org/get-started/previous-versions/#osx-71)

    pip install torch==1.0.0 torchvision==0.2.1
    

##### Linux and Windows[](https://pytorch.org/get-started/previous-versions/#linux-and-windows-71)

    # CUDA 10.0
    Download and install wheel from https://download.pytorch.org/whl/cu100/torch_stable.html
    
    # CUDA 9.0
    Download and install wheel from https://download.pytorch.org/whl/cu90/torch_stable.html
    
    # CUDA 8.0
    Download and install wheel from https://download.pytorch.org/whl/cu80/torch_stable.html
    
    # CPU only
    Download and install wheel from https://download.pytorch.org/whl/cpu/torch_stable.html
    

## Commands for Versions < 1.0.0[](https://pytorch.org/get-started/previous-versions/#commands-for-versions--100-1)

### Via conda[](https://pytorch.org/get-started/previous-versions/#via-conda)

> This should be used for most previous macOS version installs.

To install a previous version of PyTorch via Anaconda or Miniconda, replace “0.4.1” in the following commands with the desired version (i.e., “0.2.0”).

Installing with CUDA 9

`conda install pytorch=0.4.1 cuda90 -c pytorch`

or

`conda install pytorch=0.4.1 cuda92 -c pytorch`

Installing with CUDA 8

`conda install pytorch=0.4.1 cuda80 -c pytorch`

Installing with CUDA 7.5

`conda install pytorch=0.4.1 cuda75 -c pytorch`

Installing without CUDA

`conda install pytorch=0.4.1 -c pytorch`

### From source[](https://pytorch.org/get-started/previous-versions/#from-source)

It is possible to checkout an older version of [PyTorch](https://github.com/pytorch/pytorch) and build it. You can list tags in PyTorch git repository with `git tag` and checkout a particular one (replace ‘0.1.9’ with the desired version) with

`git checkout v0.1.9`

Follow the install from source instructions in the README.md of the PyTorch checkout.

### Via pip[](https://pytorch.org/get-started/previous-versions/#via-pip)

Download the `whl` file with the desired version from the following html pages:

-   [https://download.pytorch.org/whl/cpu/torch\_stable.html](https://download.pytorch.org/whl/cpu/torch_stable.html) # CPU-only build
-   [https://download.pytorch.org/whl/cu80/torch\_stable.html](https://download.pytorch.org/whl/cu80/torch_stable.html) # CUDA 8.0 build
-   [https://download.pytorch.org/whl/cu90/torch\_stable.html](https://download.pytorch.org/whl/cu90/torch_stable.html) # CUDA 9.0 build
-   [https://download.pytorch.org/whl/cu92/torch\_stable.html](https://download.pytorch.org/whl/cu92/torch_stable.html) # CUDA 9.2 build
-   [https://download.pytorch.org/whl/cu100/torch\_stable.html](https://download.pytorch.org/whl/cu100/torch_stable.html) # CUDA 10.0 build

Then, install the file with `pip install [downloaded file]`

Note: most pytorch versions are available only for specific CUDA versions. For example pytorch=1.0.1 is not available for CUDA 9.2







Via pip
Download the whl file with the desired version from the following html pages:

https://download.pytorch.org/whl/cpu/torch_stable.html # CPU-only build
https://download.pytorch.org/whl/cu80/torch_stable.html # CUDA 8.0 build
https://download.pytorch.org/whl/cu90/torch_stable.html # CUDA 9.0 build
https://download.pytorch.org/whl/cu92/torch_stable.html # CUDA 9.2 build
https://download.pytorch.org/whl/cu100/torch_stable.html # CUDA 10.0 build
Then, install the file with pip install [downloaded file]

Note: most pytorch versions are available only for specific CUDA versions. For example pytorch=1.0.1 is not available for CUDA 9.2

(Old) PyTorch Linux binaries compiled with CUDA 7.5
These predate the html page above and have to be manually installed by downloading the wheel file and pip install downloaded_file

These predate the html page above and have to be manually installed by downloading the wheel file and `pip install downloaded_file`

-   [cu75/torch-0.3.0.post4-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.3.0.post4-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.3.0.post4-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl)
-   [cu75/torch-0.3.0.post4-cp27-cp27m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp27-cp27m-linux_x86_64.whl)
-   [cu75/torch-0.2.0.post3-cp36-cp36m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post3-cp36-cp36m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post3-cp35-cp35m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post3-cp35-cp35m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post3-cp27-cp27mu-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post3-cp27-cp27mu-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post3-cp27-cp27m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post3-cp27-cp27m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post2-cp36-cp36m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post2-cp36-cp36m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post2-cp35-cp35m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post2-cp35-cp35m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post2-cp27-cp27mu-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post2-cp27-cp27mu-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post2-cp27-cp27m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post2-cp27-cp27m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post1-cp36-cp36m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post1-cp36-cp36m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post1-cp35-cp35m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post1-cp35-cp35m-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post1-cp27-cp27mu-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post1-cp27-cp27mu-manylinux1_x86_64.whl)
-   [cu75/torch-0.2.0.post1-cp27-cp27m-manylinux1\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.2.0.post1-cp27-cp27m-manylinux1_x86_64.whl)
-   [cu75/torch-0.1.12.post2-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post2-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.12.post2-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post2-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.12.post2-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post2-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.12.post1-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post1-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.12.post1-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post1-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.12.post1-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.12.post1-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post5-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post5-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post5-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post5-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post5-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post5-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post4-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post4-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post4-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post4-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.11.post4-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.11.post4-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post2-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post2-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post2-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post2-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post2-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post2-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post1-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post1-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post1-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post1-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.10.post1-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.10.post1-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post2-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post2-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post2-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post2-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post2-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post2-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post1-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post1-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post1-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post1-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.9.post1-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.9.post1-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.8.post1-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.8.post1-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.8.post1-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.8.post1-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.8.post1-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.8.post1-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.7.post2-cp36-cp36m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.7.post2-cp36-cp36m-linux_x86_64.whl)
-   [cu75/torch-0.1.7.post2-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.7.post2-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.7.post2-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.7.post2-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.6.post22-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.6.post22-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.6.post22-cp27-none-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.6.post22-cp27-none-linux_x86_64.whl)
-   [cu75/torch-0.1.6.post20-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.6.post20-cp35-cp35m-linux_x86_64.whl)
-   [cu75/torch-0.1.6.post20-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/cu75/torch-0.1.6.post20-cp27-cp27mu-linux_x86_64.whl)

### Windows binaries[](https://pytorch.org/get-started/previous-versions/#windows-binaries)

-   [cpu/torch-1.0.0-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp35-cp35m-win_amd64.whl)
-   [cu80/torch-1.0.0-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-1.0.0-cp35-cp35m-win_amd64.whl)
-   [cu90/torch-1.0.0-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-1.0.0-cp35-cp35m-win_amd64.whl)
-   [cu100/torch-1.0.0-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu100/torch-1.0.0-cp35-cp35m-win_amd64.whl)
-   [cpu/torch-1.0.0-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-cp36m-win_amd64.whl)
-   [cu80/torch-1.0.0-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-1.0.0-cp36-cp36m-win_amd64.whl)
-   [cu90/torch-1.0.0-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-1.0.0-cp36-cp36m-win_amd64.whl)
-   [cu100/torch-1.0.0-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu100/torch-1.0.0-cp36-cp36m-win_amd64.whl)
-   [cpu/torch-1.0.0-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp37-cp37m-win_amd64.whl)
-   [cu80/torch-1.0.0-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-1.0.0-cp37-cp37m-win_amd64.whl)
-   [cu90/torch-1.0.0-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-1.0.0-cp37-cp37m-win_amd64.whl)
-   [cu100/torch-1.0.0-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu100/torch-1.0.0-cp37-cp37m-win_amd64.whl)
-   [cpu/torch-0.4.1-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-0.4.1-cp35-cp35m-win_amd64.whl)
-   [cu80/torch-0.4.1-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-0.4.1-cp35-cp35m-win_amd64.whl)
-   [cu90/torch-0.4.1-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-0.4.1-cp35-cp35m-win_amd64.whl)
-   [cu92/torch-0.4.1-cp35-cp35m-win\_amd64.whl](https://download.pytorch.org/whl/cu92/torch-0.4.1-cp35-cp35m-win_amd64.whl)
-   [cpu/torch-0.4.1-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-win_amd64.whl)
-   [cu80/torch-0.4.1-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-0.4.1-cp36-cp36m-win_amd64.whl)
-   [cu90/torch-0.4.1-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-0.4.1-cp36-cp36m-win_amd64.whl)
-   [cu92/torch-0.4.1-cp36-cp36m-win\_amd64.whl](https://download.pytorch.org/whl/cu92/torch-0.4.1-cp36-cp36m-win_amd64.whl)
-   [cpu/torch-0.4.1-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cpu/torch-0.4.1-cp37-cp37m-win_amd64.whl)
-   [cu80/torch-0.4.1-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu80/torch-0.4.1-cp37-cp37m-win_amd64.whl)
-   [cu90/torch-0.4.1-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu90/torch-0.4.1-cp37-cp37m-win_amd64.whl)
-   [cu92/torch-0.4.1-cp37-cp37m-win\_amd64.whl](https://download.pytorch.org/whl/cu92/torch-0.4.1-cp37-cp37m-win_amd64.whl)

### Mac and misc. binaries[](https://pytorch.org/get-started/previous-versions/#mac-and-misc-binaries)

For recent macOS binaries, use `conda`:

e.g.,

`conda install pytorch=0.4.1 cuda90 -c pytorch` `conda install pytorch=0.4.1 cuda92 -c pytorch` `conda install pytorch=0.4.1 cuda80 -c pytorch` `conda install pytorch=0.4.1 -c pytorch` # No CUDA

-   [torchvision-0.1.6-py3-none-any.whl](https://download.pytorch.org/whl/torchvision-0.1.6-py3-none-any.whl)
-   [torchvision-0.1.6-py2-none-any.whl](https://download.pytorch.org/whl/torchvision-0.1.6-py2-none-any.whl)
-   [torch-1.0.0-cp37-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp37-none-macosx_10_7_x86_64.whl)
-   [torch-1.0.0-cp36-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp36-none-macosx_10_7_x86_64.whl)
-   [torch-1.0.0-cp35-none-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp35-none-macosx_10_6_x86_64.whl)
-   [torch-1.0.0-cp27-none-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/cpu/torch-1.0.0-cp27-none-macosx_10_6_x86_64.whl)
-   [torch-0.4.0-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.4.0-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.4.0-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.4.0-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.4.0-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.4.0-cp27-none-macosx_10_6_x86_64.whl)
-   [torch-0.3.1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.3.1-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.1-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.3.1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.1-cp27-none-macosx_10_6_x86_64.whl)
-   [torch-0.3.0.post4-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.0.post4-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.3.0.post4-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.0.post4-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.3.0.post4-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.3.0.post4-cp27-none-macosx_10_6_x86_64.whl)
-   [torch-0.2.0.post3-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post3-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post3-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post3-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post3-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post3-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post2-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post2-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post2-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post2-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post2-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post2-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post1-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post1-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.2.0.post1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.2.0.post1-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post2-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post2-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post2-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post2-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post2-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post2-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post1-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post1-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.1.12.post1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.12.post1-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post5-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post5-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post5-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post5-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post5-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post5-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post4-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post4-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post4-cp35-cp35m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post4-cp35-cp35m-macosx_10_7_x86_64.whl)
-   [torch-0.1.11.post4-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.11.post4-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.10.post1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.10.post1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.10.post1-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.10.post1-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.10.post1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.10.post1-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.9.post2-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post2-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.9.post2-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post2-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.9.post2-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post2-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.9.post1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.9.post1-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post1-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.9.post1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.9.post1-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.8.post1-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.8.post1-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.8.post1-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.8.post1-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.8.post1-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.8.post1-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.7.post2-cp36-cp36m-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.7.post2-cp36-cp36m-macosx_10_7_x86_64.whl)
-   [torch-0.1.7.post2-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.7.post2-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.7.post2-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.7.post2-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.6.post22-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post22-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1.6.post22-cp27-none-macosx\_10\_7\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post22-cp27-none-macosx_10_7_x86_64.whl)
-   [torch-0.1.6.post20-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post20-cp35-cp35m-linux_x86_64.whl)
-   [torch-0.1.6.post20-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post20-cp27-cp27mu-linux_x86_64.whl)
-   [torch-0.1.6.post17-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post17-cp35-cp35m-linux_x86_64.whl)
-   [torch-0.1.6.post17-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1.6.post17-cp27-cp27mu-linux_x86_64.whl)
-   [torch-0.1-cp35-cp35m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1-cp35-cp35m-macosx_10_6_x86_64.whl)
-   [torch-0.1-cp27-cp27m-macosx\_10\_6\_x86\_64.whl](https://download.pytorch.org/whl/torch-0.1-cp27-cp27m-macosx_10_6_x86_64.whl)
-   [torch\_cuda80-0.1.6.post20-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch_cuda80-0.1.6.post20-cp35-cp35m-linux_x86_64.whl)
-   [torch\_cuda80-0.1.6.post20-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch_cuda80-0.1.6.post20-cp27-cp27mu-linux_x86_64.whl)
-   [torch\_cuda80-0.1.6.post17-cp35-cp35m-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch_cuda80-0.1.6.post17-cp35-cp35m-linux_x86_64.whl)
-   [torch\_cuda80-0.1.6.post17-cp27-cp27mu-linux\_x86\_64.whl](https://download.pytorch.org/whl/torch_cuda80-0.1.6.post17-cp27-cp27mu-linux_x86_64.whl)









---
