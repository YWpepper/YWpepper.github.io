---
layout: post
title: 'FinRpt_PapperReading_AAAI2026'
date: 2025-11-14
author: pepper
tags: [papperReading, AAAI2026]
comments: true
toc: true
pinned: false
---
这篇博客介绍了FinRpt论文的阅读笔记。
<!-- more -->


## **<font style="color:rgb(0,0,0);">FinRpt</font>** 
尽管逻辑学习模型（LLM）在股票预测和问答等金融任务中取得了显著成功，但其在完全自动化生成股票研究报告方面的应用仍处于探索阶段。本文首次提出了股票研究报告（ERR）生成任务。为了解决**数据稀缺**和**评估指标缺失**的问题，我们提出了一个开源的**ERR生成评估基准**——FinRpt。我们构建了一个**数据集构建流程**，该流程集成了7种金融数据类型，并自动生成高质量的ERR数据集，可用于模型训练和评估。此外，我们还引入了一个包含11个指标的综合评估系统，用于评估生成的ERR。我们提出了一个专门针对此任务的多智能体框架，名为FinRpt-Gen，并**使用监督微调和强化学习**在所提出的数据集上训练了多个基于LLM的智能体。实验结果表明，基准FinRpt的数据质量和指标有效性以及FinRpt-Gen的优异性能，展现了它们在推动ERR生成领域创新方面的潜力。所有代码和数据集均公开可用。

### Methods
本工作首次正式定义了 ERR（Equity Research Report，股票研究报告）生成任务。给定一家公司的股票代码$s$和研究日期$t$，**系统自动收集和结构化最近的相关信息**，然后利用这些信息生成一份 ERR$R$。这种设置复刻了现实世界中研究分析师起草 ERR 的工作流程。在本文中，输入信息源$S = [O, F, A, N, P, M]$包括公司信息（Company Information）$O$、财务指标（Financial Indicators）$F$、公司公告（Company Announcements）$A$、公司相关新闻（Company-related News）$N$、历史股价（Historical Stock Prices）$P$和历史市场指数（Historical Market Indices）$M$。为了定义输出 ERR 的格式，我们总结了尽管各证券公司格式不一，一份理想的公司 ERR 至少应包含 6 个关键部分：财务分析（Financial Analysis）$R_{fin}$、新闻分析（News Analysis）$R_{news}$、管理与发展分析（Management and Development Analysis）$R_{manage}$、风险分析（Risks Analysis）$R_{risk}$、投资潜力评估（Investment Potential Assessment）$R_{invest}$和建议评级（Recommendation Rating）$R_{rec}$（建议买入评级或卖出评级）。我们在附录图 6 中展示了一个生成的 ERR 案例。

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763087961164-921b6ad2-182c-46bf-8252-1037298ed8ba.png" width="70%" alt="FinRpt Framework Diagram" />



#### Data Collection Module 数据采集模块

高质量的数据能确保从中得出的分析、预测和见解是有意义且值得信赖的。因此，设计良好的数据采集模块是必要的，它应能从各种**可靠来源**收集关键信息，这些来源需提供及时且全面的公司信息。

借鉴了以往研究的见解（Zhang et al. 2024b; Penman 2013; Greenwald et al. 2020; Yu et al. 2024a; Zhang et al. 2024a; Yu et al. 2024b; Fatemi and Hu 2024），我们精心选择了六种有价值且互补的公司相关数据类型，并将它们整合到我们的数据采集模块中：

+ (1) 公司信息 (Company Information)$O$：提供基础的公司信息（Yu et al. 2024b）。
+ (2) 财务指标 (Financial Indicators)$F$：反映公司的运营状况，并按季度发布（Fatemi and Hu 2024）。
+ (3) 公司公告 (Company Announcements)$A$：关于投资决策、人事变动或突发事件等重大变化，反映了公司的管理和发展（Zhang et al. 2024a）。此外，我们利用 GPT-4o-mini 来对公告进行总结。
+ (4) 公司相关新闻 (Company-related News)$N$：反映与特定公司相关的事件，影响投资者情绪并冲击股票走势（Yu et al. 2024a）。类似于公告总结，GPT-4o-mini 被用于总结新闻内容并过滤掉与公司股票无关的新闻。此外，我们移除了简短文章，并利用 BERTScore (Zhang et al. 2019) 和 MinHash (Broder 1997) 来对相似新闻进行去重。
+ (5) 历史股价 (Historical Stock Prices)$P$：在一定程度上反映了公司的价值，并为潜在的投资评估提供了有价值的见解（Zhang et al. 2024b）。
+ (6) 历史市场指数 (History Market Indices)$M$：反映了市场状况以及投资者的热情和信心（Yoo et al. 2021）。



#### Dataset Construction Pipeline 数据集构建流程  
为弥补 ERR 生成任务中数据稀疏性的不足，我们构建了一个 ERR 数据集，该数据集涵盖了中国市场 CSI800（中证 800）指数中的 800 支股票。这些对应的公司通常具有较高的市值，从而确保媒体上存在大量信息。数据范围从 2024 年 9 月 3 日到 2024 年 11 月 5 日，分析日期间隔为一周，每只股票共计有 10 个分析日期。最终，数据集包含 6,825 个数据样本（每个样本包括输入源信息和对应的 ERR）。

**1. 初始数据采集与过滤**

+ 数据采集： 首先，我们使用数据采集模块 (Data Collection Module) **收集**每只股票代码$s$和分析日期$t$的输入信息$S = [O, F, A, N, P, M]$，从而形成一个输入样本$(s, t, S)$。
+ 数据过滤： 随后，我们应用一个**过滤流程**来提高输入数据$(s, t, S)$的质量，剔除不满足以下条件的数据：
    - 缺乏财务指标$F$的数据。
    - 新闻文章$N$少于两篇的数据。
    - 总结后的公告$A$长度少于 300 个汉字的数据。

**2. ERR 自动生成**

+ 接下来，我们使用将在下一节介绍的多智能体框架 FinRpt-gen，其中每个 LLM（大型语言模型）智能体使用 **GPT-4o**，来自动生成 ERR$R$**，**从而得到一个完整的输入-输出数据样本$(s, t, S, R)$。

**3. 数据集增强模块 (Dataset Enhancement Module)**

为了使生成的 ERR 与专家撰写的 ERR 保持一致，我们开发了一个数据集增强模块来提升生成 ERR 的质量：

+ (1) 建议评级校正器 (Recommendation Rating Corrector)： 对于每个样本$(s, t, S, R)$，将$R$中建议评级$R_{rec}$与基本事实趋势标签 (ground truth trend label) 进行比较。如果不一致，则认为该 ERR 无效，并对该样本进行重新推理 (re-inferred)，直到生成正确的预测。
+ (2) 专家撰写 ERR 校正器 (Expert-written ERRs Corrector)： 对于每个样本$(s, t, S, R)$，我们从东方财富 (Eastmoney) 检索分析日期$t$前一周内与股票$s$相关的报告，作为可靠的 专家 ERR ($R_{experts}$)。然后，利用检索到的报告$R_{experts}$和生成的报告$R$来提示 LLM (GPT-4o)，以审查和改进信息的准确性、逻辑一致性和写作风格。详细的提示见附录表 16。
+ (3) LLM 润色器 (LLM Polisher)： 最后，我们将每个 ERR$R$输入到 LLM (GPT-4o) 中进行写作润色，以增强其可读性、连贯性和逻辑流畅性。

#### Dataset Statistics 数据集统计

我们分析了所构建数据集 FinRpt 的几项统计数据。该数据集包含从 2024 年 9 月 3 日到 2024 年 11 月 5 日期间的总计 6,825 份报告。

+ 平均而言，每只股票大约有 9 份报告。
+ 每个分析日期的报告总数约为 683 份。
+ 详细的行业分布统计如图 2 所示。


<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763088808278-6046aeac-df99-4f02-ae3f-3c940f022868.png" width="60%" alt="Industry Distribution Chart" />



图 2：FinRpt 数据集中不同行业报告的比例。

我们对数据集进行了如下划分：

+ **训练集 (Training Set) 和验证集 (Validation Set)**：2024 年 10 月 31 日之前的数据以 **9:1** 的比例随机划分为训练集和验证集。
+ **测试集 (Test Set)**：2024 年 10 月 31 日之后的样本用作测试集。

划分结果如下：训练集包含 5,556 个样本；验证集包含 617 个样本；测试集包含 652 个样本。

### FinRpt-Gen 框架
ERR（股票研究报告）生成任务要求模型具备广泛的**金融知识**、**标准化的报告**撰写风格以及出色的逻辑分析和预测能力。在这项工作中，我们提出了 FinRpt-Gen，如图 3 所示，这是首个专门为 ERR 生成任务设计的**多智能体框架**。鉴于已构建的数据集 FinRpt，FinRpt-Gen 包含三个模块：信息**提取**模块 (Information **Extraction** Module)、**分析模**块 (**Analysis** Module) 和**预**测模块 (**Prediction** Module)，共涉及扮演不同角色的九个智能体 (agent)。我们在附录中展示了每个智能体的提示示例。

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763088943088-3b33d7c0-9733-4bf2-858e-3ffeea824ae0.png" width="70%" alt="FinRpt-Gen Framework Diagram" />


```text
● 数据采集: 股票代码：600519.SS，分析日期：2024-11-05
● 信息提取模块 (Info. Extraction Module)
  ○ 新闻提取智能体 (News Extraction Agent)
  ○ 收入提取智能体 (Income Extraction Agent)
  ○ 资产负债提取智能体 (Balance Extraction Agent)
  ○ 现金流提取智能体 (Cash Extraction Agent)
● 信息分析模块 (Info. Analysis Module)
  ○ 财务分析智能体 (Finance Analysis Agent)
  ○ 新闻分析智能体 (News Analysis Agent)
  ○ 状态分析智能体 (Status Analysis Agent)
  ○ 风险分析智能体 (Risks Analysis Agent)
● 预测模块 (Prediction Module)
  ○ 预测智能体 (Prediction Agent)
● 生成(Generator)
● 输出： ERR (R)
```



##### Information Extraction Module 信息提取模块

信息提取模块从给定的输入数据 $ (s, t, S) $ 中提取相关信息。该模块涉及四个不同的智能体：

- (1) 新闻提取智能体 (News Extraction Agent)： 根据新闻对股票 $ s $ 的影响对所提供的新闻文章 $ N $ 进行排名，<u>并输出最有可能影响股价的前 10 条新闻</u>。代码路径: `finrpt/module/NewsAnalyzer.py`
- (2) 收入提取智能体 (Income Extraction Agent)： 给定财务指标 $ F $ 中的利润表 (income statement)，<u>提取关键财务指标</u>，例如收入 (revenue)、净利润 (net income)、每股收益 (earnings per share) 等。
- (3) 资产负债提取智能体 (Balance Extraction Agent)： 给定财务指标 $ F $ 中的资产负债表 (balance sheet)，重点关注资产 (assets)、负债 (liabilities) 和股本 (equity) 等关键<u>财务指标</u>。
- (4) 现金流提取智能体 (Cash Extraction Agent)： 给定财务指标 $ F $ 中的现金流量表 (cash flow statement)，重点关注来自经营活动、投资活动和融资活动的现金流。
  - 上述三个财务相关智能体的代码路径: `finrpt/module/FinancialsAnalyzer.py`

基于精心设计的提示和 LLM（大型语言模型）的**表格理解能力** (Sui et al. 2024)，这些智能体可以有效地**提取关键的财务指标和新闻**，以进行进一步的分析。

根据先前定义的 ERR 格式，我们设计了以下分析模块和预测模块，以系统地完成 ERR 的六个特定部分 $ R = [R_{fin}, R_{news}, R_{manage}, R_{risk}, R_{invest}, R_{rec}] $。


##### Information Analysis Module 信息分析模块

- (1) 财务分析智能体 (Finance Analysis Agent)： 根据收入、资产负债和现金流分析智能体的输出，该智能体<u>总结</u>公司的财务健康状况、盈利能力和现金流状况，生成财务分析 ($ R_{fin} $)。`代码路径: finrpt/module/FinRpt_analyst_finance.py`
- (2) 新闻分析智能体 (News Analysis Agent)： 根据新闻分析智能体的输出，该智能体强调所选新闻将如何影响未来的股票表现，然后生成新闻分析 ($ R_{news} $)。`代码路径: finrpt/module/FinRpt_analyst_news.py`
- (3) 状态分析智能体 (Status Analysis Agent)： 根据最新的公司公告 (Company Announcements) $ A $ 导出管理与发展分析 ($ R_{manage} $)。`代码路径: finrpt/module/Advisor.py`
- (4) 风险分析智能体 (Risk Analysis Agent)： 整合上述分析智能体提供的财务、新闻、管理和发展分析内容，分析应关注的关键风险 ($ R_{risk} $)。`代码路径: finrpt/module/RiskAssessor.py`


##### Prediction Module 预测模块 
预测模块中的预测智能体 (Prediction Agent) 收集 $ R_{fin} $、$ R*{news} $、$ R*{manage} $ 和 $ R*{risk} $ 的分析内容，以及<u>历史股价 </u>$ P $ 和<u>历史市场指数 </u>$ M $，然后<u>预测投资潜力评估 (</u>$ R*{invest} $<u>) 和建议评级 (</u>$ R*{rec} $<u>)</u>。`代码路径: finrpt/module/Predictor.py`

建议评级 ($ R\_{rec} $) 指对一项投资进行的评估或判断，反映了分析师对其表现潜力的意见或建议，通常分为“买入 (buy)” 或“卖出 (sell)”。


### SFT 监督微调  
在 FinRpt-Gen 框架内，我们专注于微调**四个最关键的智能体**：财务分析智能体 (Finance Analysis Agent)、新闻分析智能体 (News Analysis Agent)、状态分析智能体 (Status Analysis Agent) 和预测智能体 (Prediction Agent)。这些智能体负责处理生成深入、专业见解的最复杂任务。

我们使用来自 FinRpt 数据集相应部分的示例样本 (demonstration samples)。例如，给定一个数据样本$(s, t, S, R)$，对于财务分析智能体，输入是来自收入提取智能体、资产负债提取智能体和现金流提取智能体生成的内容。输出是$R$中的**财务分析 (**$R_{fin}$**) 部分**。

微调利用带有 **LoRA (Low-Rank Adaptation)** (Hu et al. 2022) 的 SFT，旨在学习一组低秩适配器参数$\Delta\theta$，以**最大化**给定输入$X$时生成目标文本$Y$的**似然性 (likelihood)**。优化目标公式如下：

$$\max_{\Delta\theta} \sum_{(X,Y) \in D_{demo}} \log P(Y | X; \theta_0 + \Delta\theta)$$

其中，$D_{demo}$是相应智能体的示例数据集，$\theta_0$代表预训练模型的原始参数，$\Delta\theta$是通过 LoRA 学习到的低秩更新参数。


训练框架与入口（LoRA 实现与训练管线）
```bash
finetune/LLaMA-Factory/
这是项目内嵌的训练框架，承担 LoRA 微调的核心实现与训练入口。
相关入口与示例：
  finetune/LLaMA-Factory/train_lora/（LoRA 训练脚本目录）
  finetune/LLaMA-Factory/examples/train_lora/（LoRA 训练示例与参考）
  finetune/LLaMA-Factory/README.md、README_zh.md（使用说明）
训练时使用的模型/数据/超参均通过 YAML 配置文件指定。
四个智能体的 SFT 配置（按智能体/任务分类）

财务分析智能体（Finance Analysis Agent）
  finetune/LLaMA-Factory/inference/llama3_lora_sft_finance.yaml
  finetune/LLaMA-Factory/merge_lora/llama3_lora_sft_finance.yaml
  finetune/LLaMA-Factory/merge_lora/qwen2.5_lora_sft_finance.yaml
  finetune/LLaMA-Factory/merge_lora/glm4_lora_sft_finance.yaml
新闻分析智能体（News Analysis Agent）
  finetune/LLaMA-Factory/inference/llama3_lora_sft_news.yaml
  finetune/LLaMA-Factory/merge_lora/llama3_lora_sft_news.yaml
  finetune/LLaMA-Factory/merge_lora/qwen2.5_lora_sft_news.yaml
  finetune/LLaMA-Factory/merge_lora/glm4_lora_sft_news.yaml
报告/状态（Report/Status，与你笔记中的“状态分析/报告生成”对应）
  finetune/LLaMA-Factory/inference/llama3_lora_sft_report.yaml
  finetune/LLaMA-Factory/merge_lora/llama3_lora_sft_report.yaml
  finetune/LLaMA-Factory/merge_lora/qwen2.5_lora_sft_report.yaml
  finetune/LLaMA-Factory/merge_lora/glm4_lora_sft_report.yaml
趋势/预测（Trend/Prediction，对应预测智能体）
  finetune/LLaMA-Factory/inference/llama3_lora_sft_trend.yaml
  finetune/LLaMA-Factory/merge_lora/llama3_lora_sft_trend.yaml
  finetune/LLaMA-Factory/merge_lora/qwen2.5_lora_sft_trend.yaml
  finetune/LLaMA-Factory/merge_lora/glm4_lora_sft_trend.yaml


说明：
  inference/ 下的 YAML 常用于推理/验证配置；
  merge_lora/ 下的 YAML 常用于合并 LoRA 权重或产线部署版本；
  实际训练脚本位于 train_lora/ 与 examples/train_lora/，通过 CLI 或脚本读取上述 YAML 执行训练。
```

训练框架与入口（LoRA 实现与训练管线）
```bash
数据/样本构建与处理（用于“示例样本”D_demo）
  dataset/alignment_research_report.py（研究报告对齐/样本构建）
  dataset/report_generate.py（生成报告相关的数据流）
  dataset/report_processing.py（报告清洗与整理）
  dataset/get_humman_data.py（人工数据采集/整理）
  dataset/statistics.py（数据统计与分析）
  dataset/filter_report.py（样本过滤）
  dataset/translate.py（必要的文本翻译处理）
这些脚本协同产出各智能体对应的“demonstration samples”，即笔记里提到的demo，供 LLaMA-Factory 的 LoRA-SFT 使用。
```



#### RL 强化学习 
为了进一步增强预测智能体 (Prediction Agent)，我们在 SFT 之后引入了强化学习阶段。此阶段超越了模仿模式，旨在优化智能体的输出以实现现实世界的投资目标。我们采用<u><font style="background-color:#FBF5CB;"> DAPO (Yu et al. 2025)</font></u>**，这是一种源自 <u><font style="background-color:#FBF5CB;">GRPO</font></u><u><font style="background-color:#FBF5CB;"> (Shao et al. 2024) 的</font></u>**<u><font style="background-color:#FBF5CB;">高级策略梯度算法</font></u>，用于将智能体的生成与准确性和理由质量的关键指标对齐。

###### Reward Function 奖励函数 
首先，我们设计了一个奖励函数 Reward$(Y, Y^*)$，用于整体评估生成的响应$$Y = [R_{invest}, R_{rec}]$$ 及其基本事实 $$Y^* = [R_{invest}^*, R_{rec}^*]$$ 该奖励是建议评级 ($R_{rec}$) 准确性和通过ROUGE (Lin 2004) 衡量的投资分析 ($R_{invest}$) 质量的加权组合。具体定义如下：

$$
Reward(Y, Y^*) = \alpha \cdot ACC(R_{rec}, R_{rec}^*) + \beta \cdot \text{ROUGE-1}(R_{invest}, R_{invest}^*) + \gamma \cdot \text{ROUGE-L}(R_{invest}, R_{invest}^*)
$$


其中，$\alpha$、$\beta$和$\gamma$是平衡每个组成部分重要性的超参数。在我们的配置中，我们将这些参数设置为$\alpha = 0.6$、$\beta = 0.2$和$\gamma = 0.2$。这种设置旨在优先考虑建议准确性，同时也兼顾分析内容的质量。

###### DAPO 优化目标
随后，<u><font style="background-color:#FBF5CB;">DAPO 算法通过最大化裁剪替代目标 (clipped surrogate objective) </font></u>来优化策略$\pi_\theta$，这是从<u><font style="background-color:#FBF5CB;">PPO (Proximal Policy Optimization) (Schulman et al. 2017) </font></u><u><font style="background-color:#FBF5CB;">继承</font></u>的原则，以确保训练稳定。该目标可以概念性地表达为：

$$
J_{DAPO}(\theta) \approx \mathbb{E}_{h} \min \left[ r(\theta) \hat{A}, \text{clip}(r(\theta), 1 - \epsilon_l, 1 + \epsilon_h) \hat{A} \right]
$$

这里，$r(\theta)$是新旧策略之间的概率比率，$\hat{A}$代表生成序列的标准化优势 (standardized advantage)。该目标鼓励提高奖励的更新，同时惩罚较大的策略偏移。完整、详细的公式在附录中提供。

### Evaluation 评估系统 
为了全面评估生成的 ERR（股票研究报告），我们设计了一个综合评估系统，它与我们之前构建的 FinRpt 数据集一起，形成了一个完整的基准 (benchmark)。

##### Basic Metrics 基本指标
基本指标用于从**文本相似性**和**预测准确性**的角度评估生成的 ERR：

+ (1) 完成率 (Completion Rate)： 揭示了该方法成功生成符合所需格式的 ERR 的案例比例。
+ (2) 准确率 (Accuracy)： 评估生成的建议评级（买入或卖出）的准确性。
+ (3)**<u><font style="background-color:#FBF5CB;"> BERTScore (Zhang et al. 2019)</font></u>**：使用 BERT 嵌入 (embeddings) 评估语义相似性。
+ (4)**<u><font style="background-color:#FBF5CB;"> ROUGE-L (Lin 2004)</font></u>**：ROUGE 指标家族中的一种，常用于评估摘要、文本生成和机器翻译的质量。
+ (5) 数值率 (Number Rate)： 衡量生成报告$N_{gen}$中数学数值的数量与参考 ERR$N_{ref}$中数值数量的比值，揭示了生成报告中数值内容的丰富程度。其计算公式为：

$\text{NumberRate} = \max(N_{gen}/N_{ref}, 1)$

##### LLM Evaluations 评估 
为了从语义含义和上下文方面评估生成的 ERR，我们参考了相关学术研究 (Penman 2013; Greenwald et al. 2020) 和行业实践，开发了一套指标：

+ (1) 财务数值 (Financial Numeric, FN)： 评估报告中提供数据的精确度和财务分析的深度。
+ (2) 新闻 (News)： 评估新闻分析与公司及其股票表现的相关性和全面性。
+ (3) 公司、市场与行业 (Company & Market & Industry, CMI)： 衡量模型对公司的管理结构、发展轨迹、市场趋势和整体行业环境的洞察力。
+ (4) 投资 (Invest)： 评估投资建议是否基于透彻、逻辑清晰且论据充分的分析。
+ (5) 风险 (Risk)： 评估报告对投资该股票潜在风险的分析彻底程度。
+ (6) 写作 (Writing)： 衡量整体的连贯性、可读性和逻辑一致性。

我们遵循以往的工作<u> (Zheng et al. 2023; Liu et al. 2024; Fu et al. 2023)</u>，采用一种保守的方法来比较 LLM 的性能。

+ 对比流程： 对于每个样本，<u><font style="background-color:#FBF5CB;">使用裁判智能体 (Judge Agent, GPT-4o) 对不同模型生成的 ERR 进行两两比较 (pairwise)</font></u>。
+ 消除位置偏差： 为消除位置偏差，裁判智能体交换报告的顺序，进行两次评估。
+ 获胜判定： 仅当一种答案在两种顺序下都被判定为更优时，才记录为获胜 (Win)；否则，结果标记为平局 (Tie)。
+ 计算： 评审过程结束后，我们可以计算获胜次数 (Win Counts)、平局次数 (Tie Counts) 和失败次数 (Loss Counts)。

为了方便比较，我们进一步计算了<u>调整获胜率 (Adjusted Win Rate)</u>：

$\text{Adjusted Win Rate} = \frac{\text{Win Counts} + 0.5 \cdot \text{Tie Counts}}{\text{Win Counts} + \text{Loss Counts} + \text{Tie Counts}}$

###  Experiments    实验  
**实现细节 (Implement Detail)**

+ 开源模型通过本地的 Ollama Python Library 访问，而闭源模型则通过其官方 API 访问。
+ SFT（监督微调）阶段在<u> 8 块 NVIDIA 3090 GPU</u> 上进行，而 RL（强化学习）阶段使用 <u>8 块 NVIDIA A100 GPU</u>。
+ 我们从 FinRpt 测试集中随机选择了 100 个样本进行评估。
+ 有关详细的超参数和进一步的实现细节，请参阅附录 (Appendix)。
+ 基线 (Baselines)：  
  我们针对四种类型的基线对我们的方法进行了评估：(1) 独立的先进 LLM（大型语言模型），(2) 我们的 FinRpt-Gen 框架与闭源 LLM 结合，(3) 该框架与开源 LLM 结合，以及 (4) 该框架与经过微调的开源 LLM 结合。有关所有基线的更详细描述，请参阅附录。

#### Basic Metrics 基本指标的主要结果
我们将 FinRpt-Gen 的性能与强大的基线进行比较，结果如表 1 所示，从中可以得出以下结论：

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763090342595-0bf241b9-6d16-4f19-a253-d5b03dc72be4.png" alt="Basic Metrics Results Table" style="width:70%; height:auto;" />


1. <u>多智能体框架 FinRpt-Gen 的性能显著优于单个 LLM</u>，这突出了我们多智能体框架的有效性。
2. 在**没有 SFT 和 RL** 的情况下，闭源模型 **Gemini-2.5-Pro 和 GPT-4o** 的性能明显优于所选的开源模型。这是一个预期的结果，因为 Gemini-2.5-Pro 和 GPT-4o 被广泛认为是该领域的领先模型。
3. 在构建的 FinRpt 数据集上**应用 SFT** 后，性能相比没有 SFT 的结果有了明显的提高，并且在几乎所有评估方面甚至超越了这两个闭源模型。
4. 通过** RL** 进一步**增强**后，实现了**最优性能**。这部分反映了我们数据集的高质量。

#### LLM 评估的主要结果 
基于前面详述的 LLM 评估指标，我们从金融专业性的角度比较了模型的性能。结果如图 4 所示。详细的定量结果可在附录表 5 中找到。

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763090552045-16530f29-7b27-4bc9-98e6-f0cc225b61dc.png" alt="LLM Evaluation Radar Chart" style="width:60%; height:auto;" />


+ 这个雷达图表明，我们训练后的模型取得了与 GPT-4o 相媲美的优异性能，并超越了所有其他强大的基线。
+ 值得注意的是，我们的训练模型在 CMI（公司、市场与行业）、新闻 (News) 和 FN（财务数值） 指标上甚至优于 FinRpt-Gen (GPT-4o)。
+ 通过比较结果，我们还可以得出 FinRpt-Gen 框架和 FinRpt 训练数据集的有效性。
+ 为了进一步验证我们的 LLM 评估的可靠性，我们在附录中进行了人工评估研究 (human evaluation study)。

#### Resource Requirements Analysis资源需求分析 
该框架的资源需求极少。从数据抓取 (data crawling) 到报告创建的整个 ERR 生成过程大约在 3 到 4 分钟内完成。有关资源需求的详细分解，包括处理时间和 API 成本，请参阅附录。

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763090647063-5da1a9c7-ebc8-4b63-bfee-6533770ae208.png" width="70%" alt="FinRpt-Gen Framework Diagram" />


---