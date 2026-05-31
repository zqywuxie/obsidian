---
title: "Deep Peptide Recognition Profiling (PRP) Decodes TCR Specificity — Wang et al. 2026"
tags: [source, paper, tcr, epitope, prediction, prp, deep-learning, yeast-display, hla-b27, autoantigen]
created: 2026-05-19
updated: 2026-05-19
sources:
  - type: paper
    title: "Deep peptide recognition profiling decodes TCR specificity and enables disease-associated antigen discovery"
    authors: "Wang N, Yeh H, Lai B, et al."
    journal: "Nature Biotechnology"
    year: 2026
    doi: "10.1038/s41587-026-03128-x"
    url: "https://doi.org/10.1038/s41587-026-03128-x"
  - type: article
    title: "科普解读 — 计算生物前沿（微信公众号）"
    url: "https://mp.weixin.qq.com/s/YZCDBZkHLuSFPgorCmoW1w"
    raw: "raw/wang-2026-prp-tcr-specificity-nbt.md"
---

# Deep Peptide Recognition Profiling (PRP) — Wang et al. 2026

> Wang N, Yeh H, Lai B, *et al.* *Nature Biotechnology* (2026)
> DOI: [10.1038/s41587-026-03128-x](https://doi.org/10.1038/s41587-026-03128-x)

## Summary

这篇论文提出了 **深度肽识别图谱（Deep Peptide Recognition Profiling, PRP）** —— 一个实验-计算整合平台，用于系统解码 TCR 特异性并发现疾病相关抗原。

### 核心方法：两步策略

**Step 1 — 实验筛选（PRP 构建）：**
- 使用高通量酵母展示（yeast display）构建巨大 9 肽文库（>10⁹ 种肽）
- 将肽通过 HLA-B\*27:05 展示在酵母表面
- 让单个 TCR 筛选文库 → 多轮富集后通过 NGS 读出阳性肽
- 为每个 TCR 生成一张"深度肽识别图谱"（PRP）

**Step 2 — 计算建模（蛋白语言模型训练）：**
- 将 TCR CDR3β 序列与抗原肽序列输入蛋白语言模型
- 用 PRP 实验数据训练模型 → 学习 TCR 识别肽的规则
- 模型性能：ROC-AUC > 0.95, PR-AUC > 0.66（酵母展示留出测试）
- 归因分析显示模型关注的肽位点与实验基序和晶体结构一致

### 关键发现

1. **序列相似 ≠ 识别相似**：基于 PRP 的功能聚类与 CDR3β 序列树不一致。TCR 的"功能亲缘关系"不能简单从序列推断——真正定义 TCR 关系的，是它们识别肽的整体模式。

2. **PSG5 候选自身抗原**：模型扫描人蛋白组（>20 万 HLA-B\*27:05 候选 9 肽），发现 PSG5 肽被多个疾病相关 TCR 识别。单细胞转录组提示 PSG5 在虹膜色素上皮细胞中表达；HLA-B27⁺ 强直性脊柱炎/急性前葡萄膜炎（AAU）患者中 PSG5 特异性 CD8⁺ T 细胞频率显著高于 HLA-B27⁺ 健康对照；晶体结构显示 PSG5 肽与已知 YEIH 肽有相似的 TCR 结合方式。

3. **TCR 功能邻域（Functional Neighborhood）**：对 TCR 19.2 进行 CDR3β 突变实验，发现邻近突变体的 PRP 高度相似，构成功能邻域。联合建模（合并邻域内多个 TCR 的 PRP 数据）显著提升 T 细胞激活预测能力。

4. **泛化取决于功能距离**：留一交叉验证显示，模型对新 TCR 的预测能力取决于 PRP 功能距离（而非序列距离）。PR 表现与 PRP 功能距离强负相关（r ≈ −0.78, p < 0.001）。引入马氏距离作为模型内部的不确定性指标。

### 与项目关联

- **TCR-表位预测新范式**：从"序列相似性聚类"转向"实验测定的肽识别相似性"
- **HLA-B27 自身免疫疾病**：直接相关于强直性脊柱炎和急性前葡萄膜炎的抗原发现
- **TCR 工程**：功能邻域联合建模为 TCR 工程和细胞治疗提供新思路
- **可迁移框架**：方法不限于 HLA-B27，可推广到其他 HLA 类型的 TCR 特异性研究

### References
- Wang N, Yeh H, Lai B, *et al.* *Nat Biotechnol* (2026). DOI: 10.1038/s41587-026-03128-x
