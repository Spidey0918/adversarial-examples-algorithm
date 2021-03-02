# adversarial-examples-algorith
## 2021.1.31
### paper1:DaST: Data-free Substitute Training for Adversarial Attacks

## 2021.2.9
### paper2:The Elements of End-to-end Deep Face Recognition: A Survey of Recent Advances（2020）
- face detection、face preprocessing, and face representation
- face detection：多阶段、单阶段、基于锚点、无锚点、多任务风格、CPU 实时和面向问题的方法
- face preprocessing：人脸对齐：基于标志点：坐标回归、热图回归、3D模型拟合  
---------------------------------：无标志点  
--------------------：正面化       
- face representation：网络架构：通用架构、专业架构  
---------------------：培训监督：分类、特征嵌入、混合

---

## 2020.2.24
### paper3:Recover Canonical-View Faces in the Tild with Deep Neural Networks 
设计了一种新的测量方法来为每个身份自动选择或合成标准视图图像   
通过使用基于面部成分的卷积神经网络，从恢复的标准视角面部图像中学习面部特征，在LFW数据集上实现了最先进的性能   
应用于人脸验证
#### 从具有复杂变化集的人脸图像转换到规范视图
- 鲁棒特征提取：小姿态和简单的照明变化
- 人脸归一化：大姿态和不同照明下的人脸变化   
#### 过程：
- 判断图像是否是正面拍摄：结合矩阵的秩和对称性
- 面部修复：最小化损失误差
- FCN（面部组件深度网络）：原始图像用作输入，通过FCN（恢复和裁剪、特征学习、特征约简）进行人脸验证   
#### 数据集：LFW
#### 实验：
- 在受限协议下使用除LFW之外的外部训练数据
- 在不受限制协议下在LFW训练   
两种训练效果都不错
