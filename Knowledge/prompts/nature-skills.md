---
title: Nature Skills — 学术工作流技能
tags: [prompt, reference, nature, academic, writing, workflow]
created: 2026-05-15
updated: 2026-05-15
---

# Nature Skills — 学术工作流技能

> 安装自 [nature-skills](https://github.com/zqywuxie/nature-skills)（上海交通大学袁一哲博士维护）。
> 共 9 个技能，覆盖从文献精读到论文发表全流程。

---

## 快速使用

所有技能通过自动化触发，当你的请求匹配技能描述时会自动激活，**无需手动调用**。

也可以**主动提及技能名**来触发：
- "用 nature-reader 精读这篇论文"
- "用 nature-figure 优化这个图"
- "用 nature-writing 写一段 Introduction"

---

## 技能清单

### 1. `nature-reader` — 文献精读

**用途**：将论文（PDF/DOI/arXiv/HTML）转为中英对照 Markdown 精读笔记，图表原位嵌入，保留段落结构和来源锚点。

**触发场景**：你说"翻译这篇论文"、"中英对照"、"全文翻译解读"、"精读"时。

**输出**：`paper.md`（完整精读）+ `source_map.json` + `translation_notes.md` + `assets/`（图片）

### 2. `nature-figure` — 科学图表

**用途**：按 Nature 期刊标准优化科学图表——配色方案、字体、分辨率、排版布局、可访问性。

**触发场景**：你说"优化这张图"、"调色"、"改图表风格"、"Nature 格式的图"时。

### 3. `nature-writing` — 学术写作

**用途**：按 Nature 文章模式起草/重构摘要、引言、结果、讨论等章节。强调"先论证再写句"。

**触发场景**：你说"写一段 Introduction"、"写 Discussion"、"起草摘要"、"重构 Results"时。

**配套参考**：
- `references/article-architecture.md` — 文章结构策略
- `references/abstract.md` — 摘要写作模式
- `references/introduction.md` — 引言框架
- `references/method.md` — 方法写作
- `references/experiments.md` — 实验/结果部分
- `references/conclusion.md` — 结论写作
- `references/paragraph-flow.md` — 段落流畅度检查
- `references/paper-review.md` — 稿件自查
- `references/chinese-author-workflow.md` — 中文作者工作流

### 4. `nature-polishing` — 论文润色

**用途**：将学术草稿/中文稿润色为 Nature 级别的英文，基于 Nature 文章模式和 Academic Phrasebank。

**触发场景**：你说"润色这段"、"改英文"、"polish paragraph"、"提升语言质量"时。

### 5. `nature-paper2ppt` — 论文转 PPT

**用途**：将论文转为 Nature 风格的科研汇报 PPTX，自动识别论文类型、选择关键图表、写中文幻灯片和讲稿笔记。

**触发场景**：你说"做 PPT"、"做 slides"、"文献汇报"、"journal club"、"组会汇报"时。

### 6. `nature-citation` — 引文管理

**用途**：严格按 Nature/CNS 期刊标准添加引用——搜索 Nature Portfolio / Science / Cell Press 系列期刊，管理 .nbib/.ris/.bib 文献文件。

**触发场景**：你说"加引用"、"查引用格式"、"管理参考文献"、"导出 BibTeX"时。

### 7. `nature-data` — 数据可用性

**用途**：按 Nature 标准准备/审核 Data Availability Statement、数据仓库方案、数据集引用、FAIR 元数据清单。

**触发场景**：你说"数据可用性声明"、"写 Data Availability"、"选数据仓库"、"FAIR 原则"时。

### 8. `nature-response` — 审稿回复

**用途**：起草/审核 Nature 级别的逐点审稿回复信（point-by-point response letter）。

**触发场景**：你说"写回复信"、"response letter"、"回复审稿人"、"rebuttal letter"时。

### 9. `nature-academic-search` — 学术搜索

**用途**：多源文献检索、引文验证、MeSH 搜索策略、文献文件格式转换（.nbib/.ris/.bib），通过 MCP 工具（PubMed, CrossRef, arXiv）实现。

**触发场景**：你说"搜索文献"、"查引用"、"MeSH 检索"、"文献管理"时。

---

## 完整工作流示例

```
文献检索          → nature-academic-search
   ↓
文献精读          → nature-reader
   ↓
数据/图表分析     → nature-data / nature-figure
   ↓
论文写作          → nature-writing
   ↓
润色              → nature-polishing
   ↓
引用管理          → nature-citation
   ↓
审稿回复          → nature-response
   ↓
汇报展示          → nature-paper2ppt
```

---

## 注意事项

- 所有 skill 的完整文档和参考文件在 `.claude/skills/nature-*/` 目录下
- `nature-reader` 的默认输出是中英对照全文精读，不是摘要
- `nature-writing` 严格要求基于作者提供的证据，不会编造结果
- 版本更新：`cd ~/nature-skills && git pull` 后重新 `cp -r skills/nature-* .claude/skills/`
