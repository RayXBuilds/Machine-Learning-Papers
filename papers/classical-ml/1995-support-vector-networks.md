---
id: support-vector-networks
primary_topic: classical-ml
tags: [svm, kernel-methods, classification]
type: paper
added: 2026-10-27
verified: 2026-10-27
source: https://link.springer.com/article/10.1007/BF00994018
status: summary
---

# Support-vector networks

- 作者：Corinna Cortes、Vladimir Vapnik。
- 年份与版本：1995 年 9 月，Machine Learning，20：273–297；正式期刊论文。
- 原始来源：[出版方页面](https://link.springer.com/article/10.1007/BF00994018) · [DOI](https://doi.org/10.1007/BF00994018)。
- 官方代码：本次核对的出版页未提供作者实现；不将后来的通用机器学习库标作本论文官方代码。

## 解决的问题

当两类训练样本不能完全分开时，如何延续支持向量方法的分类思想？

## 主要方法

将输入映射到高维特征空间，再构造线性决策面；论文将此前针对可分样本的方法扩展到非可分数据，并以字符识别开展比较。[出版方摘要](https://link.springer.com/article/10.1007/BF00994018)

## 贡献与局限

这是理解非可分情形支持向量分类的重要原始论文，不能称作支持向量思想的首次提出。当前导读只核对书目与摘要，未完整核对全文、证明或实验；不据摘要推断其在现代任务上的普遍优势。

## 前置知识与阅读重点

前置知识包括线性分类、内积与约束优化。后续全文阅读重点是间隔与错误容忍如何权衡、哪些样本决定边界，以及特征映射如何影响分类。

## 收录理由

补齐维护队列中的 SVM 原始论文，与现有随机森林和 XGBoost 导读形成方法对照。

## 相关主题与版本

DOI：`10.1007/BF00994018`。年份采用正式期刊发表年份。历史库的生物信息学 SVM 综述是不同文献，不替代本条目。
