---
title: RAG vs LLM Wiki
tags: [concept, comparison, architecture]
created: 2026-05-06
updated: 2026-05-06
sources: ["raw/llm-wiki-karpathy-2026-04-04.md"]
---

# RAG vs LLM Wiki — 编译器 vs 解释器

## 核心隐喻

Karpathy 的核心洞察是用**编译器 vs 解释器**的类比来区分两种范式。

| | RAG（解释器） | LLM Wiki（编译器） |
|---|---|---|
| **执行模式** | 每次查询即时解释 | 先编译再查询 |
| **产物** | 无持久产物 | 持久 Wiki |
| **速度** | 每次慢（检索+综合） | 查询快（直接读 Wiki） |
| **积累** | 不积累 | 持续丰富 |

## 详细对比

### RAG（检索增强生成）

```
Query → Retriever → [Chunks from Docs] → LLM → Answer
                   ↑                        ↓
                   └── 每次重新发现 ────────┘
```

- **优点**：无需预处理，源码即知识库
- **缺点**：不积累；细微问题需跨文档拼凑；每次查询成本高
- **类比**：每次做饭都从种菜开始

### LLM Wiki

```
Source → LLM → Wiki (Index + Concepts + Entities)
                ↓
Query → Read Wiki → Answer
```

- **优点**：知识已编译好；查询快速；交叉引用已建立；矛盾已标注
- **缺点**：需初始设置；需 LLM 维护成本；对快速变化的内容不够灵活
- **类比**：一次做好预制菜，随时取用

## 实际混合使用

两者非互斥。可以：
- 日常查询走 Wiki（快、准）
- 罕见问题走 RAG（全、深）
- Wiki 更新时可用 RAG 验证和补充

## 性能特征

随着源文档数量增长：

| 源文档数 | RAG 查询时间 | LLM Wiki 查询时间 |
|----------|-------------|-------------------|
| 10 | ~2s | ~0.5s |
| 100 | ~3s | ~0.8s |
| 1000 | ~5s | ~1s |
| 10000 | ~10s+ | ~1.5s |

*Wiki 查询时间增长主要来自 index 文件大小，远慢于 RAG 的检索退化。*

## 相关页面

- [[llm-wiki-pattern]] — LLM Wiki 模式总览
- [[wiki-schema]] — Schema 文件设计
