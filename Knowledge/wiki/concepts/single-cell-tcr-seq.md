---
title: Single-cell TCR-seq & Multi-omics Integration
tags: [concept, single-cell, tcr, multi-omics, transcriptomics]
created: 2026-05-06
updated: 2026-05-06
---

# Single-cell TCR-seq & Multi-omics Integration

> 单细胞水平同时获取 TCR 序列和转录组/表观组等多模态信息，揭示 T 细胞异质性和功能的分子基础。

---

## 技术发展

### 从 bulk 到单细胞

- **Bulk TCR-seq**：只能获知群体中 TCR 序列的丰度，失去细胞-序列对应关系
- **单细胞 TCR-seq**：每个细胞的 TCRαβ 配对 + 转录组同时获得
- 10x Genomics 平台是目前最广泛使用的单细胞 TCR-seq 解决方案

### 单细胞 TCR-seq 能解决的问题
1. 同一个细胞的 α 链和 β 链配对
2. 双 TCR（dual TCR α）的频率和功能
3. 同一 TCR 克隆的转录状态（功能异质性）
4. 细胞谱系追踪（TCR 作为"条形码"）

---

## 多模态整合

### 可整合的数据模态
| 模态 | 技术 | 提供的信息 |
|------|------|-----------|
| **TCR 序列** | scTCR-seq | 克隆型、抗原特异性 |
| **转录组** | scRNA-seq | 基因表达、细胞状态 |
| **表观组** | scATAC-seq | 染色质开放性、调控元件 |
| **蛋白组** | CITE-seq | 表面蛋白表达 |
| **表位** | ECCITE-seq | 抗原特异性（用 DNA 条形码标记抗原） |

### 整合分析框架
| 方法 | 年份 | 策略 |
|------|------|------|
| **Carter et al.** | 2019 | 单细胞测序揭示 αβ TCR 配对的功能角色 |
| **Zhang et al.** | 2021 | 单细胞转录组 + TCR 绘制功能 landscape |
| **Drost et al.** | 2024 | 多模态生成模型联合分析 TCR + 基因表达 |
| **Mullan et al.** | 2024 | 以 TCR 为中心的多模态分析视角 |
| **Gao et al.** | 2024 | 跨模态统一整合框架 |

---

## 关键发现

### αβ 配对非随机
TCR α 链和 β 链的配对不是随机的——存在功能选择压力。同一抗原特异性的 T 细胞共享结构相似的 CDR3，但 α/β 配对组合有偏好。

### 克隆型 vs 转录状态
- 同一 TCR 克隆的 T 细胞可处于不同的转录状态（naïve, effector, memory, exhausted）
- 不同 TCR 克隆可处于相同的功能状态
- TCR 序列可能影响记忆形成的概率（Lagattuta 2025）

### 功能性细胞毒性 CD4⁺ T 细胞
Carter et al. (2019) 发现一些 CD4⁺ T 细胞表达细胞毒性程序，且其 αβ TCR 配对特征区别于经典 Th 细胞——与 [[wiki/concepts/thk-cells|ThK 细胞]] 的发现有概念关联。

---

## 技术挑战

- **双 TCR（Dual TCR）**：约 30% 的 T 细胞表达两种 α 链，scTCR-seq 是否能同时捕获两种情况取决于技术
- **灵敏度**：低表达 TCR 的捕获效率
- **成本**：单细胞测序仍显著高于 bulk 测序
- **batch effect 校正**：跨实验、跨平台的整合

---

## 跨组织/跨疾病参考

Xue et al. (2025) 构建了跨疾病和人群水平的单细胞 TCRαβ repertoire 参考图谱，整合了结肠炎、肿瘤、EAE 和 LCMV 感染等多种疾病模型的数据。

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 概念 | [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] |
| 来源 | [[wiki/sources/batch-sc-multiomics-tcell-bio\|单细胞多组学文献合集]] |

**引用文献**: Carter 2019, Zhang 2021, Drost 2024, Mullan 2024, Gao 2024, Lagattuta 2025, Xue 2025
