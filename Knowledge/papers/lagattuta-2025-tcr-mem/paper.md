---
title: "The T cell receptor sequence influences the likelihood of T cell memory formation"
title_cn: "T细胞受体序列影响T细胞记忆形成的可能性"
authors: "Kaitlyn A. Lagattuta, Ayano C. Kohlgruber, Nouran S. Abdelfattah, Aparna Nathan, Laurie Rumker, Michael E. Birnbaum, Stephen J. Elledge, Soumya Raychaudhuri"
journal: "Cell Reports, 2025 Jan 28;44(1):115098"
doi: "10.1016/j.celrep.2024.115098"
pmcid: "PMC11785489"
pmid: "39731734"
source_url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11785489/"
created: "2026-05-25"
type: "bilingual-reader"
tags: [TCR, T-cell-memory, rCCA, Atchley-factors, single-cell, TCR-mem, thymic-selection]
---

# The T cell receptor sequence influences the likelihood of T cell memory formation
# T细胞受体序列影响T细胞记忆形成的可能性

**期刊:** Cell Reports | **发表:** 2025-01-28 | **PMC:** PMC11785489 | **PMID:** 39731734

---

## 目录 | Index

1. [[#摘要 | Abstract]]
2. [[#引言 | INTRODUCTION]]
3. [[#结果 | RESULTS]]
   - 3.1 [[#T细胞转录状态注释 | T cell transcriptional state annotation]]
   - 3.2 [[#不同个体中相同TCR序列的转录命运匹配 | Transcriptional fate matching between T cells with the same TCR sequence from different individuals]]
   - 3.3 [[#揭示引导T细胞命运的TCR序列特征的多维方法 | A multidimensional approach to uncover TCR sequence features that guide T cell fate]]
   - 3.4 [[#rCCA识别出四种受TCR序列影响的T细胞命运 | rCCA identifies four T cell fates informed by TCR sequence]]
   - 3.5 [[#TCR评分函数量化告知T细胞命运的TCR序列特征 | TCR scoring functions quantify TCR sequence features that inform T cell fate]]
   - 3.6 [[#TCR评分函数在不同个体间普遍适用 | TCR scoring functions generalize across individuals]]
   - 3.7 [[#替代TCR评分方案 | Alternative TCR scoring schemes]]
   - 3.8 [[#V(D)J重排的未翻译产物不影响T细胞命运 | Untranslated products of V(D)J recombination do not affect T cell fate]]
   - 3.9 [[#TCR-mem预测抗原特异性群体内更强的T细胞激活 | TCR-mem predicts increased T cell activation within antigen-specific populations]]
   - 3.10 [[#TCR-mem与抗原结合亲和力不同 | TCR-mem is distinct from antigen binding affinity]]
   - 3.11 [[#胸腺选择压力在外周持续存在 | Thymic selection pressures on the TCR sequence continue in the periphery]]
4. [[#讨论 | DISCUSSION]]
5. [[#研究的局限性 | Limitations of the study]]
6. [[#数据与代码可用性 | Data and code availability]]
7. [[#图表示 | Figures and Tables]]

---

<a id="S001"></a>
## 摘要 | Summary

**Source:** p.1 Summary

**Original:**
The amino acid sequence of the T cell receptor (TCR) varies between T cells of an individual's immune system. Particular TCR residues nearly guarantee mucosal-associated invariant T (MAIT) and natural killer T (NKT) cell transcriptional fates. To define how the TCR sequence affects T cell fates, we analyze the paired αβTCR sequence and transcriptome of 961,531 single cells. We find that hydrophobic complementarity-determining region (CDR)3 residues promote regulatory T cell fates in both the CD8 and CD4 lineages. Most strikingly, we find a set of TCR sequence features that promote the T cell transition from naive to memory. We quantify the extent of these features through our TCR scoring function "TCR-mem." Using TCR transduction experiments, we demonstrate that increased TCR-mem promotes T cell activation, even among T cells that recognize the same antigen. Our results reveal a common set of TCR sequence features that enable T cell activation and immunological memory.

**中文:**
T细胞受体（TCR）的氨基酸序列在个体免疫系统的不同T细胞之间各不相同。特定的TCR残基几乎可以保证黏膜相关不变T（MAIT）细胞和自然杀伤T（NKT）细胞的转录命运。为了定义TCR序列如何影响T细胞命运，我们分析了961,531个单细胞的配对αβTCR序列和转录组。我们发现疏水性互补决定区（CDR）3残基在CD8和CD4两个谱系中都促进了调节性T细胞命运。最引人注目的是，我们发现了一组促进T细胞从初始状态向记忆状态转化的TCR序列特征。我们通过TCR评分函数"TCR-mem"来量化这些特征的程度。通过TCR转导实验，我们证明即使识别相同抗原的T细胞中，较高的TCR-mem也能促进T细胞激活。我们的结果揭示了一组通用的TCR序列特征，这些特征能够促进T细胞激活和免疫记忆。

---

<a id="S002"></a>
## 引言 | INTRODUCTION

**Source:** p.1 Introduction

**Original:**
T cells are critical lymphocytes of the adaptive immune system. Early in T cell development, stochastic genome rearrangement on chromosomes 7 and 14 defines each T cell with its own T cell receptor (TCR).¹ In the thymus and periphery, T cell differentiation depends critically on TCR activation.²⁻⁸ One prominent example is the PLZF^high, innate-like transcriptional fate, which is nearly guaranteed when V(D)J recombination selects TRAV1-2 and TRAJ33, TRAJ20, or TRAJ12.⁹

Given the central role of the TCR in T cell activation and differentiation, we¹⁰ and others¹¹⁻¹⁶ have identified differences in TCR sequences (e.g., hydrophobicity, V gene selection) using bulk sequencing of flow-sorted T cell populations. However, bulk sequencing obscures the pairing of TCR α and β chains. Furthermore, flow sorting requires predefining T cell states for investigation and may miss important transcriptional heterogeneity of T cells.

Now, single-cell sequencing assays enable joint profiling of the TCR and transcriptome. In contrast to bulk sequencing methods, single-cell technology anchors α and β TCR reads to individual cells, allowing reconstruction of the full TCR α/β heterodimer. Moreover, genome-wide transcriptional analysis can comprehensively define T cell states. Early methods to jointly analyze TCR and transcriptional data¹⁷,¹⁸ have suggested that TCR sequence similarity may correspond to similarity in transcriptional state.

To statistically define the relationship between the TCR sequence and T cell state, we analyze 961,531 T cells with quality-controlled αβTCR and transcriptional profiling at single-cell resolution from seven published datasets (Table 1). Rather than pre-specifying transcriptional states, we use paired dimensionality reduction to uncover relevant transcriptional states in an unbiased fashion. Our results define four TCR scoring functions that quantify the transcriptional fate predisposition conferred by the TCR. We apply these scoring functions to better understand thymic selection as well as cell state variation within antigen-specific T cell populations.

**中文:**
T细胞是适应性免疫系统中关键的淋巴细胞。在T细胞发育早期，7号和14号染色体上的随机基因组重排使每个T细胞拥有其独特的T细胞受体（TCR）¹。在胸腺和外周，T细胞分化关键依赖于TCR激活²⁻⁸。一个显著的例子是PLZF^high先天样转录命运——当V(D)J重组选择了TRAV1-2和TRAJ33、TRAJ20或TRAJ12时，这一命运几乎必然发生⁹。

鉴于TCR在T细胞激活和分化中的核心作用，我们¹⁰及其他研究者¹¹⁻¹⁶已经通过流式分选T细胞群体的批量测序，识别出了TCR序列的差异（如疏水性、V基因选择）。然而，批量测序模糊了TCR α链和β链的配对关系。此外，流式分选需要预先定义待研究的T细胞状态，可能会遗漏T细胞重要的转录异质性。

如今，单细胞测序技术使得TCR和转录组的联合分析成为可能。与批量测序方法不同，单细胞技术将α链和β链TCR读数锚定到单个细胞，从而能够重建完整的TCR α/β异二聚体。此外，全基因组转录分析可以全面定义T细胞状态。早期联合分析TCR和转录数据的方法¹⁷,¹⁸提示，TCR序列的相似性可能对应转录状态的相似性。

为了统计学地定义TCR序列与T细胞状态之间的关系，我们分析了来自七个已发表数据集的961,531个经质量控制的αβTCR和单细胞分辨率转录谱（表1）。我们没有预先指定转录状态，而是使用配对降维方法以无偏方式发现相关的转录状态。我们的结果定义了四个TCR评分函数，量化TCR赋予的转录命运倾向。我们应用这些评分函数来更好地理解胸腺选择以及抗原特异性T细胞群体内的细胞状态变异。

---

<a id="S003"></a>
## 结果 | RESULTS

### T细胞转录状态注释 | T cell transcriptional state annotation

**Source:** p.2 Results

**Original:**
To construct an accurately annotated reference of T cells, we used dataset 1 (from the COMBAT consortium¹⁹; Table 1) with 371,621 T cells from 122 individuals with multimodal TotalSeq profiling of mRNA and surface proteins. We clustered the cells in two ways: first, agnostic to protein expression (clusters A1–A9; Figures 1A and S1), and second, incorporating traditional surface markers via a linear multimodal strategy²⁶,²⁷ (clusters B1–B9; Figure S2). Cluster A9, representing the PLZF^high innate-like T cell state, accounted for nearly all canonical mucosal-associated invariant T (MAIT) or natural killer T (NKT) TCRs (Figures 1B and 1C). Clusters B1–B9 delineated CD4, CD8, central memory (CM), and effector memory (EM) states based on a curated list of 10 surface proteins, including CD45RO and CD45RA (Figure S2; STAR Methods). To standardize cell state definitions across datasets, we projected all additional datasets (Table 1) into these two embeddings and transferred annotations via k-nearest-neighbors classification (k = 5; STAR Methods).

**中文:**
为构建精确注释的T细胞参考图谱，我们使用了数据集1（来自COMBAT联合体¹⁹；表1），包含来自122个个体的371,621个T细胞，具有mRNA和表面蛋白的多模态TotalSeq谱。我们以两种方式对细胞进行聚类：第一，不依赖蛋白表达（簇A1–A9；图1A和图S1）；第二，通过线性多模态策略²⁶,²⁷整合传统表面标志物（簇B1–B9；图S2）。簇A9代表PLZF^high先天样T细胞状态，几乎包含了所有经典的黏膜相关不变T（MAIT）或自然杀伤T（NKT）TCR（图1B和1C）。簇B1–B9基于包括CD45RO和CD45RA在内的10种表面蛋白的精选列表，区分了CD4、CD8、中央记忆（CM）和效应记忆（EM）状态（图S2；STAR Methods）。为标准化跨数据集的细胞状态定义，我们将所有其他数据集（表1）投影到这两个嵌入空间中，并通过k近邻分类（k = 5；STAR Methods）转移注释。

---

<a id="S004"></a>
### 不同个体中相同TCR序列的转录命运匹配 | Transcriptional fate matching between T cells with the same TCR sequence from different individuals

**Source:** p.2-3 Results

**Original:**
We first used dataset 1 (Table 1) to assess whether perfect TCR sequence matching raised the likelihood of T cell state matching. Within an individual, identical TCR sequences likely reflect an expanded T cell clone, comprised of cells that tend to be transcriptionally similar. To avoid clonally related cells, we focused on identical TCR sequences sampled from two different individuals. We identified 115 pairs of "TCR twins": two T cells from two different individuals with the same TCR α and β amino acid sequences (Figure 1D; STAR Methods). To test the general relationship between the TCR sequence and T cell state, we asked whether the transcriptional states of TCR twins were concordant more often than expected by chance.

Under the null, we would expect 25 (of 115) transcriptionally concordant TCR-twin pairs (see STAR Methods). Instead, we observed 80 (p = 6.1 × 10⁻²⁸, exact binomial test, Figure 1E; STAR Methods). To assess if this enrichment was explained by MHC(-like) restriction, we repeated our analysis with MAIT cell and NKT cell TCRs removed and observed an enrichment in concordant states (p = 2.3 × 10⁻²¹, exact binomial test). Partitioning into CD4⁺ and CD8⁺ populations did not obviate enrichment either (p = 4.0 × 10⁻⁹, p = 0.00018, exact binomial test). Recognizing that SARS-CoV-2 infection is a potential confound, we filtered to individuals that were PCR negative for SARS-CoV-2 but continued to observe enrichment (13 matches versus 6 expected by chance, p = 0.00048; 11 matches versus 6 expected by chance, p = 0.00138). To account for shared HLA alleles, we repeated this analysis in an HLA-genotyped dataset²⁵ and continued to observe enrichment regardless of whether the TCR twins were sampled from individuals with a shared HLA allele (p = 2.9 × 10⁻¹⁰¹, exact binomial test). These results suggest a consistent influence of TCR sequence on T cell fate in unrelated individuals.

This analysis is limited to TCRs found in more than one individual ("public TCRs"), which comprise <0.01% of the TCRs in this cohort. Public TCRs have distinct structural features²⁸ and could demonstrate transcriptional state matching due to recognition of common antigens. We hypothesized, however, that these results were driven to some extent by the distinct biophysical features of the TCR sequences. If so, similar, but not identical, TCR sequences would also promote similar T cell fates.

**中文:**
我们首先使用数据集1（表1）来评估完全相同的TCR序列是否提高了T细胞状态匹配的可能性。在个体内，相同的TCR序列可能反映了扩增的T细胞克隆，这些细胞倾向于转录相似。为避免克隆相关细胞，我们重点关注来自两个不同个体的相同TCR序列。我们识别出115对"TCR双胞胎"：来自两个不同个体的两个T细胞，具有相同的TCR α和β链氨基酸序列（图1D；STAR Methods）。为检验TCR序列与T细胞状态之间的一般关系，我们询问TCR双胞胎的转录状态是否比随机预期更频繁地一致。

在原假设下，我们预期115对中有25对转录一致的TCR双胞胎（见STAR Methods）。然而，我们观察到了80对（p = 6.1 × 10⁻²⁸，精确二项检验，图1E；STAR Methods）。为评估这种富集是否由MHC（样）限制所解释，我们在排除MAIT细胞和NKT细胞TCR后重复分析，仍观察到一致状态的富集（p = 2.3 × 10⁻²¹，精确二项检验）。将细胞分为CD4⁺和CD8⁺群体也未消除富集（p = 4.0 × 10⁻⁹, p = 0.00018，精确二项检验）。考虑到SARS-CoV-2感染是潜在的混杂因素，我们将分析限制在PCR阴性的个体，但继续观察到富集（观察到13对一致而预期6对，p = 0.00048；11对一致而预期6对，p = 0.00138）。为解释共享HLA等位基因的影响，我们在HLA基因分型数据集²⁵中重复分析，无论TCR双胞胎是否来自共享HLA等位基因的个体，都继续观察到富集（p = 2.9 × 10⁻¹⁰¹，精确二项检验）。这些结果表明，在无关个体中，TCR序列对T细胞命运存在一致的影响。

该分析仅限于在多个个体中发现的TCR（"公共TCR"），它们占该队列TCR的不到0.01%。公共TCR具有独特的结构特征²⁸，可能由于识别共同抗原而表现出转录状态的匹配。然而，我们假设这些结果在一定程度上是由TCR序列独特的生物物理特征驱动的。如果是这样，相似但不相同的TCR序列也会促进相似的T细胞命运。

---

<a id="S005"></a>
### 揭示引导T细胞命运的TCR序列特征的多维方法 | A multidimensional approach to uncover TCR sequence features that guide T cell fate

**Source:** p.3 Results

**Original:**
To extend our study to private TCRs, we converted each TCR sequence into a vector of biophysical features. Consistent with other numerical representations of the TCR,¹⁷,²⁹ we translated each amino acid residue in both the α and β chains of the TCR into five Atchley factors.³⁰ These factors correspond to hydrophobicity, size, charge, secondary structure, and heat capacity. Applying this to α and β complementarity-determining and framework regions of the TCR yielded 1190 biophysical features. Excluding invariant positions and framework regions and adding interaction terms between adjacent residues yielded 1,250 TCR features (Figures 2A and 2B; Table S2; STAR Methods).

We aimed to identify TCR sequence effects on T cell state in an unbiased fashion, without restricting to preselected cell states. To find generalizable associations, we combined dataset 1 with a second published dataset (dataset 2, Table 1; STAR Methods), resulting in 494,419 quality-controlled T cells from 256 individuals. We applied regularized canonical correlation analysis (rCCA) (STAR Methods). Each axis identified by rCCA denotes a weighted sum of gene expression PC scores (a transcriptional state) that correlates with a weighted sum of TCR sequence features. We mitigated technical confounding in our rCCA implementation. First, to prevent confounding by variable clone size, we selected one cell at random to represent each clone. We confirmed that results were invariant to the specific set of cells sampled (STAR Methods). To mitigate overfitting, we added a ridge regularization to the covariance matrix for each of the inputs to rCCA, using 5-fold cross-validation to tune both lambda penalty values. To assess overfitting, we randomly assigned 68 donors to a validation test set, such that ~30% of clones (29.3%) were held out from training.

**中文:**
为将研究扩展到私有TCR，我们将每个TCR序列转换为生物物理特征向量。与其他TCR数值表示方法一致¹⁷,²⁹，我们将TCR α链和β链的每个氨基酸残基翻译为五个Atchley因子³⁰。这些因子对应疏水性、大小、电荷、二级结构和热容量。将该方法应用于TCR的α和β互补决定区和框架区，产生了1,190个生物物理特征。排除不变位点和框架区，并加入相邻残基之间的相互作用项后，得到了1,250个TCR特征（图2A和2B；表S2；STAR Methods）。

我们旨在以无偏方式识别TCR序列对T细胞状态的影响，不局限于预先选择的细胞状态。为发现可推广的关联，我们将数据集1与第二个已发表数据集（数据集2，表1；STAR Methods）合并，得到来自256个个体的494,419个经质量控制的T细胞。我们应用了正则化典型相关分析（rCCA）（STAR Methods）。rCCA识别的每个轴代表基因表达PC分数（一种转录状态）的加权和，该加权和与TCR序列特征的加权和相互关联。我们在rCCA实施中减轻了技术混杂因素。首先，为防止可变克隆大小的混杂，我们随机选择一个细胞代表每个克隆。我们确认结果对所采样的特定细胞集是不变的（STAR Methods）。为减轻过拟合，我们对rCCA的每个输入协方差矩阵添加了岭正则化，使用5折交叉验证调整两个lambda惩罚值。为评估过拟合，我们将68名供者随机分配到验证测试集，使得约30%的克隆（29.3%）被保留不参与训练。

---

<a id="S006"></a>
### rCCA识别出四种受TCR序列影响的T细胞命运 | rCCA identifies four T cell fates informed by TCR sequence

**Source:** p.4 Results

**Original:**
We observed canonical correlations between the TCR sequence and T cell state descending from R = 0.54. To assess the statistical significance of each canonical correlation, we permuted our data 1,000 times and re-applied rCCA (STAR Methods). We observed empirical p values <0.001 for both training and held-out testing data for the first four canonical variates (CVs) (Figure 2C).

To interpret the four continuous T cell states identified by rCCA, we examined CVs 1–4 in terms of cell scores and expression correlates (Figures 2D–2H; Table S3; STAR Methods). Cells scoring the highest on CV1 localized to transcriptional cluster A9 (Figures 2E and S3A), the innate-like, PLZF^high transcriptional fate for canonical MAIT and NKT cell TCRs (Figures 1B and 1C). CV2 tracked closely with CD8 versus CD4 surface expression, delineating CD4⁺ T versus CD8⁺ T populations (Figures 2F and S3B–S3D). These results point to families of peptide presentation molecules as the primary source of covariation between the TCR sequence and T cell state. Indeed, it is well established that unconventional (MR1, CD1d), MHC class I, and MHC class II families each prefer biophysically distinct αβTCR sequences.⁹,¹³,¹⁴,³¹⁻³⁵

In addition to these known relationships, rCCA proposed previously unknown connections between the TCR sequence and T cell state. CV3 highlighted TCR sequence similarity between FOXP3-expressing CD4⁺ regulatory T (Treg) cells and KIR⁺HELIOS⁺ CD8 T cells (Figures 2G and S3E–S3K), which have recently been described as human CD8⁺ Treg cells.³⁶ This suggests that the same TCR sequence features may promote suppressive functional states in both the CD4 and CD8 compartments. Most strikingly, CV4 appeared to capture TCR sequence differences between naive and memory T cells (Figures 2H and S3L). Surface protein measurements indicated that both EM and CM CD4⁺ and CD8⁺ T cells scored highly on CV4 (Figures S3M and S3N). This raises the intriguing possibility that some sequence features render the TCR more generally prone to activation.

**中文:**
我们观察到TCR序列与T细胞状态之间的典型相关性从R = 0.54开始递减。为评估每个典型相关性的统计显著性，我们将数据进行了1,000次置换并重新应用rCCA（STAR Methods）。我们观察到前四个典型变量（CV）在训练和保留测试数据中的经验p值均<0.001（图2C）。

为解释rCCA识别的四个连续T细胞状态，我们检查了CV 1–4的细胞分数和表达相关性（图2D–2H；表S3；STAR Methods）。CV1得分最高的细胞定位于转录簇A9（图2E和S3A），即经典MAIT和NKT细胞TCR的先天样PLZF^high转录命运（图1B和1C）。CV2与CD8对CD4表面表达密切相关，区分了CD4⁺ T和CD8⁺ T群体（图2F和S3B–S3D）。这些结果表明肽呈递分子家族是TCR序列与T细胞状态之间共变的主要来源。事实上，非常规（MR1、CD1d）、MHC I类和MHC II类家族各自偏好生物物理特征不同的αβTCR序列这一点已有充分证据⁹,¹³,¹⁴,³¹⁻³⁵。

除了这些已知的关系外，rCCA还提出了TCR序列与T细胞状态之间先前未知的联系。CV3突出了表达FOXP3的CD4⁺调节性T（Treg）细胞与KIR⁺HELIOS⁺ CD8 T细胞之间的TCR序列相似性（图2G和S3E–S3K），这些CD8 T细胞最近被描述为人类CD8⁺ Treg细胞³⁶。这表明相同的TCR序列特征可能在CD4和CD8两个区室中都促进抑制性功能状态。最引人注目的是，CV4似乎捕捉到了初始T细胞与记忆T细胞之间的TCR序列差异（图2H和S3L）。表面蛋白测量表明，效应记忆和中央记忆的CD4⁺及CD8⁺ T细胞在CV4上均得分较高（图S3M和S3N）。这提出了一个有趣的可能性：某些序列特征使TCR更倾向于普遍激活。

---

<a id="S007"></a>
### TCR评分函数量化告知T细胞命运的TCR序列特征 | TCR scoring functions quantify TCR sequence features that inform T cell fate

**Source:** p.4-5 Results

**Original:**
The continuous T cell states defined by rCCA nominated four contrasts in T cell state for further study: PLZF^high versus other, CD8T versus CD4T, regulatory T (Treg) versus conventional T (Tconv), and memory versus naive. For each of these recognizable T cell fate decisions, we used logistic regression on the same observations from datasets 1 and 2 to learn a more precise predictive weighting scheme on the 1,250 TCR sequence features (Table S2; STAR Methods). As a secondary analysis, we trained separately on COVID-positive and COVID-negative samples and verified that these predictive weighting schemes were robust to infection status (Figures S4A and S4B). We named each predictive weighting scheme, or TCR scoring function, by the T cell state of interest: "TCR-innate" to predict the innate-like, PLZF^high state, "TCR-CD8" to predict the CD8⁺ state, "TCR-reg" to predict the Treg cell state, and "TCR-mem" to predict the memory state.

To interpret each of these TCR scoring functions, we examined relative contributions from each complementarity-determining region (CDR) and amino acid residue (Figures 2I–2P and S4C–S4F; STAR Methods). TCR-innate was characterized by critical amino acids in CDR2α, reflecting TRAV gene selection (Figure S4C). As expected from previous studies,¹³,¹⁴ TCR-CD8-high sequences were depleted for positive charge in the junctional mid-region of CDR3 (Figure 2N). TCR-reg reflected increased hydrophobic CDR3β residues in CD4 Treg cells, consistent with previous reports.¹⁰,¹² Paired αβ TCR sequencing data revealed that enrichment for hydrophobic amino acids extended to CDR3α (Figure 2O). For TCR-mem, feature dependence analysis highlighted the importance of CDR3α and CDR3β (Figure 2L). We assessed TCR-reg and TCR-mem separately in CD4⁺ and CD8⁺ T cells and observed that these TCR scoring functions were equally applicable to both lineages (Figures S4G and S4H; STAR Methods).

**中文:**
rCCA定义的连续T细胞状态提名了四个有待进一步研究的T细胞状态对比：PLZF^高表达对其他、CD8T对CD4T、调节性T（Treg）对常规T（Tconv）、以及记忆对初始。对于每个可识别的T细胞命运决策，我们在来自数据集1和2的相同观察上使用逻辑回归，学习1,250个TCR序列特征上更精确的预测加权方案（表S2；STAR Methods）。作为辅助分析，我们分别在COVID阳性和COVID阴性样本上训练，验证了这些预测加权方案对感染状态的稳健性（图S4A和S4B）。我们根据目标T细胞状态命名每个预测加权方案（即TCR评分函数）："TCR-innate"预测先天样PLZF^高表达状态，"TCR-CD8"预测CD8⁺状态，"TCR-reg"预测Treg细胞状态，"TCR-mem"预测记忆状态。

为解释每个TCR评分函数，我们检查了每个互补决定区（CDR）和氨基酸残基的相对贡献（图2I–2P和S4C–S4F；STAR Methods）。TCR-innate的特征是CDR2α中的关键氨基酸，反映了TRAV基因的选择（图S4C）。与先前研究¹³,¹⁴预期一致，TCR-CD8高表达的序列在CDR3的连接中部区域正电荷减少（图2N）。TCR-reg反映了CD4 Treg细胞中CDR3β疏水性残基的增加，与先前报道一致¹⁰,¹²。配对的αβ TCR测序数据揭示疏水性氨基酸的富集延伸到了CDR3α（图2O）。对于TCR-mem，特征依赖性分析突出了CDR3α和CDR3β的重要性（图2L）。我们分别在CD4⁺和CD8⁺ T细胞中评估了TCR-reg和TCR-mem，观察到这些TCR评分函数对两个谱系同样适用（图S4G和S4H；STAR Methods）。

---

<a id="S008"></a>
### TCR评分函数在不同个体间普遍适用 | TCR scoring functions generalize across individuals

**Source:** p.5-6 Results

**Original:**
We considered the possibility that the associations between the TCR sequence and T cell state were driven by a subset of individuals. We first stratified each dataset by clinical status (COVID, sepsis, influenza, none of the above) and used mixed-effects logistic regression to calculate β_TCRscore, the association between the TCR score calculated based on both α and β chains, and the target T cell state (β_TCRscore = log odds ratio [OR] per standard deviation increase in TCR score; see STAR Methods). In each clinical stratum, we observed a statistically significant positive association for each TCR scoring function (24 tests, maximum p = 0.001; Figures 3A–3D; Table S4). Reassured that our TCR scoring functions were not driven by the clinical subset, we considered the possibility of an unknown individual-level mediator, such as HLA genotype. We computed β_TCR-innate, β_TCR-CD8, β_TCR-reg, and β_TCR-mem within each individual's T cells separately and estimated the proportion of individuals for whom our TCR score does not raise the odds of its target T cell state (the local false sign rate³⁷). Random effects meta-analysis indicated a near-zero proportion for each of our four TCR scoring functions (<1 × 10⁻⁶; Figures S4I–S4L; STAR Methods). We concluded that since our TCR scoring functions were robust to inter-individual variation, they should generalize to unseen samples.

We next applied our TCR scoring functions to data outside of our training set. In the 30% of dataset 1 and dataset 2 T cell clones held out from training, we observed replication of each TCR scoring function (Figures 3E–3H; STAR Methods). In an external dataset of peripheral blood T cells (dataset 3, Table 1), we observed a consistent and statistically significant increase in the odds of the T cell state of interest for each TCR scoring function (Figures 3I–3P; Table S4). Compared to T cells in the lowest TCR-mem decile, T cells in the highest TCR-mem decile had a 66% greater odds of being observed in a memory state (OR = 1.66, 95% CI = [1.57–1.76], p = 3.5 × 10⁻⁶⁸; Table S4). These results indicate a substantial role for TCR-mem in shaping the odds of T cell memory formation.

**中文:**
我们考虑了TCR序列与T细胞状态之间的关联可能由部分个体驱动的可能性。我们首先根据临床状态（COVID、脓毒症、流感、其他）对每个数据集进行分层，并使用混合效应逻辑回归计算β_TCRscore——即基于α和β链计算的TCR评分与目标T细胞状态之间的关联（β_TCRscore = 每增加一个标准差TCR评分的对数比值比[OR]；见STAR Methods）。在每个临床分层中，我们观察到每个TCR评分函数均存在统计学显著的正向关联（24项检验，最大p = 0.001；图3A–3D；表S4）。在确认我们的TCR评分函数并非由临床亚组驱动后，我们考虑了未知的个体水平中介因素的可能性，如HLA基因型。我们分别计算了每个个体T细胞内部的β_TCR-innate、β_TCR-CD8、β_TCR-reg和β_TCR-mem，并估计了我们的TCR评分不提高其目标T细胞状态几率的个体比例（局部假符号率³⁷）。随机效应荟萃分析表明，我们四个TCR评分函数的这一比例均接近零（<1 × 10⁻⁶；图S4I–S4L；STAR Methods）。我们得出结论：由于我们的TCR评分函数对个体间变异具有稳健性，它们应该能推广到未见过的样本。

接下来，我们将TCR评分函数应用于训练集之外的数据。在保留不参与训练的数据集1和数据集2的30% T细胞克隆中，我们观察到每个TCR评分函数的可重复性（图3E–3H；STAR Methods）。在外周血T细胞的外部验证数据集（数据集3，表1）中，我们观察到每个TCR评分函数的目标T细胞状态的几率一致且统计学显著地增加（图3I–3P；表S4）。与最低TCR-mem十分位数的T细胞相比，最高TCR-mem十分位数的T细胞处于记忆状态的几率高出66%（OR = 1.66，95% CI = [1.57–1.76]，p = 3.5 × 10⁻⁶⁸；表S4）。这些结果表明TCR-mem在塑造T细胞记忆形成几率方面具有重要作用。

---

<a id="S009"></a>
### 替代TCR评分方案 | Alternative TCR scoring schemes

**Source:** p.6-7 Results

**Original:**
We next benchmarked our TCR scoring functions against existing TCR metrics. We previously developed a Treg cell TCR scoring function, "TiRP," using the TCR β chain alone.¹⁰ With the additional information of the α chain, TCR-reg clearly outperformed TiRP (β_TiRP = 0.14, 95% CI = [0.10–0.18]; β_TCR-reg = 0.29, 95% CI = [0.25–0.32]; dataset 3 CD4T cells). Amino acid interaction strength³⁸ (AAIS) has been postulated to estimate a TCR's average affinity to peptide-MHC (pMHC),³⁹ but this has not been directly tested. In dataset 3, increasing AAIS corresponded to an increase in the odds of memory state only when applied to CDR3 amino acids (β_AAIS = 0.02, 95% CI = [0.003–0.03], p = 0.008). The effect size for AAIS was minimal compared to TCR-mem (β_TCR-mem = 0.14, 95% CI = [0.12–0.15]), however. Including AAIS as a covariate did not substantially change the estimated effect size of TCR-mem (conditional β_TCR-mem = 0.14, 95% CI = [0.12–0.15], heterogeneity p = 0.92). TCR-reg and TCR-mem clearly outperform these alternative TCR scoring functions by capturing both α and β TCR sequence features that promote recognition in the context of the TCR-pMHC interface.

We next wanted to assess if more complex models would provide better TCR scoring functions. For each of the four T cell states of interest, we trained a convolutional neural network (CNN) to detect possibly nonlinear associations between TCR amino acid motifs and T cell fate (STAR Methods). However, this deep learning approach provided no substantial benefit in discovery or external validation data (Figure S5; Table S6).

**中文:**
接下来，我们将我们的TCR评分函数与现有的TCR指标进行了基准比较。我们之前仅使用TCR β链开发了一个Treg细胞TCR评分函数"TiRP"¹⁰。有了α链的额外信息，TCR-reg明显优于TiRP（β_TiRP = 0.14，95% CI = [0.10–0.18]；β_TCR-reg = 0.29，95% CI = [0.25–0.32]；数据集3 CD4T细胞）。氨基酸相互作用强度³⁸（AAIS）被推测能估计TCR对肽-MHC（pMHC）的平均亲和力³⁹，但这一点尚未被直接验证。在数据集3中，AAIS增加仅在应用于CDR3氨基酸时才对应于记忆状态几率的增加（β_AAIS = 0.02，95% CI = [0.003–0.03]，p = 0.008）。然而，与TCR-mem相比，AAIS的效应量极小（β_TCR-mem = 0.14，95% CI = [0.12–0.15]）。将AAIS作为协变量纳入并未实质性地改变TCR-mem的估计效应量（条件β_TCR-mem = 0.14，95% CI = [0.12–0.15]，异质性p = 0.92）。TCR-reg和TCR-mem通过捕获在TCR-pMHC界面促进识别的α和β链TCR序列特征，明显优于这些替代TCR评分函数。

我们接下来想要评估更复杂的模型是否能提供更好的TCR评分函数。对于四个目标T细胞状态中的每一个，我们训练了一个卷积神经网络（CNN）来检测TCR氨基酸基序与T细胞命运之间可能的非线性关联（STAR Methods）。然而，这种深度学习方法的发现在发现数据集或外部验证数据中并没有带来实质性的提升（图S5；表S6）。

---

<a id="S010"></a>
### V(D)J重排的未翻译产物不影响T细胞命运 | Untranslated products of V(D)J recombination do not affect T cell fate

**Source:** p.7 Results

**Original:**
Because stochastic V(D)J recombination precedes T cell fate decisions, TCR sequence associations to T cell state likely reflect causal effects of V(D)J recombination. However, a causal pathway that begins with V(D)J recombination and ends with the T cell state likely includes several important biological mediators. To better understand these mediators, we decomposed V(D)J recombination into three products: (1) DNA-level excisions and insertions, (2) amino acid changes in the surface TCR, and (3) antigen recognition. To isolate (1) from (2), we analyzed nonproductive V(D)J recombination sequences that are not translated into surface TCR proteins. Then, to distinguish (3) from (2), we examined the TCR sequences and T cell states of antigen-labeled single cells.

Nonproductive TCR sequence transcripts can be detected when an out-of-frame V(D)J recombination event on one chromosome is followed by an in-frame V(D)J recombination event on the other.⁴⁰ Due to stop codons and frameshift errors, these nonproductive TCRs represent V(D)J genome rearrangements that are not translated into surface antigen receptors.⁴¹ To assess whether these DNA-level changes are sufficient to produce the observed effects on T cell state, we applied our TCR scoring functions to nonproductive TCR sequences (dataset 4, Table 1). We observed no evidence of association for any of the four TCR scoring functions (p > 0.05). Down-sampling did not obviate associations for productive TCRs, confirming that the lack of association was not due to reduced statistical power (Table S4; STAR Methods). We concluded that the DNA-level excisions and insertions from V(D)J recombination are, in general, not sufficient to affect T cell state; recombination products must be expressed at the protein level.

**中文:**
由于随机V(D)J重组发生在T细胞命运决定之前，TCR序列与T细胞状态的关联可能反映了V(D)J重组的因果效应。然而，从V(D)J重组开始到T细胞状态结束的因果通路可能包含几个重要的生物学中介因素。为更好地理解这些中介因素，我们将V(D)J重组分解为三个产物：（1）DNA水平的切除和插入，（2）表面TCR中的氨基酸变化，以及（3）抗原识别。为将（1）与（2）区分开，我们分析了不翻译为表面TCR蛋白的非生产性V(D)J重组序列。然后，为区分（3）与（2），我们检查了抗原标记单细胞的TCR序列和T细胞状态。

当一条染色体上的移码V(D)J重组事件后跟另一条染色体上的框内V(D)J重组事件时，可以检测到非生产性TCR序列转录本⁴⁰。由于终止密码子和移码错误，这些非生产性TCR代表了不翻译为表面抗原受体的V(D)J基因组重排⁴¹。为评估这些DNA水平的变化是否足以产生观察到的对T细胞状态的影响，我们将TCR评分函数应用于非生产性TCR序列（数据集4，表1）。我们没有观察到四种TCR评分函数中的任何一个存在关联证据（p > 0.05）。降采样并未消除生产性TCR的关联，确认了缺乏关联并非由于统计功效降低（表S4；STAR Methods）。我们得出结论：来自V(D)J重组的DNA水平切除和插入通常不足以影响T细胞状态——重组产物必须在蛋白质水平表达。

**解析 | Analysis**

**核心问题：** TCR 序列与 T 细胞命运的关联是源于 DNA 重排本身，还是源于表面 TCR 蛋白的功能？

**实验逻辑：**

V(D)J 重组 → TCR 序列 → T 细胞命运的因果路径包含三层中介产物：

```
① DNA 切除与插入（非编码）
        ↓
② 表面 TCR 氨基酸序列
        ↓
③ 抗原识别（TCR-pMHC 结合）
        ↓
   T 细胞命运决定
```

为区分 ① 与 ②/③，论文利用了一种天然的生物学对照——**非生产性 TCR（nonproductive TCR）**。当一条染色体的 V(D)J 重组产生移码而另一条框内时，细胞仍能存活并表达功能性 TCR，但移帧等位基因的转录本（含终止密码子，不翻译为蛋白）也会被检出。这些 nonproductive TCR 代表了**纯净的 DNA 重排信号**（仅产物 ①），完全不涉及 ② 和 ③。

**关键设计细节（STAR Methods）：**
- 使用 Cell Ranger vdj (v5.0.1) 标注为 high confidence, full length, nonproductive 的 contigs
- **CDR3 长度门槛取消**：因 nonproductive 常因终止密码子变短
- **单链评分函数策略**：α 和 β 链极少在同一 nonproductive 中共检，故将 4 个评分函数拆为 α-only 和 β-only 版本（4×2=8 个单链函数），权重仍在 datasets 1+2 的生产性 TCR 上训练
- **降采样对照**：对生产性 TCR 降采样后重新测试，以排除"无关联是因为 nonproductive 样本量太小"的可能性

**结果：**

| TCR 评分函数 | Nonproductive TCR 关联 (p) | Productive TCR 降采样后 |
|-------------|--------------------------|-----------------------|
| TCR-innate  | > 0.05（无关联） | 仍显著 |
| TCR-CD8     | > 0.05（无关联） | 仍显著 |
| TCR-reg     | > 0.05（无关联） | 仍显著 |
| TCR-mem     | > 0.05（无关联） | 仍显著 |

**结论：** DNA 水平的 V(D)J 重排（RAG 介导的切割与 TdT 介导的 N-添加）本身不足以驱动 T 细胞命运——重组产物必须在蛋白质水平表达为表面 TCR，才能通过 pMHC 识别影响细胞状态。

**方法学亮点：**
1. **天然的阴性对照** — nonproductive TCR 是不依赖实验干预的"DNA-only"对照，与生产性 TCR 共享相同的细胞环境
2. **因果分解三步走** — 本节排除了 ① DNA 水平；后续两节（TCR-mem 预测激活 / TCR-mem ≠ 亲和力）区分了 ② 与 ③，形成完整的因果路径验证
3. **生物信息学技巧** — 单链评分函数解决了非生产性双链数据稀疏的问题

---

<a id="S011"></a>
### TCR-mem预测抗原特异性群体内更强的T细胞激活 | TCR-mem predicts increased T cell activation within antigen-specific populations

**Source:** p.7-9 Results

**Original:**
T cell activation, marked by CD69 upregulation, is a critical first step in T cell memory formation.⁴²,⁴³ If TCR-mem increases the odds of memory formation by promoting early activation, then (1) recently activated T cells (CD69^high, MK67^high, CD38⁺, HLA-DR⁺) should exhibit high TCR-mem, and (2) this phenomenon should be apparent in Jurkat cells, which biologically resemble T cells in activation but not the subsequent steps of memory formation. We identified recently activated T cells (CD69^high, MK67^high, CD38⁺, HLA-DR⁺) in dataset 1 and observed that TCR-mem in this subset was just as high as TCR-mem in other memory subsets (Figure 4A). Thus, we hypothesized that TCR-mem sequence features promote T cell activation.

First, we tested whether higher TCR-mem led to greater cellular activation in Jurkat cells. We selected four naturally occurring TCR sequences found in human data²³ that spanned the range of our TCR-mem metric and transduced each TCR into Jurkat cells (Figure 4B). All four TCR sequences recognize the same "ELA-" antigenic peptide from melanoma-associated antigen recognized by T cells (MART-1), presented on HLA-A*02:01.²³ Thus, this array of TCR sequences allows us to examine whether changes in amino acid composition that increase TCR-mem indeed causally promote T cell memory formation while controlling for cognate antigen and HLA (Table 2).

Each TCR sequence exhibited greater CD69 upregulation compared to baseline (fold change > 1), confirming specific reactivity to the MART-1 antigen. However, the extent of activation, quantified by the percentage of CD69⁺ cells compared to baseline, clearly tracked with the TCR-mem score (Figure 4C). Thus, the TCR sequence features that we have observed to differ between memory and naive cells in vivo appear to causally promote T cell activation in vitro.

To assess the stability of this finding, we examined the CD69 response at different antigen doses. We titrated the amount of MART-1-expressing antigen-presenting cells (APCs) and repeated the overnight co-culture. These titrations showed the expected dose-response relationship, which indeed escalated with increasing TCR-mem (Figure S6A). At each antigen dose, increased TCR-mem scores corresponded to greater CD69 responses.

We next assessed if altering individual residues to increase or decrease TCR-mem tracked with changes in activation. For this, we examined a different antigen, the "NLV-" peptide from the cytomegalovirus (CMV) antigen pp65 presented on HLA-A*02:01. We repeated the co-culture experiment with four TCR sequences that differ by one to four amino acids in CDR3α but are otherwise identical in sequence (Table 2). These TCRs were synthetically engineered and previously shown to recognize the "NLV-" antigenic peptide (Schub et al.⁴⁴ and Abdelfattah et al.⁴⁵). As in the MART-1 experiments, we saw that each incremental gain in TCR-mem induced a greater fold change in activation (Figures 4D and S6B). Thus, our TCR-mem metric identifies replicable differences in immune reactivity between TCR sequences, even when sequence differences are as minor as one CDR3α amino acid.

To extend our analyses beyond these two HLA-A*02:01 antigens, we examined single-cell profiling data²³ (dataset 5, Table 1) with 44 Dextramers, including HLA-A*02:01, HLA-B*07:02, and HLA-B*35:01. Briefly, 80 million CD8⁺ T cells from the peripheral blood of four human donors were exposed to 44 pMHC-barcoded Dextramers. Multimodal sequencing then assayed the αβTCR sequence, transcriptome-wide expression, and pMHC Dextramer counts for each Dextramer-positive cell. Using Symphony and k-nearest neighbors, we assigned T cell states based on our multimodal T cell reference (Figure 4E).

Following custom normalization of Dextramer UMI counts (Figures S7A–S7D; STAR Methods), we observed a mixture of transcriptional states within each antigen-specific population (Figure S7E). Within each antigen-specific population, we tested the association between TCR-mem and memory state using a single cell per TCR clone (STAR Methods). Consistent with our TCR transduction experiments, we observed β > 0 for the majority of antigens (19/29), including seven antigen-specific populations with a nominally significant (one-tailed p < 0.05) result (Table S7). Given a lack of statistical power within each antigen-specific population (Figure S7F), we conducted a meta-analysis across antigen-specific populations. We observed a significant effect of TCR-mem on memory state, adjusted for antigen specificity (Figures 4F and S7G, β_TCR-mem = 0.11, p = 0.002; STAR Methods). We observed minimal evidence for a difference in β_TCR-mem before and after adjusting for antigen specificity (heterogeneity p = 0.45) and minimal heterogeneity in β_TCR-mem across antigen-specific populations (I² = 29.2%, H² = 1.41, Q = 39.6, p = 0.07). TCR-mem associations hold after adjusting for Dextramer staining intensity (STAR Methods) as a proxy for TCR-pMHC affinity. These results suggest that TCR-mem sequence features predispose pMHC recognition in general, regardless of the cognate antigen.

**中文:**
T细胞激活以CD69上调为标志，是T细胞记忆形成的关键第一步⁴²,⁴³。如果TCR-mem通过促进早期激活来增加记忆形成的几率，那么（1）近期激活的T细胞（CD69^高表达、MK67^高表达、CD38⁺、HLA-DR⁺）应表现出高TCR-mem，并且（2）这种现象在Jurkat细胞中应很明显——Jurkat细胞在生物学上类似于激活状态下的T细胞，但不具备后续的记忆形成步骤。我们在数据集1中识别出近期激活的T细胞（CD69^高表达、MK67^高表达、CD38⁺、HLA-DR⁺），并观察到该亚群中的TCR-mem与其他记忆亚群中的TCR-mem同样高（图4A）。因此，我们假设TCR-mem序列特征促进T细胞激活。

首先，我们测试了更高的TCR-mem是否导致Jurkat细胞中更强的细胞激活。我们选择了在人类数据中发现的四个天然TCR序列²³，它们覆盖了TCR-mem指标的范围，并将每个TCR转导到Jurkat细胞中（图4B）。所有四个TCR序列都识别相同的"ELA-"抗原肽——来自黑色素瘤相关抗原MART-1，通过HLA-A*02:01呈递²³。因此，这一系列的TCR序列使我们能够在控制同源抗原和HLA的条件下，检查增加TCR-mem的氨基酸组成变化是否确实因果性地促进T细胞记忆形成（表2）。

与基线相比，每个TCR序列都表现出更强的CD69上调（倍变 > 1），确认了对MART-1抗原的特异性反应。然而，通过CD69⁺细胞百分比（相对于基线）量化的激活程度，明显与TCR-mem评分呈正相关（图4C）。因此，我们在体内观察到的记忆细胞与初始细胞之间差异的TCR序列特征，似乎在体外因果性地促进了T细胞激活。

为评估这一发现的稳定性，我们检查了不同抗原剂量下的CD69反应。我们滴定表达MART-1的抗原呈递细胞（APC）的数量，并重复过夜共培养实验。这些滴定显示了预期的剂量-反应关系，且随着TCR-mem的增加而增强（图S6A）。在每个抗原剂量下，更高的TCR-mem评分对应更强的CD69反应。

接下来，我们评估改变个别残基以增加或减少TCR-mem是否与激活的变化相对应。为此，我们检查了一种不同的抗原——来自巨细胞病毒（CMV）抗原pp65的"NLV-"肽，通过HLA-A*02:01呈递。我们用四个在CDR3α上相差1到4个氨基酸但其他序列完全相同的TCR序列重复了共培养实验（表2）。这些TCR是合成设计的，先前已被证明能识别"NLV-"抗原肽（Schub等⁴⁴和Abdelfattah等⁴⁵）。与MART-1实验一样，我们观察到TCR-mem的每一次递增都诱导了更大的激活倍变（图4D和S6B）。因此，我们的TCR-mem指标识别出了TCR序列之间可重复的免疫反应性差异，即使序列差异小到只有一个CDR3α氨基酸。

为将分析扩展到这两个HLA-A*02:01抗原之外，我们检查了包含44种Dextramer的单细胞数据²³（数据集5，表1），包括HLA-A*02:01、HLA-B*07:02和HLA-B*35:01。简而言之，来自四个人类供者外周血的8000万个CD8⁺ T细胞被暴露于44种pMHC条形码标记的Dextramer。多模态测序随后检测了每个Dextramer阳性细胞的αβTCR序列、全转录组表达和pMHC Dextramer计数。使用Symphony和k近邻方法，我们基于多模态T细胞参考图谱分配了T细胞状态（图4E）。

经过对Dextramer UMI计数进行自定义标准化（图S7A–S7D；STAR Methods）后，我们在每个抗原特异性群体内观察到转录状态的混合（图S7E）。在每个抗原特异性群体内，我们使用每个TCR克隆一个细胞测试了TCR-mem与记忆状态之间的关联（STAR Methods）。与我们的TCR转导实验一致，我们观察到大多数抗原（19/29）的β > 0，包括七个名义显著（单尾p < 0.05）的抗原特异性群体（表S7）。鉴于每个抗原特异性群体内统计功效不足（图S7F），我们在抗原特异性群体间进行了荟萃分析。我们观察到在调整抗原特异性后，TCR-mem对记忆状态存在显著效应（图4F和S7G，β_TCR-mem = 0.11，p = 0.002；STAR Methods）。我们在调整抗原特异性前后观察到β_TCR-mem差异的证据极小（异质性p = 0.45），且不同抗原特异性群体间的β_TCR-mem异质性极小（I² = 29.2%，H² = 1.41，Q = 39.6，p = 0.07）。在将Dextramer染色强度（STAR Methods）作为TCR-pMHC亲和力的代理指标进行调整后，TCR-mem关联仍然成立。这些结果表明，TCR-mem序列特征通常会预置pMHC识别，而不依赖于同源抗原。

**解析 | Analysis**

**核心问题：** TCR-mem 是否因果性地促进 T 细胞激活？这效应是抗原特异性的还是普遍的？

**本节在整个论文中的定位：**

这是因果验证三步走的第二步（上一节排除了 ① DNA 水平后，本节检验 ②→③ 路径）：

```
V(D)J 重组 → TCR 蛋白 → 抗原识别 → T 细胞激活 → 记忆形成
   ① (已排除)       ②            ③           TCR-mem?
                    ↑─── 本节焦点 ───↑
                表面 TCR 序列特征能否预测激活？
```

**三个递进层次的实验设计：**

---

**层次 1：体内观察（相关性）**

从数据集 1 的 scRNA-seq 数据中，识别出近期激活的 T 细胞（CD69^high, MK67^high, CD38⁺, HLA-DR⁺），发现其 TCR-mem 与经典记忆亚群同样高（图 4A）。

→ 相关性存在，但无法区分因果方向：是 TCR-mem 高导致激活，还是激活后 TCR-mem 升高？

---

**层次 2：体外因果验证——Jurkat 转导实验**

Jurkat 细胞的选择极巧妙：它们**在激活层面与 T 细胞相似，但缺乏后续记忆形成的信号通路**。因此，如果在 Jurkat 中观察到 TCR-mem 差异导致 CD69 差异，就能将效应锁定在"激活"这一早期步骤，排除记忆维持等晚期过程的混杂。

**实验 A：MART-1（天然 TCR，全序列差异）**

| TCR | TCR-mem | TRAV | TRAJ | CDR3α | TRBV | TRBJ | CDR3β |
|-----|---------|------|------|-------|------|------|-------|
| MART-a | **−2.25** | TRAV12-2 | TRAJ45 | CGVSGGGADGLTF | TRBV6-2 | TRBJ2-7 | CASTDSPGLAGGYEQYF |
| MART-b | **−0.92** | TRAV12-2 | TRAJ31 | CAGNNARLMF | TRBV28 | TRBJ1-5 | CASRGTGLGNQPQHF |
| MART-c | **−0.02** | TRAV12-2 | TRAJ17 | CAVKNAGNKLTF | TRBV7-2 | TRBJ2-7 | CASSLNDFYEQYF |
| MART-d | **+1.35** | TRAV12-2 | TRAJ11 | CASSWGGYSTLTF | TRBV20-1 | TRBJ2-7 | CSARVETSGIHEQYF |

- 所有 4 个 TCR 识别**同一个** MART-1 抗原肽（ELA-）+ HLA-A*02:01
- TCR-mem 从 −2.25 到 +1.35，跨度 3.6 个标准差
- CD69⁺ 细胞百分比随 TCR-mem 递增（图 4C）
- 抗原剂量滴定实验确认该关系在各剂量下均成立（图 S6A）

**实验 B：NLV（工程 TCR，仅 CDR3α 差异）**

| TCR | TCR-mem | CDR3α 序列 | α 链差异 |
|-----|---------|-----------|----------|
| NLV-a | **−0.84** | CAGPMITSQDKVIF | 基准 |
| NLV-b | **−0.59** | CAGPMLTSQDKVIF | **1 aa** (I→L) |
| NLV-c | **−0.11** | CAGPNPTTYDKVIF | **2 aa** (MI→NP) |
| NLV-d | **+0.03** | CAGPMKTSYDKVIF | **3 aa** (MI→MK, Q→Y) |

关键设计：四个 TCR 的 **β 链完全一致**（TRBV12-4, TRBJ1-2, CASSSANYGYTF），仅 CDR3α 有 1–4 个氨基酸差异。排除了 β 链变异带来的混杂。

→ 每个 TCR-mem 的递增都对应 CD69 激活的递增（图 4D）

**→ 因果证据成立：改变少数氨基酸→改变 TCR-mem→改变激活强度**

---

**层次 3：体内泛化——44-重 Dextramer 荟萃分析**

| 特性 | 数值 |
|------|------|
| 供者 | 4 人 |
| 筛选细胞数 | 8×10⁷ CD8⁺ T 细胞 |
| Dextramer 种类 | 44 种（跨越 HLA-A*02:01, B*07:02, B*35:01）|
| 抗原特异性群体 | 29 个（有足够细胞进行统计检验）|
| β_TCR-mem > 0 | 19/29（65.5%）|
| 名义显著（单尾 p < 0.05） | 7/29 |
| 荟萃分析 β_TCR-mem | **0.11** (p = 0.002) |

**三个重要的阴性对照（混杂因素排除）：**

1. **调整抗原特异性后 β 不变**（异质性 p = 0.45）→ 效应不是由某个抗原驱动
2. **跨群体异质性极小**（I² = 29.2%, p = 0.07）→ 效应在各抗原间一致
3. **调整 Dextramer 染色强度后关联仍存在** → 效应不是由 TCR-pMHC 亲和力差异介导（与 S012 节衔接）

---

**关键结论：**

> TCR-mem 序列特征**因果性地**促进 T 细胞激活，且这种效应是**抗原非依赖的**——无论 TCR 识别哪种抗原，高 TCR-mem 的序列都更倾向于激活。

---

**方法学亮点：**

1. **Jurkat 系统的精妙选择** — 将"激活"从"记忆形成"的整个过程中解耦出来，使得 TCR-mem 的效应可以被准确归因到激活这一特定步骤
2. **天然 TCR + 工程 TCR 双验证** — MART-1 实验用天然存在的全序列差异检验生态效度；NLV 实验用工程改造的微扰（perturbation）检验因果精度，两者互相印证
3. **从单抗原到多抗原的泛化链** — 两抗原（MART-1, NLV）→ 44 Dextramer（29 群体），逐步扩展结论的适用范围
4. **荟萃分析解决稀疏性问题** — 单个抗原特异性群体内统计功效不足，但跨群体荟萃后效应显著且一致

---

<a id="S012"></a>
### TCR-mem与抗原结合亲和力不同 | TCR-mem is distinct from antigen binding affinity

**Source:** p.9-10 Results

**Original:**
While TCR-mem is a property of the TCR sequence alone, binding affinity is a property of a TCR and antigen pair. For a given TCR sequence, binding affinity varies widely with choice of antigen. For example, TCR 1E6⁵⁰ exhibits approximately eight times greater binding affinity to RQFGPDWIVA-HLA-A*02 compared to ALWGPDPAAA-HLA-A*02 (buried surface area: 32,593.7 compared to 3,956.5 Å², PDBePISA). Thus, we did not expect TCR-mem to correspond to binding affinity for any particular antigen.

To assess whether TCR-mem corresponds to TCR-pMHC binding affinity, we (1) conducted tetramer dilution experiments, (2) examined published micropipette adhesion data, and (3) computed buried surface areas in crystal structures. First, we stained each of our four MART-1-specific Jurkat populations with increasing concentrations of MART-1 tetramer (Figure S6C). We approximated each TCR's affinity to the MART-1 tetramer with EC₅, the tetramer concentration at which 5% of Jurkat cells stain positively for tetramer. EC₅ measurements for the MART-reactive TCRs did not reveal a clear relationship between TCR-mem and binding affinity (Figure S6E).

Given the potential limitations of tetramers,⁵¹,⁵² we next analyzed data from a micropipette adhesion assay that simultaneously measures two-dimensional (2D) TCR affinity and TCR sequence (iTAST).⁵³ The published iTAST dataset⁵³ includes 33 αβ-paired TCRs that bind the hepatitis C virus (HCV) antigen KLVALGINAV complexed with HLA-A*02. We calculated TCR-mem scores for these 33 TCR sequences and again observed no clear relationship between TCR-mem score and binding affinity (R = −0.1; Figure S6F).

Third, we analyzed crystal structures of αβTCRs complexed with class I MHC from the Protein Data Bank (PDB). Following quality control, we obtained 138 structures, corresponding to 86 unique epitopes and 17 unique class I HLA alleles. We used PDBePISA to estimate the amount of surface area buried between the TCR and pMHC, a known proxy for binding affinity.⁵⁴ We observed no significant relationship between TCR-mem and binding affinity (R = 0.009; Figure S6G). Thus, three lines of evidence (Figures S6E–S6G) indicate minimal correspondence between TCR-mem and binding affinity. TCR-mem appears to capture a TCR characteristic that is distinct from binding affinity yet reliably promotes T cell activation.

**中文:**
虽然TCR-mem仅是TCR序列本身的属性，结合亲和力却是TCR与抗原配对的一个属性。对于给定的TCR序列，结合亲和力随抗原选择而大幅变化。例如，TCR 1E6⁵⁰对RQFGPDWIVA-HLA-A*02的结合亲和力是对ALWGPDPAAA-HLA-A*02的大约八倍（埋藏表面积分别为32,593.7和3,956.5 Å²，PDBePISA）。因此，我们并不预期TCR-mem会与任何特定抗原的结合亲和力相对应。

为评估TCR-mem是否与TCR-pMHC结合亲和力对应，我们（1）进行了四聚体稀释实验，（2）检查了已发表的微吸管粘附测定数据，以及（3）计算了晶体结构中的埋藏表面积。首先，我们用递增浓度的MART-1四聚体染色了四个MART-1特异性Jurkat群体中的每一个（图S6C）。我们用EC₅——即5% Jurkat细胞对四聚体染色呈阳性的四聚体浓度——来近似每个TCR对MART-1四聚体的亲和力。MART反应性TCR的EC₅测量结果并未揭示TCR-mem与结合亲和力之间的明确关系（图S6E）。

考虑到四聚体的潜在局限性⁵¹,⁵²，我们接下来分析了一个同时测量二维（2D）TCR亲和力和TCR序列的微吸管粘附测定（iTAST）的数据⁵³。已发表的iTAST数据集⁵³包括33个与HLA-A*02复合的丙型肝炎病毒（HCV）抗原KLVALGINAV结合的αβ配对TCR。我们计算了这33个TCR序列的TCR-mem评分，再次观察到TCR-mem评分与结合亲和力之间没有明确关系（R = −0.1；图S6F）。

第三，我们分析了来自蛋白质数据库（PDB）的与I类MHC复合的αβTCR晶体结构。经过质量控制，我们获得了138个结构，对应86个独特表位和17个独特的I类HLA等位基因。我们使用PDBePISA估计TCR与pMHC之间的埋藏表面积——这是结合亲和力的已知代理指标⁵⁴。我们观察到TCR-mem与结合亲和力之间没有显著关系（R = 0.009；图S6G）。因此，三条证据线（图S6E–S6G）均表明TCR-mem与结合亲和力之间的对应关系极小。TCR-mem似乎捕捉到了一种与结合亲和力不同但能可靠促进T细胞激活的TCR特征。

---

<a id="S013"></a>
### 胸腺选择压力在外周持续存在 | Thymic selection pressures on the TCR sequence continue in the periphery

**Source:** p.10-11 Results

**Original:**
Given the consistent association of TCR-mem to memory state across antigenic peptides, we hypothesized that TCR-mem reflects reactivity to the underlying MHC(-like) molecule. Specifically, to promote recognition of many different pMHCs, such reactivity would be focused on elements of MHC that are conserved across MHC genes and alleles. This TCR property, referred to as "generic MHC reactivity," has been theorized based on thymic development in TCR-transgenic mice.⁵⁷

If TCR-mem reflects generic MHC reactivity, then TCR-mem sequence features should also help to explain which T cells survive thymic positive selection. Only T cells with a sufficient signaling response to pMHC survive thymic positive selection, which is marked by progression from a double-positive (DP) phenotype to a single-positive (SP) phenotype. Thus, if TCR-mem reflects generic MHC reactivity, then SP T cells should have higher TCR-mem compared to DP T cells, 90%² of which never progress to the SP stage.

Thus, we compared TCR-mem scores between SP and DP prenatal T cells (14,584 cells, dataset 6, Table 1; STAR Methods). TCR-mem was designed to describe differences between naive and memory TCRs in the periphery. We observed, however, that the same TCR sequence weighting scheme also described differences between DP and SP TCRs (Figure 5A, β_TCR-mem = 0.14, p = 1.3 × 10⁻⁷; Table S4). Strikingly, the TCR-mem difference between SP and DP thymic T cells was statistically indistinguishable from the TCR-mem difference between memory and naive peripheral T cells (heterogeneity p = 0.86). Thus, TCR differences between peripheral naive and memory T cells appear to echo TCR filtering by thymic positive selection (Figure 5B). The influence of TCR-mem persists in the absence of foreign and peripheral antigens, suggesting that TCR-mem reflects generic pMHC reactivity. While thymic selection imposes a minimum threshold for pMHC reactivity, TCRs that survive this threshold by a wider margin appear more likely to reach a memory T cell state in the periphery.

An alternative possibility we considered is that higher TCR-mem T cells had developed earlier in life and therefore accrued more opportunities to transition their transcriptional state. This time-related confound would require systematic shifts in V(D)J recombination with human age. However, we observed no relationship between age and TCR-mem (Figure S6H). Prenatal TCR sequences from dataset 6 allowed us to further extend our age-related line of inquiry. Some prenatal T cells lack DNTT expression, precluding non-templated insertion of TCR nucleotides and resulting in systemically shorter TCR sequences.⁵⁸ To identify these age-related TCRs, we applied IGoR⁵⁹ to infer the number of nucleotide insertions in each thymic TCR. We observed that additional nucleotide insertions corresponded to a decrease in the odds of thymic positive selection, but this effect did not account for the effect of TCR-mem (Figure 5C). Controlling for the number of nucleotide insertions, TCR-mem actually demonstrated a stronger effect on the odds of positive selection (conditional β_TCR-mem = 0.22, 95% CI = [0.13–0.30], p = 3.8 × 10⁻⁷, compared to unconditional β_TCR-mem = 0.14, 95% CI = [0.09–0.19], p = 1.3 × 10⁻⁷; Table S4; STAR Methods). Thus, TCR-mem associations are not explained by developmental time points.

In contrast to TCR-mem, TCR-innate was not applicable to thymic data. Thymic T cells expressing canonical TCRs for MAIT cells and NKT cells had not yet reached the innate-like, PLZF^high transcriptional fate (Figure 5D). This is consistent with previous reports showing that PLZF^high fate acquisition is dependent on peripheral antigen recognition.⁶⁰⁻⁶² TCR-reg and TCR-CD8, however, were applicable to thymic data (Figures 5E and 5F, β_TCR-CD8 = 0.78, p = 4.3 × 10⁻⁹⁷; β_TCR-reg = 0.14, p = 2.8 × 10⁻⁵; Table S4; STAR Methods), indicating that these associations between TCR sequence and T cell state are not dependent on peripheral antigen recognition. Evidently, TCR sequence features shape T cell differentiation outcomes in both the thymus and periphery, influencing which T cells are able to generate an effective immune response.

**中文:**
鉴于TCR-mem与记忆状态在不同抗原肽间的一致关联，我们假设TCR-mem反映了对底层MHC（样）分子的反应性。具体而言，为促进对许多不同pMHC的识别，这种反应性将集中在MHC基因和等位基因间保守的MHC元件上。这种TCR特性被称为"通用MHC反应性"，基于TCR转基因小鼠的胸腺发育理论已被提出⁵⁷。

如果TCR-mem反映了通用MHC反应性，那么TCR-mem序列特征也应有助于解释哪些T细胞能在胸腺阳性选择中存活。只有对pMHC产生足够信号反应的T细胞才能通过胸腺阳性选择，其标志是从双阳性（DP）表型进展为单阳性（SP）表型。因此，如果TCR-mem反映通用MHC反应性，那么SP T细胞的TCR-mem应该高于DP T细胞——其中90%²从未进展到SP阶段。

因此，我们比较了SP和DP产前T细胞之间的TCR-mem评分（14,584个细胞，数据集6，表1；STAR Methods）。TCR-mem是为了描述外周初始和记忆TCR之间的差异而设计的。然而，我们观察到相同的TCR序列加权方案也描述了DP和SP TCR之间的差异（图5A，β_TCR-mem = 0.14，p = 1.3 × 10⁻⁷；表S4）。引人注目的是，SP与DP胸腺T细胞之间的TCR-mem差异与外周记忆与初始T细胞之间的TCR-mem差异在统计学上无法区分（异质性p = 0.86）。因此，外周初始与记忆T细胞之间的TCR差异似乎反映了胸腺阳性选择对TCR的筛选（图5B）。在缺乏外源和外周抗原的情况下，TCR-mem的影响仍然存在，表明TCR-mem反映了通用pMHC反应性。虽然胸腺选择施加了pMHC反应性的最低阈值，但以更大裕度超过这一阈值的TCR似乎更可能在外周达到记忆T细胞状态。

我们考虑的另一种可能性是，具有更高TCR-mem的T细胞在生命更早期就已发育，因此积累了更多转变其转录状态的机会。这种时间相关的混杂因素需要V(D)J重组随人类年龄发生系统性变化。然而，我们未观察到年龄与TCR-mem之间的关系（图S6H）。数据集6中的产前TCR序列使我们能够进一步扩展与年龄相关的探究。一些产前T细胞缺乏DNTT表达，阻碍了TCR核苷酸的非模板插入，导致系统性更短的TCR序列⁵⁸。为识别这些与年龄相关的TCR，我们应用IGoR⁵⁹推断每个胸腺TCR中的核苷酸插入数量。我们观察到额外的核苷酸插入对应于胸腺阳性选择几率的降低，但这种效应并不能解释TCR-mem的效应（图5C）。在控制核苷酸插入数量后，TCR-mem实际上对阳性选择几率表现出更强的效应（条件β_TCR-mem = 0.22，95% CI = [0.13–0.30]，p = 3.8 × 10⁻⁷，相较于无条件β_TCR-mem = 0.14，95% CI = [0.09–0.19]，p = 1.3 × 10⁻⁷；表S4；STAR Methods）。因此，TCR-mem关联不能用发育时间点来解释。

与TCR-mem不同，TCR-innate不适用于胸腺数据。表达MAIT细胞和NKT细胞经典TCR的胸腺T细胞尚未达到先天样PLZF^高表达的转录命运（图5D）。这与先前报道一致，表明PLZF^高表达命运的获得依赖于外周抗原识别⁶⁰⁻⁶²。然而，TCR-reg和TCR-CD8适用于胸腺数据（图5E和5F，β_TCR-CD8 = 0.78，p = 4.3 × 10⁻⁹⁷；β_TCR-reg = 0.14，p = 2.8 × 10⁻⁵；表S4；STAR Methods），表明TCR序列与T细胞状态之间的这些关联不依赖于外周抗原识别。显然，TCR序列特征在胸腺和外周都塑造了T细胞分化结果，影响着哪些T细胞能够产生有效的免疫反应。

---

<a id="S014"></a>
## 讨论 | DISCUSSION

**Source:** p.11 Discussion

**Original:**
In this study, we define four TCR scoring functions that estimate the TCR's contribution to four T cell fates. These scoring functions are robust across numerous genetic and clinical contexts. Even among T cells that recognize the same antigen, these TCR scores help to explain variation in T cell states.

Our CCA-based quantitative approach allows us to understand the relative strength of previously observed connection between TCR sequence and T cell state. The most deterministic relationship belongs to MAIT cells. Structural studies have shown that MHC-like molecule MR1 buries small metabolite antigens so that they do not contact TCR.⁶³,⁶⁴ Consequently, MAIT cell TCRs need only recognize MR1, which marks a highly distinct transcriptional population of PLZF^high, innate-like T cells. This tight link from αβ TCR sequence to T cell fate is unusual; were there other relationships of similar magnitude, we believe that our model would have identified them.

We observe elevated CDR3 hydrophobicity in KIR⁺HELIOS⁺ CD8 T cells, consistent with a previous report.¹⁸ Schattgen et al.¹⁸ hypothesized that this CD8 population may be "MHC-independent, noncanonical, or self-specific." Our framework unifies this observation with CD4 investigations¹⁰,¹⁶: KIR⁺CD8⁺ T cells, which may functionally represent human CD8 Treg cells,³⁶ appear to resemble CD4 Treg cells in terms of TCR sequence. In general, hydrophobic and aromatic (F, L, I, C, Y, W) junctional CDR3 residues (both α and β) may increase a T cell's likelihood of recognizing self-antigens, driving FOXP3 Treg cell fate in the case of CD4 co-receptors and KIR⁺HELIOS⁺ fate in the case of CD8 co-receptors.

We take particular interest in TCR-mem because it describes TCR sequence features that are generally advantageous for reaching a memory T cell state. Our own tetramer dilution experiments, external micropipette adhesion data, and buried surface area calculations each indicate that TCR-mem is distinct from antigen binding affinity. Rather, our TCR-mem scoring function can distinguish which TCR sequences recognizing a common antigen are more likely to activate. We have shown this with respect to endogenous TCR sequences recognizing a self-antigen (MART-1) and engineered TCR sequences recognizing a viral antigen (pp65). Increased TCR-mem also corresponds to positive selection in the thymus, extending previous observations that T cells with high self-reactivity (CD5^high) also have higher reactivity to foreign antigens.⁶⁵⁻⁶⁷ With TCR-mem, we have identified a common set of TCR sequence features that promote both central and peripheral⁶⁸ selection of the T cell repertoire.

It is now clear that a TCR sequence conveys two types of information: transcriptional fate bias and antigen specificity. Both types of information may be crucial to the immune response in autoimmunity, cancer, and infection. TCR features may play a particularly important role in influencing T cell fate for T cells that recognize autoantigens, which ought to be relatively anergic. The therapeutic design of TCRs may need to consider not only recognition of the antigenic target but also differentiation into an effective T cell state.

**中文:**
在本研究中，我们定义了四个TCR评分函数，用于估计TCR对四种T细胞命运的贡献。这些评分函数在多种遗传和临床背景下都具有稳健性。即使在识别相同抗原的T细胞中，这些TCR评分也有助于解释T细胞状态的变异。

我们基于CCA的定量方法使我们能够理解先前观察到的TCR序列与T细胞状态之间关联的相对强度。最具确定性的关系属于MAIT细胞。结构研究表明，MHC样分子MR1埋藏了小分子代谢抗原，使它们不与TCR接触⁶³,⁶⁴。因此，MAIT细胞TCR仅需识别MR1，这标志着一个高度独特的PLZF^高表达先天样T细胞转录群体。这种从αβ TCR序列到T细胞命运的紧密联系是不寻常的；如果存在其他类似幅度的关系，我们相信我们的模型本应能够识别它们。

我们观察到KIR⁺HELIOS⁺ CD8 T细胞中的CDR3疏水性升高，这与先前的报告一致¹⁸。Schattgen等¹⁸假设这个CD8群体可能是"MHC非依赖、非经典或自身特异性的。"我们的框架将这一观察与CD4研究¹⁰,¹⁶统一起来：KIR⁺CD8⁺ T细胞——可能在功能上代表人类CD8 Treg细胞³⁶——在TCR序列上似乎与CD4 Treg细胞相似。总的来说，疏水性和芳香族（F、L、I、C、Y、W）连接区CDR3残基（包括α和β链）可能增加T细胞识别自身抗原的可能性，在CD4共受体情况下驱动FOXP3 Treg细胞命运，在CD8共受体情况下驱动KIR⁺HELIOS⁺命运。

我们对TCR-mem特别感兴趣，因为它描述了通常有利于达到记忆T细胞状态的TCR序列特征。我们自己的四聚体稀释实验、外部的微吸管粘附数据和埋藏表面积计算都表明，TCR-mem与抗原结合亲和力不同。相反，我们的TCR-mem评分函数能够区分识别共同抗原的哪些TCR序列更可能被激活。我们已经在识别自身抗原（MART-1）的内源性TCR序列和识别病毒抗原（pp65）的工程化TCR序列中证明了这一点。升高的TCR-mem也对应于胸腺中的阳性选择，扩展了先前的观察：具有高自身反应性（CD5^高表达）的T细胞对外来抗原也具有更高的反应性⁶⁵⁻⁶⁷。通过TCR-mem，我们识别出了一组通用的TCR序列特征，这些特征促进了T细胞库的中枢和外周⁶⁸选择。

现已明确，TCR序列传递两种类型的信息：转录命运偏向和抗原特异性。这两类信息可能对自身免疫、癌症和感染中的免疫反应都至关重要。TCR特征可能在影响识别自身抗原（这些T细胞应相对无反应）的T细胞命运中发挥特别重要的作用。TCR的治疗性设计可能需要不仅考虑对抗原靶标的识别，还要考虑分化成有效的T细胞状态。

---

<a id="S015"></a>
## 研究的局限性 | Limitations of the study

**Source:** p.11 Discussion

**Original:**
There are several limitations to our study. First, our study is restricted to αβ TCR sequences by virtue of the standard custom primer set for V(D)J amplification. The usage of gamma-delta, rather than αβ, TCR genes, has clear effects on the transcriptional state⁶⁹ that merit further study. Second, our approach to defining a standard set of TCR sequence features excluded T cells in which more than one α or one more than one β chain was detected. We expect that dual-α chain T cells follow similar relationships between the TCR sequence and T cell state, but demonstrating this would require separate analysis approaches. Lastly, our TCR scoring functions are consistent across individuals and antigens, but they are insufficient to accurately classify T cell states. After all, the TCR sequence is only one minor influence on the transcriptional state of a given T cell.

**中文:**
本研究存在若干局限性。首先，由于V(D)J扩增使用标准的定制引物组，我们的研究仅限于αβ TCR序列。使用γδ而非αβ TCR基因对转录状态有明显的影响⁶⁹，值得进一步研究。其次，我们定义标准TCR序列特征集的方法排除了检测到多于一条α链或一条β链的T细胞。我们预期双α链T细胞在TCR序列与T细胞状态之间遵循类似的关系，但证明这一点需要单独的分析方法。最后，我们的TCR评分函数在个体和抗原间具有一致性，但不足以精确分类T细胞状态。毕竟，TCR序列只是对给定T细胞转录状态的众多微小影响之一。

---

<a id="S016"></a>
## 数据与代码可用性 | Data and code availability

**Source:** p.11 Resource Availability

**Original:**
- All sequencing data analyzed in this study were previously deposited in online databases (Table S1).
- Custom analysis code for this manuscript is available at https://github.com/immunogenomics/tcrpheno_analysis. An R package to apply our TCR scoring functions to new data is available at https://github.com/kalaga27/tcrpheno.
- Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request.

**中文:**
- 本研究分析的所有测序数据先前已存放在在线数据库中（表S1）。
- 本文的自定义分析代码可在 https://github.com/immunogenomics/tcrpheno_analysis 获取。将我们的TCR评分函数应用于新数据的R包可在 https://github.com/kalaga27/tcrpheno 获取。
- 重新分析本文报告的数据所需的任何其他信息均可应要求向主要联系人获取。

---

<a id="T001"></a>
## 表1 | Table 1. Datasets analyzed in this study

| Name | Reference | Sample size | No. of T cells after QC | Purpose |
|------|-----------|-------------|------------------------|---------|
| Dataset 1 | COMBAT19¹⁹ | 77 COVID-19, 23 sepsis, 12 influenza, 10 healthy | 282,639 | twin TCR analysis, developing TCR scoring functions |
| Dataset 2 | Ren et al.²⁰ | 117 COVID-19, 17 healthy | 211,780 | developing TCR scoring functions |
| Dataset 3 | Stephenson et al.²¹ | 89 COVID-19, 26 healthy | 144,175 | validating TCR scoring functions |
| Dataset 4 | Dominguez Conde et al.²² | 8 organ donors | 30,702 | validating TCR scoring functions |
| Dataset 5 | Boutet et al.²³ | 4 healthy individuals | 136,546 | assessing TCR scoring functions within antigen-specific populations |
| Dataset 6 | Suo et al.²⁴ | 6 prenatal samples | 13,930 | assessing TCR scoring functions in the thymus |
| HLA-genotyped | Su et al.²⁵ | 129 COVID-19 | 141,759 | twin TCR analysis, accounting for HLA genotypes |

---

<a id="T002"></a>
## 表2 | Table 2. TCR sequences used in transduction experiments

| ID | Antigen | Vα | Jα | CDR3α | Vβ | Jβ | CDR3β | TCR-mem |
|----|---------|----|----|-------|----|----|-------|---------|
| MART-a | MART-1 | TRAV12-2 | TRAJ45 | CGVSGGGADGLTF | TRBV6-2 | TRBJ2-7 | CASTDSPGLAGGYEQYF | −2.25 |
| MART-b | MART-1 | TRAV12-2 | TRAJ31 | CAGNNARLMF | TRBV28 | TRBJ1-5 | CASRGTGLGNQPQHF | −0.92 |
| MART-c | MART-1 | TRAV12-2 | TRAJ17 | CAVKNAGNKLTF | TRBV7-2 | TRBJ2-7 | CASSLNDFYEQYF | −0.02 |
| MART-d | MART-1 | TRAV12-2 | TRAJ11 | CASSWGGYSTLTF | TRBV20-1 | TRBJ2-7 | CSARVETSGIHEQYF | 1.35 |
| NLV-a | pp65 | TRAV35 | TRAJ50 | CAGPMITSQDKVIF | TRBV12-4 | TRBJ1-2 | CASSSANYGYTF | −0.84 |
| NLV-b | pp65 | TRAV35 | TRAJ50 | CAGPMLTSQDKVIF | TRBV12-4 | TRBJ1-2 | CASSSANYGYTF | −0.59 |
| NLV-c | pp65 | TRAV35 | TRAJ50 | CAGPNPTTYDKVIF | TRBV12-4 | TRBJ1-2 | CASSSANYGYTF | −0.11 |
| NLV-d | pp65 | TRAV35 | TRAJ50 | CAGPMKTSYDKVIF | TRBV12-4 | TRBJ1-2 | CASSSANYGYTF | 0.03 |

---

## 图表示 | Figures and Tables

### 图1 | Figure 1

**T cells with matching TCR sequences reach similar transcriptional fates in different individuals**
**TCR序列相同的T细胞在不同个体中达到相似的转录命运**

![[assets/fig1.jpg]]

(A) Uniform manifold approximation and projection (UMAP) embedding of 282,639 T cells from 122 individuals in dataset 1, clustered into A1–A9 (left; agnostic to surface protein expression) and B1–B9 (right; incorporating surface proteins).
(B–C) Clusters A9/B9 are enriched for canonical MAIT and NKT cell TCR amino acid sequences.
(D) Schematic of "TCR twin" design: identical TCR αβ sequences sampled from two different individuals.
(E) Concordance barplot: 80/115 TCR twin pairs are transcriptionally concordant (p = 6.1 × 10⁻²⁸, exact binomial test).

---

### 图2 | Figure 2

**A quantitative approach to uncover TCR sequence features that influence T cell fate**
**揭示影响T细胞命运的TCR序列特征的定量方法**

![[assets/fig2.jpg]]

(A–B) Schematic of the rCCA approach: 1,250 TCR biophysical features derived from Atchley factors across CDR and framework regions of α and β chains.
(C) Canonical correlations (R) descending from 0.54; first four CVs are statistically significant (permutation test p < 0.001).
(D–H) UMAP embedding of CV1–CV4 scores: CV1 (innate-like), CV2 (CD8/CD4), CV3 (Treg), CV4 (naive/memory).
(I–P) CDR contribution plots for each TCR scoring function (TCR-innate, TCR-CD8, TCR-reg, TCR-mem).

---

### 图3 | Figure 3

**TCR scoring functions generalize across individuals and datasets**
**TCR评分函数在不同个体和数据集间普遍适用**

![[assets/fig3.jpg]]

(A–D) Forest plots of β_TCRscore by clinical stratum (COVID, sepsis, influenza, other) for each scoring function.
(E–H) Held-out validation in 30% of datasets 1 and 2 not used in training.
(I–P) External validation in dataset 3: decile analysis showing monotonic increase in odds of target state with increasing TCR score.

---

### 图4 | Figure 4

**TCR sequences that recognize the same antigen can be poised for different fates**
**识别相同抗原的TCR序列可倾向不同的命运**

![[assets/fig4.jpg]]

(A) TCR-mem in recently activated T cells (CD69^high, MK67^high, CD38⁺, HLA-DR⁺) is as high as in other memory subsets.
(B–C) MART-1 Jurkat transduction: 4 TCRs spanning TCR-mem from −2.25 to 1.35; CD69 activation tracks with TCR-mem.
(D) NLV titration: 4 TCRs differing by 1–4 aa in CDR3α show TCR-mem-dependent activation.
(E–F) Dextramer meta-analysis across 29 antigen-specific populations: TCR-mem positively associated with memory state (β = 0.11, p = 0.002).

---

### 图5 | Figure 5

**Thymic selection pressures on the TCR sequence continue in the periphery**
**胸腺选择压力对TCR序列的影响在外周持续存在**

![[assets/fig5.jpg]]

(A) TCR-mem in SP vs DP prenatal thymocytes (β = 0.14, p = 1.3 × 10⁻⁷; dataset 6).
(B) The TCR-mem difference between SP and DP thymocytes is indistinguishable from the naive–memory difference in peripheral T cells (heterogeneity p = 0.86).
(C) TCR-CD8 and TCR-reg scoring functions in the thymus: TCR-CD8 distinguishes SP4 vs SP8 thymocytes; TCR-reg distinguishes Treg from conventional SP thymocytes.

---

## 参考文献 | References

1. Chi, X., Li, Y., and Qiu, X. (2020). V(D)J recombination. *Immunology* **160**, 233–247.
2. Klein, L., et al. (2014). Positive and negative selection of the T cell repertoire. *Nat. Rev. Immunol.* **14**, 377–391.
3. Merkenschlager, M., et al. (1997). How many thymocytes audition for selection? *J. Exp. Med.* **186**, 1149–1158.
4. Yun, T.J., and Bevan, M.J. (2001). The Goldilocks conditions applied to T cell development. *Nat. Immunol.* **2**, 13–14.
5. Nakayama, T., and Yamashita, M. (2010). TCR-mediated signaling pathways controlling helper T cell differentiation. *Semin. Immunol.* **22**, 303–309.
6. Hogquist, K.A., and Jameson, S.C. (2014). The self-obsession of T cells. *Nat. Immunol.* **15**, 815–823.
7. Kaech, S.M., and Cui, W. (2012). Transcriptional control of effector and memory CD8+ T cell differentiation. *Nat. Rev. Immunol.* **12**, 749–761.
8. Pauken, K.E., Lagattuta, K.A., et al. (2022). TCR sequencing in cancer and autoimmunity. *Trends Immunol.* **43**, 180–194.
9. Treiner, E., et al. (2003). Selection of MAIT cells by MR1. *Nature* **422**, 164–169.
10. Lagattuta, K.A., et al. (2022). Repertoire analyses reveal TCR sequence features that influence T cell fate. *Nat. Immunol.* **23**, 446–457.
11. DerSimonian, H., et al. (1991). Increased frequency of TCR Vα12.1 on CD8+ T cells. *J. Exp. Med.* **174**, 1287.
12. Stadinski, B.D., et al. (2016). Hydrophobic CDR3 residues promote self-reactive T cells. *Nat. Immunol.* **17**, 946–955.
13. Li, H.M., et al. (2016). TCRβ repertoire of CD4+ and CD8+ T cells. *J. Leukoc. Biol.* **99**, 505–513.
14. Carter, J.A., et al. (2019). Single T Cell Sequencing demonstrates functional role of αβ TCR pairing. *Front. Immunol.* **10**, 1516.
17. Zhang, Z., et al. (2021). Mapping the functional landscape of TCR repertoires by single-T cell transcriptomics (tessa). *Nat. Methods* **18**, 92–99.
18. Schattgen, S.A., et al. (2022). Integrating TCR sequences and transcriptional profiles by CoNGA. *Nat. Biotechnol.* **40**, 54–63.
19. COMBAT Consortium (2022). A blood atlas of COVID-19. *Cell* **185**, 916–938.e58.
20. Ren, X., et al. (2021). COVID-19 immune features by single-cell transcriptome atlas. *Cell* **184**, 5838.
21. Stephenson, E., et al. (2021). Single-cell multi-omics of immune response in COVID-19. *Nat. Med.* **27**, 904–916.
22. Dominguez Conde, C., et al. (2022). Cross-tissue immune cell analysis. *Science* **376**, eabl5197.
23. Boutet, S.C., et al. (2019). Characterization of antigen-specific CD8 T cells using multi-omics single cell analysis. *J. Immunol.* **202**, 131–134.
24. Suo, C., et al. (2022). Mapping the developing human immune system. *Science* **376**, eabo0510.
25. Su, Y., et al. (2020). Multi-Omics Resolves Disease-State Shift in COVID-19. *Cell* **183**, 1479–1495.e20.
30. Atchley, W.R., et al. (2005). Solving the protein sequence metric problem. *PNAS* **102**, 6395–6400.
36. Li, J., et al. (2022). KIR+CD8+ T cells suppress pathogenic T cells. *Science* **376**, eabi9591.
41. Manfras, B.J., et al. (1999). Non-productive human TCR β chain genes. *Hum. Immunol.* **60**, 1090–1100.
42. Kaech, S.M., and Ahmed, R. (2001). Memory CD8+ T cell differentiation. *Nat. Immunol.* **2**, 415–422.
45. Abdelfattah, N.S., et al. (2024). T-Switch: engineering safe T cell therapeutics. *Immunity* **57**, 2945–2958.e5.
53. Zhang, S.-Q., et al. (2016). Direct measurement of TCR affinity and sequence. *Sci. Transl. Med.* **8**, 341ra77.
57. Scott-Browne, J.P., et al. (2009). Germline-encoded amino acids in TCR control thymic selection. *Nature* **458**, 1043–1046.
71. Korsunsky, I., et al. (2019). Fast, sensitive integration of single-cell data with Harmony. *Nat. Methods* **16**, 1289–1296.
72. Kang, J.B., et al. (2021). Efficient single-cell reference atlas mapping with Symphony. *Nat. Commun.* **12**, 5890.
73. Amari, S., et al. (1997). Asymptotic statistical theory of overtraining. *IEEE Trans. Neural Netw.* **8**, 985–996.
