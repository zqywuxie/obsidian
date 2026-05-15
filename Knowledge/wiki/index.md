---
title: Knowledge Base Index
tags: [index, moc, navigation]
created: 2026-05-06
updated: 2026-05-07
---

# 📚 知识库索引

> 所有页面的内容导航。查询时从此出发，按类别深入。

---

## 📂 Sources（来源摘要）

| 页面 | 简介 | 源文档 |
|------|------|--------|
| [[wiki/sources/llm-wiki-karpathy\|LLM Wiki — Karpathy]] | Karpathy 的 LLM Wiki 模式概述与核心理念 | `raw/llm-wiki-karpathy-2026-04-04.md` |
| [[wiki/sources/xie-et-al-2026-thk-cells\|Xie et al. 2026 — ThK Cells]] | GZMK⁺EOMES⁺ CD4⁺ T 新亚群的发现 | `raw/xie-et-al-2026-thk-cells-nature-immunology.pdf` |
| [[wiki/sources/batch-tcr-repertoire-analysis\|TCR Repertoire 分析合集]] | TCR 库分析、ML 方法、生成模型等 12 篇 | `raw/pdfs/` (12 个 PDF) |
| [[wiki/sources/batch-tcr-epitope-prediction\|TCR-表位预测合集]] | TCR 结合预测、表示学习、数据库等 10 篇 | `raw/pdfs/` (10 个 PDF) |
| [[wiki/sources/batch-sc-multiomics-tcell-bio\|单细胞多组学合集]] | scTCR-seq、T 细胞生物等 12 篇 | `raw/pdfs/` (12 个 PDF) |
| [[wiki/sources/batch-bioinfo-methods\|生信方法合集]] | 组学整合、基础模型、临床应用等 10 篇 | `raw/pdfs/` (10 个 PDF) |
| [[wiki/sources/hla-typing-guide\|HLA 分型技术指南]] | HLA 分型 16 问：短读长到长读长，算法到落地 | `raw/hla-typing-guide-2025.md` |
| [[wiki/sources/s41592-025-02913-x\|ImmunoMatch — Guo et al. 2026]] | 抗体重轻链配对预测模型 | `raw/s41592-025-02913-x.pdf` |

## 🧠 Concepts（概念）

| 页面 | 简介 |
|------|------|
| [[wiki/concepts/llm-wiki-pattern\|LLM Wiki 模式]] | 增量构建和维护持久化个人知识库的核心方法论 |
| [[wiki/concepts/rag-vs-llm-wiki\|RAG vs LLM Wiki]] | 解释器模式 vs 编译器模式的对比 |
| [[wiki/concepts/wiki-schema\|Wiki Schema]] | Schema 配置文件的角色和设计 |
| [[wiki/concepts/knowledge-ingest-workflow\|Knowledge Ingest Workflow]] | 导入工作流的详细拆解 |
| [[wiki/concepts/thk-cells\|ThK 细胞]] | 新发现的 CD4⁺ GZMK⁺ T 细胞亚群，EOMES 驱动 |
| [[wiki/concepts/eomes-transcription-factor\|EOMES 转录因子]] | T-box 家族转录因子，ThK 细胞的 master regulator |
| [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] | TCR 库的生成、多样性、影响因素与定量分析 |
| [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] | 从 TCR 序列预测抗原特异性的计算方法 |
| [[wiki/concepts/single-cell-tcr-seq\|Single-cell TCR-seq]] | 单细胞 TCR 测序 + 多模态整合分析 |
| [[wiki/concepts/obsidian-agent-skills\|Obsidian Agent Skills]] | LLM 与 Obsidian 交互的标准化技能层 |
| [[wiki/concepts/hla-typing\|HLA 分型技术]] | HLA 分型策略、工具对比、质控与 IVD 验证 |
| [[wiki/concepts/antibody-hl-pairing\|抗体 H-L 链配对]] | 抗体重轻链配对规则、计算方法与 ImmunoMatch |

## 👤 Entities（实体）

| 页面 | 简介 |
|------|------|
| [[wiki/entities/andrej-karpathy\|Andrej Karpathy]] | LLM Wiki 模式的提出者，OpenAI/Tesla 前 AI 科学家 |
| [[wiki/entities/obsidian\|Obsidian]] | Markdown 知识管理工具，本知识库的 IDE |
| [[wiki/entities/qmd\|qmd]] | 本地 Markdown 搜索引擎，混合 BM25/向量搜索 |
| [[wiki/entities/chen-dong\|Chen Dong（董晨）]] | 免疫学家，Th17/Tfh/ThK 发现者，西湖大学教授 |
| [[wiki/entities/tian-xie\|Tian Xie（谢天）]] | 清华大学博士生，ThK 研究第一作者 |
| [[wiki/entities/tcrdb\|TCRdb]] | 综合性 TCR 序列数据库 (Chen et al. 2021) |
| [[wiki/entities/sonnia\|soNNia]] | 深度生成选择模型 (Isacchini et al. 2021) |
| [[wiki/entities/deeptcr\|DeepTCR]] | VAE 深度 TCR 库学习框架 (Sidhom et al. 2021) |
| [[wiki/entities/mixcr\|MiXCR]] | 免疫组库测序分析软件 |
| [[wiki/entities/immunomatch\|ImmunoMatch]] | 基于 AntiBERTa2 的 H-L 链配对预测框架 |
| [[wiki/entities/obsidian-markdown-skill\|obsidian-markdown]] | Obsidian 风味 Markdown 编写技能 |
| [[wiki/entities/obsidian-bases-skill\|obsidian-bases]] | Obsidian Bases 数据库视图技能 |
| [[wiki/entities/json-canvas-skill\|json-canvas]] | JSON Canvas 可视化画布技能 |
| [[wiki/entities/obsidian-cli-skill\|obsidian-cli]] | Obsidian CLI 命令行交互技能 |
| [[wiki/entities/defuddle-skill\|defuddle]] | 网页提取干净 Markdown 技能 |

## 🔬 Syntheses（综合分析）

> 当前为空。好的查询答案将会归档在此。

## ⚡ Prompts（操作模板）

| 页面 | 用途 |
|------|------|
| [[prompts/ingest-source\|Ingest — 导入新源]] | 将新文档整合到 Wiki 的完整流程 |
| [[prompts/query-wiki\|Query — 查询知识库]] | 基于 Wiki 综合回答问题的流程 |
| [[prompts/lint-wiki\|Lint — 健康检查]] | 定期检查矛盾、过时内容、孤立页面 |
| [[prompts/explore-topic\|Explore — 深度探索]] | 结合网络搜索研究新主题 |
| [[prompts/synthesize\|Synthesize — 综合分析]] | 多页面横向比较与综合 |
| [[prompts/update-wiki\|Update — 维护更新]] | 批量修复链接、统一格式、重组结构 |

---

## 统计

| 指标 | 数值 |
|------|------|
| 页面总数 | 43 |
| 原始资料 | 4 个文件 + ~44 个 PDF |
| 操作模板 | 6 |
| 概念页 | 11 |
| 实体页 | 15 |
| 来源摘要 | 7 |
| Agent Skills | 5（已安装到 .claude/skills/） |
