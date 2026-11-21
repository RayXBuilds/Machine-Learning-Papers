---
id: lasso
primary_topic: foundations
tags: [regularization, variable-selection]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://academic.oup.com/jrsssb/article/58/1/267/7027929
status: summary
---

# Regression Shrinkage and Selection Via the Lasso

- 作者：Robert Tibshirani
- 年份与版本：1996 年，Journal of the Royal Statistical Society, Series B 58(1), 267–288。
- 原始来源：[原文](https://academic.oup.com/jrsssb/article/58/1/267/7027929)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

回归变量较多时，能否一边压缩估计方差，一边得到变量子集？

## 主要方法

在平方残差最小化中限制回归系数绝对值之和。约束区域的尖角使最优解可能把某些系数压到零。

## 贡献与局限

同一个优化问题兼顾收缩和选择。系数取决于变量尺度，相关变量之间的选择也可能随样本变化。

## 前置知识与阅读重点

熟悉最小二乘和岭回归后，画出二维损失等高线与菱形约束集，观察首次接触的位置。

## 收录理由

把统计估计中的偏差与方差取舍连接到凸优化的几何图像。

## 相关主题与版本

[DOI 10.1111/j.2517-6161.1996.tb02080.x](https://doi.org/10.1111/j.2517-6161.1996.tb02080.x)。延伸阅读见[支持向量机](../classical-ml/1995-support-vector-networks.md)。

核对范围为书目信息与方法概要，未做实验复现。
