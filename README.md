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

Python foolbox package can help to generate AEs\



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



目前了解的人脸识别进攻的主要方向是：

1. Makeup attack

2. Face morphing attack
3. Spoofing Face attack