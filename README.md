# 2021/1/4

在vscode里设置好了bash终端，准备复习数电，冲鸭！

---

# 2021/1/28

paper1: `Efficient Decision-based Black-box Adversarial Attacks on Face Recognition`

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210128111649.png)

人脸识别：主要分为Face Detection(FD)和Face Recognition(FR)两类。

攻击人脸识别的效果：主要分为Dodging attack和Impersonation attack两类。

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210201105929.png)



---

# 2021/1/29

Python foolbox package can help to generate AEs



# 2021/1/31

paper2：`Adversarial Attack on Facial Recognition using Visible Light`

非常新颖的提出了用可见光进行人脸识别攻击的方法。文中提到了两种进攻：Infra red attack和laser attack。其中laser attack是通过模拟one pixel attack完成的。本篇文章没有数理推导，但是提出了两个生成网络，分别是生成红外线照射区域和激光照射区域的网络，均使用黑盒攻击，并在github上开源。

Infra red attack是个很好的思路，因为人眼不可见但camera会捕捉到，从而影响FD和FR准确度。但是似乎较容易防御，比如拥有红外滤波的摄像头，以及针对暗环境自动补光识别。这两个会是用光攻击人脸识别的一个难点。包括后面的laser attack都是需要在低亮度的环境进行。

这篇文章中生成投射光位置的两个网络值得学习，这是进行physical world attack 的重要手段。

Infra red attack的三大问题：

* the IRH has limited range on how far the light can be moved on the face.
* light is extremely hard to model and the LPO only uses a single standard spot type
* low light testing which was observed as a limitation earlier adds unnecessary constraints to the testing environment.

laser attack 的问题：

* 环境亮度要求较暗
* The current attack is difficult to setup as the LZP is manually pointed and aligned on the face. It would be ideal to automate this using a microcontroller that is fed the LPOs recommendation.



可以研究的方向：

* 能否通过“光攻击”进行Impersonation attack，甚至是targeted attack
* 能否解决上述”光攻击“的一些问题
* GAN生成伪造人脸



目前了解的人脸识别进攻的主要方向是：

1. Makeup attack
2. Face morphing attack
3. Spoofing Face attack
4. Presentation Attack(照片、屏幕视频、面具)



# 2020/2/2

活体检测方法：

1. 配合式防伪
   * 眨眼、摇头
   * rPPG皮肤细微亮度变化
     要求噪声小、环境光稳定，人脸静止
   * 运动模式分析
     检测人脸上光流。缺点：摄像头需固定、无法防御面具和视频回放
   * 三维重建法

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210202121317.png)

2. 静默防伪
   * 基于纹理分析(摩尔纹、真假人频域分析)
   * 基于分类：高频图像特征+传统分类器
   * 深度学习方法
     * 基于深度图回归
     * 朴素二分类
     * 基于分块
     * 基于辅助监督信号
     * rPPG回归 +(深度图)
     * Aurora Guard：手机屏幕光照可控变化(打不同颜色的光照)
3. 伪造检测
   * 检测用GAN生成的伪造人脸(Deep Fake Detection Challenge)
4. 多光谱防伪(硬件防伪)
5. 多模态防伪(多模态融合卷积神经网络)

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210202122938.png)

人脸防伪数据库：活体检测数据仍然很缺乏

* 防伪数据增强
* Replay虚拟生成
* 照片虚拟生成
* 小样本学习(Meta-Learning)

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210202123833.png)



人脸采集设备

1. 可见光摄像头
   分辨率最高、数据最丰富、模态最不稳定，受各种因素(尤其是光照)影响大，防伪性能较弱

2. 近红外摄像头
   接受器：只接受近红外分量(室内极少、白炽灯不包含)
   发射器：主动近红外打光(不依赖环境光源)
   **优点：分辨率较高(480p)、单摄像头性价比最高、模态稳定，几乎不受环境光源影响，夜间可用。隐式包含3D信息，防伪能力强。**

   **缺陷：使用距离有要求，不能太远。数据需要设备专门采集，缺乏训练数据。**

3. 深度摄像头
   包含显式的三维信息，对防御平面媒体攻击及其有效。精度极低(高精度设备太贵太重)。对距离有严格要求，既不能太近也不能太远。采集非常困难，极其缺乏训练数据(万级)



人脸防伪挑战

1. 光照(侧光、逆光、暗光)
2. 跨模态
3. 姿态
4. 未知攻击方式

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210202124309.png)



人脸防伪发展方向：

* 软件
  * 增强模型的泛化性：训练集和测试集场景经常是不一致的
  * 小样本学习：快速应对新的攻击方式
  * 数据增强：基于成像原理及图形学的虚拟生成
  * 数据收集：成本更低假体及收集
* 硬件
  * 新的光谱：与皮肤材质有显著不同
  * 新的主动光源

---

Lecture: `A Novel Attack Paradigm in the Deployment Stage：Targeted Attack against Deep Neural Networks via Flipping Limited Weight Bits`

AML(Adversarial ML) --- GAN(Generative Adversarial Networks)

AML:

1. Backdoor Learning/Attack(Training stage)
2. Weight Attack(Deployment stage)
3. Adversarial Examples(Testing stage)

AML:three attack paradigms

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210202152459.png)

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210202152257.png)

**Weight Attack**

* Physical fault injection
* Row hammer attack: reading from the same address in memory can corrupt data in nearby addresses
* Laser beam attack: using laser beam to flip the bits stored in the chip

Our task: *changing the weights stored in the memory via bit flipping to achieve some malicious goals*



# 2020/2/4~2020/2/9 

美赛加油！



# 2020/2/21

Paper3:`VLA: A Practical Visible Light-based Attack on Face Recognition Systems in Physical World`



### Main Idea

利用POV(视觉暂留)通过可见光对人脸识别进行targeted和untargeted的进攻。主要通过构造了Perturbation frame和concealing frame对人脸进行照射来达到对抗样本的效果。

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210221165115.png)

![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/lhc/image/QQ%E5%9B%BE%E7%89%8720210224132824.png)

### My Thoughts

文中在分析了physical world attack和digital attack的差异，即在现实情况下的攻击，难以以上传一张对抗样本图片的方式完成进攻，而digital attack下的对抗样本图片的扰动都很细小，若是直接套用到physical world很容易收到摄像机分辨率影响或者受到图片裁剪等影响使得效果很差。而现实世界的对抗样本同样也应该满足不易被人发现的特质。

其中attack FR using infrared确实达到了不被人眼所发现，但目前的camera如CMOS都配有infrared filter，这会直接影响到这类进攻。

这篇文章提供给我的一个思路是寻找人眼的一些特殊现象，比如视觉暂留等，利用这些现象去制作一些人眼难以察觉但能被camera察觉到的对抗样本扰动。

有个新想法是关于噪点的，能否通过某些手段在camera识别人脸时产生噪点从而影响识别。

从红外进攻引发的想法，既然红外进攻虽然不易被人眼识别，但容易被camera滤去，那我们可以尝试结合这篇文章的思路，不将目标人脸投射到真人脸上，而是通过infrared攻击网络计算出的位置投上高频闪烁的可见光以通过视觉暂留现象让人眼难以察觉的同时被机器接受到。

---------

针对中期汇报，目前想法是用可见光/红外进行对抗样本攻击。

- 人脸识别网络
- AdvHat
- 光线投射区域的生成网络

