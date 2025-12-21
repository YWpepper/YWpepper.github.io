---
layout: post
title: 'Training-Free GRPO_PapperReading'
date: 2025-12-07
author: pepper
tags: [papperReading, Note]
comments: true
toc: true
pinned: false
---

这篇博客介绍了腾讯Training-Free GRPO论文的阅读笔记。

<!-- more -->
[代码仓库](https://github.com/TencentCloudADP/youtu-agent/tree/main)
[参考论文1-腾讯](https://arxiv.org/pdf/2510.08191)
[参考论文2-字节](https://arxiv.org/pdf/2511.06449)

## 摘要

大型语言模型 (Large Language Model, LLM) 智能体在近期取得了进展，展现了其有前景的通用能力。然而，由于难以有效集成外部工具和特定的提示策略，它们在专业化的现实世界领域中的性能通常会下降。虽然已经提出了诸如智能体强化学习 (agentic reinforcement learning) 等方法来解决这个问题，但*它们通常依赖成本高昂的参数更新*，例如通过一个使用监督微调 (Supervised Fine-Tuning, SFT) 随后进行强化学习 (Reinforcement Learning, RL) 阶段（采用群体相对策略优化 (Group Relative Policy Optimization,**GRPO**)）来改变输出分布的过程。

💡然而，我们认为 LLMs 可以通过将经验知识 (experiential knowledge) 作为标记先验 (**token prior**) 来学习，从而对输出分布产生类似的效果，这是一种轻量得多 (far more lightweight) 的方法，它不仅解决了实际*数据稀疏性* (practical data scarcity) 的问题，而且避免了常见的*过拟合* (overfitting) 问题。

💡为此，我们提出了*免训练群体相对策略优化* (Training-Free Group Relative Policy Optimization, Training-Free GRPO)，这是一种*成本效益高的解决方案*，可以在不进行任何参数更新的情况下增强 LLM 智能体的性能。我们的方法利用每组推演 (rollouts) 内的群体相对语义优势而非数值优势，在**最小量的真实数据** (minimal ground-truth data) 上进行多轮 (multi-epoch) 学习过程中，迭代地提炼 (iteratively distilling) 高质量的经验知识。此类知识作为习得的标记先验，在 LLM API 调用期间被无缝集成以指导模型的行为。

在数学推理 (mathematical reasoning) 和网络搜索 (web searching) 任务上的实验表明，Training-Free GRPO 应用于 DeepSeek-V3.1-Terminus 时，显著改善了域外性能 (out-of-domain performance)。仅凭几十个训练样本 (few dozen training samples)，Training-Free GRPO 的性能就超越了具有少量训练数据和成本的微调小型 LLMs (fine-tuned small LLMs)。

## Introduction

大型语言模型 (Large Language Models, LLMs) 正在成为强大的通用智能体 (general-purpose agents)，能够与复杂的现实世界环境进行交互。它们在一系列广泛的任务中展现出卓越的能力，包括复杂问题解决 [4, 5, 6]、高级网络研究 [7, 8, 9, 10]、代码生成与调试 [11, 12]，以及熟练的计算机使用 [13, 14, 15]。

尽管它们的能力令人印象深刻，但 LLM 智能体在专业化的现实世界领域中往往表现不佳。这些场景通常要求集成外部工具 （例如，计算器、API、数据库），以及领域特定的任务定义和提示策略 (prompting strategies)。在这样的设置中，开箱即用 (out-of-the-box) 地部署通用智能体，通常由于对领域特定要求的不熟悉或对必要工具的接触不足而导致次优性能 (suboptimal performance)。


### Challenges in Agentic Training

为了弥合这一差距，智能体训练 (agentic training) 已成为促进 LLM 智能体适应特定领域及其相关工具的一种有前景的策略 [4, 7, 8, 16]。最近，智能体强化学习 (Agentic Reinforcement Learning, Agentic RL) 方法的进展采用了 **群体相对策略优化** (Group Relative Policy Optimization, GRPO) [17] 及其变体 [18, 19, 20] 来在参数空间 (parameter space) 中对齐模型行为。尽管这些方法有效地增强了任务特定能力，但它们依赖于调整 LLM 参数，带来了若干实际挑战：

* 计算成本 (Computational Cost)： 即使对于较小的模型，微调也需要大量的计算资源，这使其既昂贵又对环境不可持续。对于更大的模型，成本变得令人望而却步 (prohibitive)。此外，微调后的模型需要**专用部署** (dedicated deployment)，并且通常局限于特定应用，相对于更通用的模型而言，对于低频用例 (low-frequency use cases) 效率低下。
* 泛化能力差 (Poor Generalization)： 通过参数调整优化的模型通常会遭受不尽如人意的跨域泛化 (unsatisfactory cross-domain generalization)，限制了它们的适用范围仅限于狭窄的任务。因此，必须部署多个专业化模型 (multiple specialized models) 来处理一套全面的任务，这显著增加了系统复杂性 (system complexity) 和维护开销 (maintenance overhead)。
* 数据稀缺性 (Data Scarcity)： 微调 LLMs 通常需要大量高质量、精心标注的数据，而这些数据在专业领域往往稀缺 且获取成本极高 (prohibitively expensive)。此外，样本有限时，模型极易受到过拟合 (overfitting) 的影响，导致泛化能力差。
* 回报递减 (Diminishing Returns)： 令人望而却步的训练成本通常迫使现有方法微调参数少于 320 亿的较小 LLMs，这是由于资源限制而非最优设计选择。虽然更大型的模型会更受青睐，但微调的计算开销迫使了这种妥协。矛盾的是，基于 API 或开源的更大型 LLMs 通常通过可扩展性和持续的模型更新提供更好的成本-性能比 (cost-performance ratios)。然而，这些通用模型在需要微调的专业领域表现不佳，从而产生了成本-性能困境 (cost-performance dilemma)。

### Proposed Solution

> 参数调整固有的这些限制促使了一个基础性的研究问题：应用 RL 在参数空间中是唯一可行的途径吗？我们能否以非参数方式，用更低的数据和计算成本来增强 LLM 智能体的性能？

我们通过提出**免训练群体相对策略优化** (Training-Free Group Relative Policy Optimization, Training-Free GRPO)，肯定地回答了这个问题。这是一种新颖且高效 的方法，它以类似于原始 GRPO 的方式改进 LLM 智能体的行为，同时保持原始模型参数不变 (preserving the original model parameters unchanged)。

我们的方法源于一个洞察：LLMs 已经拥有适应新场景的基本能力，**只需通过有限样本进行最小量的实践 即可达到强大的性能**。因此，与其通过参数调整来调整它们的输出分布，不如利用**轻量级标记先验 (lightweight token prior)** 的上下文学习 (in-context learning) 也能封装从最小训练数据集中学到的经验知识。

Taining-Free GRPO 保留了原始 GRPO (vanilla GRPO) 的**多轮学习机制** (multi-epoch learning mechanism)。💡在每一轮中，**系统会为每个查询生成多个输出**，以提供一组推演 (group of **rollouts**)，这有助于探索**策略空间** (explore the **policy** space) 和**评估潜在策略** (evaluate **potential** **strategies**)。

然而，原始 GRPO 依赖基于**梯度的参数更新** (gradient-based parameter updates) 来迭代改进策略性能，而 Training-Free GRPO 通过💡使用 LLMs（大型语言模型）的仅推理操作 (inference-only operations) 消除了这一要求。在每个优化步骤中，我们的方法不是为每组推演中的梯度上升 (gradient ascent) 计算数值优势 (numerical advantage)，而是利用 LLMs 对每组进行内省 (introspect) 并提炼出语义优势 (semantic advantage)。

这种优势精炼了外部经验知识 (experiential knowledge)，并基于不断演变的上下文先验 (contextual priors) 来指导策略输出，从而在不修改任何模型参数的情况下实现了策略优化效果。

通过评估富有挑战性的数学推理和交互式网络搜索任务，我们证明了该方法能够显著**增强冻结策略模型** (frozen policy models)，例如 DeepSeek-V3.1-Terminus [3] 的性能，**仅需数十个训练样**本。它在性能上超越了**经过微调**的 32B 模型，而所需的计算资源仅占其一小部分，为传统微调技术提供了一种更简单、效率更高的替代方案。

我们的主要贡献有以下三方面：

* 一种新的免训练 RL 范式 (A New **Training-Free** RL Paradigm)：我们引入了 Training-Free GRPO，它通过利用不断演变的经验知识作为标记先验 (token priors)，将**策略优化**从**参数空间**转移到**上下文空间** (context space)，无需梯度更新。
* 语义群体优势 (Semantic Group Advantage)：我们用语义群体优势取代了原始 GRPO 中的数值群体优势，使 LLMs 能够内省自身的推演，并在多个优化步骤中持续更新经验知识。
* 数据和计算效率 (Data and Computational Efficiency)：实验证实，Training-Free GRPO 能用最少的训练样本有效提升冻结策略的性能，为不同领域提供了一种实用且成本效益高的替代方案。
* 卓越的泛化能力 (Superior Generalization)：通过保持模型参数冻结并插入不同的标记先验，我们的方法完全保留了泛化能力，消除了部署多个微调专家模型的成本和复杂性。


<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1765115609308-0106c8a6-68e6-47ff-9065-504fecf54408.png?x-oss-process=image%2Fformat%2Cwebp" width="85%"/>


## 2 Training-Free GRPO

本节介绍我们的免训练 GRPO (Training-Free GRPO)，该方法旨在复制 GRPO 算法的对齐效益，而无需对策略模型的参数执行任何基于梯度的更新。

### 原始 GRPO (Vanilla GRPO)

原始 GRPO 过程首先使用当前策略 LLM $\pi_{\theta}$ 为给定查询 $q$ 生成一组 $G$ 个输出 $\{o_1, o_2, \ldots, o_G\}$，即 $\pi_{\theta}(o_i \| q)$。然后，每个输出 $o_i$ 通过一个奖励模型 $R$ 进行独立评分。随后，利用奖励 $r = \{r_1, \ldots, r_G\}$，它为每个输出 $o_i$ 计算一个群体相对优势 (group-relative advantage)：

$$
\hat{A}_i = \frac{r_i - \text{mean}(r)}{\text{std}(r)}
$$

通过结合针对参考模型 (reference model) 的 KL 散度惩罚 (KL-divergence penalty)，它构建了一个 PPO 裁剪目标函数 (PPO-clipped objective function)：

$$
J_{\text{GRPO}}(\theta)
$$

然后通过最大化该函数来更新 LLM 参数 $\theta$。

### Training-Free GRPO 的核心逻辑

Training-Free GRPO 重新利用了这种基于群体的相对评估的核心逻辑，但将其转化为非参数化 (non-parametric) 的推理时过程 (inference-time process)。我们永久冻结参数 $\theta$，并维护一个外部经验知识 (external experiential knowledge) $E$，其初始化为 $\emptyset$，而不是更新参数 $\theta$。

#### 推演与奖励 (Rollout and Reward)

我们的推演和奖励过程与 GRPO 完全一致。给定一个查询 $q$，我们执行一个并行推演 (parallel rollout)，使用 LLM 生成一组 $G$ 个输出 $\{o_1, o_2, \ldots, o_G\}$。值得注意的是，虽然 GRPO 使用当前的可训练策略 $\pi_{\theta}$，但我们的策略以经验知识 $E$ 为条件，即 $\pi_{\theta}(o_i \| q, E)$。与标准 GRPO 设置相同，我们通过奖励模型 $R$ 对每个输出 $o_i$ 进行评分，以获得一个标量奖励 (scalar reward) $r_i = R(q, o_i)$。

#### 群体优势计算 (Group Advantage Computation)

为了为策略参数提供优化方向，原始 GRPO 计算一个数值优势 $\hat{A}_i$，用于**量化每个输出 $o_i$ 在其群体内的相对质量**。类似地，Training-Free GRPO 在每个群体内执行类似的比较，但会以自然语言经验的形式产生群体相对语义优势 (group relative semantic advantage)。

> 📌 **注意**：在原始 GRPO 中，当所有 $G$ 个输出获得相同奖励（即 $\text{std}(r) = 0$）时，$\hat{A}_i = 0$，因此我们仅对存在明确赢家和输家的群体生成这种语义优势。

具体来说，对于每个输出 $o_i$，我们首先询问同一个 LLM $M$ 分别提供一个相应的总结：

$$
s_i = M(p_{summary}, q, o_i)
$$

其中 $p_{summary}$ 是一个提示模板，它结合了查询 $q$ 和输出 $o_i$ 来形成一个结构化的总结请求。给定总结 $\{s_1, s_2, \ldots, s_G\}$ 和当前的经验知识 $E$，LLM $M$ 阐明了输出相对成功或失败的原因，然后提取一个简洁的自然语言经验：

$$
A_{\text{text}} = M(p_{extract}, q, s_i, E)
$$

其中 $p_{extract}$ 是另一个用于经验提取的提示模板。

这种自然语言经验 $A_{\text{text}}$ 作为我们的语义优势，在功能上等同于原始 GRPO 的 $\hat{A}_i$，它编码了什么行动导致高奖励的关键经验知识。

#### 优化 (Optimization)

原始 GRPO（vanilla GRPO）通过在单个批次中计算得到的所有优势 (all advantages) 对 $J_{\text{GRPO}}(\theta)$ 进行梯度上升 (gradient ascent) 来更新其模型参数 $\theta$。

> 📌 **而我们则使用当前批次中的所有语义优势 $A_{\text{text}}$ 来更新我们的经验库 (experience library) $E$**。

具体来说，给定现有的经验库 $E$，我们提示 LLM 根据所有这些 $A_{\text{text}}$ 生成一个操作列表 (list of operations)，其中每个操作可以是：

- **添加 (Add)**：将 $A_{\text{text}}$ 中描述的经验直接附加到经验库 $E$ 中。
- **删除 (Delete)**：基于 $A_{\text{text}}$，从经验库 $E$ 中移除一条低质量经验。
- **修改 (Modify)**：基于 $A_{\text{text}}$ 中的见解，对经验库 $E$ 中现有的经验进行精炼或改进。
- **保留 (Keep)**：经验库 $E$ 保持不变。




### 案例研究 (A Case Study)

在数学推理和网络搜索场景中，我们提供了示例，说明 Training-Free GRPO (免训练群体相对策略优化) 如何使用 DeepSeek-V3.1-Terminus 和相应的工具来增强 ReAct [1]。

#### A.1 经验引导的工具集成数学推理
 > Experience-Guided Tool-Integrated Math Reasoning

<img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1765117594966-b3fce48c-accb-43ef-a086-a79f16daf7a9.png?x-oss-process=image%2Fformat%2Cwebp" width="85%"/>

我们考虑一个包含两个矩形 ABCD 和 EFGH 的几何配置，其中 D、E、C、F 依次共线，并且 A、D、H、G 共圆 (concyclic)。已知 $BC = 16$，$AB = 107$，$FG = 17$，$EF = 184$，任务是确定 $CE$ 的长度。

##### 📌工具集成数学推理（无经验）

---
**问题 (Question)**  
矩形 ABCD 和 EFGH 被绘制，使得 D、E、C、F 共线。此外，A、D、H、G 四点位于同一个圆上。如果 $BC = 16$，$AB = 107$，$FG = 17$，$EF = 184$，那么 $CE$ 的长度是多少？

**轨迹 (Trajectory)**  
1. **[Agent]** 我将点 D 放置在原点 $(0, 0)$，并使用一条水平线表示 D、E、C、F。对于矩形 ABCD，设置 $A = (0, 16)$，$B = (107, 16)$，$C = (107, 0)$，$D = (0, 0)$。  
2. **[Tool]** 相应地设置坐标。  
3. **[Agent]** 由于 EFGH 是一个矩形，$EF$ 水平且 $FG = 17$，设置 $F = (x_f, 0)$，$E = (x_f - 184, 0)$，并初步设置 $G = (x_f, +17)$，$H = (x_f - 184, +17)$。  
4. **[Agent]** 使用四点行列式条件 (4-point determinant condition)，强制执行 $A(0, 16)$、$D(0, 0)$、$G(x_f, 17)$、$H(x_f - 184, 17)$ 的共圆性 (concyclicity)，推导出关于 $x_f$ 的方程。  
5. **[Tool]** 解出所得的二次方程 $x_f$；得到 $x_f \approx 184.092$，因此 $x_e = x_f - 184 \approx 0.092$。  
6. **[Agent]** 计算 $CE = \|107 - x_e \| \approx 106.9076$。  
6. **[Agent]** 计算 $CE = \|107 - x_e\| \approx 106.9076$。  
7. **[Agent]** 交换点顺序 (D–C–E–F, E–D–C–F) 并重新推导。在某一点，使用角度-正弦关系 (angle-sine relation)，得到 $x_e(x_e + 184) = 17$，从而得出 $x_e = -92 + \sqrt{8481} \approx 0.0923$，因此 $CE \approx 106.9076$。  
8. **[Agent]** 呈现一个“精确形式” $CE = 199 - \sqrt{8481}$ 作为最终答案。

**结果 (Outcome)**  
不正确：$CE \approx 106.9076$ (报告为 $199 - \sqrt{8481}$)。

---

🌟 未受辅助的智能体初始化一个坐标系，将 $D = (0, 0)$ 并将 $ABCD$ 建模为与坐标轴对齐。对于 $EFGH$，它设置 $E = (x_f - 184, 0)$，$F = (x_f, 0)$，并且关键地设置 $G = (x_f, +17)$，$H = (x_f - 184, +17)$，即短边具有正向垂直方向 (positive vertical orientation)。然后，它通过行列式条件 (determinant condition) 强制执行 $A(0, 16)$、$D(0, 0)$、$G$、$H$ 的四点共圆性 (four-point concyclicity) 并求解 $x_f$，得到 $x_f \approx 184.092$，因此 $x_e = x_f - 184 \approx 0.092$。由此，它报告 $CE \approx 106.9076$ 以及一个“精确”表达式 $199 - \sqrt{8481}$。

这条轨迹表现出三个系统性问题：  
1. **对垂直方向的误解**（$G$、$H$ 的 $y$ 坐标符号错误）。  
2. **对 $D–E–C–F$ 顺序的不一致处理**以及缺乏对线段关系的统一参数化。  
3. **缺乏系统、全面的解后验证**——即没有集成检查最终坐标是否同时满足矩形尺寸。


在没有经验辅助的轨迹中，智能体**接受了一个虚假的解**，因为它**缺乏完整的几何验证**。请注意，虽然 $CE \approx 106.91$ 满足 $0 < CE < 107$，但这本身并不能验证该解；关键的失败在于**缺乏对所有问题约束的整体一致性检查 (holistic consistency checks)**。



##### 📌工具集成数学推理（有经验）

---
**问题 (Question)**  
矩形 ABCD 和 EFGH 被绘制，使得 D、E、C、F 依次共线。此外，A、D、H、G 四点位于同一个圆上。如果 $BC = 16$，$AB = 107$，$FG = 17$，$EF = 184$，那么 $CE$ 的长度是多少？

**经验 (Experiences)**  
- **[G1]** 在解决涉及交点的几何问题时，验证解是否位于**有界区域 (bounded regions)** 或**线段 (segments)** 内，而非**延长线 (extensions)** 上，以避免**无关解 (extraneous answers)**。  
- **[G7]** 在解决带有约束（例如，梯形）的几何问题时，验证所有条件：通过斜率验证平行边，通过叉积验证凸性，以避免无关解。  
- **[G29]** 在线段延长线上构造点时，仔细解释诸如“超出 B”之类的**方向性短语 (directional phrases)**。  
- **[G37]** 在几何问题中，如果点位于三角形的边上并给定了线段长度，首先通过求和适当的线段来确定所有三条边长。例如，如果给定 $AB, AC, BC$ 上的点，以及 $AM, MB, AN, NC, BP, PC$，则 $AB = AM + MB, AC = AN + NC, BC = BP + PC$。这确保了在放置坐标或计算面积之前，三角形是被一致定义的。

**轨迹 (Trajectory)**  
1. **[Agent]** 在一条水平线上固定顺序 $D–E–C–F$。设置 $CE = x$，并设置线段约束 $0 < x < 107$。（依据 [G29], [G1]）  
2. **[Tool]** 记录关系：$DE = 107 - x$ 和 $CF = 184 - x$（依据 [G37]）。放置 $D = (0, 0)$, $E = (107 - x, 0)$, $C = (107, 0)$, $F = (291 - x, 0)$，确保 $EF = 184$。  
3. **[Agent]** 保持垂直方向一致：由于 $A = (0, 16)$ 且 $D = (0, 0)$，设置短边 $FG = 17$ **向下**，即 $H = (107 - x, -17)$ 和 $G = (291 - x, -17)$。（这纠正了无经验路径中的符号错误）  
4. **[Agent]** 使用**圆方程** $x^2 + y^2 + Dx + Ey + F = 0$ 强制执行**共圆性 (concyclicity)**。利用 $A(0, 16)$ 和 $D(0, 0)$，得到 $F = 0$, $E = -16$。  
5. **[Tool]** 代入 $H(107- x, -17)$ 和 $G(291- x, -17)$，得到两个方程。相减以消除常数并得到 $D = 2x - 398$。  
6. **[Agent]** 代入，得到二次方程 $x^2 - 398x + 30576 = 0$。  
7. **[Tool]** 计算判别式：$398^2 - 4 \cdot 30576 = 36100 = 190^2$。根为 $x = 294$ 和 $x = 104$。  
8. **[Agent]** 应用线段约束 $0 < x < 107$ 来**舍弃** $x = 294$ 并**选择** $x = 104$（依据 [G1]）。  
9. **[Agent]** （依据 [G7] 进行**完整验证**）$DE = 107 - 104 = 3$, $CF = 184 - 104 = 80$, $EF = 184$, $FG = 17$。圆 $x^2 + y^2 - 190x - 16y = 0$ 通过 $A = (0, 16)$, $D = (0, 0)$, $H = (3, -17)$, $G = (187, -17)$。**所有约束均满足**。

**结果 (Outcome)**  
**正确 (Correct)**：$CE = 104$。

---

🌟 借助精心策划的经验池 (curated experience pool)，智能体遵循一个结构化的流程：

* **方向性排序和有界性验证 ([29], [1])：** 它在线上固定了顺序 $D–E–C–F$，并设置 $CE = x$ 且 $0 < x < 107$，确保 $E$ 位于线段 $DC$ 上且 $F$ 位于 $C$ 之外。
* **线段相加参数化 ([37])：** 它使用 $DE + EC = DC = AB = 107$ 和 $EC + CF = EF = 184$ 来获得 $DE = 107 - x$，$CF = 184 - x$，并放置 $D = (0, 0)$, $E = (107 - x, 0)$, $C = (107, 0)$, $F = (291 - x, 0)$。
* **一致的垂直方向和循环建模：** 注意到 $A = (0, 16)$, $D = (0, 0)$，它将短边向下定向（$FG = 17$），从而 $H = (107 - x, -17)$, $G = (291 - x, -17)$。使用圆方程 $x^2 + y^2 + Dx + Ey + F = 0$ 并代入 $A$ 和 $D$ 得到 $F = 0, E = -16$。代入 $H$ 和 $G$，两方程相减得到 $D = 2x - 398$；回代后简化为二次方程 $x^2 - 398x + 30576 = 0$，其判别式为 $398^2 - 4 \cdot 30576 = 36100 = 190^2$，根为 $x = 104, 294$。
* **根选择和完整验证 ([1], [7])：** 应用 $0 < x < 107$ 过滤掉 $x = 294$，选择 $x = 104$。智能体随后验证所有约束：$DE = 107 - 104 = 3$, $CF = 184 - 104 = 80$, $EF = 184$, $FG = 17$，并确认圆 $x^2 + y^2 - 190x - 16y = 0$ 通过 $A = (0, 16)$, $D = (0, 0)$, $H = (3, -17)$, $G = (187, -17)$。


#### 对比分析
这个案例揭示了经验引导的行为与正确性之间清晰的因果关系。

* 经验 [G29] 消除了方向性模糊，并强制执行了正确的共线性顺序，直接解决了基线中 $G, H$ 的错误放置。
* 经验 [G37] 引导了简洁的单变量参数化 ($DE = 107 - x, CF = 184 - x$)，将循环约束简化为一个可解的二次方程。
* 经验 [G1] 施加了必要的有界性过滤器 ($0 < x < 107$)，以丢弃无关根。
* 最后，经验 [G7] 强制要求全面解后验证（矩形尺寸、共线性、共圆性），防止接受虚假解。

与未受辅助的轨迹相比，经验知情的推理纠正了垂直方向，解决了排序和参数化不一致，并安装了有原则的验证关卡。此案例证明了在工具集成数学推理中，集成领域特定经验对可靠性和准确性的积极影响。

### 4 代码 Prompt

#### 1. PROBLEM_WITH_EXPERIENCE_TEMPLATE

问题解决与经验加载：解决问题前的标准格式。核心要求是必须先阅读和理解提供的帮助性指令和经验 (`{experiences}`)，然后解决问题 (`{problem}`)。

```python
PROBLEM_WITH_EXPERIENCE_TEMPLATE = """请解决以下问题：
{problem}
在解决问题时，您必须首先仔细阅读并理解以下有用的指令和经验：
{experiences}"""
```

#### 2. SINGLE_ROLLOUT_SUMMARY_TEMPLATE

单次轨迹总结：详细回顾一次解决问题的轨迹（已知答案和评分）。

- **步骤 1**：描述采取的行动以及每一步使用的经验。
- **步骤 2**：根据评分和正确答案，识别并解释弯路、错误或回溯，分析其发生原因和影响。
- **步骤 3**：保持每一步所有核心结果的完整性，即使过程有缺陷。

```python
SINGLE_ROLLOUT_SUMMARY_TEMPLATE = """一个智能体系统可能会被提供一些经验，然后它会产生以下轨迹来解决给定的问题。请逐步总结该轨迹：
1. 对于每一步，描述**采取了什么行动**，以及在哪一步中使用了哪条经验。
2. 根据该次运行的评分和正确答案，识别并解释任何**代表弯路、错误或回溯**的步骤，强调它们可能发生的原因以及它们对轨迹进度的影响。
3. 保持**每一步的所有核心结果**，即使该过程存在缺陷。
<trajectory>
{trajectory}
</trajectory>

<evaluation>
{grade}
</evaluation>

<groundtruth>
{answer}
</groundtruth>
只返回每一步的轨迹摘要，例如：
1. 第一步发生了什么及其核心结果
2. 第二步发生了什么及其核心结果
3. ..."""
```

#### 3. SINGLE_QUERY_CRITIQUE_TEMPLATE

经验批评与更新（学习阶段）：审查多次尝试的轨迹，提取可推广经验，并更新经验库（已知答案）。

- **更新选项**：`modify` (修改), `add` (添加)。
- **输出格式**：详细推理后，返回 JSON 列表。

```python
SINGLE_QUERY_CRITIQUE_TEMPLATE = """一个智能体系统被提供了一组经验，并多次尝试解决该问题，其中既有成功的解决方案，也有错误的解决方案。请审查这些解决问题的尝试，并提取可推广的经验。遵循以下步骤：

1. 轨迹分析：
    - 对于成功的步骤：识别关键的正确决策和见解。
    - 对于错误：确定推理在哪里以及为什么出错。
    - 注意任何使用/遗漏的重要模式或策略。
    - 审查为什么有些轨迹会失败？是否有现有的经验被遗漏，或者经验没有提供足够的指导？
2. 更新现有经验：
    - 有些轨迹可能是正确的，有些可能是错误的，您应该确保有经验可以帮助正确运行。
    - 您有两种选择：[修改 (modify), 添加 (add)]：
        * 修改：您可以修改当前的经验使其更有帮助。
        * 添加：您可以引入可能需要的新经验。
    - 对于此案例，您最多可以更新 {max_operations} 条清晰、可推广的经验教训。
    - 在更新每条经验之前，您需要：
        * 指定它最相关的时机。
        * 列出使该经验适用的关键问题特征。
        * 识别该建议适用于的类似问题模式。
3. 对每条被修改或添加的经验的要求：
    - 以经验中包含的几个词的一般背景开头。
    - 专注于战略性思维模式，而非具体的计算。
    - 强调可应用于类似问题的决策点。
请在上述 3 个步骤的指导下提供详细的推理。
在分步推理之后，您将以如下 JSON 格式返回：
{ json
[
    {
        "option": "modify",
        "experience": "the modified experience",
        "modified_from": "G17" # 指定被修改经验的 ID
    },
    {
        "option": "add",
        "experience": "the added experience"
    },
    ...
] }
请注意，您更新的经验可能不需要涵盖所有两种选项。只使用一种更新类型也是可以的。
<problem>
{problem}
</problem>

<trajectories>
{trajectories}
</trajectories>

<groundtruth>
{answer}
</groundtruth>

<experience>
{experiences}
</experience>"""
```

#### 4. BATCH_EXPERIENCE_UPDATE_TEMPLATE

目的：收集并整合多轮建议，形成最终的经验库修订计划。

- **更新选项**：`modify` (修改), `merge` (合并)。
- **经验要求**：最终经验必须不超过 32 个词，专注于战略性思维，避免重复。

```python
BATCH_EXPERIENCE_UPDATE_TEMPLATE = """一个智能体系统被提供了一组经验，并多次尝试解决该问题。根据反思，对现有经验提出了一些建议。您的任务是收集并思考最终的经验修订计划。每条最终经验必须满足以下要求：
1. 它必须是针对此案例的清晰、可推广的经验教训，不超过 32 个词。
2. 以经验中包含的几个词的一般背景开头。
3. 专注于战略性思维模式，而非具体的计算。
4. 强调可应用于类似问题的决策点。
5. 避免在多个不同的经验中重复类似的说法。
<existing_experiences>
{experiences}
</existing_experiences>

<suggested_updates>
{updates}
</suggested_updates>
请对每条建议提供推理，并思考如何更新现有经验。
您有两种更新选项：[修改 (modify), 合并 (merge)]：
  * 修改：您可以修改当前的经验使其更有帮助。
  * 合并：您可以将一些相似的经验合并成更通用的形式以减少重复。
在生成分步推理之后，您需要以如下 JSON 格式返回最终的经验修订细节：
{json
[
    {
        "option": "modify",
        "experience": "the modified experience",
        "modified_from": "C1" # 指定被修改经验的字符串 ID
    },
    {
        "option": "merge",
        "experience": "the merged experience",
        "merged_from": ["C1", "C3", "S4", ...] # 指定被合并经验的字符串 ID 列表，至少需要 2 个 ID
    },
    ...
]}
```

#### 5. SINGLE_ROLLOUT_SUMMARY_NO_GT_TEMPLATE

无标准答案的单次运行总结。

```python
SINGLE_ROLLOUT_SUMMARY_NO_GT_TEMPLATE = """一个智能体系统可能会被提供一些经验，然后它会产生以下轨迹来解决给定的问题。请逐步总结该轨迹：
1. 对于每一步，描述**采取了什么行动**，以及在哪一步中使用了哪条经验。
2. 根据该次运行的评分和正确答案，识别并解释任何**代表弯路、错误或回溯**的步骤，强调它们可能发生的原因以及它们对轨迹进度的影响。
3. 保持**每一步的所有核心结果**，即使该过程存在缺陷。
<trajectory>
{trajectory}
</trajectory>
只返回每一步的轨迹摘要，例如：
1. 第一步发生了什么及其核心结果
2. 第二步发生了什么及其核心结果
3. ..."""
```

#### 6. SINGLE_QUERY_CRITIQUE_NO_GT_TEMPLATE

```python
SINGLE_QUERY_CRITIQUE_NO_GT_TEMPLATE = """一个智能体系统被提供了一组经验，并多次尝试解决该问题。请审查这些解决问题的尝试，并提取可推广的经验。遵循以下步骤：
1. 轨迹分析：
    - 识别关键的正确决策和见解。
    - 确定推理在哪里以及为什么出错。
    - 注意任何重要模式或策略的使用/遗漏。
    - 审查为什么有些轨迹看似失败？是否有现有的经验被遗漏，或者经验没有提供足够的指导？
2. 更新现有经验：
    - 确保有经验可以帮助正确运行。
    - 您有两种选择：[修改 (modify), 添加 (add)]：
        * 修改：您可以修改当前的经验使其更有帮助。
        * 添加：您可以引入可能需要的新经验。
    - 对于此案例，您最多可以更新 {max_operations} 条清晰、可推广的经验教训。
    - 在更新每条经验之前，您需要：
        * 指定它最相关的时机。
        * 列出使该经验适用的关键问题特征。
        * 识别该建议适用于的类似问题模式。
3. 对每条被修改或添加的经验的要求：
    - 以经验中包含的几个词的一般背景开头。
    - 专注于战略性思维模式，而非具体的计算。
    - 强调可应用于类似问题的决策点。
请在上述 3 个步骤的指导下提供详细的推理。
在分步推理之后，您将以如下 JSON 格式返回：
{json
[
    {
        "option": "modify",
        "experience": "the modified experience",
        "modified_from": "G17" # 指定被修改经验的 ID
    },
    {
        "option": "add",
        "experience": "the added experience"
    },
    ...
]
}
请注意，您更新的经验可能不需要涵盖所有两种选项。只使用一种更新类型也是可以的。
<problem>
{problem}
</problem>

<trajectories>
{trajectories}
</trajectories>

<experience>
{experiences}
</experience>"""
```
---

