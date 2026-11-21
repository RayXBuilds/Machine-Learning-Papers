---
id: lloyd-quantization
primary_topic: classical-ml
tags: [clustering, quantization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://web.stanford.edu/class/ee398a/handouts/papers/Lloyd%20-%20Least%20Squares%20Q%20in%20PCM.pdf
status: summary
catalog_year: 1982
subtopic: "聚类与降维"
updated: 2026-11-21
---

# Least Squares Quantization in PCM

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Stuart P. Lloyd
- 年份与版本：1982 年，IEEE Transactions on Information Theory 28(2)。工作早在 1957 年已报告，此处采用期刊年份。
- 原始来源：[原文](https://web.stanford.edu/class/ee398a/handouts/papers/Lloyd%20-%20Least%20Squares%20Q%20in%20PCM.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/classical-ml/1982-lloyd-quantization.pdf)（IEEE Transactions on Information Theory 28(2)，1982 年 3 月期刊扫描版）。

## 解决的问题

用有限个电平表示连续信号时，如何同时选定量化区间和各区间的代表值？

## 主要方法

固定电平，将边界设在相邻电平中点。固定区间，再把电平移到区间内信号的条件均值。

## 贡献与局限

两步更新给出平方失真下的必要条件，也解释了质心聚类的交替更新。满足这些条件仍可能只是局部最优。

## 前置知识与阅读重点

先复习均方误差。对偏斜的一维分布画两个区间，观察区间中点与条件均值的区别。

## 收录理由

从标量量化读懂最近中心分配与更新质心为什么对应同一个目标。

## 相关主题与版本

[DOI 10.1109/TIT.1982.1056489](https://doi.org/10.1109/TIT.1982.1056489)。延伸阅读见[归一化割](../graph-learning/2000-normalized-cuts.md)。

核对范围为书目信息与方法概要，未做实验复现。
