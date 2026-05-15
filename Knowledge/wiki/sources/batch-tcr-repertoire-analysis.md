---
title: Batch Source — TCR Repertoire Analysis & ML
tags: [source, batch, tcr, repertoire, machine-learning]
created: 2026-05-06
updated: 2026-05-06
---

# TCR Repertoire Analysis & Machine Learning — 文献合集

> 本页汇总 TCR  repertoire 分析及机器学习应用于 repertoire 研究的相关文献。

---

## 综述

### Katayama et al. 2022 — Machine learning approaches to TCR repertoire analysis
- **期刊**: *Frontiers in Immunology* (综述)
- **DOI**: 10.3389/fimmu.2022.858057
- **要点**: TCR 多样性由 V(D)J 重组产生（潜在 > 10¹³ 种）；TCR 库受 MHC 多态性、衰老（immunosenescence）、抗原暴露影响；ML/DL 在 repertoire 分析中的应用包括：多样性度量、聚类、特征提取、疾病分类；PCR 和 NGS 引入的 batch effect 是 ML 分析的重要考量
- **文件**: `raw/pdfs/Katayama 等 - 2022 - Machine learning approaches to TCR repertoire analysis.pdf`

### Chiffelle et al. 2020 — T-cell repertoire analysis and metrics of diversity and clonality
- **期刊**: *Current Opinion in Biotechnology*
- **DOI**: 10.1016/j.copbio.2020.10.011
- **要点**: T 细胞库多样性和克隆性指标综述；不同指标（Shannon, Simpson, Chao1 等）的适用场景和局限性；强调标准化分析流程的重要性
- **文件**: `raw/pdfs/Chiffelle 等 - 2020 - T-cell repertoire analysis and metrics of diversity and clonality.pdf`

---

## TCR 库特征分析

### Dash et al. 2017 — Quantifiable predictive features define epitope-specific TCR repertoires
- **期刊**: *Nature* (2017)
- **DOI**: 10.1038/nature22383
- **要点**: 通过分析抗原特异性 TCR 库发现可量化的预测特征；CDR3 序列的物理化学性质可以预测抗原特异性；开创性工作，开启了 TCR 库的定量预测分析
- **文件**: `raw/pdfs/Dash 等 - 2017 - Quantifiable predictive features define epitope-specific T cell receptor repertoires.pdf`

### Emerson et al. 2017 — Immunosequencing identifies signatures of CMV exposure and HLA-mediated effects
- **期刊**: *Nature Genetics*
- **要点**: 大规模免疫测序揭示 CMV 暴露的 repertoire 特征；HLA 对 repertoire 组成有系统性影响；> 10^6 条序列的大规模分析
- **文件**: `raw/pdfs/Emerson 等 - 2017 - Immunosequencing identifies signatures of cytomegalovirus exposure history and HLA-mediated effects.pdf`

### Luppov et al. 2025 — Comprehensive analysis of αβTCR repertoires reveals signatures of thymic selection
- **期刊**: 2025
- **要点**: αβTCR 库的综合分析揭示胸腺选择的特征；探索胸腺选择在 repertoire 形成中留下的序列特征
- **文件**: `raw/pdfs/Luppov 等 - 2025 - Comprehensive analysis of αβT-cell receptor repertoires reveals signatures of thymic selection.pdf`

### Textor et al. 2023 — ML analysis of TCR repertoire identifies sequence features of self-reactivity
- **期刊**: 2023
- **要点**: 用 ML 方法分析 TCR 库识别自身反应性的序列特征；区分 self-reactive 和 non-self-reactive TCR
- **文件**: `raw/pdfs/Textor 等 - 2023 - Machine learning analysis of the T cell receptor repertoire identifies sequence features of self-rea.pdf`

### Ostmeyer et al. 2019 — Biophysicochemical motifs in TCR sequences distinguish repertoires from tumor infiltrating...
- **期刊**: 2019
- **要点**: TCR 序列中的生物物理化学基序可以区分肿瘤浸润 vs 外周血的 repertoire
- **文件**: `raw/pdfs/Ostmeyer 等 - 2019 - Biophysicochemical motifs in T cell receptor sequences distinguish repertoires from tumor infiltrati.pdf`

---

## TCR 生成模型

### Isacchini et al. 2021 — Deep generative selection models of T and B cell receptor repertoires with soNNia
- **期刊**: *Nature Communications*
- **DOI**: 10.1038/s41467-021-26891-1
- **要点**: soNNia 模型：用深度生成模型对 TCR 库进行 selection 分析；分离 V(D)J 重组的"生成概率"和"选择概率"；可定量评估正向/负向选择对 repertoire 的影响
- **文件**: `raw/pdfs/Isacchini 等 - 2021 - Deep generative selection models of T and B cell receptor repertoires with soNNia.pdf`

---

## 应用 & 数据集

### Lagattuta et al. 2025 — TCR sequence influences likelihood of T cell memory formation
- **期刊**: 2025
- **要点**: TCR 序列本身影响 T 细胞形成记忆的可能性；序列特征可预测记忆 vs 效应分化偏好
- **文件**: `raw/pdfs/Lagattuta 等 - 2025 - The T cell receptor sequence influences the likelihood of T cell memory formation.pdf`

### Masopust et al. 2025 — Guidelines for T cell nomenclature
- **期刊**: 2025
- **要点**: T 细胞命名的国际指南；统一不同 T 细胞亚群的命名标准
- **文件**: `raw/pdfs/Masopust 等 - 2025 - Guidelines for T cell nomenclature.pdf`

### Xue et al. 2025 — A pan-disease and population-level single-cell TCRαβ repertoire reference
- **期刊**: 2025
- **要点**: 跨疾病、人群水平的单细胞 TCRαβ repertoire 参考图谱
- **文件**: `raw/pdfs/Xue 等 - 2025 - A pan-disease and population-level single-cell TCRαβ repertoire reference.pdf`

---

**本批合计 12 篇文献**
