---
title: EOMES (Eomesodermin) — T-box Transcription Factor
tags: [concept, immunology, transcription-factor, t-box, eomes]
created: 2026-05-06
updated: 2026-05-07
sources: ["raw/xie-et-al-2026-thk-cells-nature-immunology.pdf"]
---

# EOMES（Eomesodermin）

> **定义**: T-box 家族转录因子，在 CD8⁺ T 细胞和 NK 细胞中已知调控效应功能，最新研究发现其是 ThK 细胞的核心调控因子。

---

## 基本信息

- **全称**: Eomesodermin（EOMES）
- **家族**: T-box 转录因子家族（与 T-bet 同家族）
- **在 T 细胞中的角色**:
  - **CD8⁺ T 细胞**: 调控效应分化、耗竭、记忆形成
  - **NK 细胞**: 调控成熟和效应功能
  - **CD4⁺ T 细胞**: 新发现 → ThK 细胞的主控转录因子

---

## 在 ThK 中的核心作用（Xie et al. 2026）

### 1. 表达特征
- Gzmk-tdTomato⁺ CD4⁺ T 细胞中 EOMES 显著高表达
- GZMK 与 EOMES 在人类 UC 中呈 **极强正相关**（Pearson R² = 0.953, P < 0.001）
- 在小鼠和人类 CD4⁺ T 细胞中，Eomes 和 Gzmk 在 UMAP 上几乎完全重叠的表达模式

### 2. 必要性（Loss-of-function）
- Cd4-cre *Eomes*^(fl/fl) 条件性敲除：
  - **几乎完全消除** Gzmk-tdTomato 表达
  - 显著降低 perforin 表达
  - 轻度降低 GZMB
  - 不影响 T-bet 表达
  - RORγt⁺ 和 IL-17A⁺ 细胞增加（→ 替代谱系的命运偏移）

### 3. 充分性（Gain-of-function）
- 逆转录病毒过表达 EOMES → 在非极化条件下：
  - **Gzmk 和 Prf1 是最显著上调的基因**
  - 抑制 Th17（Rorc）、Th2（Il5, Il4, Il13）基因
  - 抑制 T-bet 表达（不诱导经典 Th1 程序）
  - 上调 Prdm1（BLIMP1）→ 抑制 Tfh 分化

### 4. 直接靶基因（CUT&Tag 验证）

| 基因 | 功能 | 验证方法 |
|------|------|----------|
| *Gzmk* | 效应分子 | CUT&Tag + ATAC-seq |
| *Prf1* | 穿孔素 | CUT&Tag + ATAC-seq |
| *Ccl3, Ccl4* | 趋化因子 | 转录组整合分析 |
| *Ccr5* | 趋化因子受体 | 同上 |
| *Nkg7* | 效应分子 | 同上 |
| *Il10* | 免疫调节 | 同上 |
| *Tox* | T 细胞耗竭 | ATAC-seq 共定位 |
| *Klrg1* | 终末分化标志 | ATAC-seq 共定位 |

---

## EOMES 在其他 Th 亚群分化中的作用

| 极化条件 | EOMES 过表达效果 |
|----------|-----------------|
| Th1 | 抑制 T-bet 表达 |
| Th2 | 轻度抑制 GATA3；强烈抑制 IL-5 |
| Th17 | 显著下调 RORγt 和 IL-17A |
| Treg | 显著下调 FOXP3 |
| Tfh (体内) | 上调 BLIMP1 → 抑制 BCL6 → 减少 Tfh |

→ EOMES 不仅驱动 ThK 程序，还 **主动抑制其他 Th 谱系**。

---

## 表观遗传调控

- ThK 细胞中 *Eomes* 基因座具有 **增强的染色质可及性**（启动子+增强子）
- EOMES 结合的染色质区域在 ThK 细胞中 **开放程度更高**
- T-box 基序（包括 Eomes 自身基序）在 ThK 开放区域显著富集
- ROR、BCL6、GATA 基序在 ThK 关闭区域富集（对应 Th17、Tfh、Th2 谱系被抑制）

---

## 与其他 T-box 家族成员的关系

| 因子 | 在 ThK 中 | 关系 |
|------|-----------|------|
| **T-bet** (Tbx21) | 低表达 | EOMES 过表达抑制 T-bet；可能有部分冗余功能 |
| **EOMES** | 高表达 | ThK 的主控因子 |
| TBX6, TBR1 | 不表达 | 无关 |

---

## 实验方法速览

实验中验证 EOMES 功能的核心方法详见：

→ [[wiki/sources/xie-et-al-2026-thk-cells#实验方法详解|Xie et al. 2026 来源摘要 — 实验方法详解]]

| 验证维度 | 方法 | 关键结论 |
|---------|------|---------|
| **表达关联** | scRNA-seq + 流式 | Gzmk-tdTomato 细胞中 EOMES 高表达 |
| **必要性** | Cd4cre Eomes^fl/fl → 结肠炎 | 几乎完全消除 Gzmk-tdTomato + 缓解结肠炎 |
| **充分性** | 逆转录病毒 Eomes OE | 诱导 Gzmk/Prf1 表达，抑制其他谱系 |
| **直接靶基因** | CUT&Tag (HA-EOMES) + ATAC-seq | EOMES 直接结合 Gzmk, Prf1 等 18 个核心基因 |
| **功能贡献** | 基因整合分析 | 18 个直接靶基因（Ccl3/4, Ccr5, Nkg7 等）|

EOMES 是 ThK 致病程序的中枢调控节点：
- **靶向 EOMES** 比靶向单个效应分子（如 GZMK）更有效
- EOMES 同时调控 Gzmk, Prf1, 趋化因子等多条致病通路
- EOMES 缺失 → 致病效应消除 + 其他谱系替代（RORγt, FOXP3 上调）

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/thk-cells\|ThK 细胞]] |
| 来源 | [[wiki/sources/xie-et-al-2026-thk-cells\|Xie et al. 2026 来源摘要]] |
| 实体 | [[wiki/entities/chen-dong\|Chen Dong（董晨）]] |
