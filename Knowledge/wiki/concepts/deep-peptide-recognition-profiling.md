---
title: Deep Peptide Recognition Profiling (PRP)
tags: [concept, tcr, epitope, yeast-display, protein-language-model, specificity, hla-b27]
created: 2026-05-19
updated: 2026-05-19
sources:
  - "Wang et al. 2026, Nat Biotechnol. DOI: 10.1038/s41587-026-03128-x"
---

# Deep Peptide Recognition Profiling（深度肽识别图谱, PRP）

> 一种实验-计算整合方法：先用高通量酵母展示系统测量单个 TCR 识别哪些肽（实验 PRP），再用这些数据训练蛋白语言模型，让模型学习 TCR 识别肽的"语法"。

---

## 背景：为什么需要 PRP？

传统 TCR-表位预测方法（如 GLIPH、TCRdist）基于 **TCR 序列相似性**对 TCR 进行聚类。但该范式存在根本局限：

- **TCR 序列相似 ≠ 功能相似**：有些序列很像的 TCR 识别完全不同的抗原；有些序列差异大的 TCR 却识别同一抗原
- **从序列到特异性存在 gap**：序列相似性反映的是进化/生成关系，而非功能关系
- **缺少系统性实验数据**：过去缺乏为单个 TCR 大规模测量肽识别谱的高通量方法

PRP 的核心洞察：**从"看 TCR 序列像不像"转向"看 TCR 真实识别的肽像不像"。**

---

## 方法：两步策略

### Step 1: 实验 PRP 构建
1. **构建 9 肽文库**：覆盖 >10⁹ 种随机 9 肽序列
2. **酵母展示**：将肽通过目标 HLA 分子（如 HLA-B\*27:05）展示在酵母表面
3. **TCR 筛选**：让单个 TCR 与酵母文库孵育 → TCR 识别的酵母被富集
4. **NGS 读出**：多轮筛选后对富集肽进行高通量测序 → 得到该 TCR 的"深度肽识别图谱"

### Step 2: 蛋白语言模型训练
1. 输入特征：TCR CDR3β 序列 + 抗原肽序列
2. 训练数据：Step 1 得到的 PRP 实验数据（正：富集肽；负：未富集肽）
3. 任务：预测 TCR-肽对是否发生识别
4. 验证：留出测试集 ROC-AUC > 0.95, PR-AUC > 0.66；归因分析确认模型关注与结构一致的肽位点

---

## 关键概念

### TCR 功能距离（Functional Distance）
- 基于 PRP 的肽识别相似性来定义 TCR 之间的距离
- 与 CDR3β 序列距离（编辑距离、TCRdist）**不一致**
- 真正定义 TCR 关系的是"它们识别肽的整体模式"

### TCR 功能邻域（Functional Neighborhood）
- 一组 PRP 高度相似的 TCR 构成功能邻域
- 邻域内突变体的识别偏好高度保守
- 联合建模（合并邻域内多个 TCR 数据）显著提升激活预测
- **对 TCR 工程的意义**：设计 TCR 时应围绕功能邻域而非单个序列

### 泛化由功能距离决定
- 模型对新 TCR 的预测能力取决于 PRP 功能距离，而非序列距离
- PR 表现与 PRP 功能距离强负相关（r ≈ −0.78, p < 0.001）
- **马氏距离**作为模型内部不确定性指标，衡量新 TCR 是否在训练分布内

---

## 应用：HLA-B27 相关自身免疫病

该论文以 **HLA-B\*27:05**（与强直性脊柱炎、急性前葡萄膜炎高度相关）为模型系统。

| 发现 | 证据 |
|------|------|
| **PSG5 候选自身抗原** | 被多个疾病相关 TCR 交叉识别 |
| PSG5 在虹膜表达 | 单细胞转录组提示虹膜色素上皮细胞表达 PSG5 |
| PSG5 特异性 CD8⁺ T 细胞 | HLA-B27⁺ 患者频率显著高于 HLA-B27⁺ 健康对照 |
| 晶体结构确认 | PSG5 肽与已知 YEIH 肽的 TCR 结合方式相似 |

> ⚠️ PSG5 目前应表述为 **候选自身抗原**，而非已完全证明的致病抗原。

---

## 意义与局限

### 范式突破
- PRP 建立了从"猜抗原"到"系统测量"的方法学转变
- 实验 + 计算的闭合循环：实验 PRP → 训练模型 → 扫描蛋白组 → 验证 → 新生物学发现

### 可迁移性
- 方法不限于 HLA-B27，可推广到其他 HLA 类型
- 模型不确定性（马氏距离）为生物医学 AI 提供"知道自己不知道"的能力

### 局限
- 需要大规模酵母展示实验，技术门槛高
- 目前聚焦 9 肽和 CDR3β 主导的识别模式
- 模型泛化依赖于功能距离——全新 TCR 功能族仍需补充实验

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] |
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 来源 | [[wiki/sources/wang-2026-prp-tcr-specificity\|PRP — Wang et al. 2026]] |
| 来源 | [[wiki/sources/batch-tcr-epitope-prediction\|TCR 结合预测文献合集]] |
