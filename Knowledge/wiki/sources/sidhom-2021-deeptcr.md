---
title: "DeepTCR: Deep learning methods to model T cell receptor sequences"
tags: [source, paper, deep-learning, TCR, DeepTCR, VAE, CNN, repertoire-analysis]
created: 2026-05-16
updated: 2026-05-16
sources:
  - type: paper
    title: "DeepTCR: a suite of unsupervised and supervised deep learning methods to model T cell receptor sequences"
    authors: "Sidhom J-W, Pardoll D, Baras AS"
    journal: "Nature Communications"
    year: 2021
    doi: "10.1038/s41467-021-21879-w"
    url: "https://doi.org/10.1038/s41467-021-21879-w"
    pdf: "Knowledge/raw/sidhom-2021-deeptcr.pdf"
  - type: code
    repo: "GitHub: sidhomj/DeepTCR"
    url: "https://github.com/sidhomj/DeepTCR"
  - type: code
    repo: "PyPI: DeepTCR"
    url: "https://pypi.org/project/DeepTCR/"
---

# DeepTCR: Deep Learning Methods to Model TCR Sequences

> Sidhom J-W, Pardoll D, Baras AS. *Nature Communications* **12**:3154 (2021)

## Summary

DeepTCR is a suite of unsupervised and supervised deep learning methods for TCR sequencing data analysis. It learns a **joint representation** of TCRs by combining CDR3 sequence information (via embedding + CNN) with V/D/J gene usage information.

### Key Components

1. **TCR Featurization Block** — Core building block: CDR3 embedding (64d) → 3-layer CNN → concatenation with V/D/J embedding (48d)
2. **Unsupervised VAE** — For clustering antigen-specific TCRs; outperforms Hamming, K-mer, and alignment-based methods
3. **Supervised Sequence Classifier** — For classifying TCRs by antigen specificity; outperforms unsupervised VAE, RF, and SVM
4. **Supervised Regression** — Regresses UMI counts as proxy for binding affinity; validated on McPAS-TCR; enables **in silico perturbation analysis** (RSL) congruent with crystal structures
5. **Repertoire Classifier** — Weakly supervised multi-instance learning via multi-head attention; detects immune responses in HIV elite suppressor; discovered differential immune responses across GAG TW10 escape variants

### Key Results
- VAE-Seq-VDJ achieves best clustering among all featurization methods
- 17/18 experimentally validated TCR-peptide pairs correctly predicted
- 19/25 HIV epitopes detected (AUC > 0.90)
- RSL sensitivity correlates with crystal structure contact residues (AUC 0.82–0.91)

### Methods
- **Deep learning framework**: TensorFlow (Python)
- **Data**: 7 human + 9 murine tetramer-sorted antigens, 10x Genomics multi-chain dataset, HIV T cell culture assay
- **Installation**: `pip install DeepTCR` or from GitHub

### Links
- **Bilingual reader**: [[Knowledge/papers/sidhom-2021-deeptcr/paper.md]]
- **PDF**: [[Knowledge/papers/sidhom-2021-deeptcr/original.pdf]]
- **GitHub**: [https://github.com/sidhomj/DeepTCR](https://github.com/sidhomj/DeepTCR)
