---
title: "popV: Consensus prediction of cell type labels in single-cell data with popV"
tags: [source, paper, scRNA-seq, cell-type-annotation, ensemble-method, uncertainty-quantification, cell-ontology, popV]
created: 2026-05-18
updated: 2026-05-18
sources:
  - type: paper
    title: "Consensus prediction of cell type labels in single-cell data with popV"
    authors: "Ergen C, Xing G, Jayasuriya M, Kim M, et al. (Yosef Lab)"
    journal: "Nature Genetics"
    year: 2024
    doi: "10.1038/s41588-024-01993-3"
    url: "https://doi.org/10.1038/s41588-024-01993-3"
    pdf: "Knowledge/papers/popv-2024-cell-type-annotation/original.pdf"
  - type: code
    repo: "GitHub: YosefLab/popV"
    url: "https://github.com/YosefLab/popV"
  - type: code
    repo: "GitHub: popv-reproducibility"
    url: "https://github.com/YosefLab/popv-reproducibility"
  - type: data
    repo: "Tabula Sapiens (CELLxGENE)"
    url: "https://cellxgene.cziscience.com/collections/e5f58829-1a66-40b5-a624-9046778e74f5"
  - type: data
    repo: "Zenodo: Corrected Tabula Sapiens metadata"
    url: "https://doi.org/10.5281/zenodo.7587774"
  - type: data
    repo: "Zenodo: Pretrained models"
    url: "https://doi.org/10.5281/zenodo.7580707"
---

# popV: Consensus Prediction of Cell Type Labels

> Ergen C, Xing G, Jayasuriya M, Kim M, et al. *Nature Genetics* (2024)
> DOI: [10.1038/s41588-024-01993-3](https://doi.org/10.1038/s41588-024-01993-3)

## Summary

PopV is an ensemble method for automated cell-type annotation that integrates **8 diverse prediction algorithms** (RF, SVM, scANVI, OnClass, Celltypist, kNN+scVI, kNN+BBKNN, kNN+Scanorama) with a **Cell Ontology-based voting scheme** to produce both consensus annotations and well-calibrated **uncertainty scores** (consensus score 1–8).

### Key Findings

- **Consensus score correlates with accuracy**: Score ≥6 → >90% accuracy; score =8 → 98% accuracy
- **Three modes**: retrain (1hr/100k cells), inference (30min/100k), fast (5min/100k)
- **Three reasons for low consensus**: continuum cell states, query-specific cells, reference inaccuracies
- **Outperforms Seurat** label transfer in accuracy
- **Diverse classifiers essential**: SVM-only ensemble fails to calibrate uncertainty
- **Reference**: Tabula Sapiens (483,152 cells, 20 organs)
- **License**: CC-BY-NC-ND 4.0

### Significance

PopV's primary contribution is not higher accuracy than individual methods, but **interpretable, well-calibrated uncertainty quantification** for cell-type annotation. It enables users to focus manual inspection on cells with low consensus scores.

### Links
- **Bilingual reader**: [[Knowledge/papers/popv-2024-cell-type-annotation/paper.md]]
- **PDF**: [[Knowledge/papers/popv-2024-cell-type-annotation/original.pdf]]
- **GitHub**: [https://github.com/YosefLab/popV](https://github.com/YosefLab/popV)
- **Reproducibility**: [https://github.com/YosefLab/popv-reproducibility](https://github.com/YosefLab/popv-reproducibility)
