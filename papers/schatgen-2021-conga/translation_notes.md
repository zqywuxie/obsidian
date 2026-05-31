# Translation Notes — CoNGA (Schattgen et al. 2021)

## Paper Info
- **Title**: Integrating T cell receptor sequences and transcriptional profiles by clonotype neighbor-graph analysis (CoNGA)
- **Authors**: Schattgen SA, Guion K, Crawford JC, Souquette A, Barrio AM, Stubbington MJT, Thomas PG, Bradley P
- **Journal**: Nature Biotechnology, 2021; 40(1):54–63
- **DOI**: 10.1038/s41587-021-00989-2
- **PMID**: 34426704
- **PMCID**: PMC8832949
- **License**: Open Access (PMC), CC BY 4.0
- **PDF**: 5 pages, 7.4 MB (NIHMS author manuscript)

## Source
- Full text extracted via defuddle from PMC HTML
- Figures 1-6 downloaded from PMC blob storage
- PDF downloaded via Playwright browser from PMC

## Terminology Decisions

| Term | Translation | Notes |
|------|-------------|-------|
| clonotype neighbor-graph analysis (CoNGA) | 克隆型邻域图分析 | Core method name, keep CoNGA acronym |
| graph-vs-graph correlation analysis | 图-图相关分析 | CoNGA's primary mode |
| graph-vs-feature correlation analysis | 图-特征相关分析 | CoNGA's secondary mode |
| CoNGA score | CoNGA 分数 | Hypergeometric overlap probability × N |
| CoNGA hits | CoNGA 命中 | Clonotypes with significant CoNGA scores |
| CoNGA cluster | CoNGA 簇 | GEX:TCR cluster pair grouping |
| TCRdist | TCRdist | Keep as is (established metric from Dash et al. 2017) |
| iMHC score | iMHC 分数 | "independent of pMHC" — MHC非依赖性评分 |
| HOBIT (ZNF683) | HOBIT (ZNF683) | Transcription factor, keep gene name |
| HELIOS (IKZF2) | HELIOS (IKZF2) | Transcription factor, keep gene name |
| EPHB6 | EPHB6 | Ephrin receptor, keep gene name |
| TRBV30 | TRBV30 | V gene segment, keep as is |
| pMHC multimer | pMHC 多聚体 | DNA-barcoded MHC multimers |
| MAIT cells | MAIT 细胞 | Mucosal-associated invariant T |
| iNKT cells | iNKT 细胞 | Invariant natural killer T |
| Morisita-Horn overlap | Morisita-Horn 重叠指数 | Modified for TCR sequence similarity |
| TCR neighborhood | TCR 邻域 | Set of TCR-similar clonotypes |
| GEX neighborhood | GEX 邻域 | Set of GEX-similar clonotypes |
| kernel PCA | 核主成分分析 | Dimensionality reduction for TCRdist matrix |
| KNN graph | K 近邻图 | Underlying graph structure |
| alphadist | alphadist | Genomic distance between TRAV and TRAJ |
| publicity score | 公共性分数 | Fraction of bulk repertoires containing TCRβ |

## Figures

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `assets/fig1.jpg` | CoNGA graph-vs-graph analysis workflow + application to human CD8+ T cells |
| Fig 2 | `assets/fig2.jpg` | CoNGA identifies HOBIT+/HELIOS+ CD8+ T cell population |
| Fig 3 | `assets/fig3.jpg` | CoNGA GEX/TCR correlation in thymic T cells |
| Fig 4 | `assets/fig4.jpg` | CoNGA graph-vs-feature analysis |
| Fig 5 | `assets/fig5.jpg` | EPHB6 co-expression with TRBV30+ T cells |
| Fig 6 | `assets/fig6.jpg` | TCR and GEX similarity among pMHC-positive clonotypes |

## Omissions
- Extended Data Figs 1–10: Available in PMC HTML text and PDF
- Supplementary Information PDF (21.8MB): Not downloaded
- Supplementary Data files (TSV/XLSX): Not downloaded
- Full Methods: Only partially extracted by defuddle (CoNGA algorithm, TCR analysis, GEX analysis, pMHC analysis, flow cytometry)
- Reference list: Available in PMC; abbreviated in paper.md

## Draft Status
- [x] Full text extracted and translated (Summary, Main, Results, Discussion)
- [x] Main figures 1–6 extracted
- [x] PDF downloaded (5 pages, author manuscript)
- [ ] Extended Data figures (available in PDF)
- [ ] Supplementary Information (21.8MB PDF)
- [ ] Supplementary Data files
