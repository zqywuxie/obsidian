1. 根据barcode 获得 TCR/RNA-seq配对数据
2. 构建功能评分矩阵
	1. RNA-seq -> normalization(跨批次标准化)
	2. 功能维度：MAIT,NKT,(effector/mem),Treg,Naive,γδT（谱系维度） 、
		1. 选择marker标识，需要做co-expression，即判断选择的marker是否针对某一功能共表达
	3. 构建 TRB + TRA / TRB-only
3. 模型输入：
	1. 目前单细胞（CD4 / CD8 / 双阳细胞）输入
	2. 特征input： （CD1/2 是否会和VJ基因冲突？) +CDR3  + VJ +公共CDR3频率（在大型数据库或对照组中出现频率）（更偏Naive？）
	3. output：多功能维度 or 维度合并为单一向量


感觉差不多