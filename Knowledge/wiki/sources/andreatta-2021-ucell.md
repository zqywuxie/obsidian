---
title: "UCell: Robust and scalable single-cell gene signature scoring"
tags: [source, paper, scRNA-seq, gene-signature, UCell, signature-scoring, R-package]
created: 2026-05-16
updated: 2026-05-16
sources:
  - type: paper
    title: "UCell: Robust and scalable single-cell gene signature scoring"
    authors: "Andreatta M, Carmona SJ"
    journal: "Computational and Structural Biotechnology Journal"
    year: 2021
    doi: "10.1016/j.csbj.2021.06.043"
    url: "https://doi.org/10.1016/j.csbj.2021.06.043"
    pdf: "Knowledge/raw/andreatta-2021-ucell.pdf"
  - type: code
    repo: "GitHub: carmonalab/UCell"
    url: "https://github.com/carmonalab/UCell"
  - type: code
    repo: "GitLab: carmona/UCell_demo"
    url: "https://gitlab.unil.ch/carmona/UCell_demo"
---

# UCell: Robust and Scalable Single-Cell Gene Signature Scoring

> Andreatta M, Carmona SJ. *CSBJ* **19**:3796-3798 (2021)

## Summary

UCell is an R package for gene signature scoring in scRNA-seq data, based on the **Mann-Whitney U statistic**. Unlike Seurat's AddModuleScore (which depends on dataset composition), UCell scores depend only on the relative gene ranking within individual cells, making them robust to dataset composition. Compared to AUCell (which shares the same rank-based approach), UCell is approximately **3× faster** and uses **up to 10× less memory** (5.5 GB vs >64 GB for 100k cells).

### Key Features
1. **Dataset-independent**: Scores unaffected by which other cell types are in the dataset
2. **Efficient**: Uses `data.table::frank` for ranking; automatic batch processing
3. **Seurat-compatible**: Direct integration with Seurat objects
4. **Scalable**: Processes 100k cells in minutes on a regular machine

### How It Works
- Rank genes within each cell individually
- Truncate bottom-ranked genes at r_max = 1500
- Calculate Mann-Whitney U statistic for signature genes
- Normalize score to [0, 1] range

### Links
- **Bilingual reader**: [[Knowledge/papers/andreatta-2021-ucell/paper.md]]
- **PDF**: [[Knowledge/papers/andreatta-2021-ucell/original.pdf]]
- **GitHub**: [https://github.com/carmonalab/UCell](https://github.com/carmonalab/UCell)
