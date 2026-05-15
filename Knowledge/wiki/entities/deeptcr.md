---
title: DeepTCR
tags: [entity, tool, deep-learning, tcr]
created: 2026-05-06
updated: 2026-05-06
---

# DeepTCR

> 基于 VAE 的 TCR 库深度学习框架，用于 TCR 库的聚类、预测和特征提取。Sidhom et al., *Nature Communications*, 2021.

## 简介

DeepTCR 是一种无监督深度学习方法，利用变分自编码器（VAE）学习 TCR 序列的低维潜在表征，同时整合 CDR3 序列和 V/J 基因使用信息。

## 核心功能
- **TCR 聚类**：在潜在空间中自动聚类功能相关的 TCR
- **抗原特异性预测**：基于 TCR 序列预测其抗原特异性
- **特征重要性**：识别对区分不同抗原特异性最关键的序列位置
- **多任务学习**：同时处理多个预测任务

## 意义
深度学习可以从 TCR 序列中提取有生物学意义的"序列概念"（sequence concepts），而无需预先定义特征。

## 相关页面
- [[wiki/concepts/tcr-epitope-prediction|TCR-Epitope Binding Prediction]]
- [[wiki/sources/batch-tcr-epitope-prediction|TCR 结合预测文献合集]]
