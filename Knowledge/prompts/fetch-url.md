---
title: Fetch URL — 抓取网页并解读
tags: [prompt, ingest, web, fetch]
created: 2026-05-08
updated: 2026-05-15
---

# 抓取网页并解读 (Fetch URL)

> 访问一个 URL，抓取其内容，然后解读、分析并归档到 Wiki 知识库中。
> 与 Ingest 的区别：Ingest 处理本地文件，此流程处理在线资源。

## 使用场景

当你想把一篇在线文章、文档、GitHub 仓库 README 或任何网页内容导入知识库时。

## Prompt

```
请抓取并解读以下 URL 的内容：

<URL>

请按以下流程操作：

## 步骤 1：抓取内容
- 使用 defuddle skill 获取 URL 页面内容（优先）或 WebFetch
- 如页面内容过长，先获取关键部分（README、摘要、目录）
- 对于 GitHub 仓库，同时获取文件目录结构

## 步骤 1b：追溯原始文献与数据资源（重要）

在总结之前，先扫描页面内容，查找并提取以下**关联资源**：

### A. 原始文献信息
扫描页面中引用的 DOI、PMID、论文标题、作者 + 年份等：
```
示例：doi:10.1126/science.abl5197
      Domínguez Conde C, et al. Science. 2022;376(6594):eabl5197
```
- 如果页面直接链接到了 PDF 原文 → 下载到 Knowledge/raw/
- 如果页面只有 DOI/PMID 但无直接 PDF → 用 WebFetch 访问原文页面（至少保留摘要 + 引用信息）
- 提取完整引用信息（DOI、期刊、年份、作者、标题）→ 记录到后续的归档中

### B. Code/Data availability
扫描页面中是否提及以下信息，并提取对应的**链接和编号**：
- GitHub/GitLab 仓库 → 尝试用 defuddle 抓取 README
- GEO/SRA/ENA/ArrayExpress 等数据库编号 → 记录编号
- 工具/软件官网 → 记录 URL
- 补充数据 / 在线资源链接 → 记录 URL

#### 无法直接下载 PDF 时怎么办
- 有些文献是付费墙后的，直接 PDF 链接不可用 → 至少记录 DOI，待后续通过 Zotero/papers 渠道获取
- 对于开放获取论文（OA），直接下载 PDF 到 Knowledge/raw/
- arXiv/medRxiv/bioRxiv 等预印本 → 直接下载 PDF

### C. 记录跟踪表
将追溯到的所有资源汇总为表格，放到归档页面的 YAML frontmatter 或正文中：
```yaml
sources:
  - type: paper
    title: "原文标题"
    doi: "10.xxx/xxx"
    url: "https://..."
    pdf: "Knowledge/raw/filename.pdf"  # 如果已下载
  - type: code
    repo: "GitHub: user/repo"
    url: "https://github.com/user/repo"
  - type: data
    accession: "GSE123456"
    database: "GEO"
```

## 步骤 2：初步总结
- 总结原始 URL 页面的核心内容和目的（而非原文本身的详细论述）
- 区分"页面作者写的解读/总结"和"原文文献的原始结论"
- 如果是科普/新闻类文章，额外说明其与原文的关系
- 询问用户是否有需要深入展开的部分

## 步骤 3：解读与分析
根据内容类型进行针对性分析：

### 代码/技术仓库
- 分析架构和模块设计
- 提取关键技术和依赖
- 评估可用性和维护状态

### 科普/新闻文章（含追溯到的原始论文）
- 先说明：本文是科普解读，原始文献在下方关联资源中
- 提取科普文章的核心转述要点
- 与实际原文对比，检查是否有转述偏差或简化
- 如果原文数据/代码已获取，看能否验证文章中的具体论断

### 工具/文档
- 总结核心功能和使用方法
- 对比同类工具（如有）
- 评估是否值得引入工作流

## 步骤 4：归档到 Wiki

无论是否追溯到了原始文献，都按以下流程归档本次 fetch 的内容：

### 创建来源摘要 (wiki/sources/)
- 命名：<简短英文描述>.md
- YAML frontmatter 中写入所有追溯到的关联资源（论文 DOI、代码仓库、数据编号）
- 正文结构：
  1. 抓取的 URL 页面摘要
  2. 原始论文核心信息（如追溯到了论文）
  3. 代码/数据资源清单
  4. 本次分析笔记

### 概念/实体页面
- 提取新概念 → wiki/concepts/
- 提取新实体（工具、人物、组织）→ wiki/entities/

### 更新索引和日志
- wiki/index.md 中添加链接
- wiki/log.md 追加记录：
## [YYYY-MM-DD] fetch | <页面标题>
- 关联资源：DOI xxx | Code: xxx | Data: xxx

## 注意事项
- Web 内容可能过时或不准确，标注获取日期
- **明确区分**"页面原文内容"、"原始论文内容"、"你的分析解读"三层
- 对 GitHub 仓库优先关注：README、LICENSE、目录结构、最近提交
- PDF 下载到 Knowledge/raw/，不要放到 wiki/ 目录下
- DOI 是唯一标识符，优先于 URL 记录
```

## 流程逻辑图

```
输入 URL（科普/新闻/教程页面）
    ↓
抓取内容
    ↓
扫描页面 → 提取 DOI → 访问原文 → 下载 PDF（如 OA）
         → 提取 GitHub 链接 → 抓取 README
         → 提取 GEO/SRA 编号
    ↓
总结 + 分析（区分"原文"和"文章"）
    ↓
归档到 Wiki（含全部关联资源索引）
```
