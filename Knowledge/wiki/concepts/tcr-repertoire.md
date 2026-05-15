---
title: TCR Repertoire
tags: [concept, immunology, tcr, repertoire, vdj]
created: 2026-05-06
updated: 2026-05-06
---

# TCR Repertoire（T 细胞受体库）

> T 细胞受体库是体内所有 T 细胞克隆的 TCR 序列总和，反映了免疫系统的历史和当前状态。

---

## TCR 的生成与多样性

### V(D)J 重组
- TCR α 链由 V-J 重组产生，β 链由 V-D-J 重组产生
- 人类 β 链有 64-67 个 V 基因、2 个 J 基因、14 个 D 基因（IMGT 数据库）
- 随机插入和删除（junctional diversity）进一步增加多样性
- 理论多样性 > 10¹³ 种（Katayama 2022）

### CDR 区域
| CDR      | 位置         | 功能                |
| -------- | ---------- | ----------------- |
| CDR1     | V 基因编码     | 与 MHC 接触          |
| CDR2     | V 基因编码     | 与 MHC 接触          |
| **CDR3** | VJ/VDJ 连接区 | **直接接触抗原肽，多样性最高** |

### 双 TCR（Dual TCR）
- 人类是二倍体，α 链有等位排斥机制但约 30% 的 T 细胞表达两种不同的 α 链
- 一个 T 细胞可能有两种不同的 TCR 特异性

---

## 影响 Repertoire 的因素

### 1. 胸腺选择
- **正向选择**：与自身 pMHC 具有中等亲和力的 TCR 被选出 → MHC 限制性建立
- **负向选择**：与自身 pMHC 高亲和力的 TCR 被消除（减少 60-70% 自身反应性 T 细胞）
- 胸腺选择在 TCR 库中留下可检测的序列特征（Luppov 2025）

### 2. MHC 多态性（HLA）
- HLA 基因高度多态，决定了哪些肽能被呈递
- TCR 在胸腺选择中被"个性化"——不同 HLA 类型的个体有不同的 repertoire
- 特定序列与特定 HLA 类型之间存在关联（Emerson 2017）
- 因此，不同个体间即使识别相同抗原的 TCR 也可能不同

### 3. 衰老（Immunosenescence）
- 胸腺随年龄退化 → naïve T 细胞输出减少
- 记忆 T 细胞比例增加 → repertoire 多样性下降
- 慢性感染（如 CMV）加速这一过程
- 幼稚 T 细胞库的多样性降低导致对新抗原的应答能力减弱

### 4. 抗原暴露
- 感染、疫苗接种、肿瘤 → 特异性 T 细胞克隆扩增 → repertoire 重塑
- CMV 暴露会在 TCR 库中留下持久的特征信号（Emerson 2017）
- 记忆 T 细胞库在个体内多年保持稳定

---

## Repertoire 的定量指标

| 指标 | 类型 | 描述 |
|------|------|------|
| Shannon 熵 | 多样性 | 克隆丰度分布的均匀性 |
| Simpson 指数 | 多样性/优势度 | 随机取两个 TCR 相同的概率 |
| Chao1 | 物种丰富度 | 估计未被观测到的 TCR 种类数 |
| 克隆性 (Clonality) | 集中度 | 1 - (标准化 Shannon 熵) |
| Morisita-Horn | 相似性 | 两个 repertoire 之间的重叠度 |
| TCR 重叠率 | 相似性 | 共享 TCR 序列的比例 |

---

## Repertoire 的分析技术

### 测序技术发展
- Sanger 测序（低通量）→ NGS 高通量测序（Illumina）
- 单细胞 TCR-seq：可同时获得 α 和 β 链配对信息
- 多重 PCR 扩增 CDR3 区域
- DNA 水平测序（更定量）vs RNA 水平测序（更灵敏，可捕获全长序列）

### Batch Effect 注意事项
- PCR 引入的扩增偏好（多重引物、序列组成偏差）
- 测序错误（约 2% PCR 扩增子含错误，1-6% NGS 读段有错误）
- 引物对未知 V/J 等位基因的覆盖不足
- 生物信息学后处理（如 MiXCR）可以校正部分偏差

---

## 相关页面

| 类型 | 页面 |
|------|------|
| 概念 | [[wiki/concepts/tcr-epitope-prediction\|TCR-Epitope Binding Prediction]] |
| 概念 | [[wiki/concepts/single-cell-tcr-seq\|Single-cell TCR-seq]] |
| 概念 | [[wiki/concepts/thk-cells\|ThK 细胞]] |
| 来源 | [[wiki/sources/batch-tcr-repertoire-analysis\|TCR Repertoire 文献合集]] |
| 来源 | [[wiki/sources/batch-tcr-epitope-prediction\|TCR 结合预测文献合集]] |

**引用文献**: Katayama 2022, Dash 2017, Emerson 2017, Luppov 2025, Textor 2023, Chiffelle 2020, Isacchini 2021
