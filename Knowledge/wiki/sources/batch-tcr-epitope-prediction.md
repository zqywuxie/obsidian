---
title: Batch Source — TCR-Epitope Binding Prediction
tags: [source, batch, tcr, epitope, binding-prediction, deep-learning]
created: 2026-05-06
updated: 2026-05-06
---

# TCR-Epitope Binding Prediction — 文献合集

> 本页汇总 TCR 与抗原表位结合预测的计算方法文献。

---

## 综述

### Lu — Assessment of computational methods in predicting TCR–epitope binding recognition
- **要点**: 对现有 TCR-表位结合预测计算方法的系统性评估；比较不同方法在多个 benchmark 上的性能
- **文件**: `raw/pdfs/Lu - Assessment of computational methods in predicting TCR–epitope binding recognition.pdf`

---

## 深度学习方法

### Sidhom et al. 2021 — DeepTCR: a deep learning framework for revealing sequence concepts within T-cell repertoires
- **期刊**: *Nature Communications* (2021)
- **DOI**: 10.1038/s41467-021-22479-5
- **要点**: DeepTCR 框架：用 VAE（变分自编码器）无监督学习 TCR 序列特征；可同时对 TCR 库进行聚类、抗原特异性预测、特征提取；整合 CDR3 序列和 V/J 基因使用信息
- **文件**: `raw/pdfs/Sidhom 等 - 2021 - DeepTCR is a deep learning framework for revealing sequence concepts within T-cell repertoires.pdf`

### Fischer et al. 2020 — Predicting antigen specificity of single T cells based on TCR
- **期刊**: *Nature Biotechnology* (2020)
- **要点**: 基于 TCR 序列预测单个 T 细胞的抗原特异性；单细胞水平验证预测
- **文件**: `raw/pdfs/Fischer 等 - 2020 - Predicting antigen specificity of single T cells based on TCR.pdf`

### Kim et al. 2023 — TSpred: a robust prediction framework for TCR-epitope interactions based on ensemble deep learning
- **期刊**: 2023
- **要点**: TSpred：基于集成深度学习（ensemble）的 TCR-表位相互作用预测框架；提高预测的鲁棒性和泛化能力
- **文件**: `raw/pdfs/Kim 等 - 2023 - TSpred a robust prediction framework for TCR-epitope interactions based on an ensemble deep learnin.pdf`

### Zhao et al. 2025 — A unified deep framework for peptide-MHC-TCR binding prediction
- **期刊**: 2025
- **要点**: 统一框架同时预测肽-MHC 和 TCR 结合；pMHC-TCR 三分子复合物的端到端预测
- **文件**: `raw/pdfs/Zhao 等 - 2025 - A unified deep framework for peptide–major histocompatibility complex–T cell receptor binding predic.pdf`

### Seo & Rhee 2025 — TCR-epiDiff: solving dual challenges of TCR generation and binding prediction
- **期刊**: 2025
- **要点**: TCR-epiDiff：用扩散模型同时解决 TCR 生成和结合预测的双重挑战；扩散模型在免疫组学中的新应用
- **文件**: `raw/pdfs/Seo和Rhee - 2025 - TCR-epiDiff solving dual challenges of TCR generation and binding prediction.pdf`

---

## 表示学习

### Jiang et al. 2023 — TCR2vec: a deep representation learning framework of T-cell receptor sequence and function
- **期刊**: 2023
- **要点**: TCR2vec：深度表示学习框架，将 TCR 序列编码为功能相关的向量表示；面向 TCR 序列的专用 embedding 方法
- **文件**: `raw/pdfs/Jiang 等 - 2023 - TCR2vec a deep representation learning framework of T-cell receptor sequence and function.pdf`

### Ostrovsky-Berman et al. 2021 — Immune2vec: embedding TCR sequences in ℝ^N using natural language processing
- **期刊**: 2021
- **要点**: Immune2vec：用 NLP 方法（Word2Vec 类方法）将 TCR 序列嵌入到向量空间；利用序列上下文信息学习 representation
- **文件**: `raw/pdfs/Ostrovsky-Berman 等 - 2021 - Immune2vec embedding BT cell receptor sequences in ℝN using natural language processing.pdf`

### Wu et al. — TCR-BERT: learning the grammar of T-cell receptors for flexible antigen-binding analyses
- **期刊**: (预印本/2023)
- **要点**: TCR-BERT：基于 BERT 的 TCR 语言模型；学习 TCR 序列的"语法"用于灵活的下游任务（抗原结合预测等）；预训练 + 微调范式
- **文件**: `raw/pdfs/Wu 等 - TCR-BERT learning the grammar of T-cell receptors for flexible antigen-binding analyses.pdf`

---

## 数据库

### Chen et al. 2021 — TCRdb: a comprehensive database for T-cell receptor sequences
- **期刊**: *Nucleic Acids Research*
- **DOI**: 10.1093/nar/gkaa1040
- **要点**: TCRdb：综合性 TCR 序列数据库；支持强大的序列搜索功能；整合多个公共数据集的标准化资源
- **文件**: `raw/pdfs/Chen 等 - 2021 - TCRdb a comprehensive database for T-cell receptor sequences with powerful search function.pdf`

---

**本批合计 10 篇文献**
