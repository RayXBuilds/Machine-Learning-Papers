---
id: nearest-neighbor
primary_topic: classical-ml
tags: [nonparametric-learning, statistical-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf
status: summary
---

# Nearest Neighbor Pattern Classification

- 作者：Thomas M. Cover、Peter E. Hart
- 年份与版本：1967 年，IEEE Transactions on Information Theory 13(1), 21–27。
- 原始来源：[原文](https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

只参考一个最近训练样本的类别，在样本趋于无穷时要付出多少误差代价？

## 主要方法

在给定测试点处比较真实标签与近邻标签的条件分布，再对测试点求平均，将极限风险与贝叶斯误差联系起来。

## 贡献与局限

在论文条件下，单近邻渐近错误率至多为贝叶斯错误率的两倍。有限样本时，度量和维数都会影响邻居是否真的接近。

## 前置知识与阅读重点

熟悉条件概率和贝叶斯分类器后，用二分类后验概率手算一次两次抽样标签不同的概率。

## 收录理由

用一个无需拟合参数的规则引出分类风险及其理论下界。

## 相关主题与版本

[DOI 10.1109/TIT.1967.1053964](https://doi.org/10.1109/TIT.1967.1053964)。延伸阅读见[t-SNE](2008-tsne.md)。

核对范围为书目信息与方法概要，未做实验复现。
