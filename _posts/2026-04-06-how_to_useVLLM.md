---
layout: post
title: '服务器-vLLM多端口部署LLM'
date: 2026-04-06
author: pepper
tags: [vllm, llm, server]
comments: true
toc: true
pinned: false
---

这篇博客介绍了如何管理本地的LLM，本文将详细梳理使用xinference管理LLM模型的常用命令，以及通过vllm部署LLM模型的核心操作步骤与命令示例，帮助读者快速掌握本地LLM的管理与部署流程。

<!-- more -->
# vllm 多端口部署 LLM 模型
针对**后端多端口部署多个 LLM 模型**的需求，本文设计了一套高可维护、易扩展、符合生产环境规范的目录结构，同时配套了核心配置与启动脚本模板，直接可用。

## 目录结构
```plain
vllm/
├── config/                  # 🔧 模型配置中心（核心）
│   ├── model_7b_8000.yaml   # 7B 模型，端口 8000 配置
│   ├── model_14b_8001.yaml  # 14B 模型，端口 8001 配置
│   ├── model_70b_8002.yaml  # 70B 模型，端口 8002 配置
│   └── common.yaml          # 全局通用配置（日志、监控、超时等）
├── scripts/                 # 🚀 启动/管理脚本
│   ├── start_all.sh         # 一键启动所有模型服务
│   ├── start_single.sh      # 单模型启动脚本（传参指定端口/模型）
│   ├── stop_all.sh          # 一键停止所有服务
│   ├── stop_single.sh       # 单模型停止脚本
│   ├── restart_single.sh    # 单模型重启脚本
│   └── health_check.sh      # 服务健康巡检脚本
├── logs/                    # 📝 日志目录（按模型/端口分类）
│   ├── model_7b_8000/
│   │   ├── access.log       # 访问日志
│   │   ├── error.log        # 错误日志
│   │   └── server.log       # 服务运行日志
│   ├── model_14b_8001/
│   └── model_70b_8002/
├── models/                  # 🧠 模型权重目录（软链接/实际存储）
│   ├── qwen2-7b-instruct/
│   ├── qwen2-14b-instruct/
│   └── qwen2-72b-instruct/
├── utils/                   # 🛠️ 工具脚本
│   ├── port_check.py        # 端口占用检查工具
│   ├── gpu_monitor.py       # GPU 资源监控工具
│   └── log_rotate.py        # 日志轮转工具
├── env/                     # ⚙️ 环境配置
│   ├── .env.base            # 基础环境变量（Python 路径、CUDA 等）
│   ├── .env.7b_8000         # 7B 模型专属环境变量
│   └── .env.14b_8001        # 14B 模型专属环境变量
└── README.md                # 📖 项目说明文档
```

---

## 🎯 目录设计核心思路
### 1. 配置分离（config/）
+ **按模型/端口拆分配置**：每个模型一个独立 YAML 文件，避免配置冲突，方便单独调整参数（如 `max_num_batched_tokens`、`tensor_parallel_size`）
+ **全局配置复用**：`common.yaml` 统一管理日志格式、超时时间、监控地址等，减少重复配置
+ **支持热更新**：修改配置后无需改脚本，直接重启对应服务即可生效

### 2. 脚本标准化（scripts/）
+ **一键启停**：`start_all.sh`/`stop_all.sh` 适合批量管理，`start_single.sh` 适合单独调试
+ **参数化启动**：单模型脚本支持传参指定端口、模型路径、GPU 编号，灵活适配多场景
+ **健康巡检**：`health_check.sh` 定期检查服务状态，自动重启异常服务，保障高可用

### 3. 日志隔离（logs/）
+ **按模型分类存储**：每个模型独立日志目录，避免日志混杂，方便问题排查
+ **日志轮转**：配套 `log_rotate.py` 自动清理旧日志，防止磁盘占满
+ **日志分级**：区分访问日志、错误日志、运行日志，定位问题更高效

### 4. 模型与环境解耦（models/ + env/）
+ **模型目录独立**：支持软链接挂载外部存储，避免代码与权重耦合，方便模型版本管理
+ **环境变量隔离**：不同模型可配置不同的 Python 环境、CUDA 版本、环境变量，适配多模型部署需求

---

## 📝 核心文件模板（直接可用）
### 1. 单模型配置文件（config/model_7b_8000.yaml）
```yaml
# 模型基础配置
model: /path/to/vllm_script/models/qwen2-7b-instruct
tokenizer: /path/to/vllm_script/models/qwen2-7b-instruct
host: 0.0.0.0
port: 8000

# 服务性能配置
tensor_parallel_size: 1  # GPU 并行数，多卡部署时调整
max_num_batched_tokens: 32768
max_num_seqs: 256
max_model_len: 8192
gpu_memory_utilization: 0.9  # GPU 显存利用率，避免 OOM

# 日志配置（继承 common.yaml 可覆盖）
log_level: INFO
log_file: /path/to/vllm_script/logs/model_7b_8000/server.log
access_log_file: /path/to/vllm_script/logs/model_7b_8000/access.log
error_log_file: /path/to/vllm_script/logs/model_7b_8000/error.log

# 其他可选配置
trust_remote_code: true
enable_prefix_caching: true
api_key: your_secure_api_key  # 接口鉴权，生产环境必加
```

### 2. 单模型启动脚本（scripts/start_single.sh）
```bash
#!/bin/bash
set -e

# 加载基础环境变量
source /path/to/vllm_script/env/.env.base

# 检查参数
if [ $# -ne 3 ]; then
    echo "Usage: $0 <config_file> <port> <gpu_ids>"
    echo "Example: $0 ../config/model_7b_8000.yaml 8000 0"
    exit 1
fi

CONFIG_FILE=$1
PORT=$2
GPU_IDS=$3

# 检查端口是否被占用
bash /path/to/vllm_script/utils/port_check.sh $PORT
if [ $? -ne 0 ]; then
    echo "Error: Port $PORT is already in use!"
    exit 1
fi

# 加载模型专属环境变量
ENV_FILE="/path/to/vllm_script/env/.env.${PORT}"
if [ -f "$ENV_FILE" ]; then
    source $ENV_FILE
fi

# 启动 vLLM 服务
echo "Starting vLLM service on port $PORT, GPU: $GPU_IDS, config: $CONFIG_FILE"
CUDA_VISIBLE_DEVICES=$GPU_IDS nohup python -m vllm.entrypoints.openai.api_server \
    --config $CONFIG_FILE \
    > /path/to/vllm_script/logs/model_${PORT}/nohup.out 2>&1 &

# 记录进程 PID
echo $! > /path/to/vllm_script/logs/model_${PORT}/service.pid
echo "Service started with PID: $(cat /path/to/vllm_script/logs/model_${PORT}/service.pid)"
```

### 3. 一键启动所有服务脚本（scripts/start_all.sh）
```bash
#!/bin/bash
set -e

# 定义模型配置、端口、GPU 对应关系
declare -a models=(
    "model_7b_8000.yaml 8000 0"
    "model_14b_8001.yaml 8001 1"
    "model_70b_8002.yaml 8002 2,3"
)

# 遍历启动所有模型
for model in "${models[@]}"; do
    read config port gpu <<< "$model"
    echo "=== Starting $config on port $port, GPU: $gpu ==="
    bash /path/to/vllm_script/scripts/start_single.sh "/path/to/vllm_script/config/$config" $port $gpu
    sleep 5  # 间隔启动，避免资源抢占
done

echo "All services started successfully!"
```

### 4. 端口检查工具（utils/port_check.sh）
```bash
#!/bin/bash
PORT=$1
if lsof -i:$PORT > /dev/null 2>&1; then
    exit 1  # 端口被占用
else
    exit 0  # 端口可用
fi
```

---

## ⚙️ 多端口部署关键优化建议
### 1. GPU 资源分配
+ **单卡多模型**：通过 `gpu_memory_utilization` 控制显存占用，例如 24G 卡可部署 1 个 7B（0.5 显存）+ 1 个 14B（0.4 显存）
+ **多卡并行**：大模型（70B+）使用 `tensor_parallel_size: 2/4` 多卡部署，提升推理速度
+ **GPU 隔离**：通过 `CUDA_VISIBLE_DEVICES` 严格隔离不同模型的 GPU 资源，避免资源争抢

### 2. 高可用保障
+ **进程守护**：用 `nohup` + `systemd` 托管服务，服务器重启后自动恢复
+ **健康巡检**：`health_check.sh` 定时调用 `/health` 接口，异常自动重启
+ **限流熔断**：配置 `max_num_seqs` 限制并发请求，防止服务雪崩

### 3. 运维便捷性
+ **日志轮转**：配置 `logrotate` 或 `log_rotate.py`，定期清理 7 天前的日志
+ **监控告警**：对接 Prometheus + Grafana，监控 GPU 使用率、QPS、延迟等指标
+ **版本管理**：`models/` 目录下按版本存放模型权重，支持快速切换模型版本

---

## 📌 部署步骤（快速上手）
1. **创建目录结构**：按上述结构创建所有文件夹
2. **配置模型参数**：在 `config/` 下编写每个模型的 YAML 配置
3. **修改脚本路径**：将脚本中的 `/path/to/vllm_script` 替换为你的实际根目录
4. **添加执行权限**：`chmod +x scripts/*.sh utils/*.sh`
5. **启动服务**：`bash scripts/start_all.sh`
6. **验证服务**：`curl http://localhost:8000/v1/chat/completions` 测试接口

---

## 💡 额外优化（生产环境必看）
+ **API 鉴权**：所有模型配置 `api_key`，防止未授权访问
+ **HTTPS 加密**：用 Nginx 反向代理，配置 SSL 证书，加密传输
+ **负载均衡**：多实例部署时，用 Nginx 做负载均衡，提升并发能力
+ **模型热更新**：支持不中断服务的模型版本切换（vLLM 0.4+ 支持）

---

### 其他冷知识
日志中，GLM-4-9B 虽然标称是 **90亿参数（9B）**，但在 vLLM 加载时却吃掉了大量的显存。通过日志中的关键数据（`Model loading took 17.56 GiB memory`）来拆解，为什么一个 9B 的模型会占用这么多空间。



#### 1. 权重本身的大小（Weights）
这是最基础的占用。模型有 92.3 亿个参数，日志显示加载的精度是 `dtype=torch.bfloat16`。

+ **BF16/FP16 精度：** 每个参数占用 **2 字节（Bytes）**。
+ **计算公式：** $9.23 \times 10^9 \text{ params} \times 2 \text{ bytes/param} \approx 18.46 \times 10^9 \text{ bytes} \approx 17.19 \text{ GiB}$ 。
+ **日志对应：** 日志显示 `Loading weights took... 17.56 GiB`。这非常吻合，多出来的部分是架构本身的开销和一些临时 Buffer。

**结论：** 仅仅是把模型挂载到显存里，就需要约 **17.2 GiB**。

---

#### 2. vLLM 的显存预分配机制（KV Cache）
如果发现显存占用远超 17 GiB（比如达到了 24G 甚至更多），那是 **vLLM** 的特性导致的。

vLLM 默认会执行 **显存接管策略**：

1. **加载权重：** 消耗约 17.2 GiB。
2. **剩余显存：** vLLM 会扫描显卡剩下的空间，并根据你的配置 `gpu_memory_utilization: 0.92`，强行占掉 92% 的总显存。
3. **KV Cache 池：** 剩下的这些空间会被划分为一个个“Block”，用来存储对话过程中的中间变量（Key-Value Cache）。

**日志证据：**

`Available KV cache memory: 22.64 GiB`，这意味着 vLLM 在加载完模型后，为了保证高并发推理，预留了巨大的空间来存 Token。

---

#### 3. 其他“隐形”开销
日志里提到了几个现代推理框架的加速技术，它们也会吃掉一点显存：

+ **CUDA Graphs（显存图捕获）：**

`Estimated CUDA graph memory: 0.53 GiB total`

为了加速小 Batch 的推理，vLLM 会提前录制计算图，这通常需要几百 MB 到 1 GB。

+ **torch.compile（编译开销）：**

`Directly load the compiled graph(s)...`

虽然主要是 CPU 和时间开销，但在编译和运行 Kernel 时也会占用额外的显存 Buffer。

---

#### 总结：你的显存去哪了？

| **组成部分** | **估计大小** | **说明** |
| :--- | --- | --- |
| **模型静态权重** | **~17.2 GiB** | 9.23B 参数 $\times$ BF16(2 Bytes) |
| **CUDA Graph / Overhead** | **~0.6 GiB** | 预录制计算图，加速推理 |
| **KV Cache (用户数据池)** | **显存剩余部分** | 由 `gpu_memory_utilization`决定，越大支持的并发越高 |


#### 小贴士：如何让它变小？
如果你觉得占用太高，可以尝试：

1. **量化（Quantization）：** 使用 AWQ 或 GPTQ 4bit 格式，权重大小会直接减半（从 17 GiB 降到约 6-8 GiB）。
2. **限制显存占用：** 在启动命令中加入 `--gpu-memory-utilization 0.7`（手动限制 vLLM 只占 70% 显存）。
3. **缩短长度：** 减小 `--max-model-len`，这会显著减少 KV Cache 的压力。

## 常见精度对比表

| **格式名称** | **每个参数占用空间** | **适用场景** | **特点** |
| --- | --- | --- | --- |
| **FP32** (单精度) | 4 Bytes (32 bit) | 模型训练 / 调试 | 精度最高，但显存占用是 BF16 的两倍，推理极慢。 |
| **BF16 / FP16** | 2 Bytes (16 bit) | **当前主流推理** | 平衡了精度和速度，你的 GLM-4-9B 默认就在跑这个。 |
| **INT8** | 1 Byte (8 bit) | 早期量化方案 | 显存减半，但精度有一定损失，现在逐渐被 4bit 取代。 |
| **INT4 / FP4** | 0.5 Byte (4 bit) | **消费级显卡首选** | 显存占用仅为 BF16 的 1/4，9B 模型只需约 5-6G 显存。 |
| **FP8** | 1 Byte (8 bit) | H100 等新一代 GPU | 兼顾 INT8 的速度和浮点数的动态范围，训练和推理都很强，能够比较好处理模型中那些突然变大的异常值 |