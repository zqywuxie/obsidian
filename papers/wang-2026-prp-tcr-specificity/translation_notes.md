# Translation Notes — PRP (Wang et al. 2026)

## Paper Info
- **Title**: Deep peptide recognition profiling decodes TCR specificity and enables disease-associated antigen discovery
- **Authors**: Wang N, Yeh H, Lai B, et al.
- **Journal**: Nature Biotechnology, 2026
- **DOI**: 10.1038/s41587-026-03128-x
- **License**: Check publisher website
- **PDF**: 23 pages, 17.4MB

## Source
- Full text extracted via defuddle from publisher HTML
- Figures 1-6 downloaded from Springer Nature media server

## Terminology Decisions

| Term | Translation | Notes |
|------|-------------|-------|
| deep peptide recognition profiling (PRP) | 深度肽识别图谱 | Core concept, keep PRP acronym |
| protein language model (pLM) | 蛋白语言模型 | Standard term |
| yeast surface display | 酵母表面展示 | Standard biotech term |
| functional distance | 功能距离 | PRP divergence-based metric |
| Mahalanobis distance | 马氏距离 | Statistical term for OOD detection |
| TCR neighborhood | TCR 邻域 | TCR functional group concept |
| ankylosing spondylitis (AS) | 强直性脊柱炎 | Disease name |
| acute anterior uveitis (AAU) | 急性前葡萄膜炎 | Disease name |
| Jensen-Shannon divergence | JS 散度 | Probability distance metric |
| ipTM | ipTM | Interface predicted TM score |
| CDR3β-centric | CDR3β 中心 | Key modeling focus |
| cross-reactivity | 交叉反应性 | Standard term |
| candidate autoantigen | 候选自身抗原 | PSG5 finding |

## Figures

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `assets/fig1.png` | Experimental-computational platform overview |
| Fig 2 | `assets/fig2.png` | Functional diversity of HLA-B*27:05 TCRs |
| Fig 3 | `assets/fig3.png` | pLM predictions + proteome-wide antigen discovery |
| Fig 4 | `assets/fig4.png` | Experimental validation of predicted activating peptides |
| Fig 5 | `assets/fig5.png` | TCR neighborhood joint modeling |
| Fig 6 | `assets/fig6.png` | Generalization principles + Mahalanobis distance |

## Omissions
- Extended Data Figs 1–7: Available in PDF, not separately extracted
- Supplementary Information: Methods details, figures, tables
- Full Methods: Only partially extracted by defuddle (lines 121–200)
- Reference list: Available in source; abbreviated in paper.md

## Draft Status
- [x] Full text extracted and translated (Abstract, Main, Results, Discussion)
- [x] Main figures 1–6 extracted
- [x] PDF downloaded (23 pages)
- [ ] Extended Data figures (available in PDF)
- [ ] Full Methods (available in PDF)
