---
title: HLA Typing（HLA 分型）
tags: [concept, immunology, hla, ngs, clinical, ivd]
created: 2026-05-06
updated: 2026-05-06
---

# HLA Typing（HLA 分型技术）

> HLA（人类白细胞抗原）分型是移植配型、药物过敏筛查、疾病关联研究中的核心检测技术。由于其基因区域的极端复杂性，HLA 分型是生物信息学中公认的难题之一。

---

## HLA 基因的复杂性

HLA 是人类基因组中 **多态性最高的区域**：

| 挑战     | 说明                                                              |
| ------ | --------------------------------------------------------------- |
| 极端高多态  | IPD-IMGT/HLA 数据库已收录 >37000 个等位基因（截至 2025 年），HLA-B 有 >8000 个     |
| 高度同源   | Class I（A/B/C）之间、Class II（DRB1/3/4/5）之间序列高度相似 → 短读长易 mismapping |
| 相位模糊   | 两个等位基因的变异距离超过 read length 时无法判断单倍型                              |
| 拷贝数/缺失 | DRB3/4/5 不是每个人都有；null allele 需特别报告                              |
| 伪基因干扰  | HLA-H, HLA-J, HLA-K 等伪基因与功能基因高度相似                               |

---

## 分型策略对比

### 短读长（NGS / Illumina）

| 策略 | 代表工具 | 优点 | 缺点 |
|------|---------|------|------|
| 等位基因库比对 | **OptiType**, HLA-HD, Arcas-HLA | 简单高效，Class I >98% 准确率 | 依赖数据库，无法发现新等位基因 |
| 图比对 | HISAT-genotype | 减少 reference bias | 图构建复杂 |
| de novo 组装 | HLA-VBSeq | 理论上可发现新等位基因 | 短读长组装能力有限 |

### 长读长（Nanopore / PacBio）

| 平台 | 错误率 | 特点 |
|------|--------|------|
| **Nanopore** (R10.4.1) | ~3-5% | indel 为主（尤其 homopolymer），需 consensus 纠错 |
| **PacBio HiFi** | ~0.1-0.5% | 均匀错误分布，无 homopolymer bias |

**核心优势**：
- 天然解决相位问题（单条 read 可覆盖全基因）
- 解析同源复杂区域（明确区分 DRB1 vs DRB3/4/5）
- 无 PCR / 低 PCR 方案 → 等位基因 read balance 更好

### 其他常用工具

| 工具 | 支持 | 特点 |
|------|------|------|
| **T1K** | 长短读长 | 基于 EM 算法 |
| **HLA-LA** | 长短读长 | 计算资源需求大 |
| **OptiType** | NGS 短读长 (Class I) | ILP 优化，业界金标准之一 |
| **HLA-HD** | NGS 短读长 (Class I+II) | 对低覆盖敏感 |

---

## 质量控制

### 样本层面
- 总 read 数 / on-target rate
- 去重后有效 read 数
- Q30 比例
- 交叉污染检测（≥3 个等位基因信号）

### 分型层面
- 分型置信度分数（第一名 vs 第二名的 delta score）
- 外显子覆盖均匀性（尤其是 exon 2/3）
- 等位基因 read balance（偏离 50:50 提示 allele dropout / null allele）
- G group / P group 模糊报告

### 批次层面
- 阳性/阴性对照
- 批内重复性

---

## 临床 IVD 验证

6 大验证实验：
1. **准确性** — 用 IHWG reference panel 计算 concordance rate
2. **一致性** — 跨批次/操作员/仪器
3. **重复性** — 同批次 N 次重复
4. **LoD（检测极限）** — 梯度稀释找失败临界值
5. **抗干扰** — 血红蛋白/胆红素/脂血干扰测试
6. **交叉污染** — 高低浓度交替排列

---

## 可交付软件要求

| 要求 | 说明 |
|------|------|
| 可重复计算 | 固定随机种子 + 锁定数据库版本 + 容器化 |
| 版本管理 | SemVer + 数据库版本记录 + 升级影响评估 |
| 审计日志 | 每一步可追溯（谁、时间、版本、输入、输出） |
| 容错 | 输入异常时不崩溃，给出有意义报错 |
| 可配置 | 参数可通过配置文件调整 |

---

## 与 TCR 的关联

HLA 分型与 [[wiki/concepts/tcr-repertoire|TCR Repertoire]] 分析密切相关：
- TCR 识别抗原受 **MHC 限制性** — TCR 只有在抗原由特定 HLA 呈递时才识别
- 不同的 HLA 类型 → 不同的肽呈递谱 → 不同的 TCR repertoire 组成
- TCR-epitope 预测模型通常需要同时输入 **TCR 序列 + HLA 类型** 作为特征

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 来源 | [[wiki/sources/hla-typing-guide\|HLA 分型指南来源]] |
| 概念 | [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] |
| 概念 | [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] |
| 实体 | [[wiki/entities/mixcr\|MiXCR]] |
