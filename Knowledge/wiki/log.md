---
title: Operation Log
tags: [log, changelog]
created: 2026-05-06
---

# 📋 操作日志

> Append-only 记录。每条日志以 `## [YYYY-MM-DD] <操作类型>` 开头，便于 grep 检索。

---

## [2026-05-06] init | 知识库初始化

初始化 `Knowledge/` 知识库，严格按 Karpathy LLM Wiki 三层架构搭建。

- 创建目录：`raw/assets/`, `wiki/concepts/`, `wiki/entities/`, `wiki/sources/`, `wiki/syntheses/`
- 创建 Schema 文件：[[CLAUDE.md]]
- 创建导航：[[wiki/index.md]]
- 创建概念页面（4个）：llm-wiki-pattern, rag-vs-llm-wiki, wiki-schema, knowledge-ingest-workflow
- 创建实体页面（3个）：andrej-karpathy, obsidian, qmd
- 创建来源摘要：[[wiki/sources/llm-wiki-karpathy]]

## [2026-05-06] ingest | llm-wiki-karpathy

将 Karpathy 的 LLM Wiki 原文作为首个源文档归档并 ingest。

- 源文档：`raw/llm-wiki-karpathy-2026-04-04.md`
- 创建了来源摘要页
- 提取了 4 个核心概念并创建概念页面
- 提取了 3 个关键实体并创建实体页面
- 更新了 Wiki 索引

## [2026-05-06] ingest | Xie et al. 2026 — ThK Cells

将 Xie 等人在 *Nature Immunology* 发表的 ThK 细胞论文归档并 ingest。

- 源文档：`raw/xie-et-al-2026-thk-cells-nature-immunology.pdf`
- 创建了来源摘要页：[[wiki/sources/xie-et-al-2026-thk-cells]]
- 提取了 2 个核心概念：
  - [[wiki/concepts/thk-cells]] — ThK 细胞的定义、特征、分化调控、功能、保守性
  - [[wiki/concepts/eomes-transcription-factor]] — EOMES 的分子机制、必要性/充分性、表观遗传调控
- 提取了 2 个关键实体：
  - [[wiki/entities/chen-dong]] — 通讯作者董晨
  - [[wiki/entities/tian-xie]] — 第一作者谢天
- 更新了 Wiki 索引
- 总页面数更新：8 → 13；原始资料数：1 → 2

## [2026-05-15] fetch | Cross-tissue immune cell atlas (Science 2022)

- **来源**：流式中文网公众号文章 → 追溯原文 [DOI 10.1126/science.abl5197](https://doi.org/10.1126/science.abl5197)
- **追溯资源**：CellTypist (GitHub + 官网) | TissueImmuneCellAtlas (GitHub) | ArrayExpress E-MTAB-11536 | UCSC Cell Browser
- **新页面**：[[wiki/sources/cross-tissue-immune-cell-atlas-science-2022]]
- **更新 index**：+1 条 Sources 条目
- **更新 prompt**：fetch-url.md 新增原始文献与数据资源追溯步骤

## [2026-05-06] update | 新增 prompts 目录

在 Knowledge 根目录下新增 `prompts/` 层，存放 Wiki 操作模板。

- 创建了 6 个操作模板：
  - [[prompts/ingest-source]] — 导入新源的标准化流程
  - [[prompts/query-wiki]] — 查询知识库的流程
  - [[prompts/lint-wiki]] — 健康检查清单
  - [[prompts/explore-topic]] — 深度探索主题
  - [[prompts/synthesize]] — 综合分析
  - [[prompts/update-wiki]] — 维护更新
- 更新了 [[CLAUDE.md]] 中的目录结构描述
- 更新了 [[wiki/index]] 中的导航索引
- 总页面数：13 → 19

## [2026-05-06] ingest | Zotero 文献库批量导入

从 `C:\Users\Yun\Zotero\storage` 批量导入约 44 篇免疫学/TCR 相关文献。

**操作**：
- 复制 ~44 个唯一 PDF 到 `raw/pdfs/`（去重后，略过已导入的 ThK 论文）
- 创建 4 个按主题聚类的批量来源摘要：
  - [[wiki/sources/batch-tcr-repertoire-analysis]] — TCR 库分析 & ML（12 篇）
  - [[wiki/sources/batch-tcr-epitope-prediction]] — TCR-表位结合预测（10 篇）
  - [[wiki/sources/batch-sc-multiomics-tcell-bio]] — 单细胞多组学 & T 细胞生物（12 篇）
  - [[wiki/sources/batch-bioinfo-methods]] — 生信方法 & 其他（10 篇）

**知识提取**：
- 新增 3 个概念页：
  - [[wiki/concepts/tcr-repertoire]] — TCR 库的生成、多样性、影响因素
  - [[wiki/concepts/tcr-epitope-prediction]] — 计算方法与最新进展
  - [[wiki/concepts/single-cell-tcr-seq]] — 单细胞多模态整合分析
- 新增 4 个实体页：
  - [[wiki/entities/tcrdb]] — TCR 序列数据库
  - [[wiki/entities/sonnia]] — 深度生成选择模型
  - [[wiki/entities/deeptcr]] — VAE 深度 TCR 学习框架
  - [[wiki/entities/mixcr]] — 免疫组库分析软件

**更新**：
- [[wiki/index]] 全面更新（19 → 32 页）
- 原始资料数：2 个文件 + ~44 个 PDF

## [2026-05-06] install | obsidian-skills

从 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) 安装 5 个 Agent Skills 到 vault。

**安装**：
- 复制 skills 目录到 `.claude/skills/`
- 5 个技能已在当前 session 中生效

**Wiki 记录**：
- 新增概念页 [[wiki/concepts/obsidian-agent-skills]] — Obsidian Agent Skills 总览
- 新增 5 个实体页：
  - [[wiki/entities/obsidian-markdown-skill]] — Obsidian 风味 Markdown
  - [[wiki/entities/obsidian-bases-skill]] — Bases 数据库视图
  - [[wiki/entities/json-canvas-skill]] — JSON Canvas 画布
  - [[wiki/entities/obsidian-cli-skill]] — CLI 操控
  - [[wiki/entities/defuddle-skill]] — 网页提取
- 更新 [[wiki/entities/obsidian]] 添加技能引用
- 更新 [[CLAUDE.md]] 添加技能描述
- 更新 [[wiki/index]]（32 → 38 页）

## [2026-05-06] ingest | ImmunoMatch — Guo et al. 2026, Nature Methods

用 pdftotext 提取并 ingest Nature Methods 论文。

- 源文档：`raw/s41592-025-02913-x.pdf`
- 来源摘要：[[wiki/sources/s41592-025-02913-x]]
- 概念页：[[wiki/concepts/antibody-hl-pairing]] — 抗体 H-L 链配对预测的生物学基础与计算方法
- 实体页：[[wiki/entities/immunomatch]] — ImmunoMatch 工具详情
- 更新 [[wiki/index]]（40 → 43 页）
- 原始资料数：4 个文件 + ~44 个 PDF
- 总页面数更新：40 → 43

## [2026-05-06] ingest | HLA 分型技术指南

用 defuddle 提取微信公众号文章并 ingest。

- 源文档：`raw/hla-typing-guide-2025.md`（defuddle 保存的 Markdown）
- 来源摘要：[[wiki/sources/hla-typing-guide]]
- 概念页：[[wiki/concepts/hla-typing]] — HLA 分型策略、工具、质控、IVD 验证
- 更新 [[wiki/index]]（38 → 40 页）
- 原始资料数：3 个文件 + ~44 个 PDF

## [2026-05-07] update | Xie et al. 2026 — 补充实验方法详解

用 pdftotext 完整提取论文全文文本，详细阅读并整理了全部实验操作细节，更新到知识库。

**更新内容**：
- [[wiki/sources/xie-et-al-2026-thk-cells]] — 新增完整「实验方法详解」大章节，涵盖：
  - 所有 17 个小鼠品系及来源
  - T 细胞诱导性结肠炎模型操作流程
  - 结肠淋巴细胞分离详细步骤（含试剂浓度、时间、温度）
  - 体外 T 细胞分化方案（5 种条件，含所有细胞因子组合）
  - 逆转录病毒 Eomes 过表达实验流程
  - OVA 免疫模型
  - 体外细胞毒性实验
  - 完整流式抗体方案（21 种抗体，含克隆号、荧光、供应商）
  - 组织学分析方法
  - RT-qPCR 引物序列（4 对）
  - bulk RNA-seq / scRNA-seq / ATAC-seq / CUT&Tag 全部生信参数
  - 基因-峰整合分析逻辑
  - 统计方法细节及实验设计逻辑链流程图
- [[wiki/concepts/thk-cells]] — 新增「实验方法速览」交叉引用表格
- [[wiki/concepts/eomes-transcription-factor]] — 新增「实验方法速览」验证维度表格
- [[wiki/entities/chen-dong]], [[wiki/entities/tian-xie]] — 更新日期
- [[wiki/index]] — 更新日期
- 总页面数不变（43 页）
