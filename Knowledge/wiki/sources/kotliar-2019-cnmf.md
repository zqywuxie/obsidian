---
title: "cNMF: Identifying gene expression programs with single-cell RNA-Seq — Consensu NMF"
tags: [source, paper, scRNA-seq, NMF, matrix-factorization, cNMF]
created: 2026-05-16
updated: 2026-05-16
sources:
  - type: paper
    title: "Identifying gene expression programs of cell-type identity and cellular activity with single-cell RNA-Seq"
    authors: "Kotliar D, Veres A, Nagy MA, Tabrizi S, Hodis E, Melton DA, Sabeti PC"
    journal: "eLife"
    year: 2019
    doi: "10.7554/eLife.43803"
    url: "https://doi.org/10.7554/eLife.43803"
    pdf: "Knowledge/raw/kotliar-2019-cnmf.pdf"
  - type: code
    repo: "GitHub: dylkot/cNMF"
    url: "https://github.com/dylkot/cNMF/"
  - type: code
    repo: "GitHub: dylkot/scsim"
    url: "https://github.com/dylkot/scsim"
  - type: data
    accession: "GSE86153"
    database: "GEO"
    description: "Brain organoid scRNA-Seq (Quadrato 2017)"
  - type: data
    accession: "GSE102827"
    database: "GEO"
    description: "Visual cortex scRNA-Seq (Hrvatin 2018)"
  - type: data
    accession: "GSE71585"
    database: "GEO"
    description: "Visual cortex scRNA-Seq (Tasic 2016)"
  - type: data
    accession: "GSE50244"
    database: "GEO"
    description: "Pancreatic islets scRNA-Seq (Baron 2016)"
---

# cNMF: Identifying Gene Expression Programs with scRNA-Seq

> Kotliar D, Veres A, Nagy MA, et al. *eLife* **8**:e43803 (2019)

## Summary

This paper introduces **Consensus Non-Negative Matrix Factorization (cNMF)**, a computational method for simultaneously inferring cell-type identity and cellular activity gene expression programs (GEPs) from single-cell RNA-Seq data. The key innovation is a meta-analysis approach that runs NMF multiple times, filters outlier components, clusters the results, and takes consensus estimates, dramatically improving robustness and accuracy over single-run NMF.

### Key Findings

1. **cNMF accurately infers identity and activity GEPs**: Achieves 61% sensitivity at 5% FDR for activity program gene detection in simulations
2. **Robust to doublets**: Accurate even with 50% doublet rate
3. **Real data validation**:
   - Brain organoid: Identified cell-cycle (G1/S, G2/M) and hypoxia programs; refined "proliferative precursors" cluster into multiple cell types including immature skeletal muscle and dopaminergic neurons
   - Visual cortex: Discovered early and late response programs to light stimulation without knowledge of experimental labels; validated cross-dataset reproducibility
4. **Novel programs**: Neurosecretory (NS) and Synaptogenesis (Syn) programs in visual cortex

### Method
- Matrix factorization represents cells as linear combinations of multiple GEPs
- Runs NMF with random seeds → filters outliers via KNN distance → clusters components → takes median → final usage fit
- Uses over-dispersed gene selection and variance scaling (not log-transform)
- Outputs results in interpretable TPM units

### Limitations
- Linear combination assumption cannot model transcriptional repression
- Choice of K (number of components) requires judgment
- Batch effects can confound GEP identification

### Links
- **Bilingual reader**: [[Knowledge/papers/kotliar-2019-cnmf/paper.md]]
- **PDF**: [[Knowledge/papers/kotliar-2019-cnmf/original.pdf]]
- **Code**: [https://github.com/dylkot/cNMF/](https://github.com/dylkot/cNMF/)
