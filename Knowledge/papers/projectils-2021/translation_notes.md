# Translation Notes — ProjecTILs (Andreatta & Carmona 2021)

## Paper Info
- **Title**: Interpretation of T cell states from single-cell transcriptomics data using reference atlases
- **Authors**: Andreatta M, Carmona SJ
- **Journal**: Nature Communications, 2021; 12:6889
- **DOI**: 10.1038/s41467-021-23324-4
- **License**: Open Access (CC BY 4.0)
- **PDF**: Not downloaded (Nature Communications — online HTML available)

## Source
- Full text extracted via defuddle from nature.com HTML
- Figures 1-9 downloaded from Springer Nature media server (full resolution)

## Terminology Decisions

| Term | Translation | Notes |
|------|-------------|-------|
| ProjecTILs | ProjecTILs | Keep as is (software name) |
| reference atlas projection | 参考图谱投影 | Core concept |
| STACAS | STACAS | Keep as is (software name, "Sub-type Anchor Correction for Alignment in Seurat") |
| TIL (tumor-infiltrating lymphocyte) | 肿瘤浸润淋巴细胞 | Standard term |
| Tex (terminally exhausted) | 终末耗竭 | CD8+ T cell exhaustion state |
| Tpex (precursor exhausted) | 前体耗竭 | Tcf7+ Pdcd1+ precursor |
| EM (effector memory) | 效应记忆 | CD8+ effector memory |
| SLEC (short-lived effector cells) | 短寿命效应细胞 | Terminal effector |
| ICA (Independent Component Analysis) | 独立成分分析 | Dimensionality reduction method |
| TILPRED | TILPRED | Supervised TIL classification tool |
| ortholog mapping | 直系同源映射 | Cross-species gene mapping |
| LCMV | LCMV | Lymphocytic choriomeningitis virus |
| Regnase-1 (Zc3h12a) | Regnase-1 (Zc3h12a) | RNase, keep gene name |
| miR-155 | miR-155 | microRNA 155 |
| PTPN2 | PTPN2 | Phosphatase, immunotherapeutic target |
| XCL1-XCR1 | XCL1-XCR1 | Chemokine-receptor pair for cDC1 interaction |
| Morisita similarity index | Morisita 相似性指数 | TCR repertoire overlap metric |

## Figures

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `assets/fig1.png` | TIL reference atlas construction (STACAS integration, 9 subtypes) |
| Fig 2 | `assets/fig2.png` | ProjecTILs analysis workflow |
| Fig 3 | `assets/fig3.png` | Genetic perturbations — miR-155 and Regnase-1 KO |
| Fig 4 | `assets/fig4.png` | Virus-specific CD8+ T cell atlas (LCMV) |
| Fig 5 | `assets/fig5.png` | Tissue-specific heterogeneity in chronic infection |
| Fig 6 | `assets/fig6.png` | Cross-species human-to-mouse projection |
| Fig 7 | `assets/fig7.png` | TIL subtype conservation across studies, cancer types, species |
| Fig 8 | `assets/fig8.png` | Human TIL states across tissues and clonal relatedness |
| Fig 9 | `assets/fig9.png` | CD8+ TIL intratumoral differentiation model |

## Omissions
- Supplementary Figures 1–14: Available online, not extracted
- Supplementary Data 1: Gene lists per TIL subtype
- Full Methods: Only partially extracted (mice, scRNA-seq, ProjecTILs pipeline, ICA)
- Reference list: Available in HTML, abbreviated in paper.md

## Draft Status
- [x] Full text extracted and translated (Abstract, Introduction, Results, Discussion)
- [x] Main figures 1–9 extracted
- [x] source_map.json created
- [ ] PDF download (open access, available via nature.com)
- [ ] Supplementary materials
