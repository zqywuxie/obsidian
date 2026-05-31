---
title: "CoNGA — Schattgen et al. 2021"
tags: [source, paper, TCR, single-cell, graph-analysis, bioinformatics]
created: 2026-05-20
updated: 2026-05-20
sources:
  - type: paper
    title: "Integrating T cell receptor sequences and transcriptional profiles by clonotype neighbor-graph analysis (CoNGA)"
    authors: "Schattgen SA, Guion K, Crawford JC, Souquette A, Barrio AM, Stubbington MJT, Thomas PG, Bradley P"
    journal: "Nature Biotechnology, 2021; 40(1):54–63"
    doi: "10.1038/s41587-021-00989-2"
    pmid: "34426704"
    pmcid: "PMC8832949"
    url: "https://doi.org/10.1038/s41587-021-00989-2"
    pdf: "Knowledge/papers/schatgen-2021-conga/original.pdf"
  - type: code
    repo: "GitHub: phbradley/conga"
    url: "https://github.com/phbradley/conga"
  - type: data
    accession: "10x Genomics datasets"
    url: "https://www.10xgenomics.com/resources/datasets/"
  - type: data
    accession: "Human thymic T cell atlas"
    url: "https://developmentcellatlas.ncl.ac.uk/"
aliases:
  - "CoNGA"
  - "clonotype neighbor-graph analysis"
  - "Schattgen 2021"
---

# CoNGA: 克隆型邻域图分析整合 TCR 序列与转录谱

## 来源摘要

本文来自 **Nature Biotechnology** (2021)，由 St. Jude 儿童研究医院和 Fred Hutchinson 癌症研究中心的 Paul Thomas 和 Philip Bradley 团队合作完成。论文提出了 **CoNGA (Clonotype Neighbor-Graph Analysis)**，一种基于图论的统计方法，用于在单细胞数据集中系统性地发现 T 细胞受体（TCR）序列与基因表达谱（GEX）之间的相关性。

## 核心方法

CoNGA 包含两种分析模式：

1. **Graph-vs-graph（图-图分析）**：同时构建 GEX 相似图和 TCR 相似图（基于 TCRdist），统计检验每个克隆型在两个图中邻域的重叠显著性。显著克隆型（"CoNGA hits"）按共享的 GEX/TCR 簇分配分组为 "CoNGA clusters"。

2. **Graph-vs-feature（图-特征分析）**：将一侧的数值特征（如基因表达、CDR3 属性）映射到另一侧的相似图上，检测具有偏斜特征分布的图邻域。

## 主要发现

- **MAIT/iNKT 细胞**：CoNGA 正确识别了已知的非常规 T 细胞群体
- **HOBIT+/HELIOS+ CD8+ T 细胞**：一种此前未被描述的新群体，具有极长的 CDR3 区、富含色氨酸/半胱氨酸、表达 NK 细胞相关受体，可能是 MHC 非依赖性的"天然淋巴细胞"
- **EPHB6-TRBV30 相关性**：发现了 *EPHB6* 基因表达与 *TRBV30* 基因片段使用之间的高度显著相关性，机制源于基因组邻接（7 号染色体，~40kb间距）
- **pMHC 特异性 GEX 谱**：不同表位特异性的 T 细胞群体具有不同的基因表达谱
- **胸腺 T 细胞命运**：TCR 序列特征（TRAV 使用、CDR3 长度/属性）与胸腺细胞分化和 CD8/CD4 谱系选择相关

## 资源链接

- **论文**: https://doi.org/10.1038/s41587-021-00989-2
- **PMC**: https://pmc.ncbi.nlm.nih.gov/articles/PMC8832949/
- **GitHub**: https://github.com/phbradley/conga
- **精读笔记**: [[Knowledge/papers/schatgen-2021-conga/paper.md|CoNGA 精读]]
