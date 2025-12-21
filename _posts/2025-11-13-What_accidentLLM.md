---
layout: post
title: 'What_accidentLLM'
date: 2025-11-13
author: pepper
tags: [papperReading, Note]
comments: true
toc: true
pinned: false
---

这篇博客介绍了交通隐患大模型的研究。

## 参考仓库
## 参考仓库

| **论文** | **概述** | **年份** |
|----------|----------|----------|
| [SUTD-TrafficQA: A Question Answering Benchmark and an Efficient Network for Video Reasoning over Traffic Events](https://scholar.google.com/scholar?start=0&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=13846762936798544230&scipsc=) | 一个视频问答数据集和一个名为 Eclipse 的高效一瞥网络（Efficient glimpse network）侧重于因果推理和事件理解模型（主要是监督学习和网络架构设计）。 | 2021 |
| MAPLM: A Real-World Large-Scale Vision-Language Benchmark for Map and Traffic Scene Understanding ([代码](http://github.com/LLVM-AD/MAPLM)) | 一个用于自动驾驶和 HD 地图的多模态视觉-语言基准，侧重于数据构建和使用 CLIP/LLaMA-2 等进行视觉指令微调（visual instruction-tuning），这是一种监督或自监督学习范式。 | 2024 CVPR |
| Video-Text as Game Players: Hierarchical Banzhaf Interaction for Cross-Modal Representation Learning ([代码](https://github.com/jpthu17/HBI), [论文](https://arxiv.org/pdf/2303.14369)) | 提出了基于多变量合作博弈论和 Banzhaf 交互的 HBI 模型。核心是对比学习（Contrastive Learning）和网络架构设计（Token 合并模块），以及博弈论概念的应用。对比学习属于自监督学习范畴。 | 2023 CVPR |
| Cross-Modal Causal Relational Reasoning for Event-Level Visual Question Answering ([代码](https://github.com/HCPLab-SYSU/CMCIR), [论文](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10146482)) | 通过引入因果推断（Causal Inference）的机制，来解决现有视觉问答（VQA）模型在事件级（Event-Level）任务中存在的跨模态虚假相关性（spurious correlations）和对事件动态理解不足的问题，从而实现更鲁棒、更具因果意识的推理 | 2023-IEEE |
| Discovering the Real Association: Multimodal Causal Reasoning in Video Question Answering | 它超越了传统视频问答（VideoQA）的统计关联范式，将因果推理（Causal Reasoning）引入多模态领域。通过提出一个基于因果表示的框架，该方法能够显式地发现视频和文本模态之间真正的、稳定的因果关联（Real Association），从而有效地消除数据中普遍存在的视觉冗余和文本局部性的虚假相关性（Spurious Correlations）。 | 2023 CVPR |


## 起源

### 交通事件认知与推理
视频中的**交通事件认知与推理**是一项重要的任务，在智能交通、辅助驾驶和自动驾驶等领域有着广泛的应用。在本文中，我们创建了一个新颖的数据集 **SUTD-TrafficQA (Traffic Question Answering)**，该数据集以**视频问答（Video QA）**的形式呈现，基于收集到的 **10,080 个真实场景（in-the-wild）视频**和注释的 **62,535 个问答对**，旨在衡量复杂交通场景中**因果推理**和**事件理解**模型的认知能力。

- **具体而言**，我们提出了 **6 个具有挑战性的推理任务**，对应不同的交通场景，从而评估模型对各种复杂而实用的交通事件的推理能力。
- **此外**，我们提出了 **Eclipse**，一个新颖的**通过动态推理实现的有效一瞥网络（Efficient glimpse network via dynamic inference）**，旨在实现计算高效且可靠的视频推理。

项目页面：[https://github.com/SUTDCV/SUTD-TrafficQA](https://github.com/SUTDCV/SUTD-TrafficQA)

## 其他模型-可精读
### FinRpt模型
FinRpt:Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation  
[论文](https://arxiv.org/pdf/2511.07322) [代码](https://github.com/jinsong8/FinRpt) 

该论文首次提出了**股权研究报告（Equity Research Report, ERR）的自动生成任务**，并创建了一个完整的、面向该任务的开放基准 **FinRpt**。此外，作者还提出了一个基于大型语言模型（LLM）的**多智能体框架 FinRpt-Gen** 作为基线解决方案，旨在解决金融领域长文本生成中数据稀缺、评估复杂和推理难度大的挑战。

#### 核心创新与贡献
#### 1. 任务的首次定义与基准构建
- **定义任务：** 首次正式将 **ERR 自动生成**任务提上研究日程。ERR 要求模型整合和分析多源数据，生成包含财务分析、风险评估、投资潜力等多个专业部分的复杂长篇报告。
- **FinRpt 基准：** 建立了包含**数据集**和**评估系统**的开源基准 **FinRpt**。
    - **高质量数据集：** 通过一个**数据集构建流程（Dataset Construction Pipeline）**，自动整合了**7 种金融数据类型**（如财务报表、公司公告、新闻、历史股价等），并生成了高质量的 **ERR 中英双语数据集**（包含 6825 个样本）。该流程还包括**专家校正**和 **LLM 润色**等增强步骤。
    - **全面评估系统：** 引入了一个包含 **11 项指标**的综合评估体系，解决了现有评估指标（如 ROUGE、BERTScore）在金融专业性上的不足。新指标包括：**预测准确率（Accuracy）**、**数字覆盖率（NumberRate）**，以及基于 LLM 评估的**金融数值准确性（FN）**、**投资逻辑（Invest）**和**风险分析（Risk）**等。

#### 2. 多智能体解决方案 (FinRpt-Gen)
- **多智能体框架：** 提出了第一个专门用于 ERR 生成的**多智能体框架 FinRpt-Gen**。
- **复杂任务分解：** 框架将复杂的报告生成任务分解为**信息提取、信息分析和预测**三个阶段，并指派 **9 个专业 LLM 智能体**进行协同工作，模拟人类分析师的工作流程。例如：
    - **提取智能体：** 负责从原始数据中提取关键新闻、收入、资产和现金流指标。
    - **分析智能体：** 负责生成财务分析、新闻分析、经营分析和风险分析等核心报告章节。
- **优化训练机制：** 对关键智能体采用了**监督微调（SFT）来学习专业的分析和写作范式，并进一步使用了强化学习（RL，基于 DAPO 算法）来优化预测智能体**的性能，特别是提高**推荐评级**的准确性和投资分析的合理性。

#### 实验结论
实验结果表明：

1. **数据与指标的有效性：** FinRpt 基准的数据质量高，且其多维度评估指标能有效反映生成报告的**金融专业性和实用价值**。
2. **框架的优越性：FinRpt-Gen 多智能体框架**的性能显著优于单个 LLM 基线模型（包括 GPT-4o 和 Gemini-2.5 Pro 等顶尖模型），特别是在经过 SFT 和 RL 优化后，FinRpt-Gen 能够实现**最先进的性能**，展示了 LLM 协作在复杂金融任务中的巨大潜力。





---