---
title: Antibody Heavy-Light Chain Pairing
tags: [concept, antibody, b-cell, h-l-pairing, immunology, bcr]
created: 2026-05-06
updated: 2026-05-06
---

# Antibody H-L Chain Pairing（抗体轻重链配对）

> 抗体由重链（H）和轻链（L）组装而成，H-L 链的特异性配对是 B 细胞受体（BCR）功能性和抗体药物可开发性的核心问题。

---

## 生物学基础

### 抗体结构
- 抗体可变域由 VH（重链）和 VL（轻链）组成，共同形成抗原结合位点
- VH-VL 界面由 **CDR 环**（CDR1/2/3）和 **FWR（框架区）** 共同构成
- CDR3 多样性最高，CDR1/2 和 FWR 同样参与界面接触

### 轻链类型：κ vs λ
- 人类抗体使用两种轻链类型——κ（IGK）和 λ（IGL），由不同染色体上的基因座编码
- κ 和 λ 的 VL 域序列相似度仅 **47.8%**（vs κ 内部 69.1%，λ 内部 61.8%）
- B 细胞发育中 **κ 先重排**，若 H-κ 配对失败或不稳定 → λ 重排作为"救援"机制
- 约 60% 的人类抗体使用 κ，40% 使用 λ（比例因物种而异）

### B 细胞发育中的配对选择
1. **前 B 细胞阶段**: H 链重排 → 与替代轻链（surrogate light chain）形成 pre-BCR
2. **κ 重排**: 产生 H-κ 对 → 受中心耐受检查（阳性选择 + 阴性选择）
3. **λ 救援**: H-κ 失败 → κ 删除 → λ 重排 → H-λ 对
4. **成熟 B 细胞**: 表达功能性 BCR 后离开骨髓
5. **生发中心反应**: 体细胞高频突变 + 类别转换重组 → H-L 配对进一步优化
6. **记忆 B 细胞**: 配对分数最高，反映长期选择和优化

---

## 计算方法

### 问题定义
- **任务**: 给定一条 H 链和一条 L 链的序列，判断它们是否是天然配对（cognate pair）
- **难点**: 无法获得真实的反例（体内不稳定的 H-L 对被清除）
- **策略**: random shuffle 生成伪负例；或基于已有配对数据进行统计建模

### 方法演进

| 方法 | 特点 | 参考文献 |
|------|------|---------|
| 统计分析 (V/J 基因使用) | 检测非随机的 H-L 关联 | Brezinschek 1998, de Wildt 1999 |
| 高通量表达筛选 | 体外验证配对稳定性 | Wu 2011, Zhu 2013 |
| CNN (CDR3 编码) | 捕获局部序列模式 | Guo 2026 (baseline) |
| **AntiBERTa2 fine-tune** | 抗体特异性语言模型，捕获长程交互 | **ImmunoMatch, Guo 2026** |
| ESM-2 fine-tune | 通用蛋白质语言模型 | Guo 2026 (对比) |

### ImmunoMatch 框架（Guo et al. 2026）
- **基础**: AntiBERTa2（5.58 亿条抗体序列预训练）
- **训练**: 233,880 对 H-L（6 位健康捐赠者）
- **变体**:
  - ImmunoMatch-κ: H-κ 配对，Accuracy 0.817
  - ImmunoMatch-λ: H-λ 配对，Accuracy 0.764
- **应用**: 空间转录组 H-L 重建、治疗性抗体评估、B 细胞发育阶段分析

---

## 核心挑战

1. **H-L 混杂性（promiscuity）**：一条 H 链可与多达 1000 条不同的 L 链配对 → 真实配对的定义本身有模糊性
2. **伪负例问题**：随机 shuffle 的反例在体内可能实际可以配对
3. **轻链类型异质性**：κ 和 λ 序列差异大，混合训练降低性能
4. **从核酸到蛋白的差距**：mRNA 水平的 BCR 序列不完全反映蛋白水平的稳定配对

---

## 应用意义

### 基础研究
- 量化 B 细胞成熟过程中的 H-L 配对优化
- 研究 B 细胞肿瘤的发育起源（Pre-B-ALL → 低配对分数；生发中心淋巴瘤 → 高配对分数）

### 抗体工程
- 治疗性抗体的 developability 评估（与 solubility、immunogenicity 预测互补）
- 从空间转录组数据重建抗体对
- 抗体库质量评估（检验单细胞 BCR 测序的配对 fidelity）

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 来源 | [[wiki/sources/s41592-025-02913-x\|ImmunoMatch — Guo et al. 2026]] |
| 实体 | [[wiki/entities/immunomatch\|ImmunoMatch]] |
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire（T 细胞受体库）]] |
| 概念 | [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] |
