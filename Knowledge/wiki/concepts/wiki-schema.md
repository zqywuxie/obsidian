---
title: Wiki Schema
tags: [concept, schema, configuration]
created: 2026-05-06
updated: 2026-05-06
sources: ["raw/llm-wiki-karpathy-2026-04-04.md"]
---

# Wiki Schema

> Schema 是知识库的「大脑」— 它定义结构、约定和工作流，让 LLM 成为自律的维基维护者。

## 什么是 Schema

Schema 是一个配置文件（如 `CLAUDE.md` 或 `AGENTS.md`），放在知识库根目录。LLM 在启动时读取它，从而了解：

1. 知识库的结构是什么
2. 有什么约定要遵守
3. 遇到不同情况该怎么做

没有 Schema 的 LLM 是通用聊天机器人；有 Schema 的 LLM 是**维基管理员**。

## 必须包含的内容

一个好的 Schema 应定义：

| 要素 | 说明 | 示例 |
|------|------|------|
| **身份/角色** | LLM 在这个知识库中扮演什么角色 | "你是维基管理员" |
| **架构描述** | 目录结构及各层的用途 | "raw/ 不可变，wiki/ LLM 维护" |
| **文件规范** | Frontmatter、命名、链接格式 | "所有页面需 YAML frontmatter" |
| **操作流程** | Ingest / Query / Lint 的具体步骤 | "Ingest: 读→讨论→更新→记日志" |
| **质量准则** | 什么算"好"的 wiki 页面 | "页面间交叉引用充分" |

## Schema 的演化

Schema 不是一次写好的。它应随知识库共同演化：

- 新增页面类型时 → 更新目录结构描述
- 发现新工作流更高效 → 更新操作流程
- 用户有新的偏好 → 更新约定

## 与 CLAUDE.md 的关系

在 Claude Code 生态中，Schema 就是 `CLAUDE.md`。在其他工具中可能是 `AGENTS.md`、`INSTRUCTIONS.md` 或工具自带的 system prompt。

## 举例

见本知识库根目录的 [[CLAUDE.md]] 即为本知识库的 Schema 实现。

## 相关页面

- [[llm-wiki-pattern]] — LLM Wiki 总览
- [[knowledge-ingest-workflow]] — 具体工作流
- [[CLAUDE.md]] — 本知识库的 Schema 配置
