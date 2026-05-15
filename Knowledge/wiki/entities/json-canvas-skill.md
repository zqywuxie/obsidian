---
title: json-canvas Skill
tags: [entity, skill, obsidian, canvas, visualization]
created: 2026-05-06
updated: 2026-05-06
---

# json-canvas Skill

> 让 LLM 能创建和编辑 JSON Canvas（`.canvas` 文件）的技能。已安装到 `.claude/skills/json-canvas/`。

## 功能

遵循 [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/) 标准：

- **Nodes** — 4 种类型：`text`（支持 Markdown）、`file`（链接 vault 内文件及 heading/block）、`link`（外部 URL）、`group`（视觉容器）
- **Edges** — 连接线：可设置方向（top/right/bottom/left）、端点样式（none/arrow）、颜色、标签
- **Colors** — 6 种预设色 + 自定义 hex
- **布局** — 支持负坐标，无限画布

## 在本 Wiki 中的应用

可以用 `.canvas` 文件创建：

- 概念关系脑图（将 [[wiki/concepts/tcr-repertoire]] 与 [[wiki/concepts/thk-cells]] 等可视化关联）
- 文献阅读地图
- 知识库结构导航看板
- 研究项目流程图

## 参考来源

- [JSON Canvas Spec](https://jsoncanvas.org/spec/1.0/)
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
