---
title: obsidian-cli Skill
tags: [entity, skill, obsidian, cli, automation]
created: 2026-05-06
updated: 2026-05-06
---

# obsidian-cli Skill

> 让 LLM 能通过 CLI 命令操控 Obsidian 实例的技能。已安装到 `.claude/skills/obsidian-cli/`。需要 Obsidian 正在运行。

## 功能

### 笔记操作
| 命令 | 用途 |
|------|------|
| `obsidian read` | 读取笔记内容 |
| `obsidian create` | 创建新笔记（支持 template） |
| `obsidian append` | 追加内容 |
| `obsidian search` | 全文搜索 |
| `obsidian daily:read/append` | 操作每日笔记 |
| `obsidian property:set/get` | 属性管理 |
| `obsidian tasks` | 任务查询 |
| `obsidian tags` | 标签统计 |
| `obsidian backlinks` | 反向链接查询 |

### 插件/主题开发
| 命令 | 用途 |
|------|------|
| `obsidian plugin:reload` | 重载插件 |
| `obsidian dev:errors` | 检查错误 |
| `obsidian dev:screenshot` | 截图 |
| `obsidian dev:dom` | DOM 检查 |
| `obsidian dev:console` | 控制台日志 |
| `obsidian eval` | 执行 JS |
| `obsidian dev:mobile` | 模拟移动端 |

## 在本 Wiki 中的应用

- 搜索 vault 中所有相关文件
- 创建新笔记时直接写入 Obsidian
- 批量管理 frontmatter 属性
- 查询标签和反向链接

## 参考来源

- [Obsidian CLI 官方文档](https://help.obsidian.md/cli)
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)
