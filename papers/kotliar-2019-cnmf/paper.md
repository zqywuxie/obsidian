---
title: "Identifying gene expression programs of cell-type identity and cellular activity with single-cell RNA-Seq — 中英文精读"
authors: "Kotliar D, Veres A, Nagy MA, Tabrizi S, Hodis E, Melton DA, Sabeti PC"
journal: "eLife, 8:e43803 (2019)"
doi: "10.7554/eLife.43803"
tags: [scRNA-seq, NMF, gene-expression-program, cNMF, matrix-factorization, single-cell]
created: 2026-05-16
updated: 2026-05-16
source: "https://elifesciences.org/articles/43803"
pdf: "original.pdf"
---

# Identifying gene expression programs of cell-type identity and cellular activity with single-cell RNA-Seq

## 利用单细胞 RNA-Seq 鉴定细胞类型身份与细胞活动的基因表达程序

---

## 阅读索引

| Section | 内容 | 锚点 |
|---------|------|------|
| Abstract | 摘要 | S001 |
| Introduction | 引言 | S004 |
| Results — Simulation | 结果：模拟数据基准测试 | S011 |
| Results — Organoid | 结果：脑类器官数据 | S023 |
| Results — Visual Cortex | 结果：视觉皮层数据 | S034 |
| Discussion | 讨论 | S046 |
| Data & Code | 数据与代码可用性 | S076 |

---

## Abstract / 摘要

<a id="S001"></a>
**Original:** Identifying gene expression programs (GEPs) underlying both cell-type identity and cellular activities (e.g. life-cycle processes, responses to environmental cues) is crucial for understanding the organization of cells and tissues. Although single-cell RNA-Seq (scRNA-Seq) can quantify transcripts in individual cells, each cell's expression profile may be a mixture of both types of programs, making them difficult to disentangle. Here, we benchmark and enhance the use of matrix factorization to solve this problem. We show with simulations that a method we call consensus non-negative matrix factorization (cNMF) accurately infers identity and activity programs, including their relative contributions in each cell. To illustrate the insights this approach enables, we apply it to published brain organoid and visual cortex scRNA-Seq datasets; cNMF refines cell types and identifies both expected (e.g. cell cycle and hypoxia) and novel activity programs, including programs that may underlie a neurosecretory phenotype and synaptogenesis.

**中文:** 鉴定同时涵盖细胞类型身份的基因表达程序（GEP）和细胞活动相关GEP（如生命周期过程、对环境信号的反应）对于理解细胞与组织组织至关重要。虽然单细胞RNA测序（scRNA-Seq）可以定量单个细胞中的转录本，但每个细胞的表达谱可能是两类程序的混合体，这使得它们很难被区分。本文中，我们对矩阵分解方法进行了基准测试和优化来解决这一问题。通过模拟数据，我们证明一种名为**共识非负矩阵分解（cNMF）**的方法能够准确推断身份程序与活动程序，包括它们在每个细胞中的相对贡献。为了展示该方法所能带来的生物学洞察，我们将其应用于已发表的脑类器官和视觉皮层scRNA-Seq数据集；cNMF精细化了对细胞类型的识别，并鉴定出了预期中的（如细胞周期和低氧）以及新颖的活动程序，包括可能与神经分泌表型和突触发生相关的程序。

<a id="S002"></a>
**Original:** *eLife* **8**:e43803.
**DOI:** https://doi.org/10.7554/eLife.43803

---

## Introduction / 引言

<a id="S003"></a>
**Original:** Genes act in concert to maintain a cell's identity as a specific cell type, to respond to external signals, and to carry out complex cellular activities such as replication and metabolism. Coordinating the necessary genes for these functions is frequently achieved through transcriptional co-regulation, where genes are induced together as a gene expression program (GEP) in response to the appropriate internal or external signal (Eisen et al., 1998; Segal et al., 2003). By enabling unbiased measurement of the whole transcriptome, profiling technologies such as RNA-Seq are paving the way for systematically discovering GEPs and shedding light on the biological mechanisms that they govern (Liberzon et al., 2015).

**中文:** 基因协同作用以维持细胞作为特定细胞类型的身份、响应外部信号、执行诸如复制和代谢等复杂细胞活动。协调这些功能所需的基因通常通过转录共调控实现——即基因在适当的内部或外部信号下作为**基因表达程序（GEP）**被共同诱导（Eisen et al., 1998; Segal et al., 2003）。通过实现全转录组的无偏测量，RNA-Seq等分析技术正在为系统性发现GEP并揭示其调控的生物学机制铺平道路（Liberzon et al., 2015）。

<a id="S004"></a>
**Original:** Single-cell RNA-Seq (scRNA-Seq) has greatly enhanced our potential to resolve GEPs by making it possible to observe variation in gene expression over many individual cells. Even so, inferring GEPs remains challenging as scRNA-Seq data is noisy and high-dimensional, requiring computational approaches to uncover the underlying patterns. In addition, technical artifacts such as doublets (where two or more distinct cells are mistakenly collapsed into one) can confound analysis. Methodological advances in dimensionality reduction, clustering, lineage trajectory tracing, and differential expression analysis have helped overcome some of these issues (Amir et al., 2013; Kharchenko et al., 2014; Satija et al., 2015; Trapnell et al., 2014).

**中文:** 单细胞RNA测序极大地增强了我们解析GEP的能力，因为它使我们能够在大量单个细胞中观察基因表达的变异。即便如此，推断GEP仍然具有挑战性——scRNA-Seq数据噪声大且维度高，需要计算方法来揭示潜在的规律。此外，技术性假象如**双细胞（doublets）**（两个或多个不同细胞被错误地合并为一个）也会混淆分析。降维、聚类、谱系轨迹追踪和差异表达分析方面的方法学进展已在某种程度上克服了这些问题（Amir et al., 2013; Kharchenko et al., 2014; Satija et al., 2015; Trapnell et al., 2014）。

<a id="S005"></a>
**Original:** Here, we focus on a key challenge of inferring expression programs from scRNA-Seq data: the fact that individual cells may express multiple GEPs but we only detect cellular expression profiles that reflect their combination, rather than the GEPs themselves. A cell's gene expression is shaped by many factors including its cell type, its state in time-dependent processes such as the cell cycle, and its response to varied environmental stimuli (Wagner et al., 2016). We group these into two broad classes of expression programs that can be detectable in scRNA-Seq data: (1) GEPs that correspond to the identity of a specific cell type such as hepatocyte or melanocyte (**identity programs**) and (2) GEPs that are expressed independently of cell type, in any cell that is carrying out a specific activity such as cell division or immune cell activation (**activity programs**). In this formulation, identity programs are expressed uniquely in cells of a specific cell type, while activity programs may vary dynamically in cells of one or multiple types and may be continuous or discrete.

**中文:** 本文聚焦于从scRNA-Seq数据推断表达程序的一个核心挑战：单个细胞可能表达多个GEP，但我们只能检测到反映它们组合的细胞表达谱，而非GEP本身。一个细胞的基因表达受多种因素影响，包括其细胞类型、在细胞周期等时间依赖性过程中的状态，以及对各种环境刺激的响应（Wagner et al., 2016）。我们将这些因素分为两大可在scRNA-Seq数据中检测到的表达程序类别：
1. **身份程序（identity programs）**——对应特定细胞类型（如肝细胞或黑色素细胞）的GEP
2. **活动程序（activity programs）**——独立于细胞类型，在任一执行特定活动（如细胞分裂或免疫细胞激活）的细胞中表达的GEP

在这种设定下，身份程序仅在特定细胞类型的细胞中独特表达，而活动程序可以在一种或多种类型的细胞中动态变化，可以是连续的或离散的。

<a id="S006"></a>
**Original:** Thus far, the vast majority of scRNA-Seq studies have focused on systematically identifying and characterizing the expression programs of cell types composing a given tissue, that is identity GEPs. Substantially less progress has been made in identifying activity GEPs, primarily through direct manipulation of cells in controlled experiments, for example comparing stimulated and unstimulated neurons (Hrvatin et al., 2018) or cells pre- and post-viral infection (Steuerman et al., 2018).

**中文:** 迄今为止，绝大多数scRNA-Seq研究都集中在系统性地鉴定和描述构成特定组织的细胞类型的表达程序——即身份GEP。而在鉴定活动GEP方面的进展则少得多，目前主要通过控制实验中的直接细胞操作来实现，例如比较刺激和未刺激的神经元（Hravtin et al., 2018）或病毒感染前后的细胞（Steuerman et al., 2018）。

<a id="S007"></a>
**Original:** We hypothesized that we could infer activity GEPs directly from variation in single-cell expression profiles using matrix factorization. ...Unlike hard clustering, which reduces all cells in a cluster to a single shared GEP, matrix factorization allows cells to express multiple GEPs.

**中文:** 我们假设可以通过矩阵分解直接从单细胞表达谱的变异中推断活动GEP。……与硬聚类（将聚类中所有细胞归结为一个共享GEP）不同，矩阵分解允许细胞表达多个GEP。

<a id="S008"></a>
**Original:** We see three primary motivations for jointly inferring identity and activity GEPs in scRNA-Seq data. First, systematic discovery of GEPs could reveal unexpected or novel activity programs. Second, it could enable characterization of the prevalence of each activity GEP across cell types. Finally, accounting for activity programs could improve inference of identity programs by avoiding spurious inclusion of activity program genes.

**中文:** 我们提出在scRNA-Seq数据中联合推断身份和活动GEP的三个主要动机：第一，系统性发现GEP可能揭示意想不到的或新的活动程序；第二，它可以表征每个活动GEP在不同细胞类型中的盛行程度；第三，考虑活动程序可以避免将活动程序基因错误地归入身份程序，从而改善身份程序的推断。

<a id="S009"></a>
**Original:** While matrix factorization is widely used as a preprocessing step in scRNA-Seq analysis, a priori it is unclear which, if any, factorization approaches would be most appropriate for inferring biologically meaningful GEPs. In particular, Principal Component Analysis (PCA), Independent Component Analysis (ICA), Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) have been used for dimensionality reduction or as an approach to cell clustering. However, the dimensions inferred by these algorithms may not necessarily align with biologically meaningful gene expression programs.

**中文:** 虽然矩阵分解在scRNA-Seq分析中被广泛用作预处理步骤，但先验地看，不清楚哪些（如果有的话）分解方法最适合推断有生物学意义的GEP。特别是，主成分分析（PCA）、独立成分分析（ICA）、潜在狄利克雷分配（LDA）和非负矩阵分解（NMF）已被用于降维或细胞聚类。然而，这些算法推断出的维度不一定与有生物学意义的基因表达程序对齐。

<a id="S010"></a>
**Original:** In this study, we motivate, validate, and enhance the use of matrix factorization for GEP inference. Using simulations, we show that despite their simplifying assumptions, ICA, LDA, and NMF—but not PCA—can accurately discover both activity and identity GEPs. However, due to inherent randomness in their algorithms, they give substantially varying results when repeated multiple times. We therefore implemented a meta-analysis approach (consensus matrix factorization), which demonstrably increased robustness and accuracy. Overall, the meta-analysis of NMF, which we call **Consensus NMF (cNMF)**, gave the best performance.

**中文:** 在本研究中，我们推动、验证并增强了矩阵分解在GEP推断中的应用。通过模拟数据，我们显示——尽管有简化假设——ICA、LDA和NMF（而非PCA）可以准确发现活动和身份GEP。然而，由于其算法的固有随机性，多次重复运行时结果会有显著差异。因此，我们实现了**元分析（meta-analysis）方法**（共识矩阵分解），这显著提高了鲁棒性和准确性。总体而言，NMF的元分析版本——我们称之为**cNMF（Consensus NMF）**——表现最佳。

---

## Results — Simulation Benchmarking / 结果：模拟数据基准测试

<a id="F001"></a>
### Fig. 1. cNMF 流程示意图

**Source:** Article text, p.3

![Fig. 1](https://iiif.elifesciences.org/lax/43803%2Felife-43803-fig1-v2.tif/full/1234,/0/default.webp)

**Original caption:** Schematics of matrix factorization for single-cell RNA-Seq analysis and the consensus matrix factorization pipeline. (a) Schematic representation of how cellular gene expression can be modeled with matrix factorization. (b) Schematic of the consensus matrix factorization pipeline.

**中文图注:** 单细胞RNA-Seq分析的矩阵分解示意图和共识矩阵分解流程。(a) 矩阵分解如何建模细胞基因表达的示意图。(b) 共识矩阵分解流程示意图。

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | 矩阵分解概念图：左侧柱状图是单个细胞的基因表达，中间饼图表示每个程序的使用权重，右侧柱状图是全局GEP | 每个细胞的表达谱是多个GEP的加权混合 |
| B | cNMF流程图：多次NMF运行 → 过滤异常值 → 聚类各次复制的成分 → 取中位数作为共识估计 → 最终拟合使用矩阵 | 通过元分析策略提高稳定性和准确性 |

**🎯 核心结论：** 矩阵分解可以将细胞表达谱分解为身份GEP和活动GEP，cNMF流程通过多次运行+共识聚合克服单次NMF的不稳定性。

---

<a id="S011"></a>
**Original:** We sought to establish whether components inferred by simple matrix factorizations would align with GEPs in scRNA-seq data. We evaluated this in simulated data of 15,000 cells composed of 13 cell types, one cellular activity program that is active to varying extents in a subset of cells of four cell types, and a 6% doublet rate.

**中文:** 我们试图验证简单矩阵分解推断出的成分是否能与scRNA-Seq数据中的GEP对齐。我们在包含**15,000个细胞、13种细胞类型、一个活动程序（在4种细胞类型的子集中以不同程度活跃）以及6%双细胞率**的模拟数据中评估了这一点。

<a id="S012"></a>
**Original:** We first analyzed the performance of ICA, LDA, and NMF and noticed that they yielded different solutions when run several times on the same input simulated data... Unlike PCA, which has an exact solution, these factorizations use stochastic optimization algorithms to obtain approximate solutions in a solution space including many local optima.

**中文:** 我们首先分析了ICA、LDA和NMF的性能，发现它们在相同的模拟输入数据上多次运行时给出了不同的解……与PCA（有精确解）不同，这些因子分解使用随机优化算法在包含许多局部最优解的解空间中获取近似解。

<a id="S013"></a>
**Original:** To overcome the issue of variability of solutions, we employed a meta-analysis approach, which we call consensus matrix factorization, that averages over multiple replicates to increase the robustness of the solution. The method proceeds as follows: we run the factorization multiple times, filter outlier components, cluster the components over all replicates combined, and take the cluster medians as our consensus estimates... This approach also provides us with a guide for determining K, the number of components to use.

**中文:** 为克服解的可变性，我们采用了一种**元分析方法**——共识矩阵分解——通过对多次复制结果进行平均来提高解的稳健性。具体流程：多次运行因子分解 → 过滤异常成分 → 对所有复制的成分进行聚类 → 取聚类中位数作为共识估计……该方法还为我们确定成分数量K提供了指导。

<a id="S014"></a>
**Original:** Consensus matrix factorization inferred components underlying the GEPs as well as which cells expressed each GEP (Figure 2b–c). By contrast, principal components were linear combinations of the true GEPs. Beyond increasing robustness, the consensus approach also increased the ability of factorization to deconvolute the true GEPs — most dramatically for LDA and NMF. cNMF successfully deconvoluted the activity and identity GEPs more frequently than the other methods.

**中文:** 共识矩阵分解推断出了GEP背后的成分以及哪些细胞表达了每个GEP（图2b–c）。相比之下，主成分是真实GEP的线性组合。除了提高稳健性外，共识方法还提高了分解方法解卷积真实GEP的能力——对LDA和NMF最为显著。cNMF比其他方法更频繁地成功解卷积了活动和身份GEP。

<a id="S015"></a>
**Original:** We found that cNMF was most accurate at inferring genes in the activity program, with a sensitivity of 61% at a false discovery rate (FDR) of 5% (Figure 2e). cICA and the ground-truth clustering were next most accurate with 57% and 56% sensitivity at a 5% FDR, respectively. As expected, the clustering approaches performed worse as they inappropriately assigned activity GEP genes to identity programs, resulting in an elevated FDR.

**中文:** cNMF在推断活动程序基因方面最为准确，在5%错误发现率（FDR）下的敏感度为**61%**（图2e）。cICA和基于真实标签的聚类次之，在5% FDR下的敏感度分别为57%和56%。不出所料，聚类方法表现较差，因为它们将活动GEP基因不恰当地分配给了身份程序，导致FDR升高。

<a id="S016"></a>
**Original:** Beyond identifying the activity program itself, we found that cNMF could also accurately infer which cells expressed the activity program and what proportion of their expression was derived from the activity program (Figure 2f). With an expression usage threshold of 10%, cNMF accurately classified 91% of cells expressing the activity program and 94% of cells that did not express the program.

**中文:** 除了识别活动程序本身，cNMF还能准确推断哪些细胞表达了活动程序以及它们的表达中有多少比例源自该程序（图2f）。以10%表达使用量为阈值，cNMF正确分类了**91%表达活动程序的细胞**和**94%不表达该程序的细胞**。

<a id="S017"></a>
**Original:** We further demonstrated that cNMF was robust to the presence of doublets... We found that cNMF correctly modeled doublets as a combination of the GEPs for the two combined cell types (Figure 2g). Moreover, cNMF could accurately infer the GEPs even in a simulated dataset composed of 50% doublets.

**中文:** 我们进一步证明cNMF对双细胞的存在具有稳健性……cNMF正确地将双细胞建模为两种合并细胞类型的GEP组合（图2g）。此外，即使在**50%为双细胞**的模拟数据中，cNMF仍能准确推断GEP。

<a id="F002"></a>
### Fig. 2. 模拟数据基准测试

**Source:** Article text, p.5–8

![Fig. 2](https://iiif.elifesciences.org/lax/43803%2Felife-43803-fig2-v2.tif/full/1234,/0/default.webp)

**Original caption:** cNMF infers identity and activity expression programs in simulated data. (a) tSNE plot of an example simulation. (b) Pearson correlation between true GEPs and cNMF-inferred GEPs. (c) tSNE colored by usage. (d) Detection rate across noise levels. (e) ROC (with FDR) for activity GEP gene prediction. (f) Inferred vs simulated usage. (g) Doublet modeling.

**中文图注:** cNMF在模拟数据中推断身份和活动表达程序。(a) 示例模拟的tSNE图。(b) 真实GEP与cNMF推断GEP之间的Pearson相关性。(c) 按使用量着色的tSNE。(d) 不同噪声水平下的检测率。(e) 活动GEP基因预测的ROC曲线（以FDR为横轴）。(f) 推断使用量与模拟使用量对比。(g) 双细胞建模。

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | tSNE显示13种细胞类型（不同颜色），双细胞标记为灰色X，表达活动的细胞有黑色边框 | 模拟数据模拟了真实scRNA-Seq的复杂结构 |
| B | 热图显示推断GEP与真实GEP的Pearson相关性矩阵 | 每个cNMF成分都与一个真实GEP高度相关（深红色对角线） |
| C | 身份程序（左）和活动程序（右）的模拟使用量与cNMF推断使用量对比 | cNMF使用量与模拟值高度一致 |
| D | 3种信噪比水平下20次复制的检测率 | 高信噪比时cNMF达~95%，cNMF持续优于cICA和cLDA |
| E | 活动GEP基因预测的ROC曲线（FDR为横轴） | cNMF在5% FDR时敏感度61%，优于所有其他方法 |
| F | 散点图：推断使用量 vs 模拟使用量 | R=0.68，高相关性 |
| G | 双细胞的真实使用量（左）与cNMF推断（右） | cNMF正确将双细胞建模为两种细胞类型的混合 |

**📊 统计注释：** 模拟使用Splatter框架；敏感性计算基于5% FDR阈值；Pearson R = 0.68–0.74

**🎯 核心结论：** cNMF在模拟数据中展现出最佳的准确性、稳健性和对双细胞的容忍度，为将其应用于真实数据奠定了基础。

---

## Results — Brain Organoid Data / 结果：脑类器官数据

<a id="S018"></a>
**Original:** Having demonstrated its performance on simulated data, we then used cNMF to re-analyze a published scRNA-Seq dataset of 52,600 single cells isolated from human brain organoids (Quadrato et al., 2017).

**中文:** 在模拟数据上证明了性能后，我们将cNMF应用于重新分析一个已发表的包含**52,600个来自人脑类器官的单细胞**的scRNA-Seq数据集（Quadrato et al., 2017）。

<a id="S019"></a>
**Original:** We identified 31 distinct programs... Most cells had high usage of just a single GEP, which is consistent with expressing just an identity program. When cells expressed multiple GEPs, those typically had correlated expression profiles, suggesting identity programs of closely related cell types or cells transitioning between two developmental states. By contrast, three GEPs were co-expressed with many distinct and uncorrelated programs, suggesting that they represent activity programs that occur across diverse cell types.

**中文:** 我们识别出**31个不同的程序**……大多数细胞只高使用一个GEP，这与仅表达身份程序一致。当细胞表达多个GEP时，这些GEP通常具有相关的表达谱，表明是密切相关细胞类型的身份程序或在两个发育状态之间过渡的细胞。相比之下，**三个GEP**与许多不同且不相关的程序共表达，表明它们是跨多种细胞类型发生的活动程序。

<a id="S020"></a>
**Original:** Of the three activity programs identified, we found that two were strongly enriched for cell cycle Gene Ontology (GO) sets... one represents a G1/S checkpoint program and the other represents a G2/M checkpoint program... The third activity program is characterized by high levels of hypoxia related genes (e.g. *VEGFA*, *PGK1*, *CA9*, *P4HA1*, *HILPDA*) suggesting it represents a **hypoxia program**.

**中文:** 在识别的三个活动程序中，有两个强烈富集了细胞周期GO集……一个代表**G1/S检查点程序**，另一个代表**G2/M检查点程序**。第三个活动程序的特征是低氧相关基因高表达（如*VEGFA*、*PGK1*、*CA9*、*P4HA1*、*HILPDA*），表明它是一个**低氧程序**。

**Key insight:** 最初的研究用HIF1A染色未能检测到显著的缺氧水平，而cNMF通过无偏方法成功检测到了这一程序——这体现了cNMF的敏感性。

<a id="S021"></a>
**Original:** cNMF was further able to refine cell types by disentangling the contributions of identity and activity programs. For example, we found that a cell cluster labeled as 'proliferative precursors' is composed of multiple cell types including immature muscle and dopaminergic neurons. The predominant identity GEP of cells in this cluster is most strongly associated with the gene PAX7, a marker of self-renewing muscle stem cells.

**中文:** cNMF通过解耦身份和活动程序的贡献，进一步**精细化了对细胞类型的识别**。例如，最初被标注为"增殖前体细胞"的细胞群实际上包含多种细胞类型，包括未成熟肌肉细胞和多巴胺能神经元。该群中细胞的主要身份GEP与PAX7（自我更新肌肉干细胞的标志物）最强相关。

<a id="F003"></a>
### Fig. 3. 脑类器官数据

**Source:** Article text, p.10–13

![Fig. 3](https://iiif.elifesciences.org/lax/43803%2Felife-43803-fig3-v2.tif/full/1234,/0/default.webp)

**Original caption:** Deconvolution of activity programs from cell identity in brain organoid data.

**中文图注:** 在脑类器官数据中将活动程序从细胞身份中解卷积出来。

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | 热图：31个GEP在所有细胞中的使用百分比 | 28个身份GEP（上）各自主导不同细胞群，3个活动GEP（下）跨群分布 |
| B | tSNE按最大使用身份GEP着色，活动程序使用>10%的细胞用边框标记 | 细胞周期程序和低氧程序广泛分布 |
| C | 3个活动程序的Gene Ontology富集p值 | G1/S富集DNA复制，G2/M富集有丝分裂，低氧富集ER定位 |
| D | 三个中胚层程序的热图（快肌、慢肌、未成熟肌肉） | cNMF将"中胚层"进一步细分为具体的肌肉类型 |
| E | 三个活动程序的标志基因热图 | G1/S: *MCM*家族; G2/M: *CENP*家族; 低氧: *VEGFA*, *CA9* |
| F | 各细胞类型中表达G1/S或G2/M的比例 | 干细胞样细胞>38%在增殖，为最高 |
| G | 各细胞类型中表达低氧程序的比例 | C6-1和神经上皮中低氧比例最高 |

**🎯 核心结论：** cNMF从脑类器官中无偏地识别出细胞周期程序和意料之外的低氧程序，并将"增殖前体细胞"群重新解析为多种细胞类型（肌肉前体、多巴胺能神经元），展示了超越传统聚类的分辨能力。

---

## Results — Visual Cortex Data / 结果：视觉皮层数据

<a id="S022"></a>
**Original:** We re-analyzed scRNA-Seq data from 15,011 excitatory pyramidal neurons or inhibitory interneurons from the visual cortex of dark-reared mice that were suddenly exposed to 0 hr, 1 hr, or 4 hr of light (Hrvatin et al., 2018). We sought to determine whether cNMF would identify the relatively modest activity programs (~60 genes with FC >= 2 and FDR < 0.05) elicited by the experiment **without knowledge of the experimental design labels**.

**中文:** 我们重新分析了来自避光饲养小鼠（突然暴露于光0小时、1小时或4小时）视觉皮层的**15,011个兴奋性锥体神经元或抑制性中间神经元**的scRNA-Seq数据（Hravtin et al., 2018）。我们想知道cNMF是否能在**不知道实验设计标签**的情况下识别出实验诱导的较微弱活动程序（约60个基因，FC ≥ 2, FDR < 0.05）。

<a id="S023"></a>
**Original:** We ran cNMF on neurons combined from all three exposure conditions and identified 20 GEPs, interpreting 14 as identity and six as activity programs. Three activity programs were correlated with the stimulus — an **early response program (ERP)** induced at 1h, and two **late response programs (LRPs)** induced at 4h.

**中文:** 我们将三种光照条件的神经元合并运行cNMF，识别出**20个GEP**（14个身份，6个活动）。其中3个活动程序与刺激相关——一个在1小时诱导的**早期反应程序（ERP）**和两个在4小时诱导的**晚期反应程序（LRP）**。

<a id="S024"></a>
**Original:** Intriguingly, one LRP was more induced in superficial cortical layers, while the other was more induced in deeper layers. This supports a recently proposed model where the ERP is predominantly shared across excitatory neurons, while LRPs vary more substantially across neuron subtypes.

**中文:** 有趣的是，一个LRP在皮层浅层更易被诱导，而另一个在深层更易被诱导。这支持了一个近期提出的模型：ERP主要在兴奋性神经元中共享，而LRP在不同神经元亚型间有较大差异。

<a id="S025"></a>
**Original:** cNMF identified a depolarization induced program in visual cortex neurons that were **not experimentally manipulated** (Tasic et al., 2016 dataset)... This demonstrates that cNMF could find the depolarization induced activity program in scRNA-Seq of cells that had not been experimentally manipulated to elicit it.

**中文:** cNMF在**未经实验操作**的视觉皮层神经元（Tasic et al., 2016数据集）中也鉴定出了去极化诱导的程序……这表明cNMF能在未通过实验操作诱导的细胞的scRNA-Seq中找到去极化诱导的活动程序——即无需对照实验即可发现活动程序。

<a id="S026"></a>
**Original:** cNMF identified three additional activity programs that were not well correlated with the light stimulus: a **Neurosecretory (NS)** program characterized by secreted neuropeptides (*Vgf*, *Adcyap1*, *Scg2*, *Cck*); a **Synaptogenesis (Syn)** program characterized by synapse formation genes (*Mef2c*, *Ncam1*, *Cadm1*); and an Other program characterized by *Meg3* and genes associated with cerebral ischemic injury.

**中文:** cNMF还鉴定出了三个与光刺激相关性不大的活动程序：**神经分泌（NS）程序**（以分泌神经肽为特征：*Vgf*、*Adcyap1*、*Scg2*、*Cck*）；**突触发生（Syn）程序**（以突触形成基因为特征：*Mef2c*、*Ncam1*、*Cadm1*）；以及"其他"程序（以*Meg3*和与脑缺血损伤相关的基因为特征）。

<a id="F004"></a>
### Fig. 4. 视觉皮层数据

**Source:** Article text, p.15–18

![Fig. 4](https://iiif.elifesciences.org/lax/43803%2Felife-43803-fig4-v2.tif/full/1234,/0/default.webp)

**Original caption:** Identification of activity programs in neurons of the visual cortex.

**中文图注:** 在视觉皮层神经元中鉴定活动程序。

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | 热图：20个GEP在15,011个细胞中的使用量 | 14个身份GEP（上），6个活动GEP（下） |
| B | tSNE按最大身份GEP着色（左）；各活动程序的绝对使用量（右） | 活动程序在不同神经元亚型中广泛分布 |
| C | 箱线图：各活动程序在三种刺激条件下的使用量 | ERP在1h上调，LRPs在4h上调，NS/Syn/Other与刺激无关 |
| D | 主数据集的浅层LRP与Tasic数据集对应程序的z-score散点图 | R=0.645，跨数据集高度可重复 |
| E | 神经分泌程序在主数据与Tasic数据集之间的可重复性 | OR=53.8，p=8×10⁻²¹ |

**📊 统计注释：** ERP与1h诱导基因的Mann-Whitney检验p=8×10⁻³⁴；Fisher精确检验用于跨数据集验证

**🎯 核心结论：** cNMF在无监督条件下（不知道实验标签）识别出了光刺激诱导的活动程序（ERP和LRP），发现了浅层/深层差异，并在独立数据集中验证了这些程序的可重复性。它还发现了未被刺激诱导但可能具有生物学意义的新程序（NS、Syn）。

---

## Discussion / 讨论

<a id="S027"></a>
**Original:** In this study, we distinguished between cell type (identity) and cell type independent (activity) gene expression programs (GEPs) to motivate our use of matrix factorization, which represents cells as linear combinations of multiple GEPs.

**中文:** 在本研究中，我们通过区分细胞类型（身份）和细胞类型非依赖（活动）基因表达程序（GEP），为使用矩阵分解奠定基础——矩阵分解将细胞表示为多个GEP的线性组合。

<a id="S028"></a>
**Original:** We have provided an empirical foundation for the use of matrix factorization to simultaneously infer identity and activity programs from scRNA-Seq data. cNMF inferred the most accurate identity and activity programs of all the methods we tested. Moreover, it yielded results in interpretable units of gene expression (transcripts per million) and could accurately infer the percentage of each cell's expression that was derived from each GEP.

**中文:** 我们为使用矩阵分解从scRNA-Seq数据中同时推断身份和活动程序提供了经验基础。cNMF在所有测试方法中推断出了最准确的身份和活动程序，结果以可解释的基因表达单位（TPM）呈现，并能准确推断每个细胞中每个GEP的表达百分比。

<a id="S029"></a>
**Original:** While commonly used approaches based on clustering or pseudotemporal ordering of cells are poorly suited to achieve such insights from single-cell data, these findings emerge naturally from our matrix factorization approach.

**中文:** 虽然基于聚类或伪时间排序的常用方法很难从单细胞数据中获得这些洞察，但这些发现却自然地源于我们的矩阵分解方法。

<a id="S030"></a>
**Original:** A more fundamental limitation of matrix factorizations, including cNMF, is the built-in assumption that cells can be modeled as linear combinations of GEPs. Notably, this precludes modeling of transcriptional repression... To our knowledge, such relationships have not been represented in a matrix factorization framework, but they may be easier to incorporate in new classes of latent variable models such as variational autoencoders (VAEs).

**中文:** 矩阵分解（包括cNMF）的一个更根本的局限性在于其内置假设：细胞可以建模为GEP的线性组合。这尤其排除了对转录抑制的建模……据我们所知，这种关系尚未在矩阵分解框架中被表示，但可能更容易在变分自编码器（VAE）等新型潜变量模型中实现。

<a id="S031"></a>
**Original:** With ongoing technological progress in RNA capture efficiency and throughput, scRNA-Seq data is likely to become richer and more expansive. This will make it possible to detect increasingly subtle GEPs, reflecting biological variability in cell types, cell states, and activities. Here, we have demonstrated a computational framework that can be used to infer such GEPs directly from the scRNA-Seq data without the need for experimental manipulations, providing key insights into the behavior of cells and tissues.

**中文:** 随着RNA捕获效率和通量的持续技术进展，scRNA-Seq数据将变得更加丰富和广泛。这将使检测越来越微妙的GEP成为可能——反映细胞类型、细胞状态和活动的生物学变异。本文证明了一个无需实验操作即可直接从scRNA-Seq数据推断这类GEP的计算框架，为理解细胞和组织行为提供了关键洞察。

<a id="F005"></a>
### Fig. 5. cNMF 对 K 选择的鲁棒性

**Source:** Article text, p.20

![Fig. 5](https://iiif.elifesciences.org/lax/43803%2Felife-43803-fig5-v2.tif/full/1234,/0/default.webp)

**Original caption:** Robustness of cNMF to the number of components (K). Line plots of the maximum Pearson correlation between each cNMF component from the main analysis and components from multiple choices of K.

**中文图注:** cNMF对成分数量K的鲁棒性。主线分析的每个cNMF成分与不同K取值下的成分之间的最大Pearson相关性线图。

---

**🔬 图表解读**

| 内容 | 关键发现 |
|------|----------|
| 模拟数据中不同K值的相关性 | 活动程序（彩色线）在K值变化时保持稳定高相关性 |
| 围绕选定K±4变化 | 每步增减约一个GEP，核心GEP集保持不变 |
| 高于选定K时 | 找到与原始K程序近似匹配的成分（Pearson r > 0.7） |

**🎯 核心结论：** cNMF对K的选择在合理范围内是稳健的——核心GEP集不会随K变化而剧烈变化，支持了方法的实用性和稳定性。

---

## Key Terminology / 关键术语

| 英文 | 中文 | 说明 |
|------|------|------|
| Gene Expression Program (GEP) | 基因表达程序 | 一组协同调控、共同表达的基因 |
| Identity program | 身份程序 | 决定细胞类型的GEP |
| Activity program | 活动程序 | 响应环境或执行功能的GEP |
| cNMF | 共识非负矩阵分解 | 本文提出的方法 |
| Usage matrix | 使用矩阵 | 每个GEP在每个细胞中的贡献权重 |
| Doublet | 双细胞 | 两个细胞被误计为一个 |
| NMF | 非负矩阵分解 | 约束所有值为非负的矩阵分解 |
| Consensus | 共识 | 通过多次运行取中位数聚合结果 |
| Over-dispersed genes | 过度分散基因 | 方差高于平均水平的基因 |
| TPM | 每百万转录本 | 标准化的基因表达单位 |

---

## Resource Summary / 关联资源

### Code
- **cNMF**: [https://github.com/dylkot/cNMF/](https://github.com/dylkot/cNMF/)
- **scsim (simulation)**: [https://github.com/dylkot/scsim](https://github.com/dylkot/scsim)
- **Reproducible capsule**: [Code Ocean](https://doi.org/10.24433/CO.9044782e-cb96-4733-8a4f-bf42c21399e6)

### Data
- Brain organoid (Quadrato 2017): **GSE86153**
- Visual cortex (Hrvatin 2018): **GSE102827**
- Visual cortex (Tasic 2016): **GSE71585**
- Pancreatic islets (Baron 2016): **GSE50244**

### Original Paper
- **DOI**: [10.7554/eLife.43803](https://doi.org/10.7554/eLife.43803)
- **PDF**: [[Knowledge/papers/kotliar-2019-cnmf/original.pdf]]

---

*Generated on 2026-05-16. Bilingual reading artifact for Kotliar et al., eLife 2019.*
