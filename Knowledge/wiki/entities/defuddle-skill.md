---
title: defuddle Skill
tags: [entity, skill, web, markdown, scraping]
created: 2026-05-06
updated: 2026-05-06
---

# defuddle Skill

> 让 LLM 能使用 Defuddle CLI 从网页提取干净 Markdown 内容的技能。已安装到 `.claude/skills/defuddle/`。

## 功能

`defuddle parse <url> --md` → 直接输出干净 Markdown（去广告 / 导航 / 杂项）

| 用法 | 说明 |
|------|------|
| `defuddle parse <url> --md` | 提取内容为 Markdown |
| `defuddle parse <url> --md -o file.md` | 保存到文件 |
| `defuddle parse <url> -p title` | 提取标题 |
| `defuddle parse <url> -p description` | 提取描述 |
| `defuddle parse <url> -p domain` | 提取域名 |

## 与 WebFetch 的对比

| 维度 | WebFetch | Defuddle |
|------|----------|----------|
| 去杂 | 一般 | 好（去广告/导航） |
| Token 消耗 | 较高 | 更低 |
| 安装要求 | 无需安装 | 需要 `npm install -g defuddle` |
| URL 规则 | HTTP 自动升级 HTTPS | 标准 URL |

## 在本 Wiki 中的应用

- ingest 网络文章到 `raw/` 的前置步骤
- 保存网页内容为 Markdown，供后续导入分析
- 比 WebFetch 更省 token 的替代方案

## 安装

```bash
npm install -g defuddle
```

## 参考来源

- [Defuddle CLI GitHub](https://github.com/kepano/defuddle-cli)
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
