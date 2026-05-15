---
title: SCigblast
type: project
status: 进行中
priority: 高
start: 2026-04-28
deadline:
tags:
  - project
description: 项目路径  /data/scAnalyis/Scigblast
---

> [!abstract] 项目简介
> SCigblast 项目说明 — 将10x rawdata 拆解为下游免疫数据形式


---

## ✅ background


![[attachments/Pasted image 20260508145457.png]]

| Species      | Organism or Chain | Gene name | Gene specific Primer name | Partial adaptar(read 2)AT-tail exclude | BC802 & UMI3 | Gene specific Primer sequence | len | Joined sequence_order                                               |
| ------------ | ----------------- | --------- | ------------------------- | -------------------------------------- | ------------ | ----------------------------- | --- | ------------------------------------------------------------------- |
| Homo sapiens | TRD               | TRDC      | HTS_hTRDC_1               | GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT     | NNNAAGCACCG  | AACGGATGGTTTGGTATGAGGC        | 67  | GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCTNNNAAGCACCGAACGGATGGTTTGGTATGAGGC |

---

> bacode ： NNN**AAGCACCG**，位于R2端 拼接后进行反向互补 **CGGTGCTT**
> TSO：TTTCTTATATGGG
## 📝 进度日志

### 2026-05-08

- **今日完成：**
  - 使用 pandaseq 将 R1、R2 进行拼接，然后拆分 barcode 和 UMI
- **遇到的问题：**
  - **R2 端未以 NNN`AAGCACCG` 开头**
    - 总 header 数量：2,175,479
    - 序列中包含 `CGGTGCTT` 的数量：2,124,857（97.5%）
    - 包含 `CGGTGCTT` 但不在后 11 位前 8 位的数量：6,482（0.3%）
    - ![[attachments/52253c64331f38e96fbb8e4efd056ded.png]]
    - ![[attachments/819282ec58152af4d09f51b19342511b.png]]
  - **TSO 位置不固定**
    - 总 header 数量：2,175,479
    - 序列中 target `TTTCTTATATGGG` 在位置 27±0 的数量：1,983,323（91.2%）
    - 包含 target 但不在窗口内的数量：103,056（4.74%），cellranger  **后期抢救**
    - 完全不包含 target 的数量：89,190（4.10%）**筛去**
- **下一步计划：**
  - 根据 TSO 位置拆分：向前 10 位拆 UMI，向前 16 位拆 barcode
    - 将结果组装为 `>#barcode:umi` 格式放入 header 后面
    - 统计：按 barcode 区分细胞作为目录，按 UMI 区分克隆生成 fasta 文件（内容为 header）

### 2026-05-09

- **今日完成：**
  1. **`split_barcode_umi` 脚本开发** — 输出字段定义如下：

     - `sample`: 样本名，由 `SAMPLE_NAME` 指定；若为 None 则从输入 FASTA 文件名自动提取
     - `cell_barcode`: 细胞 barcode 序列，根据 TSO 起始位置向前提取；默认 TSO 前 26-11 bp，共 16 bp
     - `rank`: barcode 排名，按 `umi_count` 降序 → `CB_count` 降序 → `cell_barcode` 升序
     - `CB_count`: 该 barcode 下的 FASTA 记录数，每成功解析到该 barcode 的一条记录计数 +1
     - `umi_count`: 该 barcode 下的唯一 UMI 数，对同一 barcode 下解析到的 UMI 去重后计数

  3. **绘制 barcode rank plot** — 根据脚本输出的 summary 生成可视化
    ![[Pasted image 20260509150625.png]]

- **遇到的问题：**
  -
- **下一步计划：**
  -  分析每个细胞检测到的 reads 数分布
    - 按 cell barcode 统计 UMI 基因数量，配对 δ/γ 链
    - 单独滤出双细胞（两个 barcode 在同一细胞中）
  - 继续优化细胞-UMI 匹配统计