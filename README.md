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
#### 从具有复杂变化集的人脸图像转换到规范视图
- 鲁棒特征提取：小姿态和简单的照明变化
- 人脸归一化：大姿态和不同照明下的人脸变化   
#### 过程：
- 判断图像是否是正面拍摄：结合矩阵的秩和对称性
- 面部修复：最小化损失误差   
#### 数据集：LFW
