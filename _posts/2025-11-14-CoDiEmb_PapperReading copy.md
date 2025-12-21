---
layout: post
title: 'CoDiEmb_PapperReading'
date: 2025-11-17
author: pepper
tags: [papperReading, Note]
comments: true
toc: true
pinned: false
---
这篇博客介绍了腾讯CoDiEmb论文的阅读笔记。
<!-- more -->


### **<font style="color:rgb(0,0,0);">CoDiEmb</font>** 
<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1763380215321-02076dfb-a517-4ec1-aaa4-d01fc06883c6.png" width="80%" alt="FinRpt Framework Diagram"/>

CoDiEmb: A Collaborative yet Distinct Framework for Unified Representation Learning in Information Retrieval and Semantic Textual Similarity
`CoDiEmb：一种用于信息检索和语义文本相似度中统一表示学习（Unified Representation Learning）的协作而又独特框架 [代码仓库](https://github.com/TencentCloudADP/youtu-embedding)` 

<font style="color:rgb(27, 28, 29);">【摘要】学习在各种下游任务中表现优异的统一文本嵌入 (unified text embeddings) 是表示学习 (representation learning) 的一个核心目标，然而负迁移 (negative transfer) 仍然是一个持续存在的障碍。当联合训练一个单一编码器以用于信息检索 (Information Retrieval, IR) 和语义文本相似度 (Semantic Textual Similarity, STS) 这两个基础但本质上不同的任务时，这个挑战尤为突出，因为朴素的联合训练 (naive cotraining) 通常会产生剧烈的性能权衡 (trade-offs)。我们认为，解决这一冲突需要在整个训练流程中系统地解耦任务特定的学习信号 (task-specific learning signals)。为此，我们引入了 CoDiEmb，这是一个统一框架，它以协作而又独特 (collaborative yet distinct) 的方式调和了 IR 和 STS 的不同需求。CoDiEmb 集成了三项关键创新以实现有效的联合优化：</font>

1. <font style="color:rgb(27, 28, 29);">任务专业化的目标函数 (Task-specialized objectives)，搭配一个动态采样器 (dynamic sampler) 来形成单任务批次 (single-task batches) 并平衡每个任务的更新 (per-task updates)，从而防止梯度干扰 (gradient interference)。对于 IR，我们采用带有多个正例 (positives) 和困难负例 (hard negatives) 的对比损失 (contrastive loss)，并通过跨设备采样 (cross-device sampling) 进行增强。对于 STS，我们采用顺序感知目标 (order-aware objectives)，直接优化相关性 (correlation) 和排序一致性 (ranking consistency)。</font>
2. <font style="color:rgb(27, 28, 29);">Delta 引导的模型融合策略 (A delta-guided model fusion strategy)，它通过分析每个参数与其预训练初始化 (pre-trained initialization) 的偏差 (deviation) 来计算检查点 (checkpoints) 的细粒度合并权重 (fine-grained merging weights)，证明比传统的 Model Soups 更有效。</font>
3. <font style="color:rgb(27, 28, 29);">一个</font><font style="color:rgb(27, 28, 29);">高效的单阶段训练流程 (An efficient, single-stage training pipeline)</font><font style="color:rgb(27, 28, 29);">，它</font><font style="color:rgb(27, 28, 29);">简单易实现</font><font style="color:rgb(27, 28, 29);">且</font><font style="color:rgb(27, 28, 29);">收敛稳定</font><font style="color:rgb(27, 28, 29);">。</font>

<font style="color:rgb(27, 28, 29);">在涵盖三个基础编码器 (base encoders) 的 15 个标准 IR 和 STS 基准测试上进行的广泛实验验证了 CoDiEmb。我们的结果和分析表明，该框架不仅减轻了跨任务的权衡，而且可衡量地改善了嵌入空间的几何特性 (geometric properties of the embedding space)。</font>

现代自然语言处理 (Natural Language Processing, NLP) 主要由生成 (generation) 和编码 (encoding) 两种范式驱动 [Muennighoff et al., 2024]。编码器模型 (encoder models) 的输出，即文本嵌入 (text embeddings)，构成了计算语言学的基石。在文本嵌入的无数应用和基准中，语义文本相似度 (Semantic Textual Similarity, **STS**) 和信息检索 (Information Retrieval, **IR**) 脱颖而出，成为两个最关键的任务 [Gao et al., 2021]。

- STS 旨在确定两个文本片段之间的语义邻近度 (semantic proximity)，形成了推荐系统、文本聚类和内容标准化等技术的基础 [Sheng et al., 2024]。
- 另一方面，IR 侧重于衡量查询 (query) 与大型文档集合 (large document collection) 之间的相关性 (relevance)，在搜索引擎、对话平台和 AI 智能体中发挥着关键作用 [Sun et al., 2025]。

**<font style="background-color:#FBF5CB;">统一文本编码器的目标与挑战</font>**

受创建一种在两个任务家族中均表现出色的通用文本编码器 (universal text encoder) 这一目标的驱动，目前最先进的嵌入模型通常会使用对比学习 (contrastive learning) 在 STS 和 IR 数据集的大型混合上进行联合训练 (co-train) [Xiao et al., 2024, Lee et al., 2024]。虽然这种做法简单直接，但它忽略了两种任务类型之间固有的差异 (inherent discrepancies)。具体来说，STS 和 IR 在几个关键方面表现出显著的不同：

• <font style="background-color:#D9EAFC;">数据结构和对称性 (Data Structure and Symmetry)</font>

+ STS 任务通常以三元组 $ (x_1, x_2, y) $ 的形式组织数据，其中成对的文本 $ x_1 $ 和 $ x_2 $ 具有高度对称性 (highly symmetric)；交换它们的位置并不会改变标签 $ y $。
+ 相比之下，IR 数据集本质上是非对称的 (inherently asymmetric)，包括一组查询 $ \{q\}_i $、一个大型文档语料库 $ \{d\}_j $ 以及定义它们之间关系的相关性映射 (relevance mapping) $ \{(q_i, d_j)\}_{l} $。在推理过程中，查询 $ q_i $ 会与 $ \{d\}_{n} $ 中的每个文档进行匹配，但只有映射中指定的对 $ (q_i, d_j) $ 才被视为相关。

• <font style="background-color:#D9EAFC;">语义粒度和文本长度 (Semantic Granularity and Text Length)</font>

+ STS 任务要求细粒度的语义区分 (fine-grained semantic distinctions)，并且它们的训练集和评估集通常具有粒度注释分数 (granular annotation scores)。由于语义相似度的定义会随着文本长度的增加而变得更加模糊 [Deshpande et al., 2023]，因此 STS 序列通常较短。
+ 相反，IR 中查询和文档的长度高度灵活，文档经常包含数百个标记 (tokens)。因此，尽管这两个任务都利用余弦相似度 (cosine similarity) 进行高效匹配，但计算的潜在含义有所不同：STS 优先考虑语义等效性 (semantic equivalence)，而 IR 更倾向于主题 (topical) 或知识层面 (knowledge-level) 的相关性。

<font style="background-color:#D9EAFC;">• 评估指标 (Evaluation Metrics)</font>

+ STS 的主要指标是斯皮尔曼等级相关系数 (Spearman’s rank correlation coefficient) [Zar, 2005]，它衡量预测排名和真实排名之间的单调关系 (monotonic relationship)。
+ IR 中使用的 归一化折扣累积增益 (Normalized Discounted Cumulative Gain, nDCG) 指标 [Wang et al., 2013] 也是列表式 (list-wise) 的，但更强调排名靠前项的正确性。此外，由于在 IR 中，给定查询的相关文档通常是稀疏的 (sparse)，因此通常采用 nDCG@k。

这些差异导致在不加区分地优化 (optimized indiscriminately) 这两项任务时，模型性能会次优 (suboptimal)。正如我们将在第 3 节中展示的，天真地应用适用于其中一项任务的目标函数（例如，适用于 IR 的 **InfoNCE Loss** [Oord et al., 2018] 或适用于 STS 的 **CoSENT Loss** [Huang et al., 2024]）会对另一项任务造成损害。相比之下，我们提出的框架 CoDiEmb 在**联合训练**期间在 IR 和 STS 之间取得了稳健的平衡 (robust balance)，接近甚至超越了单任务微调 (single-task fine-tuning) 的性能。

值得注意的是，一些前沿研究也观察到了这些性能权衡。[_Asai et al. [2022] _](https://aclanthology.org/2023.findings-acl.225.pdf)_ _<font style="background-color:#E6DCF9;">meta公司</font>_提出为不同任务设计独特的指令 (distinct instructions) 并将其前置于输入文本_。虽然这一策略带来了显著的改进，但此类指令提供的先验信息是有限的，并且完全依赖于模型的隐式上下文理解，缺乏明确的梯度信号 (explicit gradient signals)。[Jina-embeddings-v3 [Sturua et al., 2024]](https://arxiv.org/pdf/2409.10173?) <font style="background-color:#E6DCF9;">小众德国公司</font> _引入了 Task LoRA 进行参数级别的定制_，但这需要存储一系列适配器 (adapters)。此外，如果一个文档出现在 $ k $ 个任务集中，则需要 $ k $ 个不同的嵌入，从而产生高昂的存储成本 (prohibitive storage costs)。[NV Embed [Lee et al., 2024]](https://arxiv.org/pdf/2405.17428?) <font style="background-color:#E6DCF9;">英伟达公司</font> 将所有数据类型转换为 IR 格式并构建了一个_两阶段训练流程 _(two-stage training pipeline)：首先使用困难负例 (hard negatives) 对 IR 数据集进行微调，然后对所有语料库的混合进行不带困难负例的对比学习。这个过程不可避免地丢弃了大量无法被构建成正例对 (positive pairs) 的低分 STS 数据。此外，正如先前工作所指出的，粗粒度 (coarse-grained) 的对比目标不适合带有细粒度标签的任务[ [Zhang and Li, 2024]](https://aclanthology.org/2024.emnlp-main.663.pdf)<font style="background-color:#E6DCF9;"> 清华学校 </font>。

---

#### CoDiEmb 框架的提出
这种现状揭示了对统一、有效且端到端 (end-to-end) 的** IR 和 STS** 联合优化解决方案的迫切需求。为此，我们提出了 CoDiEmb，一个从损失函数 (loss functions)、数据采样 (data sampling) 和模型融合 (model fusion) 等多个角度，协作而又独特 (Collaboratively yet Distinctly) 地处理信息检索和语义文本相似度的框架。

##### 针对 IR 任务的优化
具体来说，对于 IR 任务，我们设计了一种支持每个锚点 (anchor) 具有多个正例和困难负例的对比损失。该损失通过跨设备负采样 (cross-device negative sampling) 得到增强，这极大地扩大了比较候选池 (comparison candidates)，产生了更清晰的可分离性 (sharper separability)。在此过程中，CoDiEmb 的动态采样器 (dynamic sampler) 确保在每次迭代中，所有 GPU 严格从同一数据文件的不相交子集 (disjoint subsets) 中抽取样本，从而提供纯粹的任务梯度 (pure task gradients)。

##### 针对 STS 任务的优化
对于 STS 任务，我们没有依赖二元分类式 (binary classification-style) 的 InfoNCE Loss，也没有通过惩罚倒置对 (inverted pairs) 来近似排序目标，而是选择了直接优化顺序一致性 (direct optimization of order consistency)。在 [Pcc-tuning [Zhang and Li, 2024] ](https://aclanthology.org/2024.emnlp-main.663.pdf)中提出的 Pearson Loss 的基础上，我们引入了修改和适配的 KL 散度损失 (KL divergence Loss) 和 [PRO Loss [Peng et al., 2024]](https://arxiv.org/pdf/2311.03758) <font style="background-color:#E6DCF9;">中科大淘宝阿里巴巴 </font>，它们实质性地增强了模型的细粒度语义区分能力 (fine-grained semantic discrimination)。

##### 模型融合策略
最后，通过分析微调参数与预训练值 (pre-trained values) 的偏差 (deviation)，我们开发了一种创新性的模型融合策略。将此方法应用于来自不同训练轨迹的检查点 (checkpoints) 时，所获得的性能增益超越了标准 [Model Soups [Wortsman et al., 2022] ](about:blank)<font style="background-color:#E6DCF9;">washington+google公司</font>所达到的效果。

#### 贡献总结 
总而言之，本文的主要贡献如下：

+ 我们提出了 CoDiEmb，这是一个使模型能够在单个训练阶段内有效地收敛于 IR 和 STS 这两项任务的框架。CoDiEmb 不需要适配器组件 (adapter components)，并且其统一的数据格式与任意粒度 (arbitrary granularity) 的语料库完全兼容，从而无需丢弃任何样本。
+ 我们制定了根据 IR 和 STS 的不同特征量身定制的**专业化损失函数**。结合我们自定义的动态采样器，这种方法不仅平衡了每个任务的迭代次数，还避免了混合任务批次 (mixed-task batches) 引起的梯度干扰。
+ 通过分析不同训练设置下的参数偏移 (parameter shifts)，我们设计了一种有效的加权方案 (weighting scheme) 用于集成检查点 (ensembling checkpoints)。我们的方法超越了传统的模型级融合，达到了更精细的粒度，直接作用于可学习参数 (learnable parameters)。
+ 我们使用 MiniCPM [Hu et al., 2024]、E5 [Wang et al., 2024] 和 BGE [Xiao et al., 2024] 在 8 个 IR 和 7 个 STS 基准测试上进行了广泛的实验，充分验证了 CoDiEmb 的优越性。为了进一步阐明我们方法的基本原理，我们提供了一系列理论分析，发现 CoDiEmb 的联合优化策略有效地缓解了学习到的表示空间中的各向异性 (anisotropy) [Ethayarajh, 2019] 和过度平滑 (over-smoothing) [Shi et al., 2022]。

#### <font style="color:rgb(27, 28, 29);">CoDiEmb 框架</font>
<font style="color:rgb(27, 28, 29);">本节将介绍 CoDiEmb，我们用于跨 STS (Semantic Textual Similarity, 语义文本相似度) 和 IR (Information Retrieval, 信息检索) 任务进行统一表示学习 (unified representation learning) 的端到端框架 (end-to-end framework)。我们首先在第 2.1 节介绍我们的任务无关数据格式 (task-agnostic data format)，解释其与异构粒度 (heterogeneous granularity) 输入的兼容性及其对其他任务的可扩展性 (extensibility)。随后，在第 2.2 节中，我们详细阐述 CoDiEmb 的专业化损失函数 (specialized loss functions)，并将其设计与相应的评估指标联系起来。在此基础上，第 2.3 节描述了 CoDiEmb 的数据采样器 (data sampler) 和多设备训练配置 (multi-device training configuration)。最后，在第 2.4 节中，我们介绍我们提出的参数级别模型融合策略 (parameter-level model fusion strategy)。</font>

### 方法论
#### 统一数据格式 (Unified Data Format)
IR（信息检索）和 STS（语义文本相似度）遵循由其各自评估协议驱动的不同数据组织方案 (distinct data organization schemes)。如图 1 所示，IR 任务将来自集合 $\{q\}_m$ 的每个查询 $q_i$ 与整个文档语料库 $\{d\}_n$ 进行匹配，以_检索最相关的 top-k_ 结果。真实相关性 (Ground-truth relevance) 由映射表 $\{(q_i, d_j)\}_l$ 定义，该表通常仅存储正例样本 (positive samples) 的标识符。任何未出现在此映射中的对 $(q_i, d_j)$ 被隐式视为负例样本 (negative sample)。在这些负例文档中，有些更难以与正例区分被称为_困难负例 (hard negatives)_。社区早已认识到困难负例对于 IR 的至关重要性 [Zhan et al., 2021, Zhou et al., 2022]。因此，通常采用数据挖掘技术 (data mining techniques) 来识别给定查询 $q$ 的一组困难负例 $\{d^-\}$，从而形成 $(q, d^+, \{d^-\})$ 的数据结构。

相比之下，STS 任务中的配对 $(x_1, x_2)$ 被视为独立的实例 (independent instances)。模型通过余弦相似度 (cosine similarity) 直接预测一个分数 $\hat{y}$，然后将产生的预测列表 $\{\hat{y}\}_n$ 与真实分数 (ground-truth scores) $\{y\}_n$ 进行比较，以评估排名一致性 (rank consistency)。因此，STS 数据通常被构造为三元组 $(x_1, x_2, y)$。

为兼容这两种数据类型，CoDiEmb 采用了统一格式：$(t, q, \{d^+\}_m, \{d^-\}_n, \{y^+\}_m, \{y^-\}_n)$，其中，$t$ 是任务标识符 (task identifier)，可以在数据集级别指定。原始数据中缺失的字段将用占位符 (placeholders) 填充，这些占位符在前向传播 (forward pass) 期间被忽略，不会产生额外的内存开销。

这种集成的数据结构具有高度的可扩展性 (extensibility)。

+ 当处理 STS 任务时，我们将三元组 $(x_1, x_2, y)$ 分别映射到查询 $q$、第一个正例文档 $d_1^+$ 和第一个正例分数 $y_1^+$。
+ 对于 IR 任务，我们填充查询 $q$、正例集合 $\{d^+\}_m$ 和负例集合 $\{d^-\}_n$。如果相关性分数可用，它们可以存储在相应的 $\{y\}$ 字段中。

这种可扩展格式还自然地支持分类和聚类等其他任务。对于这些任务，数据可以按标签分区，允许进行簇内 (intra-cluster, 正例) 和簇间 (inter-cluster, 负例) 采样，以构建用于对比学习的输入。通过将输入文本分配给 $q$ 并将其标签分配给 $y^+$，该格式也与分类头架构 (classifier-head architectures) 兼容 [Reimers and Gurevych, 2019, Zhang and Li, 2024]。

利用这种统一数据结构，CoDiEmb 不仅标准化了多样化语料库的加载，还能够配置根据任务特征量身定制的差异化损失函数 (differentiated loss functions)，从而促进多粒度训练 (multi-granularity training)。尽管本文重点关注 IR 和 STS 的联合优化，但 CoDiEmb 的潜力超越了这一范围，我们计划在未来的工作中进行探索。

### 3 总结
##### CoDiEmb 框架的主要创新点 
CoDiEmb 框架通过“协作而又独特”的方式，从损失函数、数据处理和模型优化等多个维度解决了 IR 和 STS 联合优化的难题。

**1. 统一框架与单阶段训练 (Unified Framework and Single-Stage Training)**

+ 提出 CoDiEmb 框架： 提出了一种新颖的框架 CoDiEmb，使模型能够在单个训练阶段内有效收敛于 IR 和 STS 这两项本质不同的任务 。
+ 无需适配器： CoDiEmb 不需要适配器组件 (adapter components) 。
+ 统一数据格式： 采用了统一数据格式来兼容 IR 和 STS 任务，并支持与任意粒度的语料库完全兼容，从而避免了丢弃任何样本的需求。

**2. 专业化损失函数与动态采样 (Specialized Loss Functions and Dynamic Sampling)**

+ 定制化损失函数： 制定了根据 IR 和 STS 的不同特征量身定制的专业化损失函数 (specialized loss functions) 。
    - 针对 IR： 设计了支持每个锚点 (anchor) 具有多个正例和困难负例的对比损失 ，并通过跨设备负采样 (cross-device negative sampling) 增强，以扩大比较候选池，提高可分离性 。
    - 针对 STS： 引入了修改和适配的 KL 散度损失 (KL divergence Loss) $ \mathcal{L}_{RankKL} $ 和 PRO Loss，它们直接优化顺序一致性 (order consistency)，实质性地增强了模型的细粒度语义区分能力 。
+ 避免梯度干扰： 结合自定义动态采样器 (custom dynamic sampler)，该方法不仅平衡了每个任务的迭代次数，还通过严格确保各 GPU 仅处理来自同一数据集的非重叠子集，从而避免了混合任务批次 (mixed-task batches) 引起的梯度干扰，提供了纯粹的任务梯度 (pure task gradients) 。
+ STS 损失组合： 最终的 $ L_{STS} $ 是 $ L_{Pearson} $、$ L_{RankKL} $、$ L_{PRO} $ 和辅助 InfoNCE Loss $ L_{MidNCE} $ 的加权和，实现多层次优化 。

1. **分层模型融合策略 (Hierarchical Model Fusion Strategy)**

+ 创新的融合策略： 通过分析微调参数与其预训练值之间的偏差 (deviation)，设计了一种创新的模型融合策略 
+ 参数级别融合： 该方法超越了传统的模型级别融合（如 Model Soups ），达到了更精细的粒度，直接作用于可学习参数 (learnable parameters) 。
+ 融合权重方案： 设计了一种有效的加权方案 (weighting scheme) 用于集成检查点 。

**4. 几何特性改善 (Improvement in Geometric Properties)**

+ 几何特性改善： 理论分析发现，CoDiEmb 的联合优化策略有效地缓解了学习到的表示空间中的各向异性 (anisotropy) 和过度平滑 (over-smoothing) 。
+ 指标优势： 在嵌入空间质量指标上，CoDiEmb 实现了最低的标记间相似度 (Token-wise Similarity)，最高的秩 (Rank) 和 SVD 熵 (SVD Entropy)，以及显著更低的条件数 (Condition Number) 。






---