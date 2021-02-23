2021年2月10日提交

# 高效的基于决策的黑箱对抗攻击的人脸识别

## 基于当前的深度神经网络在人脸识别方面的不安全隐患，提出一种基于遗传算法的攻击方式。遗传算法：是一种通过模拟自然进化过程搜索[最优解](https://baike.baidu.com/item/最优解/5208902)的方法。

## 常见的人脸识别网络

* SphereFace，, CosFace, ArcFace

## 针对神经网络的黑盒攻击方法的三种攻击手段

* transfer-based black box attack:基于神经网络的迁移性
* score-based black box attack:基于获得模型的预测概率
* decision-based black box attack：基于获得模型的预测硬标签

### 数据集（Wild (LFW) and MegaFace）

## 之前的优化求解算法

* The boundary attack method：基于在决策边界的随机移动
* The optimization-based method 连续空间优化，计算与决策边界的位置
* NES（natural evolution strategy）

论文的主要内容：

* 提出一个在基于决策的黑盒场景下的攻击方法，（基于获得模型的预测硬标签）可以对搜索方面的局部几何进行建模，同时降低空间的维度。
* 利用上述方法，对几种最先进的人脸识别模型（SphereFace, CosFace, ArcFace）做了鲁棒性测评，并展示了这些人脸模型的脆弱性。
* 通过对真实世界中的人脸识别系统进行攻击，展示了提出的方法的实际适用性。
* 攻击建模：<img src="C:\Users\luosupeng\AppData\Roaming\Typora\typora-user-images\image-20210210094508814.png" alt="image-20210210094508814" style="zoom:150%;" />，基于CMA-ES（协方差矩阵适应进化策略）

## 论文方法的优势

这种攻击方法即使在限制对模型的查询次数也很有效，并且将其用于真实的人脸识别环境中，也攻击成功了。并且该求解算法相比于其他算法收敛速度更快，且求得的最优解

2021年2月23日提交

美国国家标准与技术研究所（NIST）将对抗式机器学习分为四类攻击：

* evasion 回避
* extraction 抽取
* poisoning 中毒
* inference 推理

### 三种扰动方法生成对抗例子

* 粒子群优化（PSO）
* 遗传算法（GA）
* 生成对抗网络（GAN）

采用的数据集：NSL-KDD和UNSW-NB15 ，应用蒙特卡罗（MC）模拟随机生成扰动

### 机器学习的三大领域

* 有监督学习（预测目标标签）
* 无监督学习（常用技术：聚类，主成分分析，矩阵补全）
* 强化学习（马尔科夫决策，最优决策）

快速梯度符号法，基于雅可比矩阵的显著攻击，Deepfool，Carlini-Wagner攻击

该噪声向量包含噪声可变部分和原始固定部分，然后被馈送到发生器神经网络，其输出是与原始输入的可变部分大小相同的向量。然后将该对抗性向量输出与输入向量的初始不可变部分组合以形成新的对抗性输入，然后将其馈送到鉴别器以生成标签（良性或恶意）。