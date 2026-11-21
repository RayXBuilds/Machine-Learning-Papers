---
id: probabilistic-matrix-factorization
primary_topic: recommender-systems
tags: [matrix-factorization, collaborative-filtering]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://papers.nips.cc/paper/2007/file/d7322ed717dedf1eb4e6e52a37ea7bcd-Paper.pdf
status: summary
catalog_year: 2007
subtopic: "协同过滤与交互建模"
updated: 2026-11-21
---

# Probabilistic Matrix Factorization

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Ruslan Salakhutdinov、Andriy Mnih（按论文首页署名）
- 年份与版本：2007 年，NIPS 2007, Advances in Neural Information Processing Systems 20。
- 原始来源：[原文](https://papers.nips.cc/paper/2007/file/d7322ed717dedf1eb4e6e52a37ea7bcd-Paper.pdf)
- 官方代码：[作者的 MATLAB 软件包，含 pmf.m](https://www.cs.utoronto.ca/~rsalakhu/BPMF.html)

## 解决的问题

用户与物品形成的评分矩阵大多为空，如何估计有用的低维因子而无需填满所有空格？

## 主要方法

只为观测评分建立高斯似然，用用户和物品因子的内积预测评分，并对因子设置高斯先验。

## 贡献与局限

后验众数估计把正则化矩阵分解与概率假设联系起来。没有任何评分的新用户仍缺少估计个性化因子的依据。

## 前置知识与阅读重点

先理解低秩分解。写出单个评分的负对数似然，再辨认正则项来自哪个先验。

## 收录理由

给神经协同过滤提供清晰的内积预测基线，也便于区分显式评分与隐式排序。

## 相关主题与版本

NIPS 2007 d7322ed717dedf1eb4e6e52a37ea7bcd。延伸阅读见[神经协同过滤](2017-ncf.md)。

核对范围为书目信息与方法概要，未做实验复现。
