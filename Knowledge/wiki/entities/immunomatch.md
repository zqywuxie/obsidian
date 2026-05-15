---
title: ImmunoMatch
tags: [entity, tool, antibody, machine-learning, language-model, b-cell]
created: 2026-05-06
updated: 2026-05-06
---

# ImmunoMatch

> 基于 AntiBERTa2 抗体语言模型的 H-L 链配对预测框架，由 Franca Fraternali 和 Joseph C. F. Ng 团队开发（UCL / Nature Methods 2026）。

---

## 基本信息

| 属性 | 值 |
|------|-----|
| **开发者** | Dongjun Guo, Deborah K. Dunn-Walters, Franca Fraternali, Joseph C. F. Ng |
| **机构** | University College London / King's College London / University of Surrey / Birkbeck |
| **发表** | *Nature Methods* 2026, Vol. 23, pp 106–117 |
| **DOI** | [10.1038/s41592-025-02913-x](https://doi.org/10.1038/s41592-025-02913-x) |
| **基础模型** | AntiBERTa2（RoBERTa 架构，5.58 亿抗体序列预训练） |
| **任务** | 二分类：cognate H-L pairs vs random pairs |
| **代码/数据** | 见论文 Online content |

---

## 模型变体

| 模型 | 训练数据 | Accuracy | AUC-ROC | F1 |
|------|---------|----------|---------|----|
| ImmunoMatch | 所有 H-L 对（混合 κ + λ） | 0.666 | 0.753 | 0.677 |
| ImmunoMatch-κ | 仅 H-κ 对 | **0.817** | **0.885** | **0.839** |
| ImmunoMatch-λ | 仅 H-λ 对 | 0.764 | 0.831 | 0.764 |

---

## 关键特性

1. **全长序列输入**: 使用 AntiBERTa2 编码全长 VH + VL 可变域（而非仅 CDR3），捕获 CDR + FWR 的界面信息
2. **轻链特异性**: κ 和 λ 分开训练，反映体内 B 细胞发育的不同选择压力
3. **B 细胞发育感知**: 配对分数随 B 细胞成熟（naïve → GC → memory）单调递增
4. **结构敏感性**: 对 VH-VL 界面位置的氨基酸差异敏感，可定位关键残基

---

## 应用场景

- 空间转录组学中 H-L 对重建（与 Engblom et al. `repair` 方法互补）
- 单细胞 BCR 测序数据质量评估
- 治疗性抗体 developability 评估
- B 细胞肿瘤发育起源研究（白血病/淋巴瘤配对分数谱）
- 抗体库模拟中的配对约束检查

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 来源 | [[wiki/sources/s41592-025-02913-x\|ImmunoMatch 论文详情]] |
| 概念 | [[wiki/concepts/antibody-hl-pairing\|抗体 H-L 链配对预测]] |
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 实体 | [[wiki/entities/deeptcr\|DeepTCR]] |
| 实体 | [[wiki/entities/sonnia\|soNNia]] |
