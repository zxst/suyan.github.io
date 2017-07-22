---
layout: post
title: Google预测分子活性
category: 新药研发
keywords: Drug discovory
---
## Predicting Properties of Molecules with Machine Learning

[原文链接](https://research.googleblog.com/2017/04/predicting-properties-of-molecules-with.html)

---
1.首先介绍了最近ML在化学方面用的不错，而之前这些研究都是利用密度泛函理论（DFT,Density Function Theory）在搞.但是DFT的计算cost 限制了search size.为了解决search size的问题，some research 采用ML对由DFT产生的数据进行训练来预测chemical properties。

2.在上一段的基础上，g采用的多种modern ML method 在[QM9 benchmark](https://www.nature.com/articles/sdata201422)上，这个benchmark是一个public collection of molecules paired weith DFT-computed electronic,热力学，和动力学参数.

3.这些研究发了两篇paper.
* [Machine learning prediction errors better than DFT accuracy Felix](C:/paper/google_first.pdf)
* [Neural Message Passing for Quantum Chemistry](C:/paper/google_sec.pdf)

4.第一篇内容
* Include a new featurization of molecule
* a new systematic assessment of ML method on QM9

5.第二篇内容
* 提出了a model family called MPNNs(Message Passing Neural Networks),表现很好。

6.本文提出一个发现就是：从ML的角度来看分子数据是很interesting的，因为natural representation of a molecule is as a graph with atoms as node and bonds as edges.
可以leverage(利用)数据中的inherent symmetries 的模型泛化能力更好。这就像图片一样，我们使用CNN处理图像，利用的也正是图像的这个性质。

7.Despite现在的progress,但是想real practice to chemists,现在还有很多工作remains。MPNNs在使用时远远比使用DFT模拟快的d多,但是只能apply to more diverse set of molecules.

end.

---
[夜间模式](http://zxst.github.io/_posts/DS/Predicting-Properties-of-Molecules-with-Machine-Learning.html)
