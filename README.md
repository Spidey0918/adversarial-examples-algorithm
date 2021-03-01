# adversarial-examples-algorithm

## `2020/12/22`
---
**大家要在自己电脑上下好Git，没装好环境的尽快装好，寒假我们工作继续！**


每次提交一定要切换到自己的分支,在自己的分支里提交文件

* `git branch -a` (查看所有分支)
* `git checkout lhc` (切换到自己名字下的分支)


提交文件操作：

* `git add README.md`
* `git commit -m "this is a test" `(这里要写清楚你干了什么)
* `git push` (最终提交)

---
vscode里若要用bash,要在settings.json里添加如下命令：
"terminal.integrated.shell.windows": "你自己的bash.exe路径",

---
## `2020/1/27`
**对抗样本方向的确定**

1. attack settings: black-box(for sure), transfer-based attack or decision-based attack...
2. application: face recognition? 
3. generate method: GAN?

以上是一些我自己最近的思路，大家最近去搜集一些自己感兴趣的对抗样本的应用方向，比如攻击人脸识别、NLP方向的等等都可以，最后我们综合一下，要尽快确定方向，有针对性的找论文了。



## `2020/2/22`

人脸识别攻击方向分组：光攻击、贴片攻击

- 光攻击
  组长：李浩川
  组员：骆素蓬、沐方晗
- 贴片攻击
  组长：石暄
  组员：韩宝恩、朱梓轩、宋炎



### 光攻击计划

1. 复现`Adversarial Attack on Facial Recognition using Visible Light`中的红外攻击和激光攻击(3月任务)

   - IRHAT制作
     ![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/main/images/QQ%E5%9B%BE%E7%89%8720210301133354.png)
     ![avatar](https://github.com/Spidey0918/adversarial-examples-algorithm/blob/main/images/QQ%E5%9B%BE%E7%89%8720210301133333.png)

   

   - 投射区域网络的改进
     Github-link: https://github.com/loumor/Adversarial-Attack-LPO-

2. POV、噪点等元素的运用，和backdoor攻击结合



### 贴片攻击计划

> 3月1日至3月14日左右，了解贴片疗法的基础知识；

> 3月15日至3月28日左右，制造“贴纸”

> 3月29日以后，应用“贴纸”，实现对抗。

> 详细计划根据具体进度情况进行调整。