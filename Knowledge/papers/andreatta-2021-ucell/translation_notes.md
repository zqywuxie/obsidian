# Translation Notes — andreatta-2021-ucell

## Source
- **Original:** Publisher HTML from CSBJ (Science Partner Journal, open access)
- **URL:** https://spj.science.org/doi/10.1016/j.csbj.2021.06.043
- **PDF:** Downloaded as `original.pdf`
- **Paper type:** Software/Web Server Article (concise methods paper)

## Terminology Choices

| English | 中文 | Notes |
|---------|------|-------|
| gene signature scoring | 基因签名评分 | Also called "gene module scoring" |
| Mann-Whitney U statistic | Mann-Whitney U 统计量 | Non-parametric rank-based test |
| AUC (Area Under the Curve) | AUC (曲线下面积) | ROC curve metric |
| ROC curve | ROC 曲线 | Receiver Operating Characteristic |
| relative ranks | 相对排名 | Per-cell gene ranking |
| dataset composition | 数据集的组成/细胞组成 | Refers to which cell types are present |
| robustness | 稳健性 | Not affected by dataset composition |
| AddModuleScore | AddModuleScore | Seurat's method, kept in English |
| AUCell | AUCell | SCENIC's method, kept in English |
| Seurat | Seurat | R package, kept in English |
| UMAP | UMAP | Dimensionality reduction, kept in English |
| CITE-seq | CITE-seq | Protein + RNA co-profiling, kept in English |

## Key Design Difference
- **UCell/AUCell**: Rank-based → scores independent of dataset composition
- **Seurat AddModuleScore**: Expression binning across entire dataset → scores depend on dataset composition

## Figures
- Fig. 1 downloaded from publisher as `assets/fig1.jpg`
- This is the only main figure in this short Software Article

## Translation Notes
- This is a concise methods paper (Software/Web Server Article type), only ~3 pages
- All main text has been translated
- Mathematical formulas preserved as-is
- R package names kept in original
