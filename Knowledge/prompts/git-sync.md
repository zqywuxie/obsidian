---
title: Git Sync — 仓库同步
tags: [prompt, maintenance, git, sync]
created: 2026-05-15
updated: 2026-05-15
---

# Git 同步 (Sync)

> 将本地 Obsidian Vault 变更提交并推送到远程 GitHub 仓库。

## 使用场景

当需要对 vault 进行版本控制、备份或与其它设备同步时。可作为周期性操作（如每日/每周一次）。

## 准备条件

- 已配置 SSH 连接 GitHub（`ssh -T git@github.com` 验证）
- 仓库已在本地初始化并连接远程

## 检查

- `.gitignore` 是否覆盖了不需要追踪的文件（session 数据、OS 文件、大文件）
- PDF 文件是否超过 50MB（GitHub 会发警告，100MB 硬限制）

## 推荐 .gitignore 配置

```
# Obsidian
.obsidian/workspace.json
.obsidian/workspace
.obsidian/cache/
.obsidian/plugins/obsidian-git/data.json

# Claude session data
.claudian/sessions/

# Obsidian Trash
.trash/

# OS files
Thumbs.db
.DS_Store
Desktop.ini
```

## Prompt

```
## 操作流程

### 步骤 1：检查状态
```bash
git status
```

### 步骤 2：检查暂存区差异
```bash
git diff --cached --stat | tail -5
```
确认提交大小合理（无意外的大文件）。

### 步骤 3：暂存变更
```bash
git add -A
```
注意检查新增的文件是否需要添加到 .gitignore。

### 步骤 4：提交变更
```bash
git commit -m "$(cat <<'EOF'
<简短描述提交内容>
EOF
)"
```

### 步骤 5：推送到远程
```bash
git push origin <branch-name>
```

## 提交信息规范

- 概括变更类型（新笔记、更新、重构、配置等）
- 简述涉及的内容范围（如"更新 3 篇文献笔记，新增 1 个概念页面"）
- 如涉及结构变更，在 commit body 中说明

## 首次初始化（新仓库）

```bash
git init
git remote add origin git@github.com:<user>/<repo>.git
# 创建 .gitignore
git add -A
git commit -m "Initial sync of Obsidian vault"
git push -u origin master
```

## 注意事项

- 大文件处理：超过 50MB 的文件会触发 GitHub 警告，超过 100MB 会推送失败。考虑使用 Git LFS 或排除此类文件的追踪
- 敏感数据：检查 `.claudian/sessions/`、API key 等是否被排除
- 嵌套仓库：如果 vault 中嵌入了其它 git 仓库（如 skill 模板），它们会以 gitlink 形式被追踪，不影响主仓库
