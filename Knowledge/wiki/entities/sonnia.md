---
title: soNNia
tags: [entity, tool, generative-model, tcr]
created: 2026-05-06
updated: 2026-05-06
---

# soNNia — Deep Generative Selection Model

> 深度生成选择模型，用于分析 T/B 细胞受体库中的选择压力。Isacchini et al., *Nature Communications*, 2021.

## 简介

soNNia 是一种深度生成模型，能够将 TCR/BCR 库中的 **生成过程（V(D)J 重组）** 与 **选择过程（胸腺选择/抗原驱动）** 分离开来。

## 核心创新
- 条件深度生成模型学习 V(D)J 重组的"基线"生成概率
- 比较观测到的 repertoire 与生成模型预测的 repertoire → 推断选择压力
- 定量评估正向选择和负向选择对每个序列的影响

## 应用场景
- 分析胸腺选择在 TCR 库形成中的作用
- 鉴定疾病特异性扩增的克隆
- 区分自身反应性和非自身反应性 TCR

## 相关页面
- [[wiki/concepts/tcr-repertoire|TCR Repertoire]]
- [[wiki/sources/batch-tcr-repertoire-analysis|TCR Repertoire 文献合集]]
