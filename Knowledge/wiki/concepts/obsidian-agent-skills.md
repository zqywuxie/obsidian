---
title: Obsidian Agent Skills
tags: [concept, obsidian, skills, agent, automation]
created: 2026-05-06
updated: 2026-05-06
---

# Obsidian Agent Skills

> LLM Agent 与 Obsidian 交互的能力层，遵循 [Agent Skills 规范](https://agentskills.io/specification)。由 Obsidian CEO Steph Ango（Kepano）开发维护。

---

## 什么是 Agent Skills

Agent Skills 是一种标准化的技能定义格式，让 LLM agent（Claude Code、Codex CLI、OpenCode 等）能够执行特定领域的任务。每个 skill 是一个包含 `SKILL.md` 的目录，描述 agent 应该知道的能力和约束。

本 vault 已安装 `kepano/obsidian-skills` 共 5 个技能。

---

## 安装列表

| 技能 | 用途 | 位置 |
|------|------|------|
| `obsidian-markdown` | 编写 Obsidian 风味 Markdown | `.claude/skills/obsidian-markdown/` |
| `obsidian-bases` | 创建和编辑 .base 数据库视图 | `.claude/skills/obsidian-bases/` |
| `json-canvas` | 创建和编辑 .canvas 画布文件 | `.claude/skills/json-canvas/` |
| `obsidian-cli` | CLI 操控 Obsidian 实例 | `.claude/skills/obsidian-cli/` |
| `defuddle` | 网页提取为 Markdown | `.claude/skills/defuddle/` |

---

## 与本知识库的协同

| Skill | 在本 Wiki 中的应用 |
|-------|-------------------|
| `obsidian-markdown` | 正确编写 `[[链接]]`、`> [!callout]`、YAML frontmatter — 已在所有页面中使用 |
| `obsidian-bases` | 创建 `.base` 文件实现文献数据库视图、动态筛选和统计 |
| `json-canvas` | 绘制概念关系 Canvas 图，可视化知识库结构 |
| `obsidian-cli` | 直接通过 CLI 搜索 vault、创建笔记、管理属性 |
| `defuddle` | 抓取网页文章并转为 Markdown 存入 `raw/`，作为 ingest 的前置步骤 |

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 实体 | [[wiki/entities/obsidian-markdown-skill\|obsidian-markdown]] |
| 实体 | [[wiki/entities/obsidian-bases-skill\|obsidian-bases]] |
| 实体 | [[wiki/entities/json-canvas-skill\|json-canvas]] |
| 实体 | [[wiki/entities/obsidian-cli-skill\|obsidian-cli]] |
| 实体 | [[wiki/entities/defuddle-skill\|defuddle]] |
| 实体 | [[wiki/entities/obsidian\|Obsidian]] |
| Schema | [[CLAUDE.md]] |
