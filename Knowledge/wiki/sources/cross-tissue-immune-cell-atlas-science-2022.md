---
title: "Cross-tissue immune cell atlas — Domínguez Conde et al. Science 2022"
tags: [source, immune-cell-atlas, scrna-seq, celltypist, tissue-immunology]
created: 2026-05-15
updated: 2026-05-15
sources:
  - type: article
    title: "人体免疫细胞跨组织分布图谱"
    url: "https://mp.weixin.qq.com/s/zn23xJ4dBGRGVw9lKcotqA"
    site: "流式中文网"
  - type: paper
    title: "Cross-tissue immune cell analysis reveals tissue-specific features in humans"
    doi: "10.1126/science.abl5197"
    pmid: "35549406"
    journal: "Science. 2022;376(6594):eabl5197"
    url: "https://www.science.org/doi/10.1126/science.abl5197"
    pdf: null  # 非开放获取，Science 付费墙
  - type: code
    repo: "Teichlab/celltypist"
    url: "https://github.com/Teichlab/celltypist"
    description: "自动细胞注释工具（逻辑回归 + SGD）"
  - type: code
    repo: "Teichlab/TissueImmuneCellAtlas"
    url: "https://github.com/Teichlab/TissueImmuneCellAtlas"
    description: "数据分析预处理和可视化 notebooks"
  - type: data
    accession: "E-MTAB-11536"
    database: "ArrayExpress"
    url: "https://www.ebi.ac.uk/biostudies/studies/E-MTAB-11536"
    description: "scRNA-seq + VDJ-seq 原始 FASTQ 文件"
  - type: tool
    name: "CellTypist"
    url: "https://www.celltypist.org/"
    description: "自动细胞注释在线平台"
  - type: visualization
    name: "Tissue Immune Cell Atlas"
    url: "https://www.tissueimmunecellatlas.org/"
    description: "处理后数据的交互式浏览门户"
  - type: visualization
    name: "UCSC Cell Browser"
    url: "https://cells.ucsc.edu/?ds=cross-tissue-maps"
    description: "UCSC 交互式单细胞浏览"
---

# Cross-tissue immune cell atlas (Science 2022)

> 来源：流式中文网公众号科普文章 → 追溯原文 + 代码 + 数据资源

---

## 一、来源 URL 摘要

本文来自**流式中文网**微信公众号，是对 2022 年 *Science* 论文 *Cross-tissue immune cell analysis reveals tissue-specific features in humans* 的中文科普解读。

### 科普文章核心转述

- 对 12 名成年器官捐献者的 **16 种匹配组织** 进行 scRNA-seq + TCR/BCR 测序
- 整合 **19 个公共数据集**，覆盖 **20 种组织** 的免疫细胞数据
- 开发 **CellTypist**（逻辑回归 + SGD 梯度下降）实现自动细胞注释，F1 ≈ 0.9
- 鉴定出 **101 种免疫细胞类型/状态**

### 转述准确度评估

整体质量较高，核心发现（巨噬细胞组织限制性、B 细胞/浆细胞分布、TRM 特征、TCR 克隆共享等）均准确。无明显简化或偏差，缺失的主要是 CellTypist 算法的技术细节。

---

## 二、原始论文核心信息

| 维度 | 内容 |
|------|------|
| **科学问题** | 免疫细胞在不同组织中的表型、功能和克隆分布差异——跳出"以血液为中心"的传统框架 |
| **样本** | 12 名成年器官捐献者，16 种匹配组织（含 LN、脾、肝、肺、肠、骨髓、皮肤等） |
| **方法** | scRNA-seq + VDJ-seq（TCR/BCR）→ CellTypist 自动注释 → 流式蛋白验证 |
| **关键发现** | ① 巨噬细胞极强的组织限制性；② B 细胞/浆细胞组织特异性 IgG/IgA 偏好；③ 同一 T 克隆可跨组织分布为不同功能状态；④ CCR7⁺ 迁移性 DC 异常表达 AIRE |
| **工具产出** | CellTypist 自动注释工具 + 泛组织免疫参考模型 |

---

## 三、数据与代码资源清单

| 类型 | 资源 | 用途 |
|------|------|------|
| 📊 **原始数据** | ArrayExpress [E-MTAB-11536](https://www.ebi.ac.uk/biostudies/studies/E-MTAB-11536) | scRNA-seq + VDJ-seq FASTQ |
| 💻 **分析代码** | GitHub [Teichlab/TissueImmuneCellAtlas](https://github.com/Teichlab/TissueImmuneCellAtlas) | 预处理 + 分析 notebook |
| 🔧 **注释工具** | [CellTypist](https://github.com/Teichlab/celltypist) / [celltypist.org](https://www.celltypist.org/) | 自动细胞注释（Python） |
| 🌐 **可视化门户** | [tissueimmunecellatlas.org](https://www.tissueimmunecellatlas.org/) | 处理数据在线浏览 |
| 🧬 **UCSC 浏览** | [cells.ucsc.edu/?ds=cross-tissue-maps](https://cells.ucsc.edu/?ds=cross-tissue-maps) | 交互式单细胞 UMAP |

---

## 四、与当前研究的关联

这篇 2022 年泛组织免疫图谱与当前正在精读的 **THK 论文（Xie et al. 2026）** 互补：

| 角度 | 2022 Science (Domínguez Conde) | 2026 Nat Immunol (Xie et al.) |
|------|-------------------------------|-------------------------------|
| **定位** | 描述性图谱——**普查** | 因果性验证——**聚焦** |
| **方法** | 生信为主 + 流式验证 | 生信发现 → 完整功能验证 |
| **范围** | 泛组织、101 种免疫细胞 | 单个新亚群（THK） |
| **产出** | CellTypist + 参考数据库 | EOMES-GZMK 调控轴 |

THK 论文中 Fig 1a 使用的 scIBD 数据集正是这类大规模跨组织参考数据的重要应用——没有这些公共参考图谱，很难在异质性 T 细胞群体中准确定位 GZMK^high 亚群。

---

## 五、分析笔记

CellTypist 作为一个基于逻辑回归 + SGD 的自动注释工具，其优势在于：
1. **速度快**——线性分类器，比神经网络快 1-2 个数量级
2. **可解释**——概率输出，可直接判断置信度
3. **分层预测**——支持高分辨率（98 类）和低分辨率（32 类）两级切换
4. **模型共享**——预训练模型可直接部署到新数据集

与 THK 论文的 CellTypist 潜在关联：在 THK 的研究中，重分析 scIBD 数据集时通过将原始"CD4 Temra"簇再分亚簇才找到 GZMK^high 群体——如果当时有 CellTypist 的泛组织免疫参考模型，是否能自动识别出这个群体？值得后续探索。
