# Translation Notes — popV

## Paper Info
- **Title**: Consensus prediction of cell type labels in single-cell data with popV
- **Authors**: Can Ergen, Gaoweiming Xing, et al. (Nir Yosef Lab)
- **Journal**: Nature Genetics, 2024
- **DOI**: 10.1038/s41588-024-01993-3
- **License**: CC-BY-NC-ND 4.0

## Source
- Full text extracted via defuddle from publisher HTML (open-access HTML)
- PDF: 19 pages, downloaded from nature.com via browser session

## Terminology Decisions

| Term | Translation | Notes |
|------|-------------|-------|
| cell-type annotation | 细胞类型注释 | Standard term in field |
| label transfer | 标签迁移 | Widely used in scRNA-seq |
| consensus score | 共识分数 | popV's key metric |
| uncertainty estimation | 不确定性估计 | Key contribution of popV |
| Cell Ontology | 细胞本体论 | Proper noun, keep English |
| query dataset | 查询数据集 | Standard scRNA-seq term |
| reference atlas | 参考图谱 | Standard term |
| majority voting | 多数投票 | Standard ML term |
| ablation study | 消融研究 | Standard ML term |
| precision–recall curve | 精确率-召回率曲线 | Standard ML metric |
| UMAP embedding | UMAP嵌入 | Standard dimensionality reduction |
| batch correction | 批次校正 | Standard scRNA-seq term |
| highly variable genes | 高变基因 | Standard scRNA-seq term |

## Figures

| Figure | File | Description |
|--------|------|-------------|
| Fig 1 | `assets/fig1.png` | Framework of popV — 8 methods → consensus voting |
| Fig 2 | `assets/fig2.png` | Lung Cell Atlas case study — accuracy vs consensus score |
| Fig 3 | `assets/fig3.png` | Thymus case study — query-specific cell types |
| Supplementary | Not downloaded | Supplementary Figs 1–19 + Tables 1–11 |

## Omissions
- Extended Data Figs 1–9: Not downloaded separately (available in PDF)
- Supplementary Information: Not downloaded (Springer PDF link timed out)
- References list: Abbreviated in paper.md; full list in source document

## Draft Status
- [x] Full text extracted and translated
- [x] Main figures (1–3) extracted
- [ ] Extended Data figures (available in PDF)
- [ ] Supplementary PDF (need manual download from https://static-content.springer.com/esm/art%3A10.1038%2Fs41588-024-01993-3/MediaObjects/41588_2024_1993_MOESM1_ESM.pdf)
