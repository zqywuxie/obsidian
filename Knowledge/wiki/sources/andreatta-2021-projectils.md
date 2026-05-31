---
title: "ProjecTILs — Andreatta & Carmona 2021"
tags: [source, paper, single-cell, T-cell, reference-atlas, bioinformatics]
created: 2026-05-20
updated: 2026-05-20
sources:
  - type: paper
    title: "Interpretation of T cell states from single-cell transcriptomics data using reference atlases"
    authors: "Andreatta M, Carmona SJ"
    journal: "Nature Communications, 2021; 12:6889"
    doi: "10.1038/s41467-021-23324-4"
    url: "https://doi.org/10.1038/s41467-021-23324-4"
  - type: code
    repo: "GitHub: carmonalab/ProjecTILs"
    url: "https://github.com/carmonalab/ProjecTILs"
  - type: code
    repo: "GitHub: carmonalab/STACAS"
    url: "https://github.com/carmonalab/STACAS"
  - type: code
    repo: "Case studies"
    url: "https://github.com/carmonalab/ProjecTILs_CaseStudies"
  - type: data
    accession: "figshare TIL atlas"
    url: "https://doi.org/10.6084/m9.figshare.12478571"
  - type: data
    accession: "figshare viral atlas"
    url: "https://doi.org/10.6084/m9.figshare.12489518"
aliases:
  - "ProjecTILs"
  - "Andreatta 2021"
  - "reference atlas projection"
---

# ProjecTILs: 参考图谱投影解读T细胞状态

## 来源摘要

本文来自 **Nature Communications** (2021)，由 Santiago Carmona 实验室的 Massimo Andreatta 完成。论文提出了 **ProjecTILs**，一种通过将新 scRNA-seq 数据投影到参考图谱上来解读 T 细胞状态的计算框架。

## 核心方法

ProjecTILs 包含以下关键步骤：

1. **参考图谱构建**：使用 STACAS 整合多来源 scRNA-seq 数据，构建了小鼠 TIL（9 亚型）和 LCMV 感染（7 亚型）两个参考图谱
2. **图谱投影**：将 query 数据与参考对齐后，应用参考的 PCA/UMAP 变换嵌入到参考空间，参考结构不变
3. **亚型分类**：最近邻分类器基于参考注释预测 query 细胞亚型
4. **ICA 判别分析**：比较 query 与参考在 ICA 维度上的差异，识别改变的基因程序
5. **偏离检测**：识别参考中未覆盖的新型细胞状态

## 主要发现

- **TIL 9 亚型框架**：naive-like (CD4/CD8), EM, early-activation, Tex, Tpex, Th1, Tfh, Treg — 在肿瘤和感染中保守
- **miR-155 KO** → T 细胞无法活化，滞留在 naive-like 状态
- **Regnase-1 KO** → 增加 Tpex 比例 + 下调 LAG3/NKG2A 抑制程序（ICA 25）
- **跨物种投影**：人 TIL scRNA-seq 可通过直系同源基因投影到小鼠图谱，准确分类
- **132 活检荟萃分析**：表达谱按 TIL 亚型而非研究/癌种/物种聚类（p < 3×10⁻⁶）
- **人 CD8+ TIL 分化模型**：EM (CXCR3⁺, pre-exhausted) → Tpex (TOX⁺ XCL1⁺, quiescent) → Tex (terminal, highly proliferative)

## 资源链接

- **论文**: https://doi.org/10.1038/s41467-021-23324-4
- **ProjecTILs**: https://github.com/carmonalab/ProjecTILs
- **STACAS**: https://github.com/carmonalab/STACAS
- **Case Studies**: https://github.com/carmonalab/ProjecTILs_CaseStudies
- **精读笔记**: [[Knowledge/papers/projectils-2021/paper.md|ProjecTILs 精读]]
