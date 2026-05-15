---

## 一、Figure 1：人肠道炎症中 GZMK⁺ CD4⁺ T 细胞亚群的鉴定

### Fig. 1a — scRNA-seq 发现 GZMK^high 细胞群

**实验类型**：公共数据重分析（生物信息学）

**步骤**：
1. **数据来源**：获取已发表的 IBD 患者 scRNA-seq 整合数据集（Nie et al. 2023, scIBD），包含 UC、Crohn 病及健康对照
2. **样本来源**：小肠、结肠、外周血和淋巴结
3. **分析流程**：对全部 CD4⁺ T 细胞进行 UMAP 降维聚类，检测经典 TH 亚群标志基因的表达（SELL, CCR7, TBX21, IFNG, GATA3, IL4, RORC, IL17A, BCL6, CXCR5, FOXP3, IL2RA）
4. **关键发现**：存在一群高表达 GZMK 但不表达经典谱系标志基因的 CD4⁺ T 细胞，且 GZMB 表达极低
5. **可视化**：使用 Nebulosa 包的 gene expression density plot（UMAP 密度图）

---

### Fig. 1b — GZMK 在活动期 UC 患者中显著升高

**实验类型**：公共 bulk RNA-seq 数据分析

**步骤**：
1. **数据来源**：GSE128682（黏膜活检 bulk RNA-seq）
2. **分组**：活动期 UC（n = 14）、缓解期 UC（n = 14）、健康对照（n = 16）
3. **分析**：比较各组间 GZMK 转录水平
4. **统计**：one-way ANOVA + Tukey 多重比较检验

> 另见：Extended Data Fig. 1（泛癌 scRNA-seq 数据中也存在 GZMK^high CD4⁺ T 细胞群）

---

### Extended Data Fig. 2 — 报告小鼠的系统鉴定（Gzmk 在稳态组织中的表达图谱）

**逻辑位置**：Fig 2a-c（生信发现 Gzmk^high cluster）→ **ED Fig. 2**（鉴定新构建的报告小鼠 + 建立稳态表达基线）→ Fig 2d-g（结肠炎诱导验证）

**为什么要做这个实验？**
论文的逻辑链是这样走的：

1. Fig 2a-c 的 scRNA-seq 分析用了**已发表公共数据集**的结肠炎小鼠数据 → 看到 Gzmk^high cluster → 但这是别人的数据，需要用自己的实验系统来验证
2. 所以构建了 Gzmk-tdTomato 报告小鼠，**第一步先看稳态（没发炎时）全肠道表达情况**
3. 关键发现是 **结肠在稳态下几乎没有 Gzmk⁺ CD4⁺ T 细胞** → 这为后续问题铺路：结肠炎是否会在结肠中诱导出 Gzmk⁺ CD4⁺ T 细胞？

**那为什么把小肠数据也放进来？**
不是因为小肠多重要，而是**既然已经做了全面扫描，就全部展示**——也正好说明 Gzmk 在其他肠道部位（小肠）的 T 细胞中是有正常表达的，报告系统是灵敏的，唯独结肠 CD4⁺ T 细胞在稳态下缺乏 Gzmk。

**简单概括：**
- 小肠数据：顺便做的，显示报告系统能检测到信号
- **结肠数据：核心发现——稳态下结肠 CD4⁺ T 细胞没有 Gzmk**
- 这个负结果才是 ED Fig 2 的关键信息，为 Fig 2d 的结肠炎实验提供了"零基线"

**实验类型**：报告小鼠的表型鉴定（Phenotypic characterization）

**步骤**：
1. **小鼠**：Gzmk-tdTomato 报告小鼠（未做任何处理，即 steady-state，n = 5）
2. **组织取材**：分别取以下 6 个解剖部位：
   - 小肠上皮内淋巴细胞（SI-IEL）
   - 小肠固有层淋巴细胞（SI-LPL）
   - 大肠上皮内淋巴细胞（LI-IEL）
   - 大肠固有层淋巴细胞（LI-LPL）
   - 派尔氏结（Peyer's Patches, PP）
   - 肠系膜淋巴结（mLN）
3. **淋巴细胞分离**：各组织按标准方法（EDTA/DTT 去上皮 → 胶原酶消化 → Percoll 梯度）分离淋巴细胞
4. **流式检测**：用抗-CD4、抗-CD8α、抗-CD8β、抗-TCRγδ 抗体标记，分析各 T 细胞亚群中 tdTomato 信号的比例
5. **结果**：
   - tdTomato 信号在小肠 IEL/LPL 的 CD4⁺、CD8α⁺、CD8β⁺、γδT 细胞中均可检测到 → **确认报告小鼠正常工作**
   - 结肠 IEL/LPL 及 mLN 中 Gzmk-tdTomato⁺ CD4⁺ T 细胞罕见 → **稳态基线已建立**

**承上启下的作用**：
- **承上**：Fig 2a-c 的 scRNA-seq 数据来自**已发表的结肠炎公共数据集**，此时需要自己的实验系统来验证 → 因此构建 Gzmk-tdTomato 报告小鼠
- **启下**：稳态下结肠中 Gzmk⁺ CD4⁺ T 细胞罕见 → 提出关键问题：**结肠炎是否会诱导 Gzmk 在结肠 CD4⁺ T 细胞中表达？** → 引出 Fig 2d 的过继转移结肠炎实验

> 逻辑链：公共数据集看到 Gzmk^high cluster（2a-c）→ 鉴定报告小鼠：确认正常工作 + 稳态结肠无 Gzmk（ED Fig 2）→ 诱导结肠炎看是否会诱导表达（2d-g）→ 确认炎症诱导 ~20% Gzmk⁺ 且不表达经典转录因子（2d）→ 定义为 THK 细胞

---

## 二、Figure 2：小鼠结肠炎中 Gzmk⁺ CD4⁺ T 细胞的特征

### Fig. 2a-c — 小鼠结肠炎 scRNA-seq 分析

**实验类型**：公共数据整合分析（生物信息学）

**步骤**：
1. **数据来源**：整合两个独立数据集 CRA016814 和 GSE235664（Bai et al. 2024; Li et al. 2024）
2. **模型**：Rag1⁻/⁻ 小鼠过继转移 naive CD4⁺ T 细胞诱导的结肠炎模型
3. **分析**：仅取 WT 细胞 → Seurat 标准流程 → Harmony 去除批次效应 → UMAP 聚类
4. **结果**：获得 6 个转录组学不同的亚群，其中 cluster 1 高表达 Gzmk，其他谱系标志基因低表达

---

### Fig. 2d — 流式验证 Gzmk⁺ CD4⁺ T 细胞

**实验类型**：过继转移结肠炎模型 + 流式细胞术

**步骤**：
1. **小鼠准备**：Gzmk-P2A-CreERT2-T2A-tdTomato（Gzmk-tdTomato）报告小鼠
2. **分选 naive CD4⁺ T 细胞**：从供体鼠脾脏和淋巴结分离 CD4⁺ T 细胞，经 FACS 分选纯化 CD4⁺CD25⁻CD44^loCD62L^hi naive T 细胞（纯度 > 98%）
3. **过继转移**：1.5-2 × 10⁶ 个分选的 naive T 细胞经尾静脉注射入 8-12 周龄雄性 Rag1⁻/⁻ 受体小鼠
4. **时间**：约 4 周后（或其他指定时间点）处死小鼠，收集结肠组织和 mLN
5. **结肠淋巴细胞分离**：
   - 结肠纵向切开 → 含 5 mM EDTA + 1 mM DTT 的 RPMI 1640 中 37°C 震荡 30 min 去上皮
   - 剪碎至 ~2 mm → 含 0.5 mg/ml 胶原酶 D + 1 mg/ml 分散酶 + 4 μg/ml DNase I 的 RPMI 中 37°C 轻柔震荡消化 30 min
   - 过 100 μm 滤网 → 37% / 70% Percoll 梯度离心 → 收集界面淋巴细胞
6. **流式染色**：
   - 先染 Fixable Viability Dye eF506 死活染料 + CD16/CD32 封闭
   - 表面染色 → FOXP3/转录因子染色缓冲液固定破膜 → 核内抗体染色（T-bet, GATA3, RORγt, BCL6, FOXP3）
   - 检测荧光蛋白信号时先用 2% PFA 固定 20 min 再破膜
7. **检测**：LSRFortessa 流式仪检测，FlowJo v10.9.0 分析
8. **结果**：
   - **Fig 2d（LP）+ ED Fig 3a（mLN）**：同一批实验的两个组织部位。约 20% 的 LP 和 mLN CD4⁺ T 细胞呈 tdTomato 阳性；Gzmk-tdTomato⁺ 细胞极少表达或不表达 T-bet、GATA3、RORγt、BCL6、FOXP3 → 定义为 **THK 细胞**

---

### Fig. 2e-g — THK 细胞效应分子特征（同批实验的 LP 数据；mLN 见 ED Fig 3b-d）

**实验类型**：同上模型的流式分析

**具体方法**：
- 细胞处理同 Fig. 2d
- 使用抗-Perforin-APC、抗-GZMB-BV785、抗-IFNγ-AF700 抗体
- 胞内细胞因子检测需先 PMA（50 ng/ml）+ Ionomycin（500 ng/ml）+ GolgiStop 刺激 4.5 h
- **结果**：

| 分图 | 组织 | ED Fig 对应 | 结果 |
|------|------|------------|------|
| e | LP | ED Fig 3b（mLN） | 大多数 Perforin⁺ CD4⁺ T 细胞为 Gzmk-tdTomato⁺ |
| f | LP | ED Fig 3c（mLN） | Gzmk-tdTomato⁺ 和 GZMB⁺ 仅小部分重叠 |
| g | LP | ED Fig 3d（mLN） | IFNγ MFI 在 Gzmk-tdTomato⁺ 中略低于 Gzmk-tdTomato⁻ |

**结论**：
1. **THK 有杀伤潜力但不特异**：表达 Perforin（大多数 Perforin⁺ CD4⁺ T 是 THK），但 ED Fig 3f-g 体外杀伤实验显示 Gzmk⁺ 和 Gzmk⁻ CD4⁺ T 细胞在有 anti-CD3 时杀伤能力相当 → 杀伤功能不是 THK 特有的
2. **THK 不是经典 cytotoxic CD4⁺ T**：GZMB 低表达（仅小部分重叠），与典型 GZMB⁺ 杀伤性 CD4⁺ T 不同
3. **IFNγ 产量低**：虽然部分 THK 产 IFNγ，但 MFI 低于 Gzmk⁻ 群体中的 IFNγ⁺ 细胞（TH1）
4. **ED Fig 3e scRNA-seq**：Gzmk 和 Prf1 主要限于 cluster 1（THK），而 Gzmb 和 Ifng 在各簇中广泛分布 → 从转录组确认 THK 的核心效应分子是 **Gzmk + Prf1**，而非 GZMB 或 IFNγ

### ED Fig 3f-g — 体外杀伤实验（功能验证）

**这一组实验的叙事逻辑**：

1. **Fig 2e-g（流式表型）**：看 THK 是否表达经典效应分子 → Perforin 部分阳性、**GZMB 低、IFNγ 低**
2. **ED Fig 3e（转录组确认）**：Gzmk 和 Prf1 高度集中于 cluster 1（THK），而 Gzmb 和 Ifng 广泛分布 → 确认 **Gzmk 和 Prf1 是 THK 的核心效应分子**
3. **既然知道 Gzmk+Prf1 是效应分子，为什么还要做杀伤验证？** →
   - 表达杀伤分子（Gzmk, Prf1）**不等于**这些细胞在功能上真的能杀伤靶细胞 → 需要功能实验确认
   - 但更重要的是：**THK 的杀伤是独有的吗？** → 对比 Gzmk⁻ CD4⁺ T 细胞（非 THK）能不能杀
   - **如果 Gzmk⁻ 也能杀** → 说明杀伤不是 THK 的特殊功能 → 引出后续问题：GZMK 的真正功能是什么？
   - 为后文 Fig 6（Gzmk KO 不减轻疾病）埋下伏笔：GZMK 在体内的致病作用不是通过直接杀伤

**实验类型**：体外细胞毒性实验

**步骤**：
1. **效应细胞**：从结肠炎小鼠 LP 中分选出 Gzmk-tdTomato⁺ 和 Gzmk-tdTomato⁻ CD4⁺ T 细胞
2. **靶细胞**：肥大细胞瘤细胞系 P815（CFSE 标记）
3. **共培养**：效应细胞 + 靶细胞 + 可溶性 anti-CD3（0 或 1 μg/ml），不同效靶比（E:T ratio），19 h
4. **检测**：Fixable Viability Dye eF506 流式检测死 P815 比例

**结果与解读**：

| 分图 | 角色 | 发现 | 解读 |
|------|------|------|------|
| **ED Fig 3f** | **质控** | 共培养 19 h 后，分选的 Gzmk⁺ 仍保持阳性、Gzmk⁻ 仍保持阴性 | 排除培养过程中 Gzmk 表达变化 → 确认分组有效，后续杀伤数据可信 |
| **ED Fig 3g** | **功能结果** | 有 anti-CD3 时 Gzmk⁺ 和 Gzmk⁻ 杀伤能力**相当**；无 anti-CD3 均不杀伤 | THK **能**杀伤，但 **Gzmk⁻ CD4⁺ T 也能杀伤，能力相当** |

**结论**：
- THK 能杀伤，但这不新鲜（Gzmk⁻ 细胞也做得到）
- 真正的问题被提出来了：**如果 GZMK 的功能不是独特的杀伤，那它在体内做什么？** → 后文 Fig 6（Gzmk KO 不减轻疾病）暗示 GZMK 可能通过胞外蛋白酶解促炎（切割补体、激活 PAR-1），而非直接杀伤

---

## 三、Figure 3：THK 分化独立于 TH1/TH2/TH17

### Fig. 3a-c — Tbx21 缺失实验

**实验类型**：共转移结肠炎模型 + 流式 + RT-qPCR

**步骤**：
1. **共转设计**：WT (CD45.1) + Tbx21⁻/⁻ (CD45.2) naive CD4⁺ T 细胞 1:1 混合 → 尾静脉注射入 Rag1⁻/⁻ 受体
   - **操作目的**：同一小鼠体内比较，排除个体差异（cell-intrinsic comparison）
2. **4 周后**：取 LP 和 mLN → 流式检测 GZMB 和 Perforin（使用 CD45.1/CD45.2 区分 donor 来源）
3. **RT-qPCR**：分选 CD45.1⁺ 和 CD45.2⁺ CD4⁺ T 细胞 → TRIzol 提取 RNA → 测浓度纯度 → HiScript III 反转录 → SYBR Green 低 ROX 定量 PCR（引物：Gzmk, Prf1, Gzmb, Actb 为内参）
4. **结果**：T-bet 缺失导致 GZMB 减少，但 Perforin⁺ 细胞频率↑，Gzmk mRNA 表达不变 → THK 不依赖 TH1

---

### Fig. 3d-e — Stat6 缺失实验

**实验类型**：同上的共转移模型

**步骤**：
1. WT (CD45.1) + Stat6⁻/⁻ (CD45.2) naive CD4⁺ T 细胞共转 Rag1⁻/⁻
2. 4 周后流式检测 Perforin + RT-qPCR 测 Gzmk
3. **结果**：Stat6 缺失不影响 Gzmk 和 Perforin 表达 → THK 不依赖 TH2

---

### Fig. 3f-g — RORγt 缺失实验

**实验类型**：同上的共转移模型

**步骤**：
1. WT (CD45.1) + Cd4cre Rorc^fl/fl (CD45.2) naive CD4⁺ T 细胞共转 Rag1⁻/⁻
2. 分选后 RT-qPCR 测 Gzmk（f）+ 流式检测 Perforin（g）
3. **结果**：RORγt 缺失后 Gzmk 和 Perforin↑ → RORγt 可能抑制 THK 分化

---

### 额外相关实验（Extended Data Fig. 4-5）

- **Bcl6 缺失**：Cd4cre Bcl6^fl/fl → Gzmk 和 Prf1 表达降低 → 提示 THK 可能来源于 Bcl6⁺ 前体细胞
- **Runx3 缺失**：Vav1cre Runx3^fl/fl → Gzmk 表达不变 → THK 不同于 CD4⁺CD8⁺ 细胞毒性 T 细胞

---

## 四、Figure 4：Eomes 与 THK 身份的转录和表观遗传关联

**⚠️ 注意 Fig 4 的结构（鼠→人→鼠）：**
作者在鼠模型中找到 Eomes 后，**先跳到人类数据验证这个发现不是鼠特有的（4d-e）**，确认跨物种保守性后才回到小鼠体系做深入的机制研究（4f-m）。这样安排是为了说明：EOMES-THK 关联具有**临床相关性**，不只是一个鼠类现象。

```
4a-c（鼠 THK 中找到 Eomes）→ 4d-e（人数据确认 GZMK-EOMES 共表达）
→ 4f（鼠蛋白水平确认）→ 4g-j（鼠 KO 看 EOMES 调控网络）
→ 4k-m（鼠 ATAC-seq 表观遗传机制）
```

### Fig. 4a — THK vs non-THK 的 bulk RNA-seq

**实验类型**：流式分选 + RNA-seq

**步骤**：
1. **分选**：从结肠炎小鼠（Gzmk-tdTomato 报告鼠 + Rag1⁻/⁻ 过继转移模型）的 LP 中分选 Gzmk-tdTomato⁺ 和 Gzmk-tdTomato⁻ CD4⁺ T 细胞
2. **RNA 提取**：PMA + Ionomycin 刺激 2 h → TRIzol 提取总 RNA
3. **建库测序**：VAHTS Universal V10 RNA-seq Library Prep kit → DNBSEQ-T7 平台，150 bp PE，约 20 M raw reads/样本
4. **分析**：fastp 质控 → HISAT2 比对 mm39 → featureCounts 定量 → DESeq2 差异分析 → 定义 top 100 DEGs 为 "THK cell signature"
5. **结果**：Eomes 是 THK 中最显著上调的转录因子之一（log₂FC 高，adj.P < 0.05）

---

### Fig. 4b — THK signature 富集评分

**方法**：用 AddModuleScore (Seurat) 对 scRNA-seq 各簇计算 THK signature 富集分数 → cluster 1 (THK) 分数最高

---

### Fig. 4c-d — Gzmk 和 Eomes 共表达（跨物种对比）

**方法**：
- **4c（鼠）**：UMAP feature plot 展示鼠结肠炎 scRNA-seq 中 Gzmk 和 Eomes 几乎一致的表达模式
- **4d（人）**：Density plot 展示人 IBD scRNA-seq 数据（scIBD，同 Fig 1a）中 GZMK 和 EOMES 的共表达

**目的**：确认 EOMES-GZMK 共表达在人和鼠之间是保守的

---

### Fig. 4e — GZMK-EOMES 表达相关性（人类数据）

**方法**：GSE128682（**人** UC 患者 + 健康对照黏膜活检 bulk RNA-seq，与 Fig 1b 同一数据集）中 Pearson 相关性分析 → R² = 0.953, P < 0.001（EOMES 是 GZMK 相关性最强的基因）

---

### Fig. 4f — EOMES 蛋白水平的流式共表达

**步骤**：
1. Gzmk-tdTomato 报告鼠结肠炎模型 LP 和 mLN CD4⁺ T 细胞
2. 抗-EOMES-eFluor 450 染色（破核膜染色）
3. 检测 Gzmk-tdTomato × EOMES 双阳性细胞

---

### Fig 4a-f 小结：三个层面验证 EOMES-GZMK 关联

| 层面 | 分图 | 方法 | 证据 |
|------|------|------|------|
| **① 转录组统计** | **4a** | bulk RNA-seq DEG 分析 | Eomes 是 Gzmk⁺ vs Gzmk⁻ 中上调最显著的 TF 之一 |
| | **4b** | signature enrichment | THK signature 特异性富集于 scRNA-seq cluster 1 |
| | **4e** | Pearson 相关性（人） | GZMK-EOMES R² = 0.953，定量确认共表达关系 |
| **② 降维可视化** | **4c** | UMAP feature plot（鼠） | Gzmk 和 Eomes 在单细胞层面几乎完全重叠 |
| | **4d** | density plot（人） | 跨物种验证同样的共表达模式 |
| **③ 蛋白质层面** | **4f** | 流式双染 | Gzmk-tdTomato 和 EOMES 蛋白在同一细胞中共表达 |

**结论**：EOMES 与 GZMK 在转录组差异、单细胞空间分布、蛋白质表达三个层面均呈现高度一致性，EOMES 是驱动 THK 细胞身份的最强候选转录因子。

---

### Fig. 4g-j — 不同 KO 背景下的 EOMES 表达

**方法**：同 Fig. 3 的共转移模型，流式检测各 KO 背景中 EOMES 的表达：

| 分图 | KO 基因 | EOMES 表达变化 | 结论 |
|------|---------|---------------|------|
| g | Tbx21⁻/⁻ | 不变 | EOMES 不依赖 T-bet |
| h | Stat6⁻/⁻ | 不变 | EOMES 不依赖 STAT6 |
| i | Cd4cre Rorc^fl/fl | ↑ | RORγt 抑制 Eomes |
| j | Cd4cre Bcl6^fl/fl | ↓ | Bcl6 支持 Eomes 表达 |

---

### Extended Data Fig. 6e — THK 细胞出现的时间动力学（自产数据）

**逻辑位置**：Fig 4g-j 已证明 EOMES 的表达不受 T-bet/STAT6/RORγt 调控 → 那么 THK 细胞在结肠炎过程中**什么时候出现**？与 TH1/TH17 的出现时间有何不同？

**实验类型**：同一结肠炎模型的不同时间点流式分析

**步骤**：
1. **模型**：Gzmk-tdTomato 报告鼠 naive CD4⁺ T → Rag1⁻/⁻（同 Fig 2d）
2. **时间点**：过继转移后第 7、14、21、28、35 天分别处死小鼠（每个时间点 n=3）
3. **检测**：流式检测 LP 和 mLN 中 EOMES、Gzmk-tdTomato、T-bet、RORγt 的表达

| 细胞群 | 第 7 天 | 第 14 天 | 3-4 周 |
|--------|---------|---------|--------|
| EOMES⁺Gzmk-tdTomato⁺ THK | 几乎检测不到 | 开始出现 | 频率稳定 |
| T-bet⁺ TH1 | **已存在** | — | — |
| RORγt⁺ TH17 | **已存在** | — | — |

**结论**：THK 是**晚期出现的效应细胞**，不同于 TH1/TH17 这类早期应答细胞 → 暗示 THK 可能参与慢性炎症的维持而非急性启动

---

### Fig. 4k-m — ATAC-seq 表观遗传学分析

**实验类型**：Bulk ATAC-seq + 整合分析

**步骤**：
1. **分选**：同上，分选约 100,000 细胞/样本
2. **建库**：Hyperactive ATAC-Seq Library Prep kit → Illumina NovaSeq X Plus，150 bp PE，约 40 M raw reads/样本
3. **分析流程**：
   - fastp 质控 → Bowtie2 比对 mm39（参数：--very-sensitive, -X 2000）
   - Picard 去 PCR 重复 → 去线粒体 + ENCODE blacklist
   - MACS2 峰 calling（BAMPE 模式, q = 0.01）
4. **差异分析**：DiffBind 鉴定差异可及峰
5. **基序富集**：HOMER 比较 Gzmk⁺ ↑ vs ↓ 峰
6. **基因-峰关联**：DEG 的 TSS ± 100 kb 内找同向 DAR
7. **结果**：
   - k：THK 基因（Eomes, Gzmk, Prf1, Cd27, Ccl5, Klrg1, Il10ra, Nr4a2, Nkg7, Il10, Ccr5, Slamf7）开放增加；其他谱系基因（Rorc, Il17a, Il17f 等）开放减少
   - l：Eomes 基因座在 Gzmk⁺ 细胞中转录增高 + 染色质可及性增强
   - m：T-box 基序（含 Eomes）在 Gzmk⁺ 开放区富集；ROR/RORγt、Bcl6、GATA 基序在 Gzmk⁻ 开放区富集

**结论**（这一组实验回答的是：EOMES-THK 关联是否有表观遗传层面的支持？）：
- **4k** → THK 的转录组差异（4a RNA-seq）有对应的**表观遗传基础**——RNA 上调的基因，其周围染色质也是开放的；下调的基因，染色质也是关闭的。说明 THK 程序不是瞬时转录波动，而是有**稳定的表观遗传编程**。
- **4l** → Eomes 基因座在 THK 细胞中**同时具备开放染色质和活跃转录**，确认 EOMES 自身也是这个表观编程的一部分。
- **4m** → **T-box（EOMES）基序在 THK 特异性开放区中富集**，提示 EOMES 可能直接结合并塑造 THK 的调控景观（→ 为 Fig 5f CUT&Tag 直接验证做铺垫）。对比之下，其他谱系基序（RORγt、Bcl6、GATA）在 Gzmk⁻ 开放区富集，与 Gzmk⁻ 中这些谱系仍有表达的观察一致。



## 五、Figure 5：EOMES 驱动 THK 程序并抑制其他 TH 命运

### Fig. 5a-c — Eomes 过表达 RNA-seq

**实验类型**：逆转录病毒过表达 + bulk RNA-seq + GSEA

**步骤**：
1. **载体构建**：小鼠 Eomes 编码序列克隆入 RVKM 逆转录病毒载体（含 IRES-BFP 报告基因），C 端加 G₄S 连接子 + HA 标签
2. **病毒包装**：Eomes-RVKM + pCL-ECO 共转染 293T 细胞（磷酸钙法）→ 48 h 后收集病毒上清
3. **T 细胞活化**：分选 naive CD4⁺ T 细胞 → plate-bound anti-CD3 (5 μg/ml) + anti-CD28 (5 μg/ml) 活化
4. **感染**：TH0 条件（anti-IFNγ 10 μg/ml + anti-IL-4 10 μg/ml）下活化 24 h → 加病毒上清
5. **培养**：感染后 24 h 换液继续培养 4 天
6. **分选 + RNA-seq**：分选 BFP⁺ 细胞 → RNA-seq（同 Fig. 4a 流程）
7. **GSEA**：clusterProfiler (fgsea 算法) 验证 THK signature 富集
8. 定义 "Eomes OE UP signature"（top 100 上调基因）→ 对比 scRNA-seq 各簇 → cluster 1 富集最高

**RNA-seq 关键结果**：
- Gzmk 和 Prf1 是最显著上调的基因
- Tbx21 被抑制（说明不是 TH1 程序）
- Rorc, Il5, Il4, Il13 显著下调

---

### Fig. 5d-e — 流式验证

**方法**：同上 Eomes 过表达体系 → 第 5 天流式检测

| 标志物 | Control | Eomes OE |
|--------|---------|----------|
| Gzmk-tdTomato⁺ | ~0.17% | ~30.4% |
| Perforin⁺ | ~0.22% | ~34.3% |

---

### Fig. 5f — CUT&Tag 验证 EOMES 直接结合

**实验类型**：CUT&Tag（Cleavage Under Targets & Tagmentation）

**步骤**：
1. **样本**：HA-tagged EOMES 过表达 CD4⁺ T 细胞（非极化条件培养 5 天），3 个生物学重复
2. **实验流程**：Hyperactive Universal CUT&Tag Assay kit + 抗-HA 抗体（Cell Signaling #3724），按说明书操作
3. **测序**：Illumina NovaSeq X Plus，150 bp PE，约 20 M reads/样本
4. **分析**：同 ATAC-seq 流程（fastp → Bowtie2 → 去重 → 过滤）→ MACS2 峰 calling → 3 重复 consensus → ChIPseeker 注释
5. **可视化**：IGV 展示 Gzmk 和 Prf1 位点的 EOMES 结合峰 + 对应 ATAC-seq 可及性
6. **结果**：EOMES 在 Gzmk 和 Prf1 基因座有强结合信号

---

### Fig. 5g — EOMES CUT&Tag ∩ ATAC-seq 韦恩图

**整合结果**：
- 5,880 个 EOMES 结合峰中：
  - 662 个与 Gzmk⁺ 开放增加区重叠（靠近 THK 基因：Gzmk, Prf1, Nkg7, Klrg1, Tox, Ccl3/4/5, Ifng, Il10）
  - 仅 66 个与 Gzmk⁺ 开放减少区重叠（靠近 Ccr6, Gata3）

---

### 额外实验：Eomes OE 对极化条件的影响（Extended Data Fig. 7）

这组分图回答两个递进的问题：

#### 问题 1：经典极化条件能诱导 THK 吗？（ED Fig 7c）

**方法**：取 Gzmk-tdTomato 报告鼠 naive CD4⁺ T → 分别在 TH1/TH2/TH17/Treg 体外极化条件 + 体内 TFH 模型（OT-II+OVA）下培养 → 流式双染（X 轴：Gzmk-tdTomato，Y 轴：EOMES）

**结果**：全部阴性 → **THK 不需要也不由经典极化信号产生**（与 Fig 3 结论一致）

#### 问题 2：如果强行让 Eomes 表达，它能否压制其他谱系的极化程序？（ED Fig 7d-i）

**方法**：Eomes OE（逆转录病毒）→ 再放入 TH1/TH2/TH17/Treg 极化条件 → 流式检测各谱系标志物

| 分图 | 极化条件 | 细胞因子/抗体 | Eomes OE 效果 |
|------|---------|--------------|-------------|
| d | TH1 | anti-IL-4 + mIL-12 | **T-bet ↓** |
| e | TH2 | anti-IFNγ + IL-4 + mIL-2 | **GATA3 轻度↓** |
| f-g | TH17 | TGF-β + IL-6 + IL-1β + IL-23 + anti-IFNγ + anti-IL-4 | **RORγt ↓↓, IL-17A ↓↓** |
| h | Treg | mIL-2 + TGF-β + anti-IFNγ + anti-IL-4 | **FOXP3 ↓↓** |
| i-j | TFH（体内） | OT-II + OVA+CFA 免疫，第 7 天分析 | **PD-1⁺CXCR5⁺ ↓, BCL6⁺CXCR5⁺ ↓** |

**结论**：EOMES **足以压制其他谱系的极化程序**，即使在强极化条件下也能将细胞拉向 THK 命运。

**额外机制提示（ED Fig 7k）**：EOMES⁺ CD4⁺ T 细胞高表达 BLIMP1（BLIMP1-EYFP 报告鼠），而 BLIMP1 是 BCL6 的拮抗因子 → 解释了为什么 Eomes OE 抑制 TFH（BCL6 依赖）。

---

## 六、Figure 6：Eomes 对 THK 分化和肠道炎症是必需的

### Fig. 6a-c — Eomes cKO 的 bulk RNA-seq

**实验类型**：条件性敲除 + RNA-seq

**步骤**：
1. **小鼠**：Cd4cre Eomes^fl/fl（Eomes cKO）（注：此处**未杂交** Gzmk-tdTomato，用 CD45.1/CD45.2 区分 donor，因为做的是 RNA-seq 而非流式）
2. **共转移模型**：Eomes cKO (CD45.2) + WT (CD45.1) naive CD4⁺ T 细胞共转 Rag1⁻/⁻
3. **4 周后分选**：从 LP 分选 CD45.1⁺ 和 CD45.2⁺ CD4⁺ T 细胞分别做 RNA-seq
4. **差异分析**：Eomes cKO vs WT → Gzmk, Prf1, Nkg7, Slamf7 等 THK 基因显著下调
5. **GSEA**：THK signature 在 Eomes cKO 中显著负富集（NES = -2.01, adj.P < 0.001）
6. **"Eomes cKO DOWN signature"** → scRNA-seq 的 cluster 1 (THK) 中富集最高

---

### Fig. 6d — 四维整合鉴定 EOMES 直接靶基因

**整合四组数据**：
1. Gzmk-tdTomato⁺ 上调基因（Fig. 4a RNA-seq）
2. Eomes OE 诱导基因（Fig. 5a RNA-seq）
3. Eomes cKO 下调基因（Fig. 6a RNA-seq）
4. EOMES CUT&Tag 结合基因（Fig. 5f）

**结果**：**18 个高置信度直接靶基因**，包括：
> Ccl3, Ccl4, Ccr5, Eomes, Gzmk, Il10, Nkg7, Prf1
> （另含：Gzma, Gzmb, Prdm1, Ccl5, Havcr2, Ikzf3, Nr4a2, Slamf7）

---

### Fig. 6e — 反向整合（抑制方向）

**整合**：Eomes OE 下调 ∩ Gzmk-tdTomato⁻ 上调 ∩ Eomes cKO 上调 ∩ EOMES binding → **仅 3 个基因**
- 说明谱系相关基因（Rorc, Ahr, Il13, Csf2, Foxp3）主要是间接调控，非 EOMES 直接抑制

---

### Fig. 6f-h — Eomes cKO 减轻结肠炎疾病严重度

**实验类型**：疾病表型分析

**步骤**：
1. **过继转移**：分别用 Eomes cKO 或对照 Eomes^fl/fl naive CD4⁺ T 细胞转移入 Rag1⁻/⁻（每组 n = 6）
2. **体重监测**：每周记录，持续 5 周
3. **结肠长度**：终点时测量
4. **组织学**：
   - 远端结肠 4% PFA 固定 → 石蜡包埋 → 5 μm 切片 → H&E 染色
   - 盲法组织学评分（0-4 分制，基于炎症细胞浸润、肠壁增厚、隐窝和杯状细胞丢失）
5. **统计**：体重用 two-way ANOVA + Bonferroni；结肠长度和组织学用 two-tailed unpaired t-test

**结果**：
- f：Eomes cKO 组体重减轻显著减轻（P = 0.0108）
- g：结肠更长（P < 0.0001）
- h：组织学评分显著降低（P = 0.0119）

---

### Fig. 6i — 细胞计数

**方法**：计数 LP 中 donor 来源 CD4⁺ T 细胞总数
**结果**：Eomes cKO 与对照组无显著差异（P = 0.2695）→ Eomes 缺失不影响 T 细胞扩增或组织归巢

---

### Fig. 6j-l — 流式检测效应分子

**方法**：流式检测 LP 中 donor CD4⁺ T 细胞：

| 标志物 | 变化 | P 值 |
|--------|------|------|
| j: Gzmk-tdTomato⁺ | ~14.4% → ~0.81%（几乎消失） | 0.0003 |
| k: Perforin⁺ | ~5.16% → ~1.15% | 0.0020 |
| l: GZMB⁺ | ~19.3% → ~12.3% | 0.0208 |

---

### 额外实验：Eomes cKO 的广泛影响 + Gzmk KO（Extended Data Fig. 9）

**Eomes cKO 对其他 CD4⁺ 亚群的影响**：

| 亚群标志物 | LP 变化 | mLN 变化 |
|-----------|---------|----------|
| RORγt⁺ | ↑ | ↑ |
| IL-17A⁺ | ↑ | ↑ |
| FOXP3⁺ | ↑ | - |
| T-bet | 不变 | 不变 |
| IFNγ | - | 轻度↓ |
| CD8α | 不变 | - |

**Gzmk⁻/⁻ 过继转移**（区分致病机制）：
1. Gzmk⁻/⁻ 和 WT naive CD4⁺ T 细胞分别转入 Rag1⁻/⁻（每组 n = 5）
2. 监测体重 + 终点结肠长度
3. **结果**：Gzmk 缺失不减轻疾病（体重和结肠长度均无差异）
4. **结论（原文逻辑）**：
- Eomes cKO → 疾病减轻 → THK 整体参与致病
- Gzmk KO → 疾病不变 → 单一 GZMK 不是致病的必需因子
- 因此，致病性依赖的是 **EOMES 调控的多个下游效应分子**（Perforin、GZMB、细胞因子等）的协同作用，而非 GZMK 单个分子

---

## 七、Extended Data Fig. 10：论文的"收尾"——跨物种 + 跨疾病保守性验证

### 为什么要放在最后？

```
Fig 1-2：发现 THK（人 + 鼠结肠炎）
Fig 3：  排除已知谱系
Fig 4-6：鉴定 EOMES 是 THK 的调控因子（关联 → 充分 → 必需）
    ↓
但所有结论都建立在"结肠炎"这一个疾病模型上
    ↓
ED Fig 10：THK 到底只是一个结肠炎相关的活化状态，还是一个**通用 CD4⁺ 亚群**？
```

论文结尾需要回答这个格局性的大问题。作者用两层验证把单病种发现**升格为一般性免疫学结论**：

| 维度           | 对比                          | 结论                             |
| ------------ | --------------------------- | ------------------------------ |
| **跨物种**（a-c） | 人 IBD + 人泛癌 vs 鼠结肠炎         | THK 程序在**人鼠之间保守**              |
| **跨疾病**（d-m） | 鼠结肠炎、肿瘤（MC38）、EAE、LCMV 四个模型 | THK 不限于肠道炎症，在**不同免疫应答场景中普遍存在** |

---

### 第一部分：人 THK 保守性分析（ED Fig 10a-c）——跨物种验证

**步骤**：
1. **IBD 数据集分析**（Extended Data Fig. 10a）：
   - 从 Fig. 1a scRNA-seq 数据中，将原始注释的 "CD4 Temra" 簇再分亚簇
   - 取主要 GZMK^high 亚群 vs 其他 CD4 亚群做差异表达分析（Wilcoxon rank-sum test, Bonferroni 校正）
2. **泛癌数据集分析**（Extended Data Fig. 10b）：
   - 直接取原始注释的 "CD4.c12(GZMK+ TEM)" 簇作为 GZMK^high 亚群
3. **跨物种交集**（Extended Data Fig. 10c）：
   - 将 Fig 4a 鼠 THK 上调基因的**小鼠基因名逐一映射为人类同源基因**（如 mouse Gzmk → human GZMK），再与人 GZMK^high 细胞的上调基因取交集
4. **结果**：**核心保守基因** — EOMES, GZMK, CCR5, PRF1, NKG7, SLAMF7

> **战略意义**：小鼠中定义的 THK 程序在人类 IBD 和肿瘤中都能找到对应的 GZMK^high 细胞 → 说明这不是鼠类生物学现象，而是**跨物种保守的免疫亚群**。

---

### 第二部分：跨疾病 THK 细胞分析（ED Fig 10d-m）

**前文所有实验都在结肠炎模型中。跨疾病比较要回答：THK 是肠道特有的，还是在不同炎症背景下都存在的通用亚群？**

选了**四个覆盖不同免疫应答类型的疾病模型**：

| 模型 | 免疫特征 | 数据集 | 样本 | Gzmk^high 细胞数 |
|------|----------|--------|------|-------------------|
| 结肠炎（已分析） | 肠道屏障炎症 | CRA016814 + GSE235664 | 结肠 LP CD4⁺ T | - |
| **肿瘤（MC38）** | 免疫抑制微环境 | GSE285225 | Hepa1-6 荷瘤鼠 TIL CD4⁺ T | n = 2,943 |
| **EAE** | CNS 自身免疫（Th1/Th17） | GSE156196 | CNS 浸润 CD4⁺ T | n = 1,882 |
| **LCMV cl13** | 慢性病毒感染 / T 细胞耗竭 | GSE201730 | 脾脏 GP66 特异性 CD4⁺ T | n = 341 |

**分析流程**：

1. **UMAP 聚类**（d-f）：各数据集独立走标准 Seurat 流程 → 无监督聚类 → 标出 Gzmk 最高表达的簇
2. **THK 签名富集**（g-i）：用结肠炎定义的 "THK cell signature" 计算各簇的模块评分 → Gzmk^high 簇在所有模型中均显著富集 THK 程序
3. **差异基因火山图**（j-l）：Gzmk^high vs 其他 CD4 亚群，Wilcoxon rank-sum test, Bonferroni 校正
4. **四模型交集**（m）：取四个模型中所有显著上调基因的交集

**结果解读**：

| 交叠范围 | 涉及的基因 | 含义 |
|---------|-----------|------|
| **全部四模型一致上调** | **Eomes, Gzmk, Prf1** | THK 的 **"核心身份基因"**——不受组织微环境影响，是 THK 谱系本身固有的程序。Eomes = 谱系定义 TF，Gzmk = 标志性效应分子，Prf1 = 杀伤功能核心 |
| **部分模型中上调** | Ccl5, Ccr5, Nkg7, Il10ra, Slamf7 | 这些基因受**疾病类型或组织微环境调控**，反映 THK 在不同疾病中的功能可塑性 |

**结论**：
- THK 细胞并非结肠炎特有，而是在炎症性肠病、自身免疫（EAE）、肿瘤、慢性感染中**广泛存在**的 CD4⁺ T 细胞亚群
- 其核心转录程序（EOMES → GZMK + PRF1）在跨物种和跨疾病尺度上高度保守
- 差异表达的基因反映 THK 在不同微环境中的功能适应

> **ED Fig 10 的收尾作用**：把前面 6 张图在单一模型中建立的"EOMES → THK → 致病"因果链条，**扩展到全景视角**——证明这不是 IBD 中偶然出现的细胞状态，而是一个普遍存在的、有核心特征程序的 CD4⁺ 效应亚群。

---

## 方法学总结：如何系统性发现和验证一个新免疫亚群

这篇论文提供了一套完整的**新细胞亚群发现与验证框架**，可归纳为以下 6 个步骤：

### 第 1 步：无偏筛选 + 生信发现
| 做法 | 本文对应 |
|------|---------|
| 利用**已发表公共 scRNA-seq 数据**，不做预设假设 | Fig 1a：重分析 scIBD 数据，从异质性的 "CD4 Temra" 簇中再聚类，找到 GZMK^high 亚群 |
| 用**独立队列验证关联性** | Fig 1b：GSE128682 bulk RNA-seq 确认 GZMK 在活动期 UC 中显著升高 |
| **跨数据集重复** | ED Fig 1：泛癌数据中同样存在 GZMK^high CD4⁺ T 细胞 |
| **关键原则**：先用生信"指路"，不盲目做动物实验 |

### 第 2 步：体内模型确认 + 功能描述
| 做法 | 本文对应 |
|------|---------|
| 构建或利用**报告小鼠**追踪目标细胞 | Gzmk-tdTomato 报告小鼠 + Rag1⁻/⁻ 过继转移结肠炎模型 → Fig 2d |
| **多组织基线扫描**，排除本底表达干扰 | ED Fig 2：稳态下扫描 6 个组织位点，确认结肠 Gzmk 几乎为 0 → 结肠炎的 Gzmk⁺ 是炎症诱导的 |
| **表型 profiling**：先看它表达什么、不表达什么 | Fig 2d-g：核内转录因子 panel 排除五种经典谱系 + 效应分子检测 |
| **关键原则**：先用报告小鼠和流式确认这个细胞在体内真实存在，并描出基本画像 |

### 第 3 步：排除已知谱系
| 做法 | 本文对应 |
|------|---------|
| 用**基因敲除鼠**逐一敲掉各已知谱系的关键 TF，看目标细胞是否受影响 | Fig 3a-g：Tbx21、Stat6、Rorc、Bcl6 等 KO → THK 依旧存在 → 不属于任何已知谱系 |
| 结合**时间动力学**排除转分化可能 | ED Fig 6e：TH1/TH17 早期出现而 THK 晚期才出现，错峰出现不支持转分化 |
| **关键原则**：否定比肯定更难，需要用遗传学手段逐一排除已知可能性 |

### 第 4 步：锁定候选调控因子
| 做法 | 本文对应 |
|------|---------|
| **无偏组学扫描**（RNA-seq + ATAC-seq）找到候选 TF | Fig 4a (RNA-seq)：Eomes 在 Gzmk⁺ 中最显著上调的 TF 之一 |
| **多层面交叉验证关联性** | Fig 4c (scRNA-seq 共表达)、Fig 4e (人类 Pearson R²=0.953)、Fig 4f (蛋白水平流式确认)、Fig 4k-m (ATAC-seq + 基序富集) |
| **跨物种保守性验证** | 每步都注意人鼠对照 → 如果跨物种不保守，可能只是鼠类现象 |
| **关键原则**：不靠猜，用组学数据不加预设地找到候选因子。关联性要用多个独立技术平台确认 |

### 第 5 步：因果验证 —— 充分性 + 必要性
| 做法 | 本文对应 |
|------|---------|
| **充分性**（OE）：体外过表达候选 TF → 看是否能驱动目标程序 | Fig 5a-g：Eomes OE → 非极化条件下 Gzmk 和 Prf1 显著上调，THK 签名富集 |
| **必要性**（KO）：体内敲除候选 TF → 看是否需要它来维持目标程序 | Fig 6a-l：Eomes cKO → Gzmk 和 Prf1 显著下降，疾病减轻 |
| **直接结合证据**：CUT&Tag/ChIP-seq 验证 TF 是否直接结合靶基因 | Fig 5f-g：CUT&Tag 确认 EOMES 直接结合 Gzmk 和 Prf1 调控区 |
| **离解单一效应分子**：敲掉标志基因（Gzmk）看是否和敲掉调控因子（Eomes）一样 | ED Fig 9o-p：Gzmk KO 不保护 → 致病靠 EOMES 的协同程序，而非单一 GZMK |
| **关键原则**：关联 ≠ 因果。必须完成 OE（充分）+ KO（必需）+ 物理结合（直接）三件套 |

### 第 6 步：泛化验证
| 做法 | 本文对应 |
|------|---------|
| **跨物种**：小鼠结论在人类数据中验证 | ED Fig 10a-c：鼠 THK 签名转同源基因后在人 IBD 和泛癌中验证 |
| **跨疾病/模型**：在不同免疫应答场景中验证 | ED Fig 10d-m：结肠炎、肿瘤、EAE、LCMV 四个模型全部存在 THK |
| **关键原则**：单个疾病模型中发现的新亚群 => 需要在多个疾病/模型中确认是普遍存在还是疾病特异 |

---

### 全文逻辑路线图

```
发现阶段：
  公共 scRNA-seq 无偏扫描 → 发现 GZMK^high 簇（Fig 1）
        ↓
  报告小鼠结肠炎模型 → 确认体内存在 → THK 命名（Fig 2）
        ↓
验证阶段：
  逐一敲除已知谱系 TF → 排除已有身份 → 这是一个新亚群（Fig 3）
        ↓
  组学扫描找调控因子 → 锁定 EOMES（Fig 4）
        ↓
因果阶段：
  OE（充分性）+ KO（必要性）+ CUT&Tag（直接结合）→ 验证 EOMES 是调控因子（Fig 5-6）
        ↓
泛化阶段：
  Gzmk KO 区分致病机制 + 跨物种/跨疾病验证（ED Fig 9-10）
```

**一句话**：这篇论文提供了一个从**生信发现 → 体内确认 → 排除已有 -> 找调控因子 → 因果验证 → 泛化论证**的完整方法论范本。

| 方法 | 核心参数/步骤 |
|------|--------------|
| **过继转移结肠炎模型** | 分选 naive CD4⁺ T 细胞（FACS, >98% 纯度）→ 1.5-2×10⁶ i.v. → Rag1⁻/⁻ → 4-5 周后分析 |
| **结肠 LP 淋巴细胞分离** | 含 EDTA/DTT 的 RPMI 37°C 30min 去上皮 → 胶原酶 D (0.5 mg/ml)+分散酶 (1 mg/ml)+DNase I (4 μg/ml) 37°C 30min 消化 → 100 μm 滤网 → Percoll 37/70% 梯度离心 |
| **流式染色（核内）** | 死活染料 (eF506) → 表面染色 → FOXP3 固定破膜缓冲液 → 核内抗体（30min, 4°C）；荧光蛋白：2% PFA 20min → 再破膜 |
| **流式染色（胞内细胞因子）** | PMA (50 ng/ml)+Ionomycin (500 ng/ml)+GolgiStop → 4.5 h → 固定破膜 → 胞内抗体 |
| **RT-qPCR** | TRIzol 提取 → HiScript III 反转录 → SYBR Green Low ROX（内参 Actb）；Gzmk F: 5'-TGGCTGGCGTTTATATGTCTTC-3' |
| **Bulk RNA-seq** | VAHTS Universal V10 建库 → DNBSEQ-T7 150bp PE ~20M reads → HISAT2 mm39 → featureCounts → DESeq2 |
| **ATAC-seq** | 10⁵ 细胞 → Hyperactive ATAC-Seq Kit → NovaSeq X Plus 150bp PE ~40M reads → Bowtie2 → MACS2 (BAMPE, q=0.01) → DiffBind → HOMER |
| **CUT&Tag** | EOMES-HA OE T 细胞（5d 培养）→ Hyperactive Universal CUT&Tag Kit + 抗 HA (CST #3724) → NovaSeq 150bp PE ~20M reads → MACS2 → 3 重复 consensus → ChIPseeker |
| **逆转录病毒过表达** | 293T 磷酸钙转染 RVKM + pCL-ECO → 48h 收毒 → T 细胞活化 24h → 加毒 → 24h 后换液 → 续培 4d → 分选 BFP⁺ |
| **体外细胞毒性实验** | 效应细胞（LP CD4⁺ T）+ P815 靶细胞（CFSE 标记）→ anti-CD3 (0 或 1 μg/ml) 共培养 19h → Fixable Viability Dye eF506 检测死细胞 |
| **各极化条件** | TH0: αIFNγ+αIL-4; TH1: αIL-4+mIL-12; TH2: αIFNγ+IL-4+mIL-2; TH17: TGF-β+IL-6+IL-1β+IL-23+αIFNγ+αIL-4; Treg: mIL-2+TGF-β+αIFNγ+αIL-4 |
| **OVA 免疫 TFH 模型** | OT-II CD4⁺ T → i.v. WT → 次日皮下 OVA (3 mg/ml)+CFA → 第 7 天分析 mLN |
| **组织学** | 远端结肠 4% PFA → 石蜡切片 (5 μm) → H&E → 盲法 0-4 分（炎症+肠壁增厚+隐窝/杯状细胞丢失） |
| **统计方法** | 配对 t 检验（共转模型）、非配对 t 检验（独立组比较）、one-way ANOVA+Tukey（多组）、two-way ANOVA+Bonferroni（体重曲线） |
