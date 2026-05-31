---
title: Operation Log
tags: [log, changelog]
created: 2026-05-06
---

# 📋 操作日志

> Append-only 记录。每条日志以 `## [YYYY-MM-DD] <操作类型>` 开头，便于 grep 检索。

---

## [2026-05-06] init | 知识库初始化

初始化 `Knowledge/` 知识库，严格按 Karpathy LLM Wiki 三层架构搭建。

- 创建目录：`raw/assets/`, `wiki/concepts/`, `wiki/entities/`, `wiki/sources/`, `wiki/syntheses/`
- 创建 Schema 文件：[[CLAUDE.md]]
- 创建导航：[[wiki/index.md]]
- 创建概念页面（4个）：llm-wiki-pattern, rag-vs-llm-wiki, wiki-schema, knowledge-ingest-workflow
- 创建实体页面（3个）：andrej-karpathy, obsidian, qmd
- 创建来源摘要：[[wiki/sources/llm-wiki-karpathy]]

## [2026-05-06] ingest | llm-wiki-karpathy

将 Karpathy 的 LLM Wiki 原文作为首个源文档归档并 ingest。

- 源文档：`raw/llm-wiki-karpathy-2026-04-04.md`
- 创建了来源摘要页
- 提取了 4 个核心概念并创建概念页面
- 提取了 3 个关键实体并创建实体页面
- 更新了 Wiki 索引

## [2026-05-06] ingest | Xie et al. 2026 — ThK Cells

将 Xie 等人在 *Nature Immunology* 发表的 ThK 细胞论文归档并 ingest。

- 源文档：`raw/xie-et-al-2026-thk-cells-nature-immunology.pdf`
- 创建了来源摘要页：[[wiki/sources/xie-et-al-2026-thk-cells]]
- 提取了 2 个核心概念：
  - [[wiki/concepts/thk-cells]] — ThK 细胞的定义、特征、分化调控、功能、保守性
  - [[wiki/concepts/eomes-transcription-factor]] — EOMES 的分子机制、必要性/充分性、表观遗传调控
- 提取了 2 个关键实体：
  - [[wiki/entities/chen-dong]] — 通讯作者董晨
  - [[wiki/entities/tian-xie]] — 第一作者谢天
- 更新了 Wiki 索引
- 总页面数更新：8 → 13；原始资料数：1 → 2

## [2026-05-15] fetch | Cross-tissue immune cell atlas (Science 2022)

- **来源**：流式中文网公众号文章 → 追溯原文 [DOI 10.1126/science.abl5197](https://doi.org/10.1126/science.abl5197)
- **追溯资源**：CellTypist (GitHub + 官网) | TissueImmuneCellAtlas (GitHub) | ArrayExpress E-MTAB-11536 | UCSC Cell Browser
- **新页面**：[[wiki/sources/cross-tissue-immune-cell-atlas-science-2022]]
- **更新 index**：+1 条 Sources 条目
- **更新 prompt**：fetch-url.md 新增原始文献与数据资源追溯步骤

## [2026-05-06] update | 新增 prompts 目录

在 Knowledge 根目录下新增 `prompts/` 层，存放 Wiki 操作模板。

- 创建了 6 个操作模板：
  - [[prompts/ingest-source]] — 导入新源的标准化流程
  - [[prompts/query-wiki]] — 查询知识库的流程
  - [[prompts/lint-wiki]] — 健康检查清单
  - [[prompts/explore-topic]] — 深度探索主题
  - [[prompts/synthesize]] — 综合分析
  - [[prompts/update-wiki]] — 维护更新
- 更新了 [[CLAUDE.md]] 中的目录结构描述
- 更新了 [[wiki/index]] 中的导航索引
- 总页面数：13 → 19

## [2026-05-06] ingest | Zotero 文献库批量导入

从 `C:\Users\Yun\Zotero\storage` 批量导入约 44 篇免疫学/TCR 相关文献。

**操作**：
- 复制 ~44 个唯一 PDF 到 `raw/pdfs/`（去重后，略过已导入的 ThK 论文）
- 创建 4 个按主题聚类的批量来源摘要：
  - [[wiki/sources/batch-tcr-repertoire-analysis]] — TCR 库分析 & ML（12 篇）
  - [[wiki/sources/batch-tcr-epitope-prediction]] — TCR-表位结合预测（10 篇）
  - [[wiki/sources/batch-sc-multiomics-tcell-bio]] — 单细胞多组学 & T 细胞生物（12 篇）
  - [[wiki/sources/batch-bioinfo-methods]] — 生信方法 & 其他（10 篇）

**知识提取**：
- 新增 3 个概念页：
  - [[wiki/concepts/tcr-repertoire]] — TCR 库的生成、多样性、影响因素
  - [[wiki/concepts/tcr-epitope-prediction]] — 计算方法与最新进展
  - [[wiki/concepts/single-cell-tcr-seq]] — 单细胞多模态整合分析
- 新增 4 个实体页：
  - [[wiki/entities/tcrdb]] — TCR 序列数据库
  - [[wiki/entities/sonnia]] — 深度生成选择模型
  - [[wiki/entities/deeptcr]] — VAE 深度 TCR 学习框架
  - [[wiki/entities/mixcr]] — 免疫组库分析软件

**更新**：
- [[wiki/index]] 全面更新（19 → 32 页）
- 原始资料数：2 个文件 + ~44 个 PDF

## [2026-05-06] install | obsidian-skills

从 [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) 安装 5 个 Agent Skills 到 vault。

**安装**：
- 复制 skills 目录到 `.claude/skills/`
- 5 个技能已在当前 session 中生效

**Wiki 记录**：
- 新增概念页 [[wiki/concepts/obsidian-agent-skills]] — Obsidian Agent Skills 总览
- 新增 5 个实体页：
  - [[wiki/entities/obsidian-markdown-skill]] — Obsidian 风味 Markdown
  - [[wiki/entities/obsidian-bases-skill]] — Bases 数据库视图
  - [[wiki/entities/json-canvas-skill]] — JSON Canvas 画布
  - [[wiki/entities/obsidian-cli-skill]] — CLI 操控
  - [[wiki/entities/defuddle-skill]] — 网页提取
- 更新 [[wiki/entities/obsidian]] 添加技能引用
- 更新 [[CLAUDE.md]] 添加技能描述
- 更新 [[wiki/index]]（32 → 38 页）

## [2026-05-06] ingest | ImmunoMatch — Guo et al. 2026, Nature Methods

用 pdftotext 提取并 ingest Nature Methods 论文。

- 源文档：`raw/s41592-025-02913-x.pdf`
- 来源摘要：[[wiki/sources/s41592-025-02913-x]]
- 概念页：[[wiki/concepts/antibody-hl-pairing]] — 抗体 H-L 链配对预测的生物学基础与计算方法
- 实体页：[[wiki/entities/immunomatch]] — ImmunoMatch 工具详情
- 更新 [[wiki/index]]（40 → 43 页）
- 原始资料数：4 个文件 + ~44 个 PDF
- 总页面数更新：40 → 43

## [2026-05-06] ingest | HLA 分型技术指南

用 defuddle 提取微信公众号文章并 ingest。

- 源文档：`raw/hla-typing-guide-2025.md`（defuddle 保存的 Markdown）
- 来源摘要：[[wiki/sources/hla-typing-guide]]
- 概念页：[[wiki/concepts/hla-typing]] — HLA 分型策略、工具、质控、IVD 验证
- 更新 [[wiki/index]]（38 → 40 页）
- 原始资料数：3 个文件 + ~44 个 PDF

## [2026-05-15] fetch | Chen et al. 2023 — TCR 序列主导 CD8+ T 细胞表型

抓取并归档 Cell Reports 论文 — 定量比较 TCR 序列 vs 环境信号对 CD8+ T 细胞表型的贡献。

- **URL**：https://www.cell.com/cell-reports/fulltext/S2211-1247(23)01291-3 → DOI: [10.1016/j.celrep.2023.113279](https://doi.org/10.1016/j.celrep.2023.113279)
- **核心发现**：TCR 序列是 CD8+ T 细胞表型和持久性的**主导因素**，远超环境信号（验证于 SARS-CoV-2/CMV/Influenza 三种抗原）
- **新页面**：
  - `raw/Chen_2023_CellReports_TCR_dominant_phenotype.md` — 原始资料
  - [[wiki/sources/chen-2023-cell-reports-tcr-dominant-phenotype]] — 来源摘要（含与 TCRCellNet 的深度关联分析）
- **更新 TCRCellNet**：README 新增第 3 篇文献条目
- **更新 index**：+1 条 Sources 条目（10 → 11），页面总数 46 → 47
- **PDF**：OA 期刊，需手动从 PMC 保存

## [2026-05-15] update | nature-reader skill — 项目感知输出目录与独立论文目录

优化 nature-reader skill，使精读输出适配当前项目（TCRCellNet）的组织方式。

**skill 更新**：
- [[.claude/skills/nature-reader/skill.md]] — 新增「Project-Aware Output Directory」章节
  - 项目上下文检测逻辑（显式指定 → 工作目录 → 源路径 → 关联实体 → 兜底）
  - 输出目录规范：`{project-root}/papers/{paper-key}/`
  - paper key 命名规则：`{首姓}-{年份}-{短描述}`
  - 相对路径要求（自包含、可移植）
- Workflow 新增 Step 0：确定项目上下文和输出路径
- Output contract 更新：所有输出移至专属目录，验证清单增加 PDF 存在检查

**现有论文迁移**：
- `TCRCellNet/papers/` → `TCRCellNet/papers/chen-2023-tcr-dominant-phenotype/`
  - `paper.md` + `PIIS2211124723012913.pdf` + `assets/` 全部移至独立子目录
  - 相对路径保持不变，Wiki 链接可用
- 项目 README 更新：目录结构图 + 已归档文献表新增「精读」链接列

**后续待迁移**：
- Afik 2017 / Monian 2021 的精读待创建时将自动使用新结构

## [2026-05-15] install | nature-skills — 学术工作流技能包

从 https://github.com/zqywuxie/nature-skills 安装 9 个学术工作流技能到 `.claude/skills/`。

- **安装技能**：
  - nature-reader — 文献精读（中英对照全文翻译）
  - nature-figure — 科学图表优化
  - nature-writing — Nature 风格学术写作
  - nature-polishing — 论文润色
  - nature-paper2ppt — 论文转 PPT
  - nature-citation — 引文管理
  - nature-data — 数据可用性声明
  - nature-response — 审稿回复
  - nature-academic-search — 学术搜索
- **新增 prompt**：[[prompts/nature-skills]] — 使用指南
- **更新 index**：+1 prompts 条目（6 → 7）

## [2026-05-15] fetch | Monian et al. 2022 — Peanut OIT 差异化抑制 Th 亚群

抓取并归档 JCI 论文 — 花生 OIT 对克隆性不同的 Th 亚群的差异化抑制。

- **URL**：https://www.jci.org/articles/view/150634 → 追溯 DOI: [10.1172/JCI150634](https://doi.org/10.1172/JCI150634)
- **追溯资源**：GitHub [mitlovelab/PNOIT2_scRNAseq] | GEO GSE158667 | dbGaP phs001897.v2.p1 | ClinicalTrials.gov NCT01750879
- **新页面**：
  - `raw/Monian_2021_JCI_peanut_OIT.md` — 原始资料（全文结构化摘要）
  - [[wiki/sources/monian-2021-jci-peanut-oit]] — 来源摘要（含方法学亮点与分析笔记）
- **更新 TCRCellNet**：README 新增第 2 篇文献条目
- **更新 index**：+1 条 Sources 条目（9 → 10）
- **PDF**：OA 期刊，当前环境自动下载受限，需手动从 PMC 保存

## [2026-05-15] init | TCRCellNet 课题目录

创建 `TCRCellNet/` 课题文献管理目录。

- **新建目录结构**：
  - `TCRCellNet/README.md` — 项目索引
  - `TCRCellNet/papers/` — 核心文献
  - `TCRCellNet/notes/` — 个人笔记
  - `TCRCellNet/data/` — 数据资源
- **首次归档文献**：[[wiki/sources/afik-2017-trapes]] — TRAPeS (Afik et al. 2017, NAR)
- **原始资料**：`raw/Afik_2017_TRAPeS.md`（元数据 + 摘要）；PDF 待手动从 PMC 下载
- **更新 index**：+1 条 Sources 条目（8 → 9），+1 课题目录

## [2026-05-18] fetch | popV — Ergen et al. 2024, Nature Genetics

抓取并精读 Nature Genetics 论文 — 集成 8 种细胞类型注释方法以提供共识预测和校准良好的不确定性评分。

- **URL**: https://www.nature.com/articles/s41588-024-01993-3 → DOI: [10.1038/s41588-024-01993-3](https://doi.org/10.1038/s41588-024-01993-3)
- **追溯资源**:
  - Code: [YosefLab/popV](https://github.com/YosefLab/popV) | [popv-reproducibility](https://github.com/YosefLab/popv-reproducibility)
  - Data: Tabula Sapiens (CELLxGENE), Lung Cell Atlas, Thymus (Park 2020), Brain (MTG/M1G)
  - Pretrained: Zenodo 10.5281/zenodo.7580707
- **新页面**:
  - [[Knowledge/papers/popv-2024-cell-type-annotation/paper.md]] — 中英文精读（含3图解读）
  - [[Knowledge/papers/popv-2024-cell-type-annotation/original.pdf]] — 原始PDF
  - [[wiki/sources/popv-2024-cell-type-annotation]] — 来源摘要
- **更新 index**: +1 条 Sources 条目（14 → 15），页面总数 51 → 52

## [2026-05-20] fetch | ProjecTILs — Andreatta & Carmona 2021

Defuddle 提取 Nature Communications 全文 + 中英文精读。

- 关联资源：DOI 10.1038/s41467-021-23324-4 | Code: carmonalab/ProjecTILs, STACAS | Data: figshare atlases + GEO datasets
- 来源摘要：[[wiki/sources/andreatta-2021-projectils]]
- 精读笔记：[[Knowledge/papers/projectils-2021/paper.md]]
- 处理内容：bilingual paper.md (24 source blocks, 9 figure blocks), source_map.json, translation_notes.md, 9 figures (9.5MB total)

## [2026-05-20] fetch | CoNGA — Schattgen et al. 2021

Defuddle 提取 PMC 全文 + 全文精读。

- 关联资源：DOI 10.1038/s41587-021-00989-2 | Code: phbradley/conga | Data: 10x Genomics + Thymus atlas
- 来源摘要：[[wiki/sources/schatgen-2021-conga]]
- 精读笔记：[[Knowledge/papers/schatgen-2021-conga/paper.md]]
- 处理内容：bilingual paper.md (27 个 source blocks, 6 个 figure blocks), source_map.json, translation_notes.md, PDF download (7.4MB), 6 figures downloaded

## [2026-05-19] fetch | PRP — Wang et al. 2026, Nature Biotechnology

From 微信公众号「计算生物前沿」科普文章 → 追溯原始论文。

- **URL**: https://mp.weixin.qq.com/s/YZCDBZkHLuSFPgorCmoW1w → 追溯 DOI: [10.1038/s41587-026-03128-x](https://doi.org/10.1038/s41587-026-03128-x)
- **新页面**:
  - `raw/wang-2026-prp-tcr-specificity-nbt.md` — 原始公众号文章存档
  - [[wiki/sources/wang-2026-prp-tcr-specificity]] — 来源摘要
  - [[wiki/concepts/deep-peptide-recognition-profiling]] — PRP 概念页（实验PRP+蛋白语言模型范式）
- **更新概念页**:
  - [[wiki/concepts/tcr-epitope-prediction]] — 新增 PRP 方法条目 + 交叉引用
- **更新 index**: +1 Concepts（11→12），+1 Sources（15→16），页面总数 52→54

## [2026-05-16] fetch | DeepTCR — Sidhom et al. 2021, Nature Communications

抓取并精读 Nature Communications 论文 — 用深度学习方法（VAE + CNN + 多实例学习）对 TCR 序列进行建模。

- **URL**: https://www.nature.com/articles/s41467-021-21879-w → DOI: [10.1038/s41467-021-21879-w](https://doi.org/10.1038/s41467-021-21879-w)
- **追溯资源**:
  - Code: [sidhomj/DeepTCR](https://github.com/sidhomj/DeepTCR) | PyPI DeepTCR
  - Data: 10x Genomics multi-chain dataset, McPAS-TCR, tetramer-sorted data
- **新页面**:
  - [[Knowledge/papers/sidhom-2021-deeptcr/paper.md]] — 中英文精读（含5图5表解读）
  - [[Knowledge/papers/sidhom-2021-deeptcr/original.pdf]] — 原始PDF
  - [[wiki/sources/sidhom-2021-deeptcr]] — 来源摘要
- **更新 index**: +1 条 Sources 条目（13 → 14），页面总数 50 → 51

## [2026-05-16] fetch | UCell — Andreatta & Carmona 2021, CSBJ

抓取并精读 CSBJ 论文 — 基于 Mann-Whitney U 统计量的单细胞基因签名评分 R 包。

- **URL**: https://spj.science.org/doi/10.1016/j.csbj.2021.06.043 → DOI: [10.1016/j.csbj.2021.06.043](https://doi.org/10.1016/j.csbj.2021.06.043)
- **追溯资源**:
  - Code: [carmonalab/UCell](https://github.com/carmonalab/UCell) | [UCell_demo](https://gitlab.unil.ch/carmona/UCell_demo)
- **新页面**:
  - [[Knowledge/papers/andreatta-2021-ucell/paper.md]] — 中英文精读
  - [[Knowledge/papers/andreatta-2021-ucell/original.pdf]] — 原始PDF
  - [[wiki/sources/andreatta-2021-ucell]] — 来源摘要
- **更新 index**: +1 条 Sources 条目（12 → 13），页面总数 49 → 50

## [2026-05-16] fetch | cNMF — Kotliar et al. 2019, eLife

抓取并精读 eLife 论文 — 用共识 NMF 从 scRNA-Seq 同时推断身份与活动基因表达程序。

- **URL**：https://elifesciences.org/articles/43803 → DOI: [10.7554/eLife.43803](https://doi.org/10.7554/eLife.43803)
- **追溯资源**：
  - Code: [dylkot/cNMF](https://github.com/dylkot/cNMF/) | [dylkot/scsim](https://github.com/dylkot/scsim)
  - Data: GSE86153 (organoid) | GSE102827 / GSE71585 (visual cortex) | GSE50244 (pancreas)
  - Reproducible capsule: Code Ocean 10.24433/CO.9044782e-cb96-4733-8a4f-bf42c21399e6
- **新页面**：
  - [[Knowledge/papers/kotliar-2019-cnmf/paper.md]] — 中英文精读全文
  - [[Knowledge/papers/kotliar-2019-cnmf/original.pdf]] — 原始PDF
  - [[wiki/sources/kotliar-2019-cnmf]] — 来源摘要
- **更新 index**：+1 条 Sources 条目（11 → 12），页面总数 48 → 49

## [2026-05-07] update | Xie et al. 2026 — 补充实验方法详解

用 pdftotext 完整提取论文全文文本，详细阅读并整理了全部实验操作细节，更新到知识库。

**更新内容**：
- [[wiki/sources/xie-et-al-2026-thk-cells]] — 新增完整「实验方法详解」大章节，涵盖：
  - 所有 17 个小鼠品系及来源
  - T 细胞诱导性结肠炎模型操作流程
  - 结肠淋巴细胞分离详细步骤（含试剂浓度、时间、温度）
  - 体外 T 细胞分化方案（5 种条件，含所有细胞因子组合）
  - 逆转录病毒 Eomes 过表达实验流程
  - OVA 免疫模型
  - 体外细胞毒性实验
  - 完整流式抗体方案（21 种抗体，含克隆号、荧光、供应商）
  - 组织学分析方法
  - RT-qPCR 引物序列（4 对）
  - bulk RNA-seq / scRNA-seq / ATAC-seq / CUT&Tag 全部生信参数
  - 基因-峰整合分析逻辑
  - 统计方法细节及实验设计逻辑链流程图
- [[wiki/concepts/thk-cells]] — 新增「实验方法速览」交叉引用表格
- [[wiki/concepts/eomes-transcription-factor]] — 新增「实验方法速览」验证维度表格
- [[wiki/entities/chen-dong]], [[wiki/entities/tian-xie]] — 更新日期
- [[wiki/index]] — 更新日期
- 总页面数不变（43 页）

## [2026-05-22] fetch | DynNet — Dou et al. 2026, Nature Communications

Defuddle 提取微信公众号科普文章 + 追溯原始 Nature Communications 论文 + 中英文精读。

- **来源**：微信公众号「计算生物前沿」文章 → 追溯 DOI: [10.1038/s41467-026-73257-z](https://doi.org/10.1038/s41467-026-73257-z)
- **原始资料**：
  - `raw/dynnet-wechat-article.md` — 公众号文章全文
  - `raw/dynnet-paper.pdf` — 原始论文 PDF（16.7MB，Article in Press，57页）
- **精读笔记**：[[Knowledge/papers/dynnet-2026/paper.md]] — 中英文对照全文（24 source blocks, 6 figure blocks）
- **新页面**：
  - [[wiki/sources/dynnet-2026]] — 来源摘要
  - [[wiki/concepts/dynnet]] — DynNet 概念页（含方法对比表）
- **更新 index**：+1 Sources（18→19），+1 Concepts（12→13），页面总数 56→58
