---
title: Knowledge Base Index
tags: [index, moc, navigation]
created: 2026-05-06
updated: 2026-05-22
---

# 📚 知识库索引

> 所有页面的内容导航。查询时从此出发，按类别深入。

---

## 📂 Sources（来源摘要）

| 页面                                                                                                             | 简介                                 | 源文档                                                                            |
| -------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------ |
| [[wiki/sources/llm-wiki-karpathy\|LLM Wiki — Karpathy]]                                                        | Karpathy 的 LLM Wiki 模式概述与核心理念      | `raw/llm-wiki-karpathy-2026-04-04.md`                                          |
| [[wiki/sources/xie-et-al-2026-thk-cells\|Xie et al. 2026 — ThK Cells]]                                         | GZMK⁺EOMES⁺ CD4⁺ T 新亚群的发现          | `raw/xie-et-al-2026-thk-cells-nature-immunology.pdf`                           |
| [[wiki/sources/batch-tcr-repertoire-analysis\|TCR Repertoire 分析合集]]                                            | TCR 库分析、ML 方法、生成模型等 12 篇           | `raw/pdfs/` (12 个 PDF)                                                         |
| [[wiki/sources/batch-tcr-epitope-prediction\|TCR-表位预测合集]]                                                      | TCR 结合预测、表示学习、数据库等 10 篇            | `raw/pdfs/` (10 个 PDF)                                                         |
| [[wiki/sources/batch-sc-multiomics-tcell-bio\|单细胞多组学合集]]                                                       | scTCR-seq、T 细胞生物等 12 篇             | `raw/pdfs/` (12 个 PDF)                                                         |
| [[wiki/sources/batch-bioinfo-methods\|生信方法合集]]                                                                 | 组学整合、基础模型、临床应用等 10 篇               | `raw/pdfs/` (10 个 PDF)                                                         |
| [[wiki/sources/hla-typing-guide\|HLA 分型技术指南]]                                                                  | HLA 分型 16 问：短读长到长读长，算法到落地          | `raw/hla-typing-guide-2025.md`                                                 |
| [[wiki/sources/s41592-025-02913-x\|ImmunoMatch — Guo et al. 2026]]                                             | 抗体重轻链配对预测模型                        | `raw/s41592-025-02913-x.pdf`                                                   |
| [[wiki/sources/cross-tissue-immune-cell-atlas-science-2022\|Cross-tissue Immune Atlas — Domínguez Conde 2022]] | 泛组织免疫细胞图谱 + CellTypist 工具          | 公众号文章追溯                                                                        |
| [[wiki/sources/afik-2017-trapes\|TRAPeS — Afik et al. 2017]]                                                   | 从短读长 scRNA-seq 重建 TCR 序列           | `raw/Afik_2017_TRAPeS.md` + `raw/pdfs/` (待手动下 PDF)                             |
| [[wiki/sources/monian-2021-jci-peanut-oit\|Peanut OIT — Monian et al. 2022]]                                   | scRNA-seq+TCR 解析 OIT 对 Th 亚群的差异化抑制 | `raw/Monian_2021_JCI_peanut_OIT.md` + `raw/pdfs/` (待手动下 PDF)                   |
| [[wiki/sources/chen-2023-cell-reports-tcr-dominant-phenotype\|TCR dominant phenotype — Chen et al. 2023]]      | TCR 序列主导 CD8+ T 细胞表型               | `raw/Chen_2023_CellReports_TCR_dominant_phenotype.md` + `raw/pdfs/` (待手动下 PDF) |
| [[wiki/sources/kotliar-2019-cnmf\|cNMF — Kotliar et al. 2019]]                                                 | 共识NMF从scRNA-Seq同时推断身份与活动GEP        | `raw/kotliar-2019-cnmf.pdf`                                                    |
| [[wiki/sources/andreatta-2021-ucell\|UCell — Andreatta & Carmona 2021]]                                        | 基于Mann-Whitney U统计量的单细胞基因签名评分      | `raw/andreatta-2021-ucell.pdf`                                                 |
| [[wiki/sources/sidhom-2021-deeptcr\|DeepTCR — Sidhom et al. 2021]]                                             | 深度学习的TCR序列建模框架（VAE+监督+库分类）         | `raw/sidhom-2021-deeptcr.pdf`                                                  |
| [[wiki/sources/popv-2024-cell-type-annotation\|popV — Ergen et al. 2024]]                                      | 集成8种方法的细胞类型注释+不确定性评分               | `raw/popv-2024-cell-type-annotation.md` (defuddle)                             |
| [[wiki/sources/wang-2026-prp-tcr-specificity\|PRP — Wang et al. 2026]]                                         | 深度肽识别图谱解码TCR特异性+发现自身抗原             | 微信公众号追溯`raw/wang-2026-prp-tcr-specificity-nbt.md`                              |
| [[wiki/sources/schatgen-2021-conga\|CoNGA — Schattgen et al. 2021]]                                            | 图论方法系统发现TCR-GEX相关性                 | `raw/schatgen-2021-conga.md`                                                   |
| [[wiki/sources/andreatta-2021-projectils\|ProjecTILs — Andreatta & Carmona 2021]]                              | 参考图谱投影解读T细胞状态                      | `raw/projectils-2021.md`                                                       |
| [[wiki/sources/dynnet-2026\|DynNet — Dou et al. 2026]]                                                         | 随机动力学推断网络从scRNA-seq重建细胞命运          | `raw/dynnet-paper.pdf` + `raw/dynnet-wechat-article.md`                        |
|                                                                                                                |                                    |                                                                                |

## 🧠 Concepts（概念）

| 页面 | 简介 |
|------|------|
| [[wiki/concepts/llm-wiki-pattern\|LLM Wiki 模式]] | 增量构建和维护持久化个人知识库的核心方法论 |
| [[wiki/concepts/rag-vs-llm-wiki\|RAG vs LLM Wiki]] | 解释器模式 vs 编译器模式的对比 |
| [[wiki/concepts/wiki-schema\|Wiki Schema]] | Schema 配置文件的角色和设计 |
| [[wiki/concepts/knowledge-ingest-workflow\|Knowledge Ingest Workflow]] | 导入工作流的详细拆解 |
| [[wiki/concepts/thk-cells\|ThK 细胞]] | 新发现的 CD4⁺ GZMK⁺ T 细胞亚群，EOMES 驱动 |
| [[wiki/concepts/eomes-transcription-factor\|EOMES 转录因子]] | T-box 家族转录因子，ThK 细胞的 master regulator |
| [[wiki/concepts/tcr-repertoire\|TCR Repertoire]] | TCR 库的生成、多样性、影响因素与定量分析 |
| [[wiki/concepts/tcr-epitope-prediction\|TCR-表位结合预测]] | 从 TCR 序列预测抗原特异性的计算方法 |
| [[wiki/concepts/single-cell-tcr-seq\|Single-cell TCR-seq]] | 单细胞 TCR 测序 + 多模态整合分析 |
| [[wiki/concepts/obsidian-agent-skills\|Obsidian Agent Skills]] | LLM 与 Obsidian 交互的标准化技能层 |
| [[wiki/concepts/hla-typing\|HLA 分型技术]] | HLA 分型策略、工具对比、质控与 IVD 验证 |
| [[wiki/concepts/antibody-hl-pairing\|抗体 H-L 链配对]] | 抗体重轻链配对规则、计算方法与 ImmunoMatch |
| [[wiki/concepts/deep-peptide-recognition-profiling\|Deep Peptide Recognition Profiling (PRP)]] | 实验+计算整合解码TCR特异性，发现自身抗原 |
| [[wiki/concepts/dynnet\|DynNet — 随机动力学推断网络]] | Neural SDE + Hill函数从scRNA-seq重建命运动力学 |

## 👤 Entities（实体）

| 页面 | 简介 |
|------|------|
| [[wiki/entities/andrej-karpathy\|Andrej Karpathy]] | LLM Wiki 模式的提出者，OpenAI/Tesla 前 AI 科学家 |
| [[wiki/entities/obsidian\|Obsidian]] | Markdown 知识管理工具，本知识库的 IDE |
| [[wiki/entities/qmd\|qmd]] | 本地 Markdown 搜索引擎，混合 BM25/向量搜索 |
| [[wiki/entities/chen-dong\|Chen Dong（董晨）]] | 免疫学家，Th17/Tfh/ThK 发现者，西湖大学教授 |
| [[wiki/entities/tian-xie\|Tian Xie（谢天）]] | 清华大学博士生，ThK 研究第一作者 |
| [[wiki/entities/tcrdb\|TCRdb]] | 综合性 TCR 序列数据库 (Chen et al. 2021) |
| [[wiki/entities/sonnia\|soNNia]] | 深度生成选择模型 (Isacchini et al. 2021) |
| [[wiki/entities/deeptcr\|DeepTCR]] | VAE 深度 TCR 库学习框架 (Sidhom et al. 2021) |
| [[wiki/entities/mixcr\|MiXCR]] | 免疫组库测序分析软件 |
| [[wiki/entities/immunomatch\|ImmunoMatch]] | 基于 AntiBERTa2 的 H-L 链配对预测框架 |
| [[wiki/entities/obsidian-markdown-skill\|obsidian-markdown]] | Obsidian 风味 Markdown 编写技能 |
| [[wiki/entities/obsidian-bases-skill\|obsidian-bases]] | Obsidian Bases 数据库视图技能 |
| [[wiki/entities/json-canvas-skill\|json-canvas]] | JSON Canvas 可视化画布技能 |
| [[wiki/entities/obsidian-cli-skill\|obsidian-cli]] | Obsidian CLI 命令行交互技能 |
| [[wiki/entities/defuddle-skill\|defuddle]] | 网页提取干净 Markdown 技能 |

## 🔬 Syntheses（综合分析）

> 当前为空。好的查询答案将会归档在此。

## ⚡ Prompts（操作模板）

| 页面 | 用途 |
|------|------|
| [[prompts/ingest-source\|Ingest — 导入新源]] | 将新文档整合到 Wiki 的完整流程 |
| [[prompts/query-wiki\|Query — 查询知识库]] | 基于 Wiki 综合回答问题的流程 |
| [[prompts/lint-wiki\|Lint — 健康检查]] | 定期检查矛盾、过时内容、孤立页面 |
| [[prompts/explore-topic\|Explore — 深度探索]] | 结合网络搜索研究新主题 |
| [[prompts/synthesize\|Synthesize — 综合分析]] | 多页面横向比较与综合 |
| [[prompts/update-wiki\|Update — 维护更新]] | 批量修复链接、统一格式、重组结构 |
| [[prompts/nature-skills\|Nature Skills — 学术工作流]] | 9 个 Nature 标准学术技能的使用指南 |

---

## 统计

| 指标 | 数值 |
|------|------|
| 页面总数 | 58 |
| 原始资料 | 8 个文件 + ~44 个 PDF |
| 操作模板 | 7 |
| 概念页 | 13 |
| 实体页 | 15 |
| 来源摘要 | 19 |
| Agent Skills | 5（已安装到 .claude/skills/） |
