---
title: "Assessment of computational methods in predicting TCR–epitope binding recognition"
aliases:
  - "Lu et al. 2026 - TCR-epitope prediction benchmark"
tags:
  - literature-note
  - reading-note
  - immunology
created: "2026-05-08"
updated:

source: "local Zotero PDF"
doi: "10.1038/s41592-025-02910-0"
zotero_item_key: "NUW8PTAX"
pdf_key: "9Q7E7XUN"
author: "Yanping Lu, Yuyan Wang, Meng Xu, Bingbing Xie, Yumeng Yang, Haodong Xu, Shengbao Suo"
year: 2026
journal: "Nature Methods"
paper_type: "research-article"
review_type:
review_scope:
review_period:
review_corpus_size:
review_method:
review_scope_tags: []

canonical_tags:
  - tcr-epitope-prediction
  - benchmark
  - computational-method
  - immune-repertoire
candidate_tags:
  - negative-sample-strategy
  - cross-reactivity

theme: "TCR–epitope 预测模型的系统性基准测试"
problem_setting: "TCR–epitope 相互作用预测"
methodology: "多维度基准评估框架"
data_source: "21 个数据集，762 个 epitope，数十万 binding TCR"
key_finding: "负样本来源显著影响模型准确性；模型在未见 epitope 上泛化能力普遍不足"
relevance: "对本项目的免疫组库分析工作流有直接指导意义"
---

# Assessment of computational methods in predicting TCR–epitope binding recognition

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 作者 | Yanping Lu, Yuyan Wang, Meng Xu, Bingbing Xie, Yumeng Yang, Haodong Xu, Shengbao Suo |
| 年份 | 2026 |
| 来源 | Nature Methods, Volume 23, January 2026, p.248–259 |
| DOI | 10.1038/s41592-025-02910-0 |
| Zotero 条目 | NUW8PTAX |
| PDF 链接 | `zotero://open-pdf/library/items/9Q7E7XUN` |
| 文献类型 | research article (benchmark / analysis) |

## 标签标记

> 这里只记录会影响检索、比较和综述写作的标签；完整标签树放在 `config/taxonomy.yaml`，不要在每篇笔记里重复展开。

- **Zotero 原始标签**：（无）
- **标签选择依据**：正文证据推断
- **已选标准标签**：`tcr-epitope-prediction`, `benchmark`, `computational-method`, `immune-repertoire`
- **新增 / 候选标签**：`negative-sample-strategy`, `cross-reactivity`

| 标签或证据 | 处理方式 | 理由 |
| --- | --- | --- |
| TCR–epitope 预测 | 标准标签 | 论文核心主题 |
| 基准测试 / benchmarking | 标准标签 | 论文主要贡献是系统性评估 |
| 负样本策略 (negative source) | 候选标签 | 是论文重要发现，但尚未在其他文献中验证 |
| 交叉反应性 (cross-reactivity) | 候选标签 | 论文涉及 TCR 相似性与交叉反应性分析 |

## 一句话摘要

> 本文对 50 个公开的 TCR–epitope 结合预测模型进行了系统性基准测试，基于 21 个数据集、762 个 epitope 和数十万条结合 TCR，揭示了负样本来源对模型准确性的关键影响，以及所有模型在未见 epitope 上泛化能力不足的普遍局限。

## 问题定位

- **研究对象**：TCR–epitope 相互作用的计算预测方法
- **核心问题**：现有模型的性能到底如何？哪些因素影响预测准确性？模型能否泛化到未见过的 epitope？
- **应用场景**：免疫组库数据分析、肿瘤新抗原识别、自身免疫病研究
- **与既有研究的差异**：
  - 相比 IMMREP22（仅评估少数模型，聚焦 seen-epitope）
  - 相比 IMMREP23（测试数据存在潜在 target leakage）
  - **本文优势**：规模最大（50 模型）、维度最全（seen + unseen epitope、原始模型 + 重训练、多种负样本策略）
- **在文献谱系中的位置**：是目前最全面的 TCR–epitope 预测模型基准测试研究，为后续模型开发提供了标准化的评估框架

## 综述论文专用部分（如适用）

> 本篇为 benchmark/analysis 论文，非综述。以下不适用，但可在文献综述可复用点中提取相关背景。

## 模型与假设

> 本篇为方法基准测试论文，不提出新模型。以下对评估框架进行分析。

### 评估框架设计

- **评估对象**：50 个模型（7 传统机器学习 + 43 深度学习）
- **模型分类**：
  - CDR3β-only 模型（仅使用 CDR3β 序列）
  - CDR3β + others 模型（额外特征：MHC、CDR3α 等）
- **评估场景**：
  - Seen epitope（训练集中出现过的 epitope）
  - Unseen epitope（训练集未出现过的新 epitope）
- **评估层级**：
  1. 原始模型评估（用独立测试集测试已发表模型的原始版本）
  2. 重训练模型评估（统一条件下重训练 31 个有开源代码的模型）

### 关键假设

- 负样本的构建策略（AS/PS/HS）会影响模型评估的公平性
- 独立测试集是避免评估偏差的关键
- TCR 序列相似性（交叉反应性）需要被严格排除

## 求解方法 / 分析方法

- **总体思路**：构建标准化的多层评估框架，从数据收集 → 测试集构建 → 原始模型评估 → 重训练模型评估 → 影响因素分析
- **关键步骤**：
  1. 从 21 个数据库收集数据
  2. 构建训练集、测试集和独立测试集
  3. 构建三类负样本：AS (antigen-specific)、PS (patient-sourced)、HS (healthy-sourced)
  4. 引入 refined cross-matching AS 策略，减少假阴性配对
  5. 排除交叉反应性 TCR（训练集和测试集之间的相似序列）
  6. 分别评估 seen-epitope 和 unseen-epitope 预测性能
- **评价指标**：AUPRC（主要）、accuracy、precision、recall

## 核心公式 / 机制

> 本篇为基准测试，不涉及核心公式。以下列出关键评估设计。

### 负样本构建策略

- **AS (Antigen-Specific)**：从已知不结合特定 epitope 的 TCR 中采样
- **PS (Patient-Sourced)**：从患者来源的 TCR 库中采样
- **HS (Healthy-Sourced)**：从健康人来源的 TCR 库中采样

> 论文核心发现：**负样本来源对模型评估结果有显著影响**，外部负样本（如 PS、HS）可能引入不可控的混杂因素，使模型性能被高估或低估。

## 数据与实验

- **数据来源**：21 个公开数据库
- **样本规模**：
  - 762 个 epitope
  - 数十万条 binding TCR
  - Seen-epitope 测试集：978 TCR（3 epitope）
  - Unseen-epitope 测试集：345 TCR（40 epitope）
- **评估模型数量**：
  - 50 个模型（含变体）
  - 46 个可获取的原始模型（31 CDR3β-only + 15 CDR3β+others）
  - 31 个可重训练模型
- **主要结果**：

### Seen-epitope 预测（CDR3β-only 模型，AS 负样本）

| 模型 | AUPRC | 表现 |
| --- | --- | --- |
| ATM-TCR | 0.70 | 最优 |
| TEIM | 0.68 | 次优 |
| TEPCAM | 0.67 | 第三 |
| PiTE-epiSplit / TITAN / TCRfinder | ~0.50 | 接近随机 |

### 关键发现

1. **负样本来源影响巨大** — AS、PS、HS 三种策略下模型排名可能显著变化
2. **数据量重要性** — 每个 epitope 的训练 TCR 数量越多，预测性能越好
3. **多特征优于单特征** — CDR3β + others 模型总体优于 CDR3β-only 模型
4. **泛化能力普遍不足** — 所有模型在 unseen epitope 上表现都较差
5. **独立测试集至关重要** — 不使用独立测试集会高估模型性能

## 研究结论

- **结论 1**：负样本的构建策略是 TCR–epitope 预测模型评估中最关键的混杂因素，AS 策略（抗原特异性负样本）最为可靠
- **结论 2**：目前所有模型在 unseen epitope 预测上泛化能力不足，是该领域的主要瓶颈
- **结论 3**：多特征融合（引入 CDR3α、MHC 等特征）能提升模型性能
- **结论 4**：未来模型开发应关注：(a) 更大的多样化训练数据 (b) 更稳健的负样本策略 (c) 对 unseen epitope 的泛化能力

## 文献综述可复用点

- **可写入背景的内容**：TCR–epitope 预测是免疫组学计算研究的核心问题；当前在该领域的模型众多但缺乏系统性评估
- **可写入研究缺口的内容**：
  - 现有模型对 unseen epitope 泛化能力差
  - 负样本策略缺乏统一标准
  - 缺乏大规模、高质量的配对 TCR–epitope 训练数据
- **可用于方法比较的内容**：本文提供了 46 个模型在统一框架下的性能排名和数据，可作为选择基线模型的参考
- **可用于实验或数据对比的内容**：本文使用的 21 个数据源可作为数据选择参考
- **需要谨慎引用或待复核的内容**：编码问题导致部分字符显示异常（如 `TCR–epitope` 显示为 `TCR�Cepitope`），需回看原始 PDF 确认

## 我的判断

- **最有价值的点**：
  - 负样本策略对模型评估的深刻影响分析
  - 规模最大的系统性基准（50 模型 × 21 数据集）
  - Seen/unseen 双场景评估设计
- **可借鉴的方法或写法**：多层基准评估框架的设计方法，对评估其他生物信息学工具也有参考价值
- **对我研究的启发**：
  - SCigblast 项目中涉及 TCR 数据分析，该文的负样本策略和独立测试集理念可直接借鉴
  - 需要关注 TCR–epitope 预测工具的选择，优先选 ATM-TCR 类表现稳健的模型
- **不足与风险**：
  - 部分元数据不完整（缺少摘要、出版年份等）
  - PDF 全文缓存文本存在字符编码问题
  - 仅评估了公开模型，未涵盖商业/闭源工具
- **后续可追问的问题**：
  - 这些评估模型在免疫组库（如 TRD/TRG 链）上的表现如何？本文主要针对 αβ TCR
  - 21 个数据集的详细列表和获取方式
  - 本文提出的 refined cross-matching AS 策略的具体实现细节
