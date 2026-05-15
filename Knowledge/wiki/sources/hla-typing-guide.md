---
title: HLA 分型技术全面指南
tags: [source, hla, ngs, long-read, clinical, ivd]
created: 2026-05-06
updated: 2026-05-06
source-file: "raw/hla-typing-guide-2025.md"
---

# HLA 分型技术全面指南

> **来源**: 微信公众号"AI生信工坊"  
> **标题**: HLA 分型面试高频 16 问：从短读长到长读长，从算法到落地  
> **提取工具**: defuddle  
> **原文链接**: https://mp.weixin.qq.com/s/vjNt5CjxJcDkuHWQ-OuATg  

---

## 内容结构

文章以 16 个面试问答形式，系统覆盖 HLA 分型的完整技术栈：

### 一、HLA 基因复杂性
- 极端高多态性（>37000 个等位基因，2025 年 IMGT/HLA 数据库）
- 高度同源性（Class I 之间、Class II 之间、DRB1/3/4/5 之间）
- 相位问题（phasing）
- 拷贝数变异与基因缺失
- 伪基因干扰

### 二、短读长（NGS/Illumina）HLA 分型
| 策略 | 代表工具 | 特点 |
|------|---------|------|
| 等位基因库比对 | OptiType, HLA-HD, Arcas-HLA | 简单高效，Class I > 98% 准确率 |
| 图比对 | vg + HLA typing, HISAT-genotype | 减少 reference bias |
| de novo 组装 | HLA-VBSeq | 理论上可发现新等位基因 |

### 三、长读长（Nanopore/PacBio）HLA 分型
- 核心优势：解决相位问题、解析同源复杂区域、减少 PCR 偏好
- 纠错策略：自纠错 consensus、错误模型集成、POA 共识

### 四、红细胞血型基因分型
- ABO、Rh（RHD/RHCE）、Kell、Duffy、Kidd 等系统
- 表型推断与特殊等位基因提示

### 五、临床报告 & IVD 验证
- 规则引擎、结果解释、LIS/HIS 对接
- 准确性/一致性/重复性/LoD/抗干扰/交叉污染验证

### 六、可交付软件
- 可重复计算、版本管理、审计日志
- 容错、日志、可配置、可验证

---

## 关键要点

1. HLA 分型的核心挑战是**高多态性 + 高同源性 + 相位模糊**
2. **短读长**方案成熟（OptiType 等），但存在相位和同源区域问题
3. **长读长**天然解决相位问题，Nanopore 错误率已降至 ~3-5%
4. 临床 IVD 验证需要 6 大实验：准确性、一致性、重复性、LoD、抗干扰、交叉污染
5. 软件需满足 SemVer、容器化、审计日志等 SaMD 合规要求

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/hla-typing\|HLA 分型技术]] |
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 工具 | [[wiki/entities/mixcr\|MiXCR]] |
