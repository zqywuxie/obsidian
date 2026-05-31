---
title: "TRAPeS — Afik et al. 2017, Nucleic Acids Research"
tags: [source, tcr, scrna-seq, trapis, cdr3, t-cell-differentiation]
created: 2026-05-15
updated: 2026-05-15
sources:
  - type: paper
    title: "Targeted reconstruction of T cell receptor sequence from single cell RNA-seq links CDR3 length to T cell differentiation state"
    doi: "10.1093/nar/gkx615"
    pmid: "28934479"
    pmcid: "PMC5766189"
    journal: "Nucleic Acids Research. 2017;45(16):e148"
    authors: "Afik S, Yates KB, Bi K, et al."
    url: "https://doi.org/10.1093/nar/gkx615"
    pdf: "raw/pdfs/Afik_2017_TRAPeS.pdf"  # 开放获取，需手动从 PMC 下载
  - type: code
    repo: "YosefLab/TRAPeS"
    url: "https://github.com/YosefLab/TRAPeS"
    description: "TRAPeS — TCR Reconstruction Algorithm for Paired-end Single-cell RNA-seq (Python/C++)"
---

# TRAPeS — TCR 序列重建工具

> 来源：Afik et al. 2017, *Nucleic Acids Research*. URL: https://academic.oup.com/nar/article/45/16/e148/3976466
> 追溯 DOI: [10.1093/nar/gkx615](https://doi.org/10.1093/nar/gkx615)

---

## 一、来源 URL 摘要

URL 页面为 Oxford Academic 上的论文发表页面，包含标题、作者、摘要、引用信息及全文链接。本文直接获取的是 PMID 摘要信息及 PMC 开放获取全文。

### 页面核心内容

本文发表于 *Nucleic Acids Research* 2017 年第 45 卷第 16 期，介绍了 **TRAPeS** 工具的开发和应用。

---

## 二、原始论文核心信息

| 维度 | 内容 |
|------|------|
| **科学问题** | TCR 序列差异如何影响 T 细胞状态异质性？如何从 scRNA-seq 中高效提取 TCR 信息？ |
| **方法** | TRAPeS（迭代 Needleman–Wunsch 动态规划）→ 从短读长 scRNA-seq 重建 TCR → 结合转录组分析 |
| **样本** | 人类 YFV 特异性 CD8+ T 细胞 + 小鼠模型 |
| **关键发现** | "Naive-like" 记忆 CD8+ T 细胞的 CDR3 显著**更长**且与 germline 序列**差异更大** → TCR 使用与 T 细胞分化状态相关 |
| **工具产出** | TRAPeS — 开源 TCR 重建工具 |

### TRAPeS 算法特点

- 直接在原始 reads 上操作（非 k-mer），提高灵敏度
- 迭代动态规划延伸 V 和 J 片段直至重叠
- 可校正已知 V/J 基因区段的突变/SNP
- 可判断链的生产性（正确阅读框 + 无终止密码子）
- 最低支持 25 bp 双端读长

---

## 三、数据与代码资源清单

| 类型 | 资源 | 用途 |
|------|------|------|
| 💻 **源代码** | GitHub [YosefLab/TRAPeS](https://github.com/YosefLab/TRAPeS) | Python/C++ 实现 (SeqAn) |
| 📄 **全文** | PMC [PMC5766189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5766189/) | 开放获取全文 PDF |

---

## 四、与当前研究的关联

TRAPeS 作为早期从 scRNA-seq 重建 TCR 序列的工具之一，与该知识库中其他 TCR 相关资源形成互补：

| 工具/资源 | 特点 |
|-----------|------|
| **TRAPeS**（本文） | 短读长 scRNA-seq TCR 重建，迭代 DP |
| **MiXCR** | 通用免疫组库分析，支持多种平台 |
| **DeepTCR** | VAE 深度 TCR 库学习框架 |
| **soNNia** | 深度生成选择模型 |

---

## 五、分析笔记

### 为何关注这篇论文

TRAPeS 解决了 scRNA-seq 数据中 TCR 序列重建的关键瓶颈——当时的其他方法需要长读长测序，成本高、通量低。TRAPeS 通过直接操作原始 reads 而非 k-mer 的策略，在短读长数据上实现了更高的灵敏度。

### 生物学发现的意义

"Naive-like" 记忆细胞（即 Tscm / 干细胞样记忆 T 细胞）相对于效应记忆细胞拥有更长的 CDR3，提示这些细胞经历了不同的选择压力。较长的 CDR3 通常意味着：
1. 更多的抗原接触可能性
2. 更高的多样性和更少的胸腺选择压力
3. 可能在维持长期记忆方面有独特优势

这一发现为本课题中探究 TCR 特征与 T 细胞功能状态之间的关系提供了早期证据。

### PDF 状态

本文为开放获取（NAR 为 OA 期刊），但本次自动归档未能直接下载 PDF（PMC 需 PoW 挑战）。PDF 已保留占位路径 `raw/pdfs/Afik_2017_TRAPeS.pdf`，后续可通过手动下载或使用浏览器访问 PMC 页面获取。

