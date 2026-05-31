# 翻译说明 | Translation Notes

## 论文信息
- **标题:** Mapping the functional landscape of T cell receptor repertoire by single T cell transcriptomics
- **作者:** Ze Zhang, Danyi Xiong, Xinlei Wang, Hongyu Liu, Tao Wang
- **期刊:** Nature Methods, 2021 Jan 6;18(1):92–99
- **PMCID:** PMC7799492

## 翻译说明

### 总体策略
- 以忠实传达科学内容为首要目标，在保持专业性的前提下兼顾中文表达流畅
- 技术术语、基因名称、蛋白质名称、模型名称保持原文不作翻译
- 数学公式、数字、引用标记保持原样

### 术语处理

| 英文原文 | 中文翻译 | 说明 |
|----------|----------|------|
| TCR repertoire | TCR库 / TCR组库 | "库"比"组库"更简洁常用 |
| tessa | tessa（不翻译） | 专有工具名称，保持原文 |
| clonotype | 克隆型 | 免疫学标准术语 |
| bottleneck layer | 瓶颈层 | 深度学习标准术语 |
| Dirichlet Process | 狄利克雷过程 | 贝叶斯统计标准术语 |
| unexplained variations | 未解释变异 | 统计学标准术语 |
| immune checkpoint inhibitor | 免疫检查点抑制剂 | 免疫学标准术语 |
| pseudotime | 伪时间 | 单细胞分析标准术语 |
| diffusion map | 扩散图 | 降维方法标准译名 |
| feature barcoding | 特征条形码 | 10x Genomics专有技术 |
| 'wisdom of the crowds' | "群体的智慧" | 引用概念，保留引号 |
| dichotomization | 二分 | 指分为两个截然不同的群体 |
| gradient | 梯度 | 表示逐渐变化的趋势 |

### 特殊处理
1. **基因名**: *TGFB1*, *IL7R*, *CXCR3*, *GZMK*, *IFNG*, *TNF*, *FOS*, *JUN*, *ITGAE*, *ENTPD1*, *GZMB*, *LAG3* — 均保持原样不译
2. **通路名**: "TGFB1/inhibition gene pathway" → 译为"TGFB1/抑制基因通路"
3. **抗体名**: "anti-PD-1 therapy" → 译为"抗PD-1治疗"
4. **数据集名**: "Healthy-CD8-1~4", "Breast-1~5", "BCC" 等 — 保持原样
5. **方法名**: "SMART-Seq2", "MATQ-Seq", "ECCITE-Seq", "GLIPH", "SCINA" — 保持原样

### 不确定的翻译
- **"putative antigen"**: 译为"推定抗原" — 在上下文中指每个TCR网络中最可能靶向的抗原
- **"gccutoff"**: 保留原文，GLIPH方法的专有参数名
- **"dCODE Dextramers"**: 保留原文，10x Genomics的专有产品名

### 质量说明
- 全文翻译完成，无跳过章节
- 所有4个主图和8个扩展数据图均已下载嵌入
- 参考文献已收录主要文献（41篇）
- 术语表已涵盖核心专业术语
- 摘要、引言、结果、讨论、在线方法均已完整翻译

### 图片说明
- 所有图片为PMC官方提供的JPG格式
- 图片来自PMC的全文图片集，分辨率为期刊出版质量
- 未对图片进行裁剪，使用原始全图
