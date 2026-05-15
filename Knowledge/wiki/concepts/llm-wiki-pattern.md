---
title: LLM Wiki Pattern
tags: [concept, methodology, knowledge-management]
created: 2026-05-06
updated: 2026-05-06
sources: ["raw/llm-wiki-karpathy-2026-04-04.md"]
---

# LLM Wiki 模式

> **Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。**
> — Andrej Karpathy

## 定义

LLM Wiki 是一种**增量构建和维护持久化个人知识库**的方法论。由 Andrej Karpathy 在 2026 年 4 月提出并迅速引爆社区（X/Twitter 1800 万+ 曝光）。

## 核心理念

**LLM 是编译器，不是解释器。**

传统 RAG 像**解释器** — 每次查询时重新解析所有源文档，没有积累。LLM Wiki 像**编译器** — 将原始材料一次性"编译"成结构化的 Wiki，之后查询直接在编译产物上运行。

## 三层架构

```
raw/          ← 原始材料（只读不可变）
wiki/         ← 编译产物（LLM 全权维护）
CLAUDE.md     ← 编译器配置（Schema）
```

## 三种操作

| 操作 | 描述 | 产出 |
|------|------|------|
| **Ingest** | 读新源，更新 Wiki | 10-15 页面被触及 |
| **Query** | 搜索 Wiki，综合答案 | 好答案归档为页面 |
| **Lint** | 健康检查 | 发现矛盾/漏洞/孤立页 |

## 为什么有效

维护知识库最繁琐的是**记账** — 交叉引用、摘要更新、矛盾标注。LLM 不会厌烦，不会忘记，一次可以触及 15 个页面。维护成本趋近于零，知识库自然持续生长。

## 对比

| 维度 | RAG | LLM Wiki |
|------|-----|-----------|
| 知识位置 | 源文档中 | Wiki 中已编译 |
| 每次查询 | 重新检索+综合 | 直接阅读 Wiki |
| 是否累积 | 否 | 是，持续变丰富 |
| 写作负担 | 无 | LLM 维护，零人工成本 |

## 相关概念

- [[rag-vs-llm-wiki]] — 详细对比分析
- [[wiki-schema]] — Schema 文件设计
- [[knowledge-ingest-workflow]] — 导入工作流
- [[wiki/entities/andrej-karpathy|Andrej Karpathy]] — 提出者
- [[wiki/entities/obsidian|Obsidian]] — 推荐的前端工具

## 参考资料

- [[wiki/sources/llm-wiki-karpathy]] — 来源摘要
- [[CLAUDE.md]] — 本知识库的 Schema 配置
