---
title: Obsidian
tags: [entity, tool, knowledge-management]
created: 2026-05-06
updated: 2026-05-06
sources: ["raw/llm-wiki-karpathy-2026-04-04.md"]
---

# Obsidian

## 简介

Obsidian 是一个基于本地 Markdown 文件的个人知识管理工具。支持双向链接、图谱视图（Graph View）、插件系统，是构建「第二大脑」的常用工具。

## 在 LLM Wiki 中的角色

在 Karpathy 的 LLM Wiki 模式中，Obsidian 的角色是 **IDE**（集成开发环境）：

> **Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。**

LLM agent 在后台操作文件，用户同时在 Obsidian 前端浏览结果：

- 点击内部链接导航
- 使用图谱视图查看页面关联
- 实时查看 LLM 的更新

## 推荐配置

根据 Karpathy 的建议：

| 设置 | 推荐值 | 用途 |
|------|--------|------|
| Attachment folder | `raw/assets/` | LLM 可读取的图片附件位置 |
| 热键 | Ctrl+Shift+D | 下载当前文件的图片附件 |

## 推荐插件

| 插件 | 用途 |
|------|------|
| **Web Clipper** | 浏览器扩展，将网页转为 Markdown 存入 raw/ |
| **Marp** | Markdown 幻灯片，适合生成演示文稿 |
| **Dataview** | 查询页面 frontmatter 生成动态表格 |
| **Excalidraw** | 绘图（可补充 Wiki 中的图示） |

## Agent Skills

本 vault 已安装 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) 共 5 个技能，让 LLM agent 能直接操作 Obsidian：

| 技能 | 功能 |
|------|------|
| [[wiki/entities/obsidian-markdown-skill\|obsidian-markdown]] | 编写 Obsidian 风味 Markdown |
| [[wiki/entities/obsidian-bases-skill\|obsidian-bases]] | 创建 .base 数据库视图 |
| [[wiki/entities/json-canvas-skill\|json-canvas]] | 创建 .canvas 可视化画布 |
| [[wiki/entities/obsidian-cli-skill\|obsidian-cli]] | CLI 操控 Obsidian 实例 |
| [[wiki/entities/defuddle-skill\|defuddle]] | 网页提取为 Markdown |

## 相关页面

- [[wiki/concepts/obsidian-agent-skills|Obsidian Agent Skills]]
- [[wiki/concepts/llm-wiki-pattern|LLM Wiki 模式]]
- [[CLAUDE.md]] — Schema 配置
