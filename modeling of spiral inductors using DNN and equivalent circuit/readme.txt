名称：宽频带范围螺旋电感DNN建模
内容：
	利用HFSS在1-119GHz的条件下，抽样仿真了一个螺旋电感，利用仿真数据建立电感模型；
	输入为频率（标准化/60GHz）、电感内径（标准化/29.6um）、电感线宽（标准化/5.1um）
	输出为MAGS11,MAGS21,DEGS11（弧度制）,DEGS21（弧度制）
说明：
	model.m  文件是matlab程序
	训练集测试集数据 文件夹是HFSS导出的原始数据和matlab预处理后的数据
	Modeling and Synthesis of On-chip Multi-layer Spiral Inductor for Millimeter-wave Regime Based on ANN Method.pdf 为以此为基础发表的EI论文；
	paper中第三部分ANN建模为本人工作