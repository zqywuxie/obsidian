---
title: TCRCellNet — 课题文献与支持内容
tags: [project, tcr, immunoinformatics, single-cell]
created: 2026-05-15
updated: 2026-05-15
---

# TCRCellNet

> 课题相关文献归档与支持内容管理目录。

---

## 目录结构

```
TCRCellNet/
├── README.md                   ← 本索引文件
├── papers/                     ← 课题核心文献（每篇论文独立目录）
│   ├── chen-2023-tcr-dominant-phenotype/
│   │   ├── paper.md            ← 精读双语全文
│   │   ├── PIIS2211124723012913.pdf  ← 原始 PDF
│   │   ├── PIIS2211124723012913.txt  ← pdftotext 提取文本
│   │   └── assets/             ← 提取的图表
│   ├── monian-2021-peanut-oit/     ← (待创建)
│   ├── afik-2017-trapes/           ← (待创建)
│   └── ...
├── notes/                      ← 个人笔记、思路、实验设计
└── data/                       ← 数据资源、跑题结果、中间文件
```

---

## 已归档文献

| # | 文献 | 精读 | 类型 | 归档日期 |
|---|------|------|------|----------|
| 1 | [[wiki/sources/chen-2023-cell-reports-tcr-dominant-phenotype\|TCR dominant phenotype — Chen et al. 2023, Cell Reports]] | [[TCRCellNet/papers/chen-2023-tcr-dominant-phenotype/paper.md\|📖 精读]] | TCR 序列主导 CD8+ T 细胞表型 | 2026-05-15 |
| 2 | [[wiki/sources/monian-2021-jci-peanut-oit\|Peanut OIT — Monian et al. 2022, JCI]] | — | scRNA-seq + TCR / 食物过敏免疫治疗 | 2026-05-15 |
| 3 | [[wiki/sources/afik-2017-trapes\|TRAPeS — Afik et al. 2017, Nucleic Acids Research]] | — | TCR 重建工具 | 2026-05-15 |

---

## 关联 Wiki 页面

- [[wiki/sources/afik-2017-trapes]] — TRAPeS 论文来源摘要
- [[wiki/sources/monian-2021-jci-peanut-oit]] — 花生 OIT 论文来源摘要
- [[wiki/sources/chen-2023-cell-reports-tcr-dominant-phenotype]] — TCR 序列主导 CD8+ T 细胞表型
- [[wiki/concepts/tcr-repertoire]] — TCR 库概念
- [[wiki/concepts/single-cell-tcr-seq]] — 单细胞 TCR-seq 概念

---

## 项目笔记

> 待补充。



# softlabel设计
原：细胞功能状态硬编码
现：细胞分化 连续概率过程
	1. 主 supervision ： UCell/AUCell programs（细胞的可能功能状态）
	2. 辅 supervision ： Palantir pseudotime（细胞的分化程度 不同谱系分化程度不同）？？
	3. entropy：对于主supervision 细胞状态模糊的判断



TCRdist：
	针对基因 和 VJ使用频率的分析


	CD4+ TFH/TN/TM/Treg


1. 输入：  
    基于 TCR的 CDR3 序列及 V/J usage 作为模型输入特征。
2. Label/reference 构建：  
    基于配对 scRNA-seq raw data，通过 marker gene program 构建多个功能维度（soft label）（如 cytotoxicity、exhaustion等），形成连续 functional-state manifold，并以此作为 reference。不同细胞亚型在该 manifold 中形成各自的功能区域分布。
	- **Q：TCR-seq 能否学到多维度信息？感觉不太行**
	- expression-density（验证维度的可行性）：expression相近的细胞，是否在 manifold 上局部连续
		- expression：该细胞当前功能维度的得分
		- density：周围细胞是否有类似功能状态
3. 模型预测与输出：  
    模型学习：

```
TCR (CDR3 + V + J)    ->functional manifold coordinates
```
预测得到的多维功能向量投影到 reference 中，取相似度最大的作为最终亚型。
![[Pasted image 20260520195053.png]]

**每个维度的correction**


相同TCR序列的细胞表型倾向相似但不完全相同，​**​且年龄差异会放大表型差异​**​。她指出同一TCR克隆可出现在不同T细胞亚群，​**​说明TCR序列并非衰老表型变化的唯一决定因素​**​。