---
title: 'What_is_trafficPrediction'
lang: zh-CN
date: 2025-02-07
author: pepper
toc: true
pinned: false
tags:
  - Study
---
Traffic Prediction 方向的研究概述
<!-- more -->

## Traffic Prediction 论文资源

### 1. 概述

  交通预测是利用历史数据(时间序列)预测道路网络(图)中未来交通测量值(如流量、速度等)的任务。

  更新列表参考: <https://github.com/lixus7/Time-Series-Works-Conferences>

### 2. 数据集

#### 公开数据集

- **METR-LA**
  - [DCRNN Google Drive](https://drive.google.com/drive/folders/10FOTa6HXPqX8Pf5WRoRwcFnW9BrNZEIX)
  - [DCRNN Baidu](https://pan.baidu.com/s/14Yy9isAIZYdU__OYEQGa_g#list/path=%2F)
  - [传感器坐标和邻接矩阵](https://github.com/liyaguang/DCRNN/tree/master/data/sensor_graph)

- **PeMS系列** (California PeMS: <http://pems.dot.ca.gov/>)
  - PeMS-BAY, PeMS-D7(M), PeMS-D7(L)
  - PeMS-04, PeMS-08, PeMS-03, PeMS-07
  - [下载地址](https://github.com/Davidham3/ASTGCN/tree/master/data)

- **LOOP**: <https://github.com/zhiyongc/Seattle-Loop-Data>

- **Q-Traffic**: <https://github.com/JingqingZ/BaiduTraffic>

### 3. 工具库

- [LibCity](https://libcity.ai/) - [GitHub](https://github.com/LibCity/Bigscity-LibCity)
- [Tsinghua Fib Lab](https://github.com/tsinghua-fib-lab/Traffic-Benchmark)
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io)

### 4. 论文列表

  | 模型 | 会议 | 年份 | 论文 | 代码 |
  |:---:|:---:|:---:|:---:|:---:|
  | G-SWaN | IoTDI | 2023 | [Link](https://arxiv.org/abs/2302.09956) | [PyTorch](https://github.com/aprbw/G-SWaN) |
  | SCPT | ArXiv | 2023 | [Link](https://arxiv.org/abs/2305.05237) | - |
  | AGCRN | ArXiv | 2020 | [Link](https://arxiv.org/abs/2007.02842) | [PyTorch](https://github.com/LeiBAI/AGCRN) |
  | DCRNN | ICLR | 2018 | [Link](https://arxiv.org/abs/1707.01926v3) | [TF](https://github.com/liyaguang/DCRNN) |
  | STGCN | IJCAI | 2018 | [Link](https://arxiv.org/abs/1709.04875) | [PyTorch](https://github.com/FelixOpolka/STGCN-PyTorch) |
  | GWN | IJCAI | 2019 | [Link](https://www.ijcai.org/Proceedings/2019/0264.pdf) | [PyTorch](https://github.com/nnzhan/Graph-WaveNet) |

### 5. 相关资源

- [Graph Neural Network for Traffic Forecasting Survey](https://arxiv.org/abs/2101.11174)
- [BigsCity LibCity论文集](https://github.com/LibCity/Bigscity-LibCity-Paper)
- [DL-Traff基准测试](https://github.com/deepkashiwa20/DL-Traff-Grid)

---
