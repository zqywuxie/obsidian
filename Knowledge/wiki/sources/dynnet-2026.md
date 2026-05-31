---
title: "DynNet — Dou et al. 2026"
tags: [source, paper, single-cell, stochastic-dynamics, GRN, cell-fate]
created: 2026-05-22
updated: 2026-05-22
sources:
  - type: paper
    title: "Inferring stochastic dynamics by biophysical Neural ODE using single-cell transcriptomics"
    authors: "Dou J, Lyu W, Chen F, Nie Q, Li C"
    journal: "Nature Communications, 2026 (Article in Press)"
    doi: "10.1038/s41467-026-73257-z"
    url: "https://doi.org/10.1038/s41467-026-73257-z"
  - type: article
    title: "DynNet：把单细胞静态快照变成细胞命运的动力学模型"
    platform: "微信公众号 — 计算生物前沿"
    url: "https://mp.weixin.qq.com/s/Um73DQFGq2KsVC0Mgek6jQ"
aliases:
  - "DynNet"
  - "Dou 2026"
  - "stochastic dynamics inference network"
---

# DynNet: 随机动力学推断网络 — Dou et al. 2026

## 来源摘要

本文来自 **Nature Communications** (2026, Article in Press)，由复旦大学和 UC Irvine 团队完成。论文提出了 **DynNet**（随机动力学推断网络），一种将神经常微分方程与生物物理模型及先验知识整合的深度学习方法，用于从多时间点 scRNA-seq 数据推断细胞命运的随机动力学。

## 核心方法

1. **随机微分方程框架**：将细胞状态演化分解为基因调控漂移项 + 随机噪声扩散项
2. **希尔函数编码**：显式建模基因激活、抑制和降解，参数具有生物可解释性
3. **先验约束机制**：硬约束（屏蔽非先验边）和软约束（惩罚非先验边，允许发现新关系）
4. **交替优化**：先优化漂移参数（动力学一致性 + 权重匹配损失），再优化噪声参数（KL 散度损失）
5. **能量景观重建**：从稳态概率分布 U(x) = -ln P_ss(x) 构建，识别吸引子、鞍点、转变路径

## 主要发现

- **MISA 模拟验证**：准确恢复三稳定态位置、决策边界、速度场；在少时间点下优于确定性 Neural ODE
- **7基因发育分支**：重建 G1→G2→G3 级联激活和 G4/G5 相互抑制驱动的命运分叉
- **肝细胞分化**：重建 MH/LB 两个吸引子的能量景观，中间态降低转变代价，MH 分化具有动力学偏向
- **EMT/MET 可塑性**：MET 经过中间态（IM/pEMT）而非直接切换；CD44 维持间质态、CDH1 抑制 EMT
- **计算敲除**：TOB1 敲除 → LB 加速，RANBP1 敲除 → MH 促进；生成可检验假设

## 资源链接

- **论文**: https://doi.org/10.1038/s41467-026-73257-z
- **微信公众号文章**: https://mp.weixin.qq.com/s/Um73DQFGq2KsVC0Mgek6jQ
- **精读笔记**: [[Knowledge/papers/dynnet-2026/paper.md|DynNet 精读]]
