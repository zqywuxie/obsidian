---
name: nature-reader
description: Build full-paper Chinese-English side-by-side, figure/table-aware, source-grounded Markdown readers for journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use whenever the user asks to translate or read a paper, make 中英文对照/原文对照/全文翻译解读, extract figures or tables into the right positions, preserve figure/table placement near relevant prose, or keep exact source anchors for every block. This skill must not degrade into a summary-only output unless the user explicitly asks for a summary.
---

# Full-Paper Markdown Reader

Use this skill to turn a research paper into a complete Markdown reading artifact.

The default output should read like a bilingual paper companion, not a summary dump:

- keep the extractable prose, paragraph structure, and section flow
- show original text and Chinese translation together at block level
- extract figures and tables as assets and place them at the first substantive mention or interpretation point
- keep captions attached to figures/tables with English caption text and Chinese caption translation
- preserve stable page and block anchors for traceability
- write a complete `paper.md` into `{project-root}/papers/{paper-key}/`, plus `original.pdf`, `source_map.json`, `translation_notes.md`, and `assets/`

This skill is for papers, preprints, and conference proceedings across disciplines. It is not limited to Nature-family journals.

## When to use

Use this skill when the user wants any of the following:

- translate an entire paper into a complete Markdown document
- make a paper easier to read without losing the original wording
- generate a full-paper reading file with original/translation alignment
- keep figures or tables visually close to the claims they support
- preserve exact source locations for every substantive block
- build a source-grounded markdown artifact rather than a slide deck or short summary

If the user only wants a summary, use a summarization skill instead. If the user only wants citation search, use a citation skill instead.

## Non-negotiable defaults

When the user asks for paper translation, reading, `nature-reader`, `中英文对照`, `原文对照`, `全文翻译`, or `翻译解读`, produce a paragraph-level bilingual reader by default.

Do not replace the reader with:

- a Chinese-only summary
- a paper review without original/translation alignment
- figure captions without figure/table crops
- a list of key points detached from source locations
- only the abstract, introduction, or selected highlights

If constraints prevent full processing, still create a draft reader and clearly label missing pages, missing figures/tables, untranslated blocks, or low-confidence OCR/crops in `translation_notes.md`.

## Core principle

Translate for meaning, not for style. Preserve the paper's structure, evidence, hedging, terminology, equations, units, and citation markers. Keep the output in prose paragraphs unless the source itself is tabular or list-like. Do not collapse the paper into keyword bullets or slide-style notes.

The reading file should help a reader move between:

- original text
- translated text
- source location
- figure or table evidence

Each substantive source block should have a stable anchor and a visible bilingual pair:

```markdown
<a id="S001"></a>
**Source:** p.1 S001

**Original:** [source paragraph]

**中文:** [faithful Chinese translation]
```

For copyrighted publisher PDFs, keep chat responses short and point to the local artifact. In local `paper.md`, include the bilingual reader only for the user-provided source file or clearly lawful open-access content; avoid reproducing large copyrighted text directly in chat.

## Project-Aware Output Directory

This vault organizes papers by project. Each paper's reading artifact lives in its own dedicated subdirectory under the project's `papers/` folder, making the artifact self-contained and portable.

### Determining the project context

Check, in order:
1. **User explicitly specifies** a project (e.g., "for TCRCellNet project")
2. **Current working context** — the PDF or source is inside an existing project's `papers/` directory tree
3. **Source path** — if the user provides a PDF from `raw/pdfs/`, check if it already has a project association in the wiki (via `wiki/sources/` backlinks)
4. **User mentions a concept/entity** — search `wiki/concepts/` and `wiki/entities/` for project associations (e.g., a TCR paper likely belongs to TCRCellNet)
5. **Fallback** — if no project is identifiable, place under `Knowledge/papers/{paper-key}/`

### Output directory convention

```
{project-root}/papers/{paper-key}/
├── paper.md               ← 精读双语全文
├── original.pdf           ← 原始 PDF 副本（如可用）
├── assets/                ← 提取的图表
│   ├── fig1.png
│   ├── fig2.png
│   └── ...
├── source_map.json        ← 稳定的源码锚点映射
└── translation_notes.md   ← 术语、不确定性、版式说明
```

### Paper key naming

Format: `{first-author-lastname}-{year}-{short-descriptive-key}`

Examples:
- `chen-2023-tcr-dominant-phenotype`
- `monian-2021-peanut-oit`
- `afik-2017-trapes`

Rules: all lowercase, hyphen-separated, no special characters. The key should be short enough to type but unique enough to distinguish from other papers.

### Creating the directory

Before generating any output:
1. Determine the project root (e.g., `Knowledge/TCRCellNet/`) and paper key
2. Create `{project-root}/papers/{paper-key}/`
3. Copy the source PDF into this directory (naming it `original.pdf` or keeping the original filename if more informative)
4. Create `assets/` subdirectory inside the paper directory
5. All reading artifacts (`paper.md`, `source_map.json`, `translation_notes.md`, `assets/`) go into this directory

Relative paths in `paper.md` (e.g., `assets/fig1.png`) must be relative to the paper's own directory so the artifact is self-contained and can be moved or shared without breaking links.

---

## Workflow

### 0. Determine project context and output path

Before touching the paper content, establish where the output will live:

1. Identify the project (see "Project-Aware Output Directory" above)
2. Generate a paper key from the first author, year, and topic
3. Verify the target `{project-root}/papers/{paper-key}/` directory does not already exist to avoid overwriting; if it does, append a distinguishing suffix
4. Create the directory structure
5. Copy the source PDF into the paper directory
6. Determine that `assets/` figure paths will be relative to the paper directory
7. **State the output path at the start** so the user can verify before processing begins

### 1. Identify the source and paper type

Determine whether the source is:

- selectable-text PDF
- scanned PDF
- publisher HTML
- DOI or arXiv link
- pasted text or notes

Then identify the paper type at a high level:

- discovery or mechanism paper
- methods or algorithm paper
- resource or dataset paper
- conference paper
- review or perspective

This helps decide how tightly to couple text, figures, and captions.

### 2. Build a full-document source map before translating

If the user provides a full paper, process the entire document. Do not stop at the abstract, introduction, or a few representative pages unless the user explicitly asks for a preview.

Create stable IDs for source blocks:

- `S001`, `S002`, ... for body text
- `C001`, `C002`, ... for captions
- `F001`, `F002`, ... for figures
- `T001`, `T002`, ... for tables

For each block, capture:

- page number
- block type
- original text
- translation
- reading-order index
- nearby figure or table references
- first substantive figure/table mention when applicable
- confidence level when extraction is uncertain

Keep the source map stable so later questions can point back to the same IDs.
For long papers, add a page index so the reader can jump across the whole document without losing location.

### 3. Translate conservatively

Translate every extractable substantive block with these rules:

- preserve technical terms unless a standard Chinese equivalent is clearly better
- keep gene names, protein names, formulas, model names, and symbols intact
- keep citations, superscripts, subscripts, and numeric values unchanged
- do not collapse methods details into vague prose
- keep paragraph order and section order unless the user asks for restructuring
- mark uncertain text instead of guessing when OCR or layout extraction is weak
- keep the source's paragraph form; do not convert dense prose into bullet-point keywords
- do not silently skip Methods, limitations, data availability, code availability, competing interests, or extended captions
- if the paper is too long for one pass, write `paper.md` incrementally by page/section and mark pending blocks rather than switching to summary mode

If a sentence contains multiple claims, keep the translation readable but do not split away the original evidence chain.

### 4. Extract and place figures and tables near the relevant discussion

Do not try to recreate the PDF pixel-for-pixel. Preserve semantic proximity instead.

Default placement rule:

- crop each figure/table into `assets/` and show it near its first substantive mention in the body text
- keep the caption attached to the figure/table
- show both original caption and Chinese caption translation
- if the caption contains critical details, keep caption and figure together
- if a table is central to the claim, keep it near the paragraph that interprets it
- if a figure/table appears before the body discussion in PDF layout, still place it where it best supports the reading flow and add `Placed near: p.X SYYY`
- if a later section mentions the same figure/table again, link back to the already inserted figure/table block instead of duplicating it

If the paper has a complex multi-column layout, prefer a clean reading layout over exact visual mimicry.

### 4b. Crop figures and tables tightly

When extracting a figure or table image:

- crop only the figure or table content area, not the whole page
- use the smallest rectangle that fully contains the visual object
- exclude page headers, footers, surrounding prose, and unrelated margins
- keep the caption separate unless the caption is part of the requested visual crop
- if the crop box is uncertain, mark it as approximate instead of enlarging it

Precision matters more than convenience here. A slightly smaller but correct crop is better than a wider crop that includes unrelated page content.

Figure/table blocks in `paper.md` should use this shape:

```markdown
<a id="F001"></a>
### Fig. 1. [short translated title]

**Placed near:** p.3 S012
**Source:** p.4 C001

![Fig. 1](assets/fig1.png)

**Original caption:** [caption text]

**中文图注:** [caption translation]

---

**🔬 图表解读**

| 面板 | 内容 | 关键发现 |
|------|------|----------|
| A | [面板 A 展示的内容] | [趋势/差异/关键数值] |
| B | [面板 B 展示的内容] | [趋势/差异/关键数值] |
| C | [面板 C 展示的内容] | [趋势/差异/关键数值] |

**📊 统计注释：** [p 值、误差棒、样本量等关键统计信息说明]

**🎯 核心结论：** 该图支持/证明了什么 claim，与正文 S00X 对应

**💡 与课题的关联：** [可选，针对当前项目（如 TCRCellNet）的启发或方法学价值]
```

For tables:

```markdown
<a id="T001"></a>
### Table 1. [short translated title]

**Source:** p.X

![Table 1](assets/table1.png)

**Original caption:** [caption text]

**中文表注:** [caption translation]

---

**🔬 表格解读**

- **行/列含义：** [行列结构说明]
- **关键数据：** [最值得关注的数据行或列]
- **趋势/对比：** [组间差异或相关性趋势]
```

### 4c. Write figure/table interpretations

After placing each figure/table, write a structured interpretation block beneath the caption. This is **not** a summary of the caption — it is an independent reading guide that helps the viewer extract the key message from the visual data.

#### What every figure interpretation must include:

| Field | Content | Example |
|-------|---------|---------|
| **面板解读表** | Per-panel breakdown of what is shown and key observed patterns | "Panel A: RNA UMAP colored by GZMB expression — cytotoxic cells cluster in upper right" |
| **统计注释** | Explain visible statistical elements: p-values, error bars, confidence bands, sample sizes, statistical tests used | "Error bars: SEM; p-values from Wilcoxon rank-sum test; n=12 patients" |
| **核心结论** | One sentence linking the figure back to the paper's main claim, cross-referencing the relevant S block | "该图支持 S009 的 claim：TCR 序列相似性与表型相似性相关" |

#### What every figure interpretation should also consider (when applicable):

- **Unexpected or negative results** visible in the figure
- **Control vs experimental** comparisons
- **Biological/clinical significance** (not just statistical)
- **Multi-panel logic** — how panels build on each other

#### Figure interpretation depth guidelines:

- **Main figures (Fig 1–5)**: Full panel-by-panel interpretation + statistics + core conclusion
- **Supplementary figures**: Shorter treatment — key observations only, no panel-by-panel unless a panel is directly referenced in the main text
- **Graphical abstract**: Brief note on what the schematic conveys
- **Tables**: Row/column structure, key data rows, group comparisons

#### Project-specific connections (optional but encouraged):

If the paper belongs to a known project (e.g., TCRCellNet), add a **💡 与课题的关联** line at the end of the figure interpretation, connecting the figure's methods or findings to the project's research questions.

Default output is a single full-paper `paper.md` file placed at `{project-root}/papers/{paper-key}/paper.md`.

The Markdown must include:

- metadata header
- a short page/section index
- page-level or section-level divisions for long papers
- paragraph-level original/Chinese pairs for all extractable substantive text
- figure and table blocks placed near the relevant discussion, each with:
  - cropped figure/table image
  - original caption + 中文图注/表注
  - **🔬 图表解读** block (panel-by-panel breakdown, statistics, core conclusion)
- source anchors on every substantive text, figure, caption, and table block
- a terminology table for recurring technical terms
- a short `阅读提示` / `critical reading notes` section only after the bilingual body, not as a replacement for it
- short uncertainty notes only when extraction is weak

Do not add an interactive Q&A panel or follow-up widget in the Markdown deliverable. If the user later asks a question, answer it in chat using the source map rather than embedding a conversational panel in the artifact.

If a browser preview is explicitly requested, a companion `reader.html` can be generated as a secondary artifact, but the Markdown file remains the primary output.

### 6. Answer follow-up questions with source grounding

When the user asks a question after the file is created:

- identify the most relevant source blocks first
- answer from the paper, not from memory
- cite the exact block IDs and page numbers
- if the answer depends on a figure or table, cite that too
- if the paper does not support the claim, say so plainly

Every substantive answer should include a source pointer such as:

- `p.4 S012-S013`
- `Fig. 2 caption`
- `Table 1`

If the answer is a synthesis across several blocks, list all supporting locations.

## Output contract

All outputs go into `{project-root}/papers/{paper-key}/`:

- `paper.md` — full-paper Markdown artifact
- `original.pdf` — copy of the source PDF (if available; keep original filename if more informative than a generic `original.pdf`)
- `source_map.json` — stable source anchors
- `translation_notes.md` — terminology, uncertainty, and layout notes
- `assets/` — extracted figures or cropped snippets
- `reader.html` — only when the user explicitly wants a browser preview

Do not hide missing information. If the source is incomplete, label the output as draft mode.

Before final response, verify:

- the paper directory `{project-root}/papers/{paper-key}/` exists and contains all expected files
- `paper.md` contains `**Original:**` and `**中文:**` block pairs
- every image/table link used in `paper.md` uses a **relative** path (e.g., `assets/fig1.png`, not an absolute path)
- every figure/table in `assets/` has a corresponding Markdown block and source pointer in `paper.md`
- every main figure block (Fig 1–5 or equivalent) contains a **🔬 图表解读** section with panel breakdown, statistical notes, and core conclusion
- supplementary figures have at minimum a brief interpretation note
- `source_map.json` parses as JSON and includes source block IDs
- `translation_notes.md` records skipped, uncertain, or draft-mode content
- if the source PDF was available, verify it exists in the paper directory

## Tooling guidance

If the input is a PDF, load the `pdf` skill first for extraction and OCR guidance.
If the user asks for a richer browser view, use `web-artifacts-builder` or `frontend-design` only as a preview layer on top of the Markdown workflow.
If the user wants citation-level grounding to original text, keep the source map explicit and do not lose the page or block IDs.

## Quality bar

Good output feels like a paper reader, not a machine translation dump.

It should let a reader:

- read the paper in two languages
- see where a claim came from
- inspect the nearby figure or table
- move through a complete Markdown file without losing source traceability
