# CLAUDE.md — LLM Wiki Schema

> 本文是知识库的 **Schema 层**（即「大脑」）。任何接入此知识库的 LLM agent 都应先读此文件。
> 它定义知识库的结构、约定和工作流，让 LLM 从一个通用聊天机器人变为**自律的维基维护者**。

---

## 1⃣ 核心哲学

**Obsidian 是 IDE，LLM 是程序员，Wiki 是代码库。**

人的工作：策展来源、指导分析、提出好问题、思考意义。
LLM 的工作：其余一切 — 总结、交叉引用、归档、记账。

关键洞察：**LLM 是编译器，不是解释器**。知识被一次性"编译"到 Wiki 中并持续更新，而不是每次查询时重新推导。

---

## 2⃣ 三层架构

```
Knowledge/
├── CLAUDE.md          ← Schema（你在这里）
├── prompts/           ← 操作模板层
│   ├── ingest-source.md
│   ├── query-wiki.md
│   ├── lint-wiki.md
│   ├── explore-topic.md
│   ├── fetch-url.md      ← 新增：抓取网页并解读
│   ├── synthesize.md
│   ├── update-wiki.md
│   └── git-sync.md       ← Git vault 推送同步
├── raw/               ← 原始资料层（不可变，只读）
│   ├── assets/        ← 图片附件
│   └── *.md           ← 源文档（文章、论文、笔记）
└── wiki/              ← Wiki 层（LLM 全权维护）
    ├── index.md       ← 内容目录
    ├── log.md         ← 操作日志
    ├── concepts/      ← 概念页面
    ├── entities/      ← 实体页面
    ├── sources/       ← 来源摘要
    └── syntheses/     ← 综合分析
```

---

## 3⃣ 文件规范

### YAML Frontmatter
所有 wiki 页面必须包含：
```yaml
---
title: 页面标题
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["source-link-or-path"]
---
```

### 链接格式
- 内部链接：`[[页面名]]`
- 引用来源：`[来源名](raw/source-file.md)`

### 命名规范
- 英文文件名，短横线分隔
- 概念页面用单数形式
- 日期格式：YYYY-MM-DD

---

## 4⃣ 三种核心操作

### 🔄 Ingest（导入）
1. 将源文档放入 `raw/`
2. 读取源文档（含嵌入图片）
3. 与用户讨论关键要点
4. 创建/更新 wiki 页面：
   - `wiki/sources/` → 来源摘要
   - `wiki/concepts/` → 相关概念
   - `wiki/entities/` → 相关实体
5. 更新 `wiki/index.md`
6. 在 `wiki/log.md` 追加记录

**一个源可能触及 10–15 个页面。**

### ❓ Query（查询）
1. 优先搜索 Wiki（查找相关页面 → 深入阅读 → 综合答案）
2. 答案引用来源
3. **有价值的答案归档为 wiki 新页面**（如分析、对比、总结）

### 🧹 Lint（健康检查）
定期检查：
- 页面间的矛盾
- 过时的声明
- 孤立页面（无入链）
- 缺少的重要概念页面
- 缺失的交叉引用
- 可通过 [[WebSearch]] 填补的数据空白

---

## 5⃣ 安装的 Agent Skills

本 vault 已安装 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)（5 个），位于 `.claude/skills/`：

| Skill | 用途 | 自动触发场景 |
|-------|------|-------------|
| `obsidian-markdown` | 编写 Wikilink、Callout、Embed 等 | 用户提到"链接/嵌入/高亮块/frontmatter" |
| `obsidian-bases` | 创建 .base 数据库视图 | 用户提到"Bases/表格视图/筛选/公式" |
| `json-canvas` | 创建 .canvas 可视化画布 | 用户提到"Canvas/画布/思维导图/流程图" |
| `obsidian-cli` | CLI 操控 Obsidian 实例 | 用户要求操作 vault/搜索/创建笔记 |
| `defuddle` | 网页提取干净 Markdown | 用户提供 URL 要求读取文章内容 |

这些 skill 在需要时自动触发，无需手动调用。

---

## 6⃣ 内置能力

LLM 可以：
- **搜索** — 使用合适的搜索工具查找 wiki 页面
- **Web 搜索** — 对知识缺口进行网络搜索补充
- **读图** — `raw/assets/` 中的图片可以读取分析
- **编程** — 生成图表（matplotlib）、幻灯片（Marp）等

---

## 6⃣ 演化

本文档应与知识库**共同演化**。随着新需求出现，更新此文件以反映：
- 新的页面类型或格式
- 新的工作流
- 新的约定

---

*基于 Andrej Karpathy 的 LLM Wiki 模式构建*
