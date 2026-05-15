---
title: obsidian-bases Skill
tags: [entity, skill, obsidian, database, base]
created: 2026-05-06
updated: 2026-05-06
---

# obsidian-bases Skill

> 让 LLM 能创建和编辑 Obsidian Bases（`.base` 文件）的技能。已安装到 `.claude/skills/obsidian-bases/`。

## 功能

- **Filters** — 多条件筛选（按 tag / 文件夹 / 属性 / 日期）
- **Formulas** — 计算属性（条件判断、日期运算、字符串格式化）
- **Views** — 4 种视图：`table`、`cards`、`list`、`map`
- **Summaries** — 汇总统计（Sum/Average/Min/Max/Median/Stddev 等）
- **GroupBy** — 按属性分组
- **Embed** — 嵌入到 Markdown 笔记中

## 在本 Wiki 中的应用

可创建以下 `.base` 文件提升知识库使用体验：

| Base 用途 | 筛选条件 | 视图类型 |
|-----------|---------|---------|
| 文献总览 | `tag:source` | table |
| 概念图谱 | `tag:concept` | cards |
| 实体清单 | `tag:entity` | table |
| 操作日志统计 | `tag:log` | table |

## 参考来源

- [Obsidian Bases 官方文档](https://help.obsidian.md/bases/syntax)
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
