---
title: "Peanut oral immunotherapy differentially suppresses clonally distinct subsets of T helper cells"
authors:
  - "Brinda Monian"
  - "Ang A. Tu"
  - "Bert Ruiter"
  - "Duncan M. Morgan"
  - "Patrick M. Petrossian"
  - "Neal P. Smith"
  - "Todd M. Gierahn"
  - "Julia H. Ginder"
  - "Wayne G. Shreffler"
  - "J. Christopher Love"
journal: "Journal of Clinical Investigation"
year: 2022
volume: 132
issue: 2
pages: "e150634"
doi: "10.1172/JCI150634"
pmid: 34813505
pmcid: PMC8759778
tags: [raw, paper, tcr, scrna-seq, oit, peanut-allergy, th2, t-cell-subsets, immunotherapy]
created: 2026-05-15
---

# Peanut OIT differentially suppresses clonally distinct subsets of T helper cells

> Monian B, Tu AA, Ruiter B, et al. *J Clin Invest.* 2022;132(2):e150634.
> DOI: [10.1172/JCI150634](https://doi.org/10.1172/JCI150634)
> PMID: [34813505](https://pubmed.ncbi.nlm.nih.gov/34813505/) | PMCID: [PMC8759778](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8759778/)

---

## Abstract

Food allergy affects an estimated 8% of children in the United States. Oral immunotherapy (OIT) is a recently approved treatment, with outcomes ranging from sustained tolerance to food allergens to no apparent benefit. The immunological underpinnings that influence clinical outcomes of OIT remain largely unresolved. Using single-cell RNA-Seq and paired T cell receptor α/β (TCRα/β) sequencing, we assessed the transcriptomes of CD154⁺ and CD137⁺ peanut-reactive T helper (Th) cells from 12 patients with peanut allergy longitudinally throughout OIT. We observed expanded populations of cells expressing Th1, Th2, and Th17 signatures that further separated into 6 clonally distinct subsets. Four of these subsets demonstrated a convergence of TCR sequences, suggesting antigen-driven T cell fates. Over the course of OIT, we observed suppression of Th2 and Th1 gene signatures in effector clonotypes but not T follicular helper–like (Tfh-like) clonotypes. Positive outcomes were associated with stronger suppression of Th2 signatures in Th2A-like cells, while treatment failure was associated with the expression of baseline inflammatory gene signatures that were present in Th1 and Th17 cell populations and unmodulated by OIT.

---

## Key Findings

### 1. Study Design
- **12 peanut-allergic patients** undergoing OIT (ClinicalTrials.gov NCT01750879)
- **4 time points**: baseline → buildup (13 wk) → maintenance (12 wk post-max dose) → avoidance (12 wk off therapy)
- **3 clinical outcome groups**: tolerance, partial tolerance, treatment failure
- **Method**: PBMC + peanut protein extract (20h stimulation) → FACS (CD154⁺/CD137⁺) → Seq-Well scRNA-seq + paired TCRα/β

### 2. Six clonally distinct Th subsets
| Subset | Key Markers | Clonal TCR Convergence |
|--------|------------|----------------------|
| Th1-conv (conventional Th1) | IFNG, GZMB | Yes |
| Tfh1-like | IFNG, GZMB, ICOS, PDCD1, TNFRSF9 | Yes |
| Th2A-like | GATA3, IL17RB, PTGDR2 | No (high diversity) |
| Tfh2-like | CXCR5, PDCD1, IL4, IL5 | Yes |
| Th2reg-like | FOXP3, TNFRSF9 | No (high diversity) |
| Th17 | (Th17 signature) | Yes |

### 3. OIT Mechanisms
- **Th2A-like and Th1-conv clones**: suppressed by OIT (anergic state) — **TCR repertoire stable**, suggesting **functional suppression not clonal deletion**
- **Tfh-like clones (Tfh1, Tfh2)**: **NOT suppressed** by OIT — refractory to modulation
- **Tfh2-like cells**: IL4/IL5 expression correlated with peanut-specific IgE (unlike Th2A-like)
- **Tregs**: No sustained induction detected (FOXP3, IL10) — no new Treg clonotypes

### 4. Baseline Predictors of Outcome
- **Treatment failure** associated with high baseline expression of: OX40, OX40L, STAT1, GPR15, Th17 signatures
- These inflammatory signatures were **not modulated by OIT**
- Suggests pre-existing inflammatory burden limits OIT efficacy

### 5. TCR Analysis Highlights
- 55% expanded clones detected across multiple time points
- Only 1.6% clonotypes shared between CD154⁺ and CD137⁺ compartments → distinct lineages
- TCR convergence within most Th subtypes → epitope-driven skewing of phenotype
- TCRdist analysis: similar TCR sequences → increased likelihood of same Th subtype

---

## Methods Highlights

- **Activation**: 20h peanut protein extract stimulation (captures ex vivo state, no proliferation)
- **Sorting**: CD154⁺ (effector) and CD137⁺ (regulatory) memory CD4⁺ T cells
- **scRNA-seq**: Seq-Well platform (nanowell-based)
- **TCR seq**: Biotinylated capture probes for TRAC/TRBC → enrichment → MiSeq 150bp PE
- **Gene modules**: Sparse PCA → 50 immune gene modules
- **TCR distance**: TCRdist (BLOSUM62-based CDR3β distance metric)

---

## Data Availability

- **dbGaP**: phs001897.v2.p1 (FASTQ)
- **GEO**: GSE158667 (processed expression + TCR data)
- **GitHub**: [mitlovelab/PNOIT2_scRNAseq](https://github.com/mitlovelab/PNOIT2_scRNAseq)

---

## PDF 下载状态

> JCI 为开放获取期刊，本文 PDF 可从以下渠道获取：
> - JCI: https://www.jci.org/articles/view/150634/pdf
> - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8759778/pdf/
> 当前环境自动下载受限（需浏览器环境），建议手动保存至 `raw/pdfs/Monian_2021_JCI_peanut_OIT.pdf`
