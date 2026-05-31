---
title: "Targeted reconstruction of T cell receptor sequence from single cell RNA-seq links CDR3 length to T cell differentiation state"
authors:
  - "Shaked Afik"
  - "Kathleen B. Yates"
  - "Kevin Bi"
  - "Samuel Darko"
  - "Jernej Godec"
  - "Ulrike Gerdemann"
  - "Leo Swadling"
  - "Daniel C. Douek"
  - "Paul Klenerman"
  - "Eleanor J. Barnes"
  - "Arlene H. Sharpe"
  - "W. Nicholas Haining"
  - "Nir Yosef"
journal: "Nucleic Acids Research"
year: 2017
volume: 45
issue: 16
pages: "e148"
doi: "10.1093/nar/gkx615"
pmid: 28934479
pmcid: PMC5766189
tags: [raw, paper, tcr, scrna-seq, trapis, cdr3, t-cell-differentiation]
created: 2026-05-15
---

# TRAPeS — Targeted reconstruction of T cell receptor sequence from single cell RNA-seq

> Afik S, Yates KB, Bi K, et al. *Nucleic Acids Res.* 2017;45(16):e148.
> DOI: [10.1093/nar/gkx615](https://doi.org/10.1093/nar/gkx615)
> PMID: [28934479](https://pubmed.ncbi.nlm.nih.gov/28934479/) | PMCID: [PMC5766189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5766189/)

---

## Abstract

The T cell compartment must contain diversity in both T cell receptor (TCR) repertoire and cell state to provide effective immunity against pathogens. However, it remains unclear how differences in the TCR contribute to heterogeneity in T cell state. Single cell RNA-sequencing (scRNA-seq) can allow simultaneous measurement of TCR sequence and global transcriptional profile from single cells. However, current methods for TCR inference from scRNA-seq are limited in their sensitivity and require long sequencing reads, thus increasing the cost and decreasing the number of cells that can be feasibly analyzed. Here we present TRAPeS, a publicly available tool that can efficiently extract TCR sequence information from short-read scRNA-seq libraries. We apply it to investigate heterogeneity in the CD8+ T cell response in humans and mice, and show that it is accurate and more sensitive than existing approaches. Coupling TRAPeS with transcriptome analysis of CD8+ T cells specific for a single epitope from Yellow Fever Virus (YFV), we show that the recently described 'naive-like' memory population have significantly longer CDR3 regions and greater divergence from germline sequence than do effector-memory phenotype cells. This suggests that TCR usage is associated with the differentiation state of the CD8+ T cell response to YFV.

---

## Key Points

1. **TRAPeS** (TCR Reconstruction Algorithm for Paired-end Single-cell RNA-seq) — 可从短读长 scRNA-seq 文库（低至 25 bp 双端）重建 TCR 序列
2. 不等同于基于 k-mer 的方法，TRAPeS 直接在原始读段上工作以提高灵敏度
3. 使用**迭代动态规划算法**（Needleman–Wunsch）延伸 V 和 J 片段直至重叠，重建 CDR3 区域
4. 可校正已知 V/J 基因区段的突变/SNP
5. 可确定链的**生产性**（正确阅读框，无终止密码子）
6. 应用到 YFV 特异性 CD8+ T 细胞，发现 "naive-like" 记忆细胞群的 CDR3 显著更长、与 germline 序列的差异更大

---

## Algorithms

- 迭代 Needleman–Wunsch 动态规划延伸 V/J 片段
- 直接在原始 reads 上操作（非 k-mer）
- Python/C++ 实现（SeqAn 库）

## Availability

- GitHub: [YosefLab/TRAPeS](https://github.com/YosefLab/TRAPeS)
- License: 开源（具体 License 见 GitHub 仓库）
- Implementation: Python / C++ (SeqAn)

## PDF 下载状态

> ⚠️ 本文为开放获取（NAR 是 OA 期刊），但由于 PMC 页面需要 PoW（Proof-of-Work）挑战，未能在本次自动归档中下载 PDF。
> 后续可通过以下方式获取：
> - 手动从 PMC 下载：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5766189/
> - 或从 Oxford Academic 获取：https://academic.oup.com/nar/article/45/16/e148/3976466
> - 建议将 PDF 保存到 `raw/pdfs/Afik_2017_TRAPeS.pdf`
