---
title: "DynNet — Dou et al. 2026 (Nature Communications)"
tags: [paper, dynnet, single-cell, stochastic-dynamics, GRN, cell-fate]
created: 2026-05-22
updated: 2026-05-22
sources:
  - type: paper
    title: "Inferring stochastic dynamics by biophysical Neural ODE using single-cell transcriptomics"
    authors: "Dou J, Lyu W, Chen F, Nie Q, Li C"
    journal: "Nature Communications, 2026 (Article in Press)"
    doi: "10.1038/s41467-026-73257-z"
    url: "https://doi.org/10.1038/s41467-026-73257-z"
  - type: article
    title: "DynNet：把单细胞静态快照变成细胞命运的动力学模型"
    platform: "微信公众号 — 计算生物前沿"
    url: "https://mp.weixin.qq.com/s/Um73DQFGq2KsVC0Mgek6jQ"
---

# DynNet: 随机动力学推断网络 — Dou et al. 2026

> **中英文精读**: 微信公众号科普文章 + 原文关键段落对照
>
> 本文基于 "计算生物前沿" 微信公众号文章（中文）翻译为英文，并辅以 Nature Communications 原文摘要和关键段落。

---

## 快速导航

| 章节 | 内容 | 源块 |
|------|------|------|
| 1. 引言 | 问题背景：静态快照与连续动态的 gap | S001 |
| 2. 已有方法局限 | 拟时序、Markov、RNA velocity 的不足 | S002-S003 |
| 3. DynNet 核心框架 | SDE 框架、Hill 函数、先验约束 | S004-S006 |
| 4. MISA 模拟验证 | 三稳定态恢复、决策边界、速度场 | S007-S009 |
| 5. 7基因发育分支 | 级联激活、相互抑制开关、约束对比 | S010-S012 |
| 6. 肝细胞分化 | MH/LB 吸引子、转变路径、敲除模拟 | S013-S016 |
| 7. EMT/MET | 能量景观、转变路径、关键基因鉴定 | S017-S022 |
| 8. 论文意义 | 统一框架的价值 | S023 |

---

<a id="S001"></a>
## 1. 引言

**Source:** 公众号文章 ¶1

**Original:**

单细胞 RNA 测序给了我们一张张前所未有清晰的细胞"照片"。我们可以看到一个组织里有多少种细胞状态，可以看到肿瘤细胞从上皮样状态走向间质样状态，也可以看到干细胞分化过程中出现不同分支。**但生命真正发生的地方，不在静态照片里，而在连续变化的动态过程里。**

问题在于，单细胞测序通常会破坏细胞。也就是说，我们能在不同时间点采样很多细胞，却很难真正追踪同一个细胞从初始状态一步步走向终末命运的完整分子轨迹。于是，单细胞领域一直有一个核心难题：**能不能只根据多个时间点的单细胞快照，反推出细胞命运变化背后的动力学规律？**

Nature Communications 这篇论文提出的 **DynNet**，正是为了解决这个问题。它的全称是随机动力学推断网络。简单说，DynNet 想做的不是再画一条更漂亮的拟时序轨迹，而是要从多时间点单细胞 RNA 测序数据中，重建细胞状态演化的 **随机动力学模型、稳定状态、命运吸引子、转变路径、转变概率和关键调控基因**。

**English:**

Single-cell RNA sequencing has given us unprecedented clarity in capturing cellular "snapshots." We can see how many cell states exist in a tissue, observe tumor cells transitioning from epithelial to mesenchymal states, and watch stem cells diverge along different differentiation branches. **But life doesn't happen in static photographs — it happens in continuous dynamic processes.**

The challenge is that single-cell sequencing typically destroys cells. This means we can sample many cells at different time points, but we cannot track the complete molecular trajectory of a single cell from its initial state to its terminal fate. This has led to a central question in the field: **Can we infer the dynamical principles underlying cell fate changes using only static single-cell snapshots from multiple time points?**

**DynNet**, proposed in this Nature Communications paper, is designed to address exactly this question. Its full name is the Stochastic Dynamics Inference Network. Simply put, DynNet's goal is not to draw a prettier pseudotime trajectory, but to reconstruct from multi-timepoint scRNA-seq data the **stochastic dynamical model, stable states, fate attractors, transition paths, transition probabilities, and key regulatory genes** of cell state evolution.

---

<a id="S002"></a>
## 2. 已有方法的局限性

**Source:** 公众号文章 ¶2

**Original:**

过去几年，单细胞 RNA 测序极大推动了发育生物学、肿瘤生物学和系统生物学。拟时序方法可以帮助我们把细胞排成一个大致的发育顺序，马尔可夫模型可以估计细胞状态之间的转移趋势，RNA velocity 可以利用剪接信息推断短期变化方向。这些方法很有价值，但它们往往更擅长回答"细胞大概从哪里到哪里"，却不一定能回答"**细胞为什么这样转变**"。

**轨迹不是机制。** 如果我们只知道细胞从 A 状态走向 B 状态，却不知道哪些基因在推动这个过程、哪个状态更稳定、哪条路径更容易发生、敲掉哪个基因会改变命运方向，那么我们对细胞命运的理解仍然是不完整的。

**English:**

Over the past few years, single-cell RNA sequencing has greatly advanced developmental biology, tumor biology, and systems biology. Pseudotime methods help us arrange cells along approximate developmental order. Markov models estimate transition tendencies between cell states. RNA velocity uses splicing information to infer short-term directional changes. These methods are valuable, but they tend to answer **where cells go** rather than **why cells change that way**.

**Trajectory is not mechanism.** If we only know that cells transition from state A to state B, but don't know which genes drive this process, which state is more stable, which path is more probable, or which gene knockout would change the fate direction, then our understanding of cell fate remains incomplete.

---

<a id="S003"></a>
**Source:** 公众号文章 ¶3

**Original:**

此外，普通的神经常微分方程模型虽然可以学习连续动力学，但它本质上是确定性的：在同一个状态附近，系统通常只有一个明确的未来方向。可是生物系统并非如此。细胞命运决定常常伴随随机性和多稳定态：同一群细胞可能分化成不同终末状态，肿瘤细胞可能停在上皮态、间质态或中间态，发育系统也可能存在多个稳定吸引子。**细胞命运不是一条单线轨迹，而更像一片有山谷、有鞍点、有岔路、有噪声扰动的能量景观。**

**English:**

Furthermore, although standard neural ODE models can learn continuous dynamics, they are inherently deterministic: near a given state, the system typically has only one clear future direction. But biological systems are not like this. Cell fate decisions are accompanied by stochasticity and multi-stability: the same population of cells can differentiate into different terminal states, tumor cells can settle in epithelial, mesenchymal, or intermediate states, and developmental systems can have multiple stable attractors. **Cell fate is not a single linear trajectory — it is more like an energy landscape with valleys, saddle points, branch points, and noise-induced fluctuations.**

---

<a id="S004"></a>
## 3. DynNet 核心框架

**Source:** 公众号文章 ¶4 | Figure: Fig 1

![DynNet 框架概览](assets/fig1_overview.png)

**Fig 1. DynNet framework overview.** The figure shows (A) data preprocessing from multi-timepoint scRNA-seq, (B) prior GRN construction, (C) SDE-based neural network architecture with Hill function gene regulation and noise estimator, (D) weight-matching loss for multi-stable distribution, (E) alternating optimization strategy, (F) energy landscape reconstruction, and (G) downstream cell fate analysis capabilities. A comparison table shows DynNet vs other methods (CellRank, scTour, DeepVelo, SDEvelo) across multiple features.

---

<a id="S005"></a>
**Source:** 公众号文章 ¶5

**Original:**

论文图1展示了 DynNet 的整体框架。它的输入是多个已知时间点的单细胞 RNA 测序数据，每个细胞被表示为一个基因表达向量，每个时间点则是一组细胞状态分布。DynNet 不把这些细胞简单排成一条线，而是假设细胞状态演化可以由随机微分方程描述。

在这个方程里，**漂移项代表基因调控驱动**，也就是细胞状态被基因网络"推向哪里"；**扩散项代表随机噪声**，包括基因表达内在波动和外部环境扰动。这个设计非常关键，因为它让 DynNet 能够描述多稳定态和随机命运转变，而不是只能给出一个确定方向。

更重要的是，DynNet 不是单纯黑箱深度学习。它把基因调控网络直接嵌入模型结构中，并用 **希尔函数** 显式表示基因之间的激活、抑制和降解作用。因此，模型参数不只是神经网络里的抽象权重，而可以对应到更有生物意义的调控强度、抑制强度、表达阈值和降解率。

**English:**

Figure 1 shows DynNet's overall framework. Its input is scRNA-seq data from multiple known time points, where each cell is represented as a gene expression vector, and each time point represents a distribution of cell states. DynNet does not simply arrange cells along a line; instead, it assumes cell state evolution can be described by stochastic differential equations (SDEs).

In these equations, the **drift term represents gene regulatory drive** — where the gene network "pushes" cell states; the **diffusion term represents stochastic noise** — including both intrinsic gene expression fluctuations and external environmental perturbations. This design is critical because it allows DynNet to describe multi-stable dynamics and stochastic fate transitions, rather than outputting only a single deterministic direction.

Importantly, DynNet is not a pure black-box deep learning model. It embeds the gene regulatory network directly into the model architecture, using **Hill functions** to explicitly represent activation, inhibition, and degradation between genes. Thus, the model parameters are not just abstract neural network weights — they correspond to biologically meaningful quantities: regulatory strength, inhibition strength, expression thresholds, and degradation rates.

---

<a id="S006"></a>
**Source:** 公众号文章 ¶6

**Original:**

DynNet 还支持两类先验网络约束。**硬约束** 会严格屏蔽先验网络中不存在的调控边，更适合先验知识可靠的情况；**软约束** 不会完全禁止新边，而是惩罚不符合先验的关系，因此允许模型在数据支持下发现潜在调控作用。最后，DynNet 通过噪声估计器学习状态依赖的扩散项，并进一步重建能量景观。在这个景观中，**局部低谷对应稳定细胞状态，鞍点对应命运转变关口，路径和能垒则反映不同命运转换的难易程度。**

**English:**

DynNet also supports two types of prior network constraints. **Hard constraints** strictly mask regulatory edges not present in the prior network, suitable when prior knowledge is reliable. **Soft constraints** do not completely prohibit new edges but penalize relationships inconsistent with the prior, thus allowing the model to discover potential regulatory interactions supported by the data. Finally, DynNet uses a noise estimator to learn state-dependent diffusion, and subsequently reconstructs the energy landscape. In this landscape, **local valleys correspond to stable cell states, saddle points correspond to fate transition gateways, and paths and energy barriers reflect the difficulty of different fate transitions.**

---

<a id="S007"></a>
## 4. MISA 模型模拟验证

**Source:** 公众号文章 ¶7 | 原文 Results §"DynNet accurately recovers multi-stable dynamics"

**Original:**

为了验证 DynNet 是否真的能学到动力学，而不是只是在真实数据上"讲故事"，作者首先使用经典的 MISA 模型进行模拟验证。MISA 是一个互相抑制、自我激活的双基因调控模块，也是研究多稳定态的经典模型。论文中模拟了 **5个时间点、每个时间点2000个样本**，系统最终形成3个稳定状态：一个是 X1 高表达状态，一个是 X2 高表达状态，还有一个是二者中等表达的平衡状态。

DynNet 需要完成的任务，是只根据这些时间点快照，恢复稳定状态位置、表达分布、决策边界、速度场和能量景观。结果显示，DynNet 能准确识别3个稳定状态，并且估计出的稳定状态中心、协方差区域和边缘分布都与模拟真值高度一致。

**English:**

To verify whether DynNet can truly learn dynamics rather than just "tell stories" on real data, the authors first used the classic MISA model for simulation-based validation. MISA is a mutual inhibition and self-activation two-gene regulatory motif, a classic model for studying multi-stability. The paper simulated **5 time points with 2000 samples each**, resulting in three stable states: an X1-high state, an X2-high state, and a balanced intermediate state.

DynNet's task was to reconstruct stable state locations, expression distributions, decision boundaries, velocity fields, and energy landscapes from only these time-point snapshots. Results showed that DynNet accurately identified all three stable states, with estimated stable state centers, covariance regions, and marginal distributions closely matching the ground truth.

---

<a id="S008"></a>
**Source:** 原文 Results | Figure: Fig 2

![MISA 验证结果](assets/fig2a_misa_model.png)
![MISA 稳定态与决策边界](assets/fig2c_decision_boundaries.png)

**Fig 2. MISA model validation.** (Left) MISA model schematic — two genes with mutual inhibition and self-activation, forming three stable states. (Right) Decision boundary comparison between ground truth data (left) and DynNet prediction (right). DynNet accurately recovers the three basins of attraction and the separating boundaries.

---

<a id="S009"></a>
**Source:** 公众号文章 ¶8

**Original:**

更关键的是，DynNet 能恢复 **决策边界**。所谓决策边界，就是在状态空间中划出不同区域：落在这个区域的细胞未来更可能走向状态1，落在另一个区域的细胞未来更可能走向状态2。对于细胞命运研究来说，这比"现在在哪里"更重要，因为我们真正关心的是：**一个命运尚未确定的细胞，未来更可能进入哪个吸引子？**

作者还将 DynNet 与普通神经常微分方程模型比较。结果显示，DynNet 在速度场和决策边界恢复上更接近真实动力学，尤其在时间点较少时表现更稳健。这说明，**对于多稳定态和随机命运转变问题，仅靠确定性动力学并不够，随机动力学框架更贴近真实生物过程。**

**English:**

More critically, DynNet can recover **decision boundaries**. Decision boundaries divide state space into different regions: cells falling in one region are more likely to transition to state 1, while cells in another region are more likely to go to state 2. For cell fate research, this is more important than "where am I now," because what we really care about is: **for a cell whose fate is not yet determined, which attractor is it most likely to enter?**

The authors also compared DynNet with standard neural ODE methods. Results showed that DynNet's velocity field and decision boundary recovery were closer to the true dynamics, and it was particularly more robust with fewer time points. This demonstrates that **for multi-stable and stochastic fate transition problems, deterministic dynamics alone are insufficient — the stochastic dynamical framework better captures real biological processes.**

---

<a id="S010"></a>
## 5. 7基因发育分支模拟

**Source:** 公众号文章 ¶9 | 原文 Results §"developmental branching process"

**Original:**

在图3中，作者进一步构建了一个7基因发育分支模拟系统。这个系统中，G1、G2、G3 逐步激活下游调控模块，G4 和 G5 形成互相抑制的开关结构，G6 和 G7 作为下游命运标志基因。整个系统从一个类似干细胞的初始状态出发，最终分化为两个不同终末状态。

DynNet 在这里要解决的问题更加接近真实发育过程：它不仅要恢复从初始状态到两个终末状态的分支轨迹，还要解释分支背后的基因调控逻辑。结果显示，DynNet 能够重建稳定状态分布和速度场，并捕捉 G1、G2、G3 的级联激活动态，以及 G4/G5 互相抑制导致 G6/G7 分叉表达的过程。

这部分结果非常重要，因为它说明 DynNet 的价值不只是"把细胞分成两条路"。它进一步说明：**哪些基因像开关一样控制命运选择，哪些调控边塑造了分支结构，哪些基因表达变化标志着命运真正开始分化。**

**English:**

In Figure 3, the authors further constructed a 7-gene developmental branching simulation system. In this system, G1, G2, and G3 progressively activate downstream regulatory modules; G4 and G5 form a mutually inhibitory toggle switch; and G6 and G7 serve as downstream fate marker genes. The entire system starts from a stem-cell-like initial state and bifurcates into two distinct terminal states.

The problem DynNet addresses here is closer to real developmental processes: it not only recovers the branching trajectory from the initial state to two terminal states but also explains the gene regulatory logic behind the branching. Results showed that DynNet reconstructed stable state distributions and velocity fields, capturing the cascade activation dynamics of G1→G2→G3 and the bifurcation of G6/G7 expression driven by G4/G5 mutual inhibition.

These results are important because they show DynNet's value goes beyond "splitting cells into two paths." It further reveals: **which genes act as switches controlling fate decisions, which regulatory edges shape the branching structure, and which gene expression changes mark the true onset of fate divergence.**

---

<a id="S011"></a>
**Source:** 原文 Results | Figure: Fig 3

![7基因分支](assets/fig3_branching.png)
![基因表达动态](assets/fig3_gene_dynamics.png)

**Fig 3. 7-gene developmental branching.** (Left) Gene regulatory network showing the cascade (G1→G2→G3), toggle switch (G4↔G5), and downstream markers (G6, G7). (Right) Temporal expression dynamics showing G1/G2/G3 transient activation, G4/G5 bifurcation, and G6/G7 divergent expression marking the two terminal fates.

---

<a id="S012"></a>
**Source:** 公众号文章 ¶10

**Original:**

图3还比较了硬约束和软约束。硬约束更快收敛，因为它严格依赖先验网络；软约束搜索空间更大，收敛更慢，但可以发现潜在新关系。不过作者也提醒，软约束推断出的新边不一定都是真实直接调控，有些可能代表间接关系或功能依赖。因此，DynNet 更适合做 **核心基因集的机制性动力学解析**，而不是直接作为全基因组基因调控网络推断工具。

**English:**

Figure 3 also compares hard and soft constraints. Hard constraints converge faster because they strictly rely on the prior network. Soft constraints have a larger search space and converge more slowly, but can discover potential new relationships. However, the authors caution that new edges inferred by soft constraints are not necessarily true direct regulations — some may represent indirect relationships or functional dependencies. Therefore, DynNet is better suited for **mechanistic dynamical analysis of core gene sets** rather than as a genome-wide GRN inference tool.

---

<a id="S013"></a>
## 6. 肝细胞分化

**Source:** 公众号文章 ¶11 | 原文 Results §"hepatocyte differentiation"

**Original:**

完成模拟验证后，作者把 DynNet 用于真实发育体系：肝细胞分化。这个过程从诱导多能干细胞出发，先进入定型内胚层阶段，再进入肝内胚层阶段；随后细胞出现分叉，一条路径走向成熟肝细胞样状态，另一条路径走向肝芽状态。论文中分别简称为 MH 和 LB。

在图4中，作者选择了20个候选关键基因，并基于异步相关分析构建参考基因调控网络，再用 DynNet 进行动力学建模。模型重建出的能量景观中出现两个稳定吸引子，分别对应 MH 和 LB。速度场显示，细胞在肝内胚层区域附近出现明显分叉，这与实验中不同培养条件驱动不同命运的现象一致。

**English:**

After simulation validation, the authors applied DynNet to a real developmental system: hepatocyte differentiation. This process starts from induced pluripotent stem cells (iPSCs), transitioning first to the definitive endoderm (DE) stage, then to the hepatic endoderm (HE) stage. Subsequently, cells bifurcate: one path leads to the mature hepatocyte-like (MH) state, and the other to the liver bud (LB) state.

In Figure 4, the authors selected 20 candidate key genes, constructed a reference GRN based on asynchronous correlation analysis, and used DynNet for dynamical modeling. The reconstructed energy landscape revealed two stable attractors, corresponding to MH and LB. The velocity field showed clear bifurcation near the HE cluster, consistent with experimental observations that different culture conditions drive different fates.

---

<a id="S014"></a>
**Source:** 原文 Results | Figure: Fig 4

![肝细胞分化](assets/fig4_hepatocyte.png)

**Fig 4. Hepatocyte differentiation.** Energy landscape with two attractors (MH and LB), velocity field showing bifurcation at HE, transition action analysis showing intermediate states lower transition barriers, and in silico knockout results (TOB1 → LB acceleration, RANBP1 → MH promotion).

---

<a id="S015"></a>
**Source:** 公众号文章 ¶12

**Original:**

接着，作者计算了 **转变作用量** 和 **首次通过时间** 。可以把转变作用量理解为细胞从一个状态转到另一个状态需要跨越的动力学代价；代价越低，转变越容易发生。结果显示，中间状态可以降低转变代价，例如从定型内胚层经过肝内胚层再走向早期肝芽状态，比直接转向肝芽状态更容易。模型还显示，走向 MH 的代价和首次通过时间低于走向 LB，提示系统在模型中存在向 MH 分化的动力学偏向。

**English:**

Next, the authors calculated **transition actions** and **first passage times (FPT)**. Transition action can be understood as the dynamical cost a cell must overcome to transition from one state to another — the lower the cost, the easier the transition. Results showed that intermediate states reduce transition costs. For example, the DE→HE→early LB path required less action than a direct DE→LB transition. The model also showed that transitions to MH required less action and shorter FPT than those to LB, suggesting a dynamical bias toward MH differentiation in this system.

---

<a id="S016"></a>
**Source:** 公众号文章 ¶13

**Original:**

最后，作者进行了模型内的基因敲除模拟。敲除 MH 相关基因 TOB1，会加速细胞向 LB 状态转变；敲除 LB 标志基因 RANBP1，则促进细胞向 MH 状态分化；敲除干性相关基因 SRGAP2 不一定改变最终命运，但会影响分化速度。这里一定要强调：**这些敲除结果是计算模拟，不是直接实验验证。** 它们的意义在于提出可检验假设：哪些基因可能维持某种状态，哪些基因可能改变命运方向，哪些基因主要影响分化速度。

**English:**

Finally, the authors performed in silico knockout simulations. Knocking out the MH-associated gene TOB1 accelerated transition toward the LB state. Knocking out the LB marker gene RANBP1 promoted differentiation toward the MH state. Knocking out the stemness-related gene SRGAP2 did not necessarily change the final fate but affected differentiation speed. It is important to emphasize: **these knockout results are computational simulations, not direct experimental validation.** Their value lies in generating testable hypotheses: which genes may maintain a given state, which may change fate direction, and which primarily influence differentiation speed.

---

<a id="S017"></a>
## 7. EMT/MET：肿瘤细胞可塑性

**Source:** 公众号文章 ¶14 | 原文 Results §"EMT landscape switching"

**Original:**

发育分化之外，作者还将 DynNet 用于肿瘤细胞可塑性研究，具体是转化生长因子β诱导的肺癌 EMT/MET 时间序列数据。这个数据集包含 **36个基因、7个时间点、超过100000个细胞**。前10天加入转化生长因子β诱导上皮-间质转化，随后撤除该信号，使细胞进入间质-上皮转化过程。

图5首先从真实数据中估计能量景观，并识别出多个关键状态：上皮态、间质态、间质-上皮转化中间态，以及部分上皮-间质转化状态。第10天时，间质态处在较低能量区域，说明细胞在诱导后已经稳定在间质状态；撤除转化生长因子β后，间质态能量升高，上皮态能量降低，系统逐渐倾向回到上皮状态。

**English:**

Beyond development, the authors applied DynNet to study tumor cell plasticity, specifically using TGF-β-induced lung cancer EMT/MET time-course data. This dataset contains **36 genes, 7 time points, and over 100,000 cells**. TGF-β was applied for the first 10 days to induce EMT, then withdrawn for the next 10 days to promote MET.

Figure 5 first estimated the energy landscape from real data, identifying multiple key states: epithelial (E), mesenchymal (M), MET intermediate (IM), and partial EMT (pEMT). At Day 10, the M state occupied low-energy regions, indicating cells had stabilized in the mesenchymal state after induction. After TGF-β withdrawal, the M state's energy increased and the E state's energy decreased, with the system gradually trending back toward the epithelial state.

---

<a id="S018"></a>
**Source:** 原文 Results | Figure: Fig 5

![EMT 能量景观](assets/fig5_emt_landscape.png)

**Fig 5. EMT landscape.** (Top) Data-driven energy landscape at Day 10 (after TGF-β induction) and Day 20 (after MET). (Bottom) Model-based energy landscape from DynNet, velocity field, and estimated weighted GRN showing mutual activation within states and inhibition between states.

---

<a id="S019"></a>
**Source:** 公众号文章 ¶15

**Original:**

如果图5回答的是"状态在哪里"，那么图6回答的是"状态之间怎么转、哪条路更容易、哪些基因在推动转变"。作者使用最小作用路径方法计算状态转变路线和转变作用量。结果显示，在撤除转化生长因子β后的第10到20天，间质态到上皮态的转变作用量低于反向转变，说明系统更倾向于发生间质-上皮转化。

但这个转变不是从间质态直接跳回上皮态。模型显示，**间质-上皮转化更可能经过中间态，而不是直接完成状态切换。** 这很符合肿瘤细胞可塑性的生物学直觉：细胞状态转变常常不是开关式瞬间变化，而是经过多个过渡状态和能量屏障。

**English:**

If Figure 5 answers "where are the states," Figure 6 answers "how do states transition, which path is easier, and which genes drive the transition." The authors used the minimum action path method to compute state transition routes and transition actions. Results showed that from Day 10 to 20 (after TGF-β withdrawal), the M→E transition action was lower than the reverse E→M transition, indicating the system favors MET.

But this transition does not happen directly from M to E. The model shows that **MET is more likely to pass through intermediate states (IM/pEMT) rather than switching directly.** This aligns well with biological intuition about tumor cell plasticity: cell state transitions are often not binary switch-like events but pass through multiple transitional states and energy barriers.

---

<a id="S020"></a>
**Source:** 公众号文章 ¶16 | 原文 Results §"Identify transition paths and critical genes"

**Original:**

作者进一步做了参数敏感性分析。结果显示，如果增强 CD44 和 VIM 等间质标志基因之间的激活作用，间质态到上皮态的转变代价会升高，说明间质状态更稳定；相反，如果增强 MUC1 和 CDH1 等上皮标志基因之间的激活作用，则会提高上皮态向间质态转变的代价，并降低间质态回到上皮态的代价，说明系统更倾向于维持或回到上皮状态。

**English:**

The authors further performed parameter sensitivity analysis. Results showed that enhancing activation between mesenchymal marker genes such as CD44 and VIM increased the M→E transition action, indicating the M state becomes more stable. Conversely, enhancing activation between epithelial marker genes such as MUC1 and CDH1 raised the E→M transition action and lowered the M→E action, suggesting the system favors maintaining or returning to the epithelial state.

---

<a id="S021"></a>
**Source:** 公众号文章 ¶17

**Original:**

在模型内敲除模拟中，敲除 CD44 会使间质态细胞回到上皮状态，提示 CD44 对维持间质态非常关键；降低 CDH1 表达则促进上皮态向间质态转变，这与 E-cadherin 丢失是上皮-间质转化关键事件的经典认识一致。模型还显示，MUC1 主要参与间质态到中间态的转变，而 VIM 在细胞接近上皮态之前发生明显变化。

**English:**

In in silico knockout simulations, knocking out CD44 caused M-state cells to revert to the E state, indicating CD44 is critical for maintaining the M state. Reducing CDH1 expression promoted E→M transition, consistent with the classic understanding that E-cadherin loss is a key event in EMT. The model also showed that MUC1 is primarily involved in the M→IM transition, while VIM changes significantly just before cells reach the E state.

---

<a id="S022"></a>
**Source:** 公众号文章 ¶18 | Figure: Fig 6

![EMT 转变路径](assets/fig6_transition_paths.png)

**Fig 6. EMT transition paths and gene regulation.** Minimum action path analysis showing M→E transition via intermediate states (IM, pEMT). Sensitivity analysis: CD44/VIM activation stabilizes M state; MUC1/CDH1 activation favors E state. Knockout simulations: CD44 knockout reverses M→E; CDH1 knockdown promotes E→M. TGF-β as exogenous regulatory node.

**Original:**

最后，作者把转化生长因子β作为外源调控节点加入模型，并通过微调降解相关参数来模拟上皮-间质转化过程。结果表明，即使模型主要基于间质-上皮转化阶段训练，加入外源信号后仍能较好模拟上皮-间质转化的稳定状态分布。这说明 DynNet 捕捉到的不是某个单一时间段的表面变化，而是 EMT/MET 背后较核心的动力学结构。

**English:**

Finally, the authors incorporated TGF-β as an exogenous regulatory node in the model and simulated the EMT process by fine-tuning degradation-related parameters. Results showed that even though the model was primarily trained on MET data, it could still accurately simulate EMT stable state distributions after adding the exogenous signal. This demonstrates that DynNet captures not just superficial changes within a single time window, but the core dynamical structure underlying EMT/MET.

---

<a id="S023"></a>
## 8. 论文意义

**Source:** 公众号文章 ¶19

**Original:**

这篇论文的意义，不只是提出了一个新模型。它真正有价值的地方在于，把过去常常分散讨论的几个概念连在了一起：**单细胞静态快照、基因调控网络、随机动力学、稳定吸引子、能量景观、命运转变路径和关键基因扰动。**

过去很多单细胞分析更像是在回答"细胞怎么排队"。而 DynNet 想推进的问题是：**细胞为什么这样转变？哪个状态更稳定？哪条路径更可能发生？改变哪个基因，可能把细胞推向另一个命运？**

这也是它区别于普通拟时序方法和普通黑箱深度学习的地方。DynNet 不是只给出一个低维轨迹，也不是只在隐藏空间中学习抽象动力学，而是直接在原始基因表达空间中建模，把基因调控作用写进动力学方程，并进一步通过能量景观解释细胞状态稳定性和转变代价。

**English:**

The significance of this paper goes beyond proposing a new model. Its real value lies in connecting several concepts that have often been discussed in isolation: **single-cell static snapshots, gene regulatory networks, stochastic dynamics, stable attractors, energy landscapes, fate transition paths, and key gene perturbations.**

Many past single-cell analyses focused on answering "how cells line up." DynNet advances the question to: **Why do cells transition this way? Which state is more stable? Which path is more probable? Changing which gene could push cells toward a different fate?**

This is what distinguishes DynNet from standard pseudotime methods and black-box deep learning. DynNet does not merely output a low-dimensional trajectory or learn abstract dynamics in a latent space. Instead, it models directly in the original gene expression space, encodes gene regulation into the dynamical equations, and interprets cell state stability and transition costs through the energy landscape.

---

<a id="S024"></a>
## 论文信息

**Original:**

| Field | Detail |
|-------|--------|
| **Title** | Inferring stochastic dynamics by biophysical Neural ODE using single-cell transcriptomics |
| **Authors** | Jingyu Dou, Wentao Lyu, Feng Chen, Qing Nie, Chunhe Li |
| **Affiliations** | Fudan University (Shanghai) + UC Irvine |
| **Journal** | Nature Communications, 2026 (Article in Press) |
| **DOI** | [10.1038/s41467-026-73257-z](https://doi.org/10.1038/s41467-026-73257-z) |
| **Received** | 16 May 2025 |
| **Accepted** | 7 May 2026 |
| **Published** | 19 May 2026 |
| **Core method** | DynNet (Stochastic Dynamics Inference Network) |
| **License** | CC BY-NC-ND 4.0 |

---

## 术语对照

| English | 中文 | Notes |
|---------|------|-------|
| DynNet | 随机动力学推断网络 | Stochastic Dynamics Inference Network |
| stochastic differential equation (SDE) | 随机微分方程 | Core mathematical framework |
| drift term | 漂移项 | Deterministic gene regulatory component |
| diffusion term | 扩散项 | Stochastic noise component |
| Hill function | 希尔函数 | f(x) = x^n / (S^n + x^n) |
| hard constraint | 硬约束 | Mask non-prior edges |
| soft constraint | 软约束 | L2 penalty on non-prior edges |
| energy landscape | 能量景观 | U(x) = -ln P_ss(x) |
| transition action | 转变作用量 | Freidlin-Wentzell action |
| first passage time (FPT) | 首次通过时间 | Mean transition time |
| MISA | MISA 模型 | Mutual Inhibition Self-Activation |
| attractor | 吸引子 | Stable state |
| decision boundary | 决策边界 | Separatrix |
| MH (mature hepatocyte-like) | 成熟肝细胞样 | Terminal state |
| LB (liver bud) | 肝芽 | Alternative terminal state |
| EMT | 上皮-间质转化 | Epithelial-mesenchymal transition |
| MET | 间质-上皮转化 | Mesenchymal-epithelial transition |
| pEMT | 部分 EMT | Partial EMT state |
| IM | MET 中间态 | MET intermediate (metastable) |

---

## 关键图表示意

| Figure | Content |
|--------|---------|
| Fig 1 | DynNet 框架：数据处理 → SDE 建模 → 先验约束 → 交替优化 → 能量景观 → 下游分析 |
| Fig 2 | MISA 模拟验证：三稳定态恢复、决策边界、速度场、能量景观 |
| Fig 3 | 7基因发育分支：级联激活、G4/G5 开关、G6/G7 分叉、硬/软约束对比 |
| Fig 4 | 肝细胞分化：MH/LB 吸引子、转变路径、FPT、敲除模拟 |
| Fig 5 | EMT 能量景观：数据驱动 → 模型重建、速度场、GRN 推断 |
| Fig 6 | EMT 转变路径：最小作用路径、参数敏感性、CD44/CDH1 敲除、TGF-β 调控 |
