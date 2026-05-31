# 翻译说明 | Translation Notes

## 论文信息
- **标题:** The T cell receptor sequence influences the likelihood of T cell memory formation
- **作者:** Kaitlyn A. Lagattuta, Ayano C. Kohlgruber, Nouran S. Abdelfattah, Aparna Nathan, Laurie Rumker, Michael E. Birnbaum, Stephen J. Elledge, Soumya Raychaudhuri
- **期刊:** Cell Reports, 2025 Jan 28;44(1):115098
- **PMCID:** PMC11785489 | **PMID:** 39731734

## 翻译说明

### 总体策略
- 以忠实传达科学内容为首要目标，在保持专业性的前提下兼顾中文表达流畅
- 技术术语、基因名称、蛋白质名称、模型名称保持原文不作翻译
- 数学公式、数字、引用标记保持原样
- 统计学术语（p值、β系数、置信区间等）保持原文格式

### 术语处理

| 英文原文 | 中文翻译 | 说明 |
|----------|----------|------|
| TCR-mem | TCR-mem（不翻译） | 专有评分函数名称，保持原文 |
| TCR-innate | TCR-innate（不翻译） | 专有评分函数名称，保持原文 |
| TCR-reg | TCR-reg（不翻译） | 专有评分函数名称，保持原文 |
| TCR-CD8 | TCR-CD8（不翻译） | 专有评分函数名称，保持原文 |
| TCR twin | TCR双胞胎 | 指不同个体中序列相同的TCR |
| rCCA | rCCA（不翻译） | 正则化典型相关分析 |
| regularized canonical correlation analysis | 正则化典型相关分析 | 统计方法标准译名 |
| Atchley factors | Atchley因子 | 氨基酸数值编码标准术语 |
| CDR (complementarity-determining region) | 互补决定区 | 免疫学标准术语 |
| public TCR | 公共TCR | 多个个体中共有的TCR |
| private TCR | 私有TCR | 仅单个个体中出现的TCR |
| naive T cell | 初始T细胞 | 免疫学标准术语 |
| memory T cell | 记忆T细胞 | 免疫学标准术语 |
| regulatory T cell (Treg) | 调节性T细胞 | 免疫学标准术语 |
| innate-like T cell | 先天样T细胞 | 免疫学标准术语 |
| generic MHC reactivity | 通用MHC反应性 | 本文提出的概念 |
| positive selection | 阳性选择 | 胸腺选择标准术语 |
| tetramer dilution | 四聚体稀释 | 亲和力测定方法 |
| Dextramer | Dextramer（不翻译） | 专有产品名 |
| iTAST | iTAST（不翻译） | 微吸管粘附测定方法名 |
| buried surface area | 埋藏表面积 | 结构生物学标准术语 |
| Jurkat cell | Jurkat细胞 | 细胞系名，保持原文 |
| MART-1 | MART-1 | 抗原名，保持原文 |
| pp65 | pp65 | 抗原名，保持原文 |
| NLV | NLV | 肽段名，保持原文 |

### 特殊处理
1. **基因名**: TCR相关基因名(TRAV, TRBV, TRAJ, TRBJ)、趋化因子(CCR7)、表面标志(CD45RO, CD45RA, CD69, CD38, HLA-DR)、转录因子(FOXP3, PLZF, HELIOS)、生长因子(TGFB1)、酶(DNTT) — 均保持原样不译
2. **评分函数名**: "TCR-innate"、"TCR-CD8"、"TCR-reg"、"TCR-mem" — 保持原文，首次出现时括号注明含义
3. **数据集名**: "Dataset 1"–"Dataset 6" — 译为"数据集1"–"数据集6"
4. **方法名**: "Harmony"、"Symphony"、"UMAP"、"rCCA"、"Seurat"、"cellranger" — 保持原样
5. **TCR序列**: CDR3区氨基酸序列（如CGVSGGGADGLTF）保持原样
6. **病毒名**: "SARS-CoV-2"、"CMV"、"HCV" — 保持原样

### 质量说明
- 全文核心章节翻译完成：摘要、引言、结果、讨论、局限性
- STAR Methods及参考文献以英文原文形式收录，未逐句翻译
- 5个主图及全部补充图表均已引用
- 表1（7个数据集）和表2（8个TCR序列）以双语对照表形式呈现
- 核心术语表已涵盖本文创新概念
