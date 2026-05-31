# Translation Notes — kotliar-2019-cnmf

## Source
- **Original:** Publisher HTML from eLife (open access, CC-BY 4.0)
- **URL:** https://elifesciences.org/articles/43803
- **PDF:** Downloaded as `original.pdf`

## Terminology Choices

| English | 中文 | Notes |
|---------|------|-------|
| gene expression program (GEP) | 基因表达程序 | Standard term in systems biology |
| identity program | 身份程序 | Referring to cell-type identity |
| activity program | 活动程序 | Cellular activity programs |
| consensus NMF (cNMF) | 共识非负矩阵分解 | Keeping "cNMF" as acronym in text |
| matrix factorization | 矩阵分解 | Standard linear algebra term |
| non-negative matrix factorization | 非负矩阵分解 | Standard ML term |
| usage matrix | 使用矩阵 | How much each GEP contributes per cell |
| doublet | 双细胞/双重细胞 | Two cells mistakenly counted as one |
| over-dispersed genes | 过度分散基因 | Statistical term for high-variance genes |
| silhouette score | 轮廓系数 | Clustering quality metric |
| Frobenius error | Frobenius误差 | Matrix norm |
| depolarization | 去极化 | Neuronal term |
| hypoxia | 低氧 | Physiological term |
| organoid | 类器官 | Standard biological term |
| neurosecretory | 神经分泌 | Cellular phenotype |
| synaptogenesis | 突触发生 | Neural development term |

## Translation Approach
- Gene symbols, protein names kept in original English (e.g., *VEGFA*, *MEF2C*)
- DOI URLs preserved in full
- Statistical notation (p-values, R values, fold-changes) kept intact
- Mathematical formulas preserved as LaTeX
- Technical method details translated for readability but precision maintained

## Figures
- Figures are embedded as web images from eLife IIIF server
- No local figure crops were extracted (source is HTML, not PDF)
- Figure references point to original eLife figure URLs

## Uncertainties
- Supplementary figures referenced in text but not individually extracted
- Some gene names may have alternative Chinese transliterations not used here
- Batch-effect supplement (Fig. 5—figure supplement 1, 2) discussed but not separately rendered
