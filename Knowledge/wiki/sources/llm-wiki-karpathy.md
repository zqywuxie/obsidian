---
title: LLM Wiki — Karpathy 原文摘要
tags: [source, summary, karpathy]
created: 2026-05-06
updated: 2026-05-06
source-file: "raw/llm-wiki-karpathy-2026-04-04.md"
---

# LLM Wiki — 来源摘要

> **原文**: Andrej Karpathy 于 2026-04-04 发布的 LLM Wiki 模式指南
> **原文位置**: `raw/llm-wiki-karpathy-2026-04-04.md`
> **影响**: X/Twitter 1800 万+ 曝光，引爆社区

## 核心论点

大多数人的 LLM + 文档体验 = **RAG**（每次查询时检索相关片段 → LLM 生成答案）。这有效，但 LLM 每次都在**重新发现知识**，没有积累。

LLM Wiki 的不同之处：LLM **增量构建和维护一个持久的 Wiki** — 结构化的、互相关联的 Markdown 文件集合。

## 关键引用

> "Wiki 是一个持久的、不断累积的产物。交叉引用已经存在，矛盾已经被标记，综合已经反映了一切。"

> "Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。"

> "人的工作是策展来源、指导分析、提出好问题、思考意义。LLM 的工作是其余一切。"

## 主要概念提取

| 概念 | 简述 | Wiki 页面 |
|------|------|-----------|
| LLM Wiki 模式 | 增量构建持久化知识库 | [[wiki/concepts/llm-wiki-pattern]] |
| 编译器 vs 解释器 | RAG = 解释器，LLM Wiki = 编译器 | [[wiki/concepts/rag-vs-llm-wiki]] |
| Schema | 配置文件让 LLM 成为维基管理员 | [[wiki/concepts/wiki-schema]] |
| Ingest 流程 | 导入 → 讨论 → 更新 → 归档 | [[wiki/concepts/knowledge-ingest-workflow]] |

## 关键实体提取

| 实体 | 简述 | Wiki 页面 |
|------|------|-----------|
| Andrej Karpathy | 提出者 | [[wiki/entities/andrej-karpathy]] |
| Obsidian | 前端工具 (IDE) | [[wiki/entities/obsidian]] |
| qmd | 搜索工具 | [[wiki/entities/qmd]] |

## 相关概念链接

- **Memex** (Vannevar Bush, 1945) — 精神先驱，文中提及
- **NotebookLM/ChatGPT 文件上传** — 作为对比对象
- **Marp** — 生成幻灯片
- **Dataview** — 查询 frontmatter
