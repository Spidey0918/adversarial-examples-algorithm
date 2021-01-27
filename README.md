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