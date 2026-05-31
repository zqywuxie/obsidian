# Translation Notes — DynNet (Dou et al. 2026, Nature Communications)

## Paper Info
- **Title**: Inferring stochastic dynamics by biophysical Neural ODE using single-cell transcriptomics
- **Authors**: Jingyu Dou, Wentao Lyu, Feng Chen, Qing Nie, Chunhe Li
- **Journal**: Nature Communications, 2026 (Article in Press)
- **DOI**: 10.1038/s41467-026-73257-z
- **License**: CC BY-NC-ND 4.0
- **PDF**: Downloaded (unedited manuscript, 57 pages)

## Source
- **Primary source**: 微信公众号文章 "DynNet：把单细胞静态快照变成细胞命运的动力学模型" from 计算生物前沿
- **Original paper**: Nature Communications HTML + PDF (unedited version)
- **Figures**: Extracted from PDF (pages 52-57)

## Terminology Decisions

| Term | Translation | Notes |
|------|-------------|-------|
| DynNet | DynNet | 随机动力学推断网络 (Stochastic Dynamics Inference Network) |
| stochastic differential equation (SDE) | 随机微分方程 | Core mathematical framework |
| drift term | 漂移项 | Deterministic gene regulatory component |
| diffusion term | 扩散项 | Stochastic noise component |
| Hill function | 希尔函数 | Gene regulation model: f(x) = x^n / (S^n + x^n) |
| hard constraint | 硬约束 | Mask non-existent edges in prior GRN |
| soft constraint | 软约束 | L2 penalty on non-prior edges |
| energy landscape | 能量景观 | U(x) = -ln P_ss(x) |
| transition action | 转变作用量 | Freidlin-Wentzell minimum action path |
| first passage time (FPT) | 首次通过时间 | Mean time to transition between states |
| MISA (Mutual Inhibition Self-Activation) | MISA 模型 | Classic bistable/multistable gene regulatory motif |
| attractor | 吸引子 | Stable state in energy landscape |
| saddle point | 鞍点 | Critical point for fate transition |
| decision boundary | 决策边界 | Separatrix between basins of attraction |
| MH (mature hepatocyte-like) | 成熟肝细胞样 | Terminal differentiation state |
| LB (liver bud) | 肝芽 | Alternative differentiation state |
| DE (definitive endoderm) | 定型内胚层 | Early differentiation stage |
| HE (hepatic endoderm) | 肝内胚层 | Intermediate stage before bifurcation |
| EMT (epithelial-mesenchymal transition) | 上皮-间质转化 | Cell plasticity in cancer |
| MET (mesenchymal-epithelial transition) | 间质-上皮转化 | Reverse process |
| pEMT (partial EMT) | 部分 EMT | Intermediate state |
| IM (MET intermediate) | MET 中间态 | Metastable state during MET |
| weight-matching loss | 权重匹配损失 | Loss term for multi-stable distribution |
| dynamical consistency loss | 动力学一致性损失 | Minimizes drift near stable states |
| TGF-β | TGF-β | Transforming growth factor beta |

## Figures

| Figure | File(s) | Description |
|--------|---------|-------------|
| Fig 1 | `assets/fig1_overview.png` | DynNet framework: workflow, SDE model, Hill function, comparison |
| Fig 2 | `assets/fig2a-2e.png` (5 files) | MISA model validation: stable states, decision boundaries, landscape |
| Fig 3 | `assets/fig3_branching.png`, `fig3_gene_dynamics.png` | 7-gene branching: cascade activation, bifurcation, hard/soft constraints |
| Fig 4 | `assets/fig4_hepatocyte.png`, `fig4a_trajectory.png` | Hepatocyte differentiation: trajectory, landscape, FPT, knockout |
| Fig 5 | `assets/fig5_emt_landscape.png`, `fig5b_landscape_2d.png` | EMT landscape: data-driven vs model, velocity field, GRN |
| Fig 6 | `assets/fig6_transition_paths.png`, `fig6b_sensitivity.png` | EMT transition: min action path, sensitivity, CD44/CDH1 knockout |

## Omissions
- Supplementary Figures 1-46: Available in PDF (pages 28-51), not extracted as individual assets
- Supplementary Information (PDF): Available at https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-73257-z/MediaObjects/41467_2026_73257_MOESM3_ESM.pdf
- Source Data (XLSX): Available at Springer Nature
- Full Methods: Partially extracted (Methods section starts on page 25)
- Reference list: 72 references, abbreviated in paper.md

## Draft Status
- [x] WeChat article full text extracted and translated
- [x] Original paper abstract + key sections extracted
- [x] Main figures 1-6 extracted from PDF
- [x] source_map.json created
- [x] translation_notes.md created
- [ ] Supplementary figures extracted
- [ ] Full Methods section translated
