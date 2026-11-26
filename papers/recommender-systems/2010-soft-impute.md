---
id: soft-impute
primary_topic: recommender-systems
catalog_year: 2010
subtopic: "协同过滤与交互建模"
updated: 2026-11-26
tags: [matrix-completion, collaborative-filtering, nuclear-norm]
type: paper
added: 2026-11-26
verified: 2026-11-26
source: https://www.jmlr.org/papers/v11/mazumder10a.html
status: summary
---

# Spectral Regularization Algorithms for Learning Large Incomplete Matrices

[主题目录](README.md) · [年份导航](../../docs/years/README.md)

- 作者：Rahul Mazumder、Trevor Hastie、Robert Tibshirani
- 年份与版本：JMLR 第 11 卷，第 2287–2322 页。按期刊版发表时间 2010 年 8 月归档。
- 原始来源：[JMLR 论文页](https://www.jmlr.org/papers/v11/mazumder10a.html)
- 仓库内 PDF：[期刊全文，36 页](../../pdfs/recommender-systems/2010-soft-impute.pdf)
- 官方代码：[作者维护的 R 包 softImpute](https://cran.r-project.org/package=softImpute)

## 解决的问题

一张用户与电影的评分表里，每个人只评过少数电影。直接把空格填成零再做矩阵分解，会把“没看过”当作真实评分。作者研究如何只用已观测位置衡量拟合误差，同时利用整张表的低秩结构估计缺失评分。

## 主要方法

目标函数把已观测评分的平方误差与核范数惩罚相加。核范数等于奇异值之和。Soft-Impute 每轮保留已观测评分，用上一轮估计填入空格，再对填好的矩阵做奇异值软阈值处理。每个奇异值减去同一阈值，减到零的方向退出模型。沿一系列逐渐减小的惩罚参数求解时，可以沿用前一组参数的解作为起点。

## 贡献与局限

作者说明了如何利用“低秩估计加稀疏残差”的结构计算矩阵乘积，使截断奇异值分解可以处理大而稀疏的评分表。编者判断，真实用户会主动选择观看和评价哪些电影，因此在留出的已知评分上预测准确，还不足以说明模型也能准确预测从未被评价的电影。

## 前置知识与阅读重点

先熟悉奇异值分解和正则化。可以取一张只有一个空格的小矩阵，手算一轮更新。观察软阈值如何同时改变已评分和未评分位置的估计，再看下一轮为何要把原始评分放回已观测位置。这个区别解释了算法怎样容许观测噪声。

## 收录理由

与[概率矩阵分解](2007-probabilistic-matrix-factorization.md)对读，可以在同一评分预测任务上比较两种控制复杂度的办法：为用户与物品设置给定维数的潜在因子，或通过奇异值惩罚调节有效秩。

## 相关主题与版本

该文连接协同过滤、矩阵补全和凸优化。导读与 PDF 均采用 JMLR 期刊版。链接的 R 包可用于阅读作者实现，本次核对覆盖期刊书目、算法与实现入口，未运行实验。
