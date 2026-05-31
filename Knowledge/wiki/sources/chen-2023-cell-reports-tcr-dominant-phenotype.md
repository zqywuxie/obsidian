---
title: "TCR sequences are the dominant factor for CD8+ T cell phenotype — Chen et al. 2023, Cell Reports"
tags: [source, tcr, cd8, t-cell-phenotype, viral-immunology, covid-19, tcr-sequence]
created: 2026-05-15
updated: 2026-05-15
sources:
  - type: paper
    title: "T cell receptor sequences are the dominant factor contributing to the phenotype of CD8+ T cells with specificities against immunogenic viral antigens"
    doi: "10.1016/j.celrep.2023.113279"
    pmid: "37883974"
    pmcid: "PMC10729740"
    journal: "Cell Reports. 2023;42(11):113279"
    authors: "Chen DG, Xie J, Su Y, Heath JR."
    url: "https://doi.org/10.1016/j.celrep.2023.113279"
    pdf: "raw/pdfs/Chen_2023_CellReports_TCR_dominant_phenotype.pdf"  # OA，需手动从 PMC 保存
  - type: correction
    title: "Erratum"
    doi: "10.1016/j.celrep.2024.113841"
    description: "Figure 5C labeling correction, conclusions unaffected"
---

# TCR sequences are the dominant factor for CD8+ T cell phenotype

> 来源：Cell Reports 论文页面 — https://www.cell.com/cell-reports/fulltext/S2211-1247(23)01291-3
> 追溯 DOI: [10.1016/j.celrep.2023.113279](https://doi.org/10.1016/j.celrep.2023.113279)

---

## 一、来源 URL 摘要

URL 页面为 Cell Press 上的论文发表页面。本文发表于 *Cell Reports* 2023 年第 42 卷第 11 期，系统比较了 TCR 序列与环境信号对 CD8+ T 细胞表型的相对贡献。

---

## 二、原始论文核心信息

| 维度 | 内容 |
|------|------|
| **科学问题** | TCR 序列 vs 环境信号，哪个对 CD8+ T 细胞表型的决定作用更大？ |
| **方法** | 纵向 COVID-19 队列 + scRNA-seq/TCR-seq + 已知抗原特异性（四聚体分选）+ 计算建模 |
| **样本** | 68 名 COVID-19 患者，679 个 CD8+ T 细胞克隆型，3 种病毒抗原（SARS-CoV-2 / CMV / Influenza） |
| **关键发现** | TCR 序列是 CD8+ T 细胞表型和持久性的**主导因素**，远超环境信号的影响 |
| **意义** | 解释了 T 细胞表型在感染早期即被决定的机制，支持 TCR 序列可作为 T 细胞行为的预测因子 |

### 核心量化结论

- 无论针对哪种病毒抗原，TCR 序列对表型的贡献都压倒性地大于环境信号
- 即使是 bystander T 细胞（非抗原特异性活化），其表型也主要受 TCR 序列而非环境影响
- 表型在感染早期即被"编程"，后续变化有限

---

## 三、与当前研究的关联

| 角度 | 本文 (Chen 2023) | 与 TCRCellNet 的关联 |
|------|-------------------|---------------------|
| **TCR 决定表型** | TCR 序列 > 环境信号 | 与 [[wiki/sources/afik-2017-trapes\|TRAPeS (Afik 2017)]] 中 CDR3 长度与分化状态的关联一致 |
| **跨抗原通用性** | SARS-CoV-2 / CMV / Flu 结果一致 | 提示 TCR-表型关联是一个免疫学通则 |
| **CD8+ T 细胞** | 聚焦 CD8+ | 与 [[wiki/sources/monian-2021-jci-peanut-oit\|Peanut OIT (Monian 2022)]] 的 CD4+ Th 研究互补 |
| **早期决定** | 表型在感染早期决定 | 对疫苗设计、免疫治疗策略有重要启示 |

### 概念页联动

- [[wiki/concepts/tcr-repertoire]] — TCR 库概念框架
- [[wiki/concepts/tcr-epitope-prediction]] — TCR-表位结合预测
- [[wiki/concepts/single-cell-tcr-seq]] — 单细胞 TCR-seq 技术

---

## 四、分析笔记

### 为什么这篇论文对 TCRCellNet 极其重要

这是目前最直接证明 **"TCR 序列 → T 细胞功能表型"因果关系**的研究之一。如果能将 TCR 序列与表型/功能的关联定量化，就有可能：
1. 从 TCR 序列预测 T 细胞的分化状态和功能
2. 设计基于 TCR 序列的免疫治疗策略
3. 理解为什么不同 T 细胞克隆对同一抗原有不同反应

### 方法学亮点

- 利用 COVID-19 疫情期间的纵向队列，天然形成了"不同抗原在同一宿主环境下"的对照
- CMV 和 Influenza 特异性细胞作为"内部对照"——它们不受 SARS-CoV-2 新抗原驱动，但暴露于相同的炎症环境
- 通过比较同一患者体内不同抗原特异性的 T 细胞，优雅地解耦了 TCR 和环境的影响

### PDF 状态

开放获取，可从 PMC [PMC10729740](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10729740/) 下载。注意 2024 年的勘误（Figure 5C 标签修正）。

