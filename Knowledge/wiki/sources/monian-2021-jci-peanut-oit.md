---
title: "Peanut OIT differentially suppresses clonally distinct Th subsets — Monian et al. 2022, JCI"
tags: [source, tcr, scrna-seq, oit, peanut-allergy, th2, t-cell-subsets]
created: 2026-05-15
updated: 2026-05-15
sources:
  - type: paper
    title: "Peanut oral immunotherapy differentially suppresses clonally distinct subsets of T helper cells"
    doi: "10.1172/JCI150634"
    pmid: "34813505"
    pmcid: "PMC8759778"
    journal: "Journal of Clinical Investigation. 2022;132(2):e150634"
    authors: "Monian B, Tu AA, Ruiter B, et al."
    url: "https://doi.org/10.1172/JCI150634"
    pdf: "raw/pdfs/Monian_2021_JCI_peanut_OIT.pdf"  # OA, 需手动保存
  - type: code
    repo: "mitlovelab/PNOIT2_scRNAseq"
    url: "https://github.com/mitlovelab/PNOIT2_scRNAseq"
    description: "分析代码 (R/Python/MATLAB)"
  - type: data
    accession: "GSE158667"
    database: "GEO"
    url: "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158667"
    description: "Processed expression + TCR clonotype data"
  - type: data
    accession: "phs001897.v2.p1"
    database: "dbGaP"
    description: "FASTQ 原始数据 (受控访问)"
  - type: trial
    name: "NCT01750879"
    url: "https://clinicaltrials.gov/ct2/show/NCT01750879"
    description: "Peanut OIT Clinical Trial"
---

# Peanut OIT 差异化抑制 Th 细胞亚群

> 来源：JCI 论文页面 — https://www.jci.org/articles/view/150634
> 追溯 DOI: [10.1172/JCI150634](https://doi.org/10.1172/JCI150634)

---

## 一、来源 URL 摘要

本文为 JCI（Journal of Clinical Investigation）2022 年的研究论文，利用单细胞 RNA-Seq + 配对 TCRα/β 测序，系统解析了花生口服免疫治疗（OIT）过程中花生反应性 CD4⁺ T 辅助细胞的异质性及临床转归关联。

---

## 二、原始论文核心信息

| 维度 | 内容 |
|------|------|
| **科学问题** | OIT 临床结局差异的免疫学基础是什么？不同 Th 亚群对 OIT 的反应如何？ |
| **方法** | 20h 花生蛋白刺激 → FACS (CD154⁺/CD137⁺) → Seq-Well scRNA-seq + 配对 TCRα/β → 稀疏 PCA 基因模块 |
| **样本** | 12 名花生过敏患者，纵向 4 时间点，总计 134,129 个细胞转录组 |
| **关键发现** | ① 6 个克隆性不同的 Th 亚群；② OIT 选择性抑制 Th2A/Th1-conv 而非 Tfh-like；③ 基线炎症特征预测治疗失败 |
| **工具产出** | 基因模块分析框架 + 花生反应性 T 细胞参考数据集 |

---

## 三、数据与代码资源清单

| 类型 | 资源 | 用途 |
|------|------|------|
| 💻 **分析代码** | GitHub [mitlovelab/PNOIT2_scRNAseq](https://github.com/mitlovelab/PNOIT2_scRNAseq) | 全部分析脚本 (R/Python/MATLAB) |
| 📊 **表达数据** | GEO [GSE158667](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158667) | 处理后的表达矩阵 + TCR clonotype |
| 🧬 **原始 FASTQ** | dbGaP phs001897.v2.p1 | 原始测序数据（受控访问） |
| 🏥 **临床试验** | ClinicalTrials.gov [NCT01750879](https://clinicaltrials.gov/ct2/show/NCT01750879) | 临床试验注册信息 |

---

## 四、与当前研究的关联

| 角度 | 本文 (Monian 2022) | 关联 |
|------|-------------------|------|
| **单细胞 + TCR 策略** | Seq-Well + 捕获探针 TCR 富集 | 与 [[wiki/sources/afik-2017-trapes\|TRAPeS]] 互补：本文用靶向富集法，TRAPeS 用计算重建法 |
| **CD4⁺ T 细胞异质性** | Th2A, Tfh2, Th1-conv 等 6 亚群 | 可参考 [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] 和 [[wiki/concepts/single-cell-tcr-seq\|Single-cell TCR-seq]] 概念 |
| **TCR 与功能状态** | 克隆型与 Th 亚型高度关联 | 与 TRAPeS 中 CDR3 长度与分化状态关联的发现一致 |

---

## 五、分析笔记

### 方法学亮点

1. **CD154/CD137 双标志物富集策略** — 相比于单用 CD154（可能遗漏 Treg）或单用 CD137（可能遗漏效应细胞），同时捕获效应性和调节性花生反应性 T 细胞
2. **稀疏 PCA 基因模块** — 非监督地识别 50 个共表达基因模块，而非依赖 pre-defined 基因集评分
3. **TCRdist 分析** — 定量化 TCR 序列相似性，证明同一 Th 亚型内存在 TCR 汇聚现象

### 与 TCRCellNet 课题的潜在联结点

- **TCR 序列特征与功能状态的关联**：本文证明 Th 亚型间 TCR 库高度分离，且存在 TCR 汇聚现象 → 支持 TCR 结构影响 T 细胞命运决定
- **OIT 作为 TCR 功能的体内扰动**：OIT 不删除克隆而抑制功能 → 提示 TCR 信号可塑性
- **基线预测特征**：OX40-OX40L、STAT1、Th17 信号等可作为免疫治疗反应的预测标志物

### PDF 状态

JCI 为开放获取期刊，PDF 可从 [JCI 页面](https://www.jci.org/articles/view/150634) 或 [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8759778/) 下载。当前环境自动下载受限，需手动保存。

