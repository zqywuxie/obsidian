---
title: "UCell: Robust and scalable single-cell gene signature scoring — 中英文精读"
authors: "Andreatta M, Carmona SJ"
journal: "Computational and Structural Biotechnology Journal, 19:3796-3798 (2021)"
doi: "10.1016/j.csbj.2021.06.043"
tags: [scRNA-seq, gene-signature, UCell, signature-scoring, Mann-Whitney, R-package]
created: 2026-05-16
updated: 2026-05-16
source: "https://spj.science.org/doi/10.1016/j.csbj.2021.06.043"
pdf: "original.pdf"
---

# UCell: Robust and scalable single-cell gene signature scoring

## UCell：稳健且可扩展的单细胞基因签名评分

---

## 阅读索引

| Section | 内容 | 锚点 |
|---------|------|------|
| Abstract | 摘要 | S001 |
| Introduction | 引言 | S002 |
| Methods | 方法 | S007 |
| Results | 结果 | S009 |
| Fig. 1 | 图 1 及解读 | F001 |
| Table 1 | 表 1 及解读 | T001 |

---

## Abstract / 摘要

<a id="S001"></a>
**Original:** UCell is an R package for evaluating gene signatures in single-cell datasets. UCell signature scores, based on the Mann-Whitney U statistic, are robust to dataset size and heterogeneity, and their calculation demands less computing time and memory than other available methods, enabling the processing of large datasets in a few minutes even on machines with limited computing power. UCell can be applied to any single-cell data matrix, and includes functions to directly interact with Seurat objects. The UCell package and documentation are available on GitHub at https://github.com/carmonalab/UCell.

**中文:** UCell 是一个用于在单细胞数据集中评估基因签名（gene signature）的 R 包。UCell 的签名分数基于 **Mann-Whitney U 统计量**，对数据集的大小和异质性**具有稳健性**，且其计算所需的时间和内存均低于其他可用方法，即使在计算能力有限的机器上也能在几分钟内处理大型数据集。UCell 可应用于任何单细胞数据矩阵，并包含直接与 Seurat 对象交互的函数。UCell 包及文档在 GitHub (https://github.com/carmonalab/UCell) 上开源提供。

---

## Introduction / 引言

<a id="S002"></a>
**Original:** In single-cell RNA-seq analysis, gene signature (or "module") scoring constitutes a simple yet powerful approach to evaluate the strength of biological signals, typically associated to a specific cell type or biological process, in a transcriptome. Thousands of gene sets have been derived by measuring transcriptional differences between different biological states or cell phenotypes, and are collected in public databases such as MSigDB. More recently, large-scale efforts to construct single-cell atlases are providing specific gene sets that can be useful to discriminate between cell types. For example, Han et al. have used single-cell RNA sequencing to quantify cell type heterogeneity in different tissues and to define gene signatures for >100 human and murine cell types.

**中文:** 在单细胞 RNA-seq 分析中，**基因签名评分**（gene signature/module scoring）是一种简单而强大的方法，用于评估转录组中生物学信号的强度——这些信号通常与特定的细胞类型或生物学过程相关。通过测量不同生物学状态或细胞表型之间的转录差异，已经推导出了数千个基因集，并收录在 MSigDB 等公共数据库中。近期，构建单细胞图谱的大规模工作正在提供可用于区分细胞类型的特定基因集。例如，Han et al. 使用单细胞 RNA 测序量化了不同组织中的细胞类型异质性，并定义了超过 100 种人类和小鼠细胞类型的基因签名。

<a id="S003"></a>
**Original:** Given such a gene set, signature scoring aims at quantifying the activity of the genes in the set, with the goal to characterize cell types, states, active biological processes or responses to environmental cues.

**中文:** 给定这样的基因集，签名评分旨在量化集合中基因的活性，目标是表征细胞类型、状态、活跃的生物学过程或对环境信号的反应。

<a id="S004"></a>
**Original:** The Seurat R package is one of the most comprehensive and widely used frameworks for scRNA-seq data analysis. Seurat provides a computationally efficient gene signature scoring function, named **AddModuleScore**, originally proposed by Tirosh et al. However, because genes are binned based on their average expression across the **whole dataset** for normalization purposes, the method generates inconsistent results for the same cell depending on the composition of the dataset.

**中文:** Seurat R 包是最全面、最广泛使用的 scRNA-seq 数据分析框架之一。Seurat 提供了一个计算高效的基因签名评分函数——**AddModuleScore**（最初由 Tirosh et al. 提出）。然而，由于该方法基于基因在**整个数据集中**的平均表达进行分箱（binning）归一化，同一细胞在不同数据集组成下会产生不一致的结果。

> ⚠️ **核心问题**：AddModuleScore 对 CD8 T 细胞在"全 T 细胞数据集"和"仅 CD8 T 细胞子集"中给出不同的分数，因为归一化的参考基线变了。

<a id="S005"></a>
**Original:** Inspired by the AUCell algorithm implemented in SCENIC, we propose **UCell**, a gene signature scoring method based on the **Mann-Whitney U statistic**. UCell scores depend only on the relative gene expression in individual cells and are therefore not affected by dataset composition.

**中文:** 受 SCENIC 中实现的 AUCell 算法启发，我们提出了 **UCell**——一种基于 **Mann-Whitney U 统计量**的基因签名评分方法。UCell 分数仅取决于**单个细胞内部**的基因相对表达，因此不受数据集组成的影响。

<a id="S006"></a>
**Original:** We provide a time- and memory-efficient implementation of the algorithm that can be seamlessly incorporated into Seurat workflows.

**中文:** 我们提供了该算法的时间高效和内存高效的实现，可以无缝整合到 Seurat 工作流中。

---

## Methods / 方法

<a id="S007"></a>
**Original:** UCell calculates gene signature scores for scRNA-seq data based on the Mann-Whitney U statistic. Given a g × c matrix X of numerical values (e.g. gene expression measurements) for g genes in c cells, we first calculate the matrix of relative ranks R by sorting each column in X; in other words, we calculate a ranked list of genes for each cell in the dataset.

**中文:** UCell 基于 Mann-Whitney U 统计量为 scRNA-seq 数据计算基因签名分数。给定一个 **g × c** 的数值矩阵 X（例如，g 个基因在 c 个细胞中的表达测量值），我们首先通过对 X 的每一列排序来计算**相对排名矩阵 R**；换句话说，我们为数据集中的每个细胞计算一个基因排名列表。

<a id="S008"></a>
**Original:** Because in scRNA-seq not all molecules in the original sample are observed, transcript counts matrices contain many zeros, resulting in a long tail of bottom-ranking genes. To mitigate this uninformative tail, we set r_{g,c} = r_{max} + 1 for all r_{g,c} > r_{max}, with r_{max} = 1500 by default (matching typical thresholds used for quality control for minimum number of genes detected).

To evaluate a gene signature s composed of n genes (s₁,…,sₙ), we calculate a UCell score U' for each cell j in X with the formula:

$$U'_j = 1 - \frac{U_j}{n \cdot r_{max}}$$

where U is the Mann-Whitney U statistic calculated by:

$$U_j = \sum_{i=1}^{n} r'_{i,j} - \frac{n(n+1)}{2}$$

and R′ is obtained by sub-setting R on the genes in signature s.

We note that the U statistic is closely related to the area-under-the-curve (AUC) statistic for ROC curves, therefore we expect UCell scores to correlate with methods based on AUC scores such as AUCell.

Internally, UCell uses the `frank` function from the `data.table` package for efficient ranks computations. Large datasets are automatically split into batches of reduced size, which can be processed serially (minimizing memory usage) or in parallel through the `future` package (minimizing execution time) depending on the available computational resources.

**中文:** 由于 scRNA-seq 并未观察到原始样本中的所有分子，转录本计数矩阵包含许多零，导致底部基因出现长尾分布。为减少这种无信息尾部的影响，我们对所有 r_{g,c} > r_{max} 的值设 r_{g,c} = r_{max} + 1，默认 r_{max} = 1500（与检测到的最少基因数的典型质控阈值一致）。

对于由 n 个基因 (s₁,…,sₙ) 组成的基因签名 s，我们为 X 中的每个细胞 j 计算 UCell 分数 U'：

$$U'_j = 1 - \frac{U_j}{n \cdot r_{max}}$$

其中 U 是 Mann-Whitney U 统计量，计算公式为：

$$U_j = \sum_{i=1}^{n} r'_{i,j} - \frac{n(n+1)}{2}$$

R′ 是通过将 R 矩阵子集化为签名 s 中的基因得到的。

我们注意到 U 统计量与 ROC 曲线的**曲线下面积（AUC）**统计量密切相关，因此 UCell 分数预计会与基于 AUC 分数的方法（如 AUCell）相关。

内部实现上，UCell 使用 `data.table` 包的 `frank` 函数进行高效的排名计算。大型数据集会自动拆分为较小尺寸的批次，可以根据可用的计算资源选择串行处理（最小化内存使用）或通过 `future` 包并行处理（最小化执行时间）。

---

## Results / 结果

<a id="F001"></a>
### Fig. 1. UCell 评估 T 细胞签名

**Placed near:** S009

![Fig. 1](assets/fig1.jpg)

**Original caption:** Evaluating T cell signatures using UCell. A) UMAP representation of T subsets from the single-cell dataset by Hao et al. B) UCell score distribution in UMAP space for five gene signatures evaluated using UCell. C-D) Comparison of UCell score (C) and Seurat's AddModuleScore (D) distributions for a two-gene CD8 T cell signature (CD8A, CD8B), evaluated on the complete T cell dataset (black outlines), or on the subset of CD8 T cells only (red outlines); UCell scores for CD8 T cell have the same distribution in the complete or subset dataset, while AddModuleScores are highly dependent on dataset composition. E-F) Running time (E) and peak memory (F) for UCell and AUCell on datasets of different sizes.

**中文图注:** 使用 UCell 评估 T 细胞签名。A) Hao et al. 单细胞数据集中 T 细胞亚群的 UMAP 表示。B) 五个基因签名的 UCell 分数在 UMAP 空间中的分布。C-D) UCell 分数 (C) 与 Seurat 的 AddModuleScore (D) 对一个双基因 CD8 T 细胞签名 (CD8A, CD8B) 的分布比较——完整 T 细胞数据集（黑色轮廓）vs 仅 CD8 T 细胞子集（红色轮廓）；UCell 分数在完整和子集数据集中分布相同，而 AddModuleScore 高度依赖数据集组成。E-F) UCell 与 AUCell 在不同大小数据集上的运行时间 (E) 和峰值内存 (F) 比较。

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | UMAP 显示 6 个 T 细胞亚群（CD4, CD8, Treg, MAIT, γδ T, 其他） | 各亚群在低维空间中形成不同聚类 |
| B | 5 个基因签名（CD4, CD8, Treg, MAIT, γδ T）在 UMAP 上的分数分布 | 每个签名在其对应亚群中显示出特异性富集 |
| C | UCell 评分：完整数据集 vs CD8 子集 → 分布完全一致（黑色与红色轮廓重叠） | ✅ **UCell 不受数据集组成影响** |
| D | AddModuleScore：完整数据集 vs CD8 子集 → 分布完全不同（中位数从 ~1 变为 ~0） | ❌ **AddModuleScore 高度依赖数据集组成** |
| E | 运行时间对比（1k → 100k 细胞） | UCell 约比 AUCell **快 3 倍** |
| F | 峰值内存对比（1k → 100k 细胞） | 100k 细胞时：UCell **5.5 GB** vs AUCell **>64 GB**（相差 10 倍以上） |

**📊 统计注释：** 时间/内存基准测试使用逐次增大的数据集；UCell 和 AUCell 使用相同的排名输入以保证公平比较

**🎯 核心结论：** UCell 同时实现了**更好的稳健性**（基于细胞内部排名，不受数据集组成干扰）和**更高的计算效率**（比 AUCell 快 3 倍、内存少 10 倍以上），是大型单细胞数据集基因签名评分的首选方法。

---

<a id="S009"></a>
**Original:** UCell is an R package for the evaluation of gene signature enrichment designed for scRNA-seq data. Given a gene expression matrix or Seurat object, and a list of gene sets, UCell calculates signature scores for each cell, for each gene set.

In the following illustrative example, we applied UCell to a single-cell multimodal dataset of human blood T cells, which were annotated by the authors using both gene (scRNA-seq) and cell surface marker expression (CITE-seq) (Fig. 1A). Provided a set of T cell subtype-specific genes (Table 1), UCell helps interpreting clusters in terms of signature enrichment in low-dimensional spaces such as the UMAP (Fig. 1B).

Importantly, UCell scores are based on the relative ranking of genes for individual cells, therefore they are robust to dataset composition. Evaluating a CD8 T cell signature on the full dataset or on CD8 T cells only, results in identical score distributions for CD8 T cells in the two settings (Fig. 1C). Conversely, AddModuleScore from Seurat normalizes its scores against the average expression of a control set of genes across the whole dataset, and is therefore dependent on dataset composition. CD8 T cells analyzed in isolation or in the context of the full T cell dataset are assigned highly different AddModuleScore scores, with median ~1 in the full dataset and median ~0 for the CD8 T cell subset (Fig. 1D).

Another widely-used method for single-cell signature scoring, AUCell, is also based on relative rankings and therefore has the same desirable property as UCell of reporting consistent scores regardless of dataset composition. Compared to AUCell, UCell is about three times faster (Fig. 1E) and uses significantly less memory (Fig. 1F). For example, AUCell requires over 64 GB of RAM to process 100,000 single-cells, while UCell uses only 5.5 GB of peak memory (Fig. 1F), making it suitable even for machines with limited computing power.

**中文:** UCell 是一个专为 scRNA-seq 数据设计的 R 包，用于评估基因签名富集。给定一个基因表达矩阵或 Seurat 对象以及一组基因集，UCell 即可为每个细胞、每个基因集计算签名分数。

在以下示例中，我们将 UCell 应用于人血液 T 细胞的单细胞多模态数据集（Hao et al.），该数据集的作者同时使用基因表达（scRNA-seq）和细胞表面标志物表达（CITE-seq）进行了注释（图 1A）。给定一组 T 细胞亚型特异性基因（表 1），UCell 帮助在 UMAP 等低维空间中以签名富集的形式解释聚类（图 1B）。

**关键在于：** UCell 分数基于单个细胞内基因的相对排名，因此对数据集组成具有稳健性。在全数据集上或在仅 CD8 T 细胞子集上评估 CD8 T 细胞签名，CD8 T 细胞在两种设置下的分数分布完全一致（图 1C）。相比之下，Seurat 的 AddModuleScore 将分数针对整个数据集上对照基因集的平均表达进行归一化，因此依赖于数据集组成。在孤立分析或在完整 T 数据集背景下分析的 CD8 T 细胞被分配了截然不同的 AddModuleScore（完整数据集的中位数约 1，CD8 子集的中位数约 0）（图 1D）。

另一种广泛使用的单细胞签名评分方法 AUCell 也基于相对排名，因此具有与 UCell 相同的理想特性——无论数据集组成如何都能产生一致的分数。与 AUCell 相比，UCell **快约 3 倍**（图 1E）且**内存使用显著更少**（图 1F）。例如，AUCell 需要超过 **64 GB** RAM 来处理 100,000 个单细胞，而 UCell 的峰值内存仅为 **5.5 GB**（图 1F），使其即使在计算能力有限的机器上也能适用。

---

<a id="T001"></a>
### Table 1. T 细胞亚型基因签名

**Source:** Results section

| T cell type | Gene set |
|-------------|----------|
| **CD4 T cell** | CD4, CD40LG |
| **CD8 T cell** | CD8A, CD8B |
| **Treg** | FOXP3, IL2RA |
| **MAIT** | KLRB1, SLC4A10, NCR3 |
| **γδ T cell** | TRDC, TRGC1, TRGC2, TRDV1 |

**中文表注:** 图 1 中使用的 T 细胞亚型基因签名

---

**🔬 表格解读**

- **行含义：** 5 种 T 细胞亚型，各对应一组标志基因签名
- **特征：** 每个签名由 2–4 个高度特异的基因组成，可用于区分 T 细胞亚型
- **实用价值：** 这些是简化的签名——实际应用中可能需要更全面的基因集以获得更高分辨率

---

## Code & Data Availability

**Original:** UCell is available as an R package at https://github.com/carmonalab/UCell, and is accompanied by vignettes for signature scoring and for seamless integration with Seurat pipelines. Source code to reproduce the results in this manuscript is available at the following repository: https://gitlab.unil.ch/carmona/UCell_demo.

**中文:** UCell 以 R 包形式在 https://github.com/carmonalab/UCell 上提供，并附有签名评分和与 Seurat 流程无缝整合的使用指南（vignettes）。复现本文结果的源代码可在 https://gitlab.unil.ch/carmona/UCell_demo 获取。

---

## Funding & CRediT / 基金与作者贡献

**Original:**
- **Funding:** Swiss National Science Foundation (SNF) Ambizione grant 180010 to SJC.
- **Massimo Andreatta:** Conceptualization, Methodology, Software, Formal analysis, Visualization, Writing
- **Santiago J. Carmona:** Conceptualization, Methodology, Software, Formal analysis, Writing, Funding acquisition

**中文:**
- **基金资助：** 瑞士国家科学基金会 Ambizione 资助（180010）给 SJC
- **Massimo Andreatta：** 概念化、方法论、软件、形式分析、可视化、撰写
- **Santiago J. Carmona：** 概念化、方法论、软件、形式分析、撰写、获取资助

---

## Key Terminology / 关键术语

| 英文 | 中文 | 说明 |
|------|------|------|
| Gene signature | 基因签名 | 一组代表特定生物学状态的基因 |
| Signature scoring | 签名评分 | 定量评估一个基因集在单个细胞中的活性 |
| Mann-Whitney U statistic | Mann-Whitney U 统计量 | 基于排名的非参数统计量 |
| Relative ranks | 相对排名 | 每个细胞内基因的表达排名（非跨细胞比较） |
| AddModuleScore | AddModuleScore | Seurat 的签名评分方法（基于分箱归一化） |
| AUCell | AUCell | SCENIC 中实现的 AUC 基于排名方法 |
| Dataset composition | 数据集组成 | 数据集中包含的细胞类型及其比例 |
| Robustness | 稳健性 | 结果不受外部因素（如数据集组成）影响 |

---

## 方法学总结

UCell 的核心创新非常简洁：

1. **按细胞排名** → 对每个细胞内的基因独立排序（避免跨细胞比较）
2. **截断尾部** → r_max = 1500（过滤低表达噪声基因）
3. **Mann-Whitney U** → 计算签名基因在排名中的位置是否显著偏前
4. **归一化** → 将分数映射到 [0,1] 区间（1 = 完全富集）

**与 Seurat AddModuleScore 的本质区别：**
- AddModuleScore 将基因按全局平均表达分箱，再用对照集校正 → 依赖数据集组成
- UCell 仅看每个细胞内签名基因的相对排名 → 不依赖数据集组成

**与 AUCell 的区别：**
- 算法理念相同（都基于排名/AUC）
- UCell 实现更高效：`data.table::frank` + 自动批处理 + `future` 并行 → **3 倍速度、10 倍内存优势**

---

*Generated on 2026-05-16. Bilingual reading artifact for Andreatta & Carmona, CSBJ 2021.*
