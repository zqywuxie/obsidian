---
title: TCR-Epitope Binding Prediction
tags: [concept, tcr, epitope, prediction, deep-learning, machine-learning]
created: 2026-05-06
updated: 2026-05-06
---

# TCR-Epitope Binding Prediction（TCR-表位结合预测）

> 基于 TCR 序列预测其识别的抗原表位，是免疫信息学中的核心挑战之一。

---

## 问题定义

给定 TCR 序列（通常为 CDR3β）和一个已知的抗原肽（epitope），预测该 TCR 是否能识别该肽。这本质上是一个**二分类问题**（结合/不结合）。

### 难点
- TCR 多样性极高（> 10¹³），实验验证稀疏
- 同一表位能被大量不同 TCR 识别（convergent recombination）
- 同一 TCR 可能有交叉反应性（cross-reactivity）
- 缺少系统性负样本数据（无法验证"不结合"）

---

## 计算方法分类

### 1. 序列相似性方法
基于已知的 TCR-表位对，通过序列相似性推断
- **代表工具**：GLIPH, TCRMatch
- **优点**：简单直观
- **缺点**：无法泛化到序列距离较远的 TCR

### 2. 物理化学特征方法
将 TCR 序列编码为物理化学特征（电荷、疏水性等）
- Dash et al. (2017) 开创性工作：鉴定抗原特异性 TCR 库的定量预测特征
- Ostmeyer et al. (2019)：生物物理化学基序区分肿瘤浸润 vs 外周血
- Textor et al. (2023)：ML 识别自身反应性 TCR 的序列特征

### 3. 深度学习方法

#### 表示学习（Embedding）
| 方法 | 年份 | 策略 |
|------|------|------|
| **Immune2vec** | 2021 | Word2Vec 类方法做 TCR 序列 embedding |
| **TCR2vec** | 2023 | 深度表示学习编码序列和功能 |
| **TCR-BERT** | 2023 | 基于 BERT 的 TCR 语言模型，预训练+微调 |

#### 端到端预测
| 方法 | 年份 | 特点 |
|------|------|------|
| **DeepTCR** | 2021 | VAE 无监督学习，整合 CDR3 及 V/J 基因 |
| **ERGO-II / pMTnet** | 2021 | 结合 pMHC 和 TCR 特征 |
| **TSpred** | 2023 | 集成深度学习，提高鲁棒性 |
| **DLpTCR / TITAN** | 2021-2023 | 不同架构的预测框架 |

#### 最新进展
| 方法 | 年份 | 创新点 |
|------|------|--------|
| **Zhao et al. Unified** | 2025 | 统一框架同时预测肽-MHC 和 TCR 结合 |
| **TCR-epiDiff** | 2025 | 扩散模型同时处理 TCR 生成和结合预测 |

---

## 代表性方法详解

### DeepTCR (Sidhom et al. 2021)
- VAE 无监督学习 CDR3α 和 CDR3β 序列的潜在表征
- 同时实现：聚类、抗原特异性预测、特征重要性分析
- 框架开源，支持多任务学习

### TCR-BERT (Wu et al.)
- 将 BERT 架构应用于 TCR 序列建模
- 大规模 TCR 序列预训练 → 学习序列的"语法"
- 下游任务微调：抗原特异性、结合预测
- 泛化能力优于传统方法

### TCR-epiDiff (Seo & Rhee 2025)
- 扩散模型（Diffusion Model）的新应用
- 双重功能：TCR 生成 + 结合预测
- 可生成针对给定表位的候选 TCR 序列

---

## Benchmark 与评估

主要挑战：
- 缺乏标准化的 benchmark 数据集
- 正负样本不平衡（已验证结合数据远少于未验证的）
- 不同研究使用的数据划分和评估指标不一

Lu (2025) 对现有计算方法进行了系统性评估。

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 概念 | [[wiki/concepts/single-cell-tcr-seq\|Single-cell TCR-seq]] |
| 来源 | [[wiki/sources/batch-tcr-epitope-prediction\|TCR-表位预测文献合集]] |
| 实体 | [[wiki/entities/tcrdb\|TCRdb 数据库]] |

**引用文献**: Sidhom 2021, Fischer 2020, Kim 2023, Zhao 2025, Seo 2025, Jiang 2023, Ostrovsky-Berman 2021, Wu TCR-BERT, Chen TCRdb, Dash 2017
