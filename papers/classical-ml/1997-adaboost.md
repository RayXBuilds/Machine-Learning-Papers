---
id: adaboost
primary_topic: classical-ml
tags: [boosting, ensembles, online-learning]
type: paper
added: 2026-10-29
verified: 2026-10-29
source: https://doi.org/10.1006/jcss.1997.1504
status: summary
---

# A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting

- 作者：Yoav Freund、Robert E. Schapire。
- 年份与版本：1997 年 8 月，Journal of Computer and System Sciences，55(1)：119–139。文件年份采用正式期刊年份；此前扩展摘要见 EuroCOLT 1995。
- 原始来源：[DOI 出版入口](https://doi.org/10.1006/jcss.1997.1504) · [作者所属机构书目与摘要](https://collaborate.princeton.edu/en/publications/a-decision-theoretic-generalization-of-on-line-learning-and-an-ap/)。
- 官方代码：本次核对的来源未提供作者代码，不将现代库实现当作原论文代码。

## 解决的问题

如何在在线决策中按反馈调整资源分配，并利用这一思想把弱学习器组合为更强的分类器？

## 主要方法

将乘法权重更新推广到一般决策框架，再用于推导自适应提升算法，无需预先知道弱学习器的性能。论文还讨论非二元输出的推广。[机构摘要](https://collaborate.princeton.edu/en/publications/a-decision-theoretic-generalization-of-on-line-learning-and-an-ap/)

## 贡献与局限

为理解 AdaBoost 与在线学习之间的联系提供原始文献。当前只核对书目和摘要，未完整核对证明或复现。编者提醒：理论条件下的保证不能直接当作任意数据上的泛化结论，实际使用仍需独立验证集。

## 前置知识与阅读重点

先理解加权分类误差、弱学习与组合预测。全文阅读重点是样本权重如何变化、弱学习条件如何进入保证，以及迭代次数如何选择。

## 收录理由

补齐维护队列中的 Boosting 基础论文，可与随机森林、XGBoost 对照阅读集成方法的不同思路。

## 相关主题与版本

DOI：`10.1006/jcss.1997.1504`。1995 扩展摘要与 1997 期刊版本在本条目说明，不重复创建导读。
