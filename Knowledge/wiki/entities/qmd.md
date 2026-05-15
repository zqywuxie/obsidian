---
title: qmd
tags: [entity, tool, search]
created: 2026-05-06
updated: 2026-05-06
sources: ["raw/llm-wiki-karpathy-2026-04-04.md"]
---

# qmd

## 简介

qmd 是一个本地 Markdown 文件搜索引擎，支持 **BM25/向量混合搜索 + LLM 重排序**，所有计算在本地设备上完成。

作者：[Tobi](https://github.com/tobi)
GitHub: [tobi/qmd](https://github.com/tobi/qmd)

## 在 LLM Wiki 中的用途

当 Wiki 规模增长到索引文件不足以高效导航时，qmd 作为**替代搜索方案**出现：

- **CLI 模式** — LLM 可以直接通过 shell 调用搜索
- **MCP 服务** — LLM 可以作为原生工具使用（更推荐）

## 优势

- 本地运行，数据不出设备
- 专为 Markdown 优化
- 支持混合检索（关键词 + 语义）
- LLM 重排序提升精度

## 对比 index.md

| 方式 | 适合规模 | 精度 | 速度 |
|------|----------|------|------|
| **index.md** | ~100 来源 / 数百页面 | 中等 | 快 |
| **qmd** | 大规模 | 高 | 快 |

Karpathy 建议：小规模用 index.md 即可，长了再上 qmd。也可以自己写一个简单的搜索脚本应急。

## 相关页面

- [[wiki/concepts/llm-wiki-pattern|LLM Wiki 模式]] — 提出背景
- [[wiki/index]] — Wiki 索引
