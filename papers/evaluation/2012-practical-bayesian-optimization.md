---
id: practical-bayesian-optimization
primary_topic: evaluation
tags: [bayesian-optimization, hyperparameters, gaussian-processes]
type: paper
added: 2026-11-22
verified: 2026-11-22
updated: 2026-11-22
source: https://proceedings.neurips.cc/paper/2012/hash/05311655a15b75fab86956663e1819cd-Abstract.html
status: summary
catalog_year: 2012
subtopic: "实验设计与数据有效性"
---

# Practical Bayesian Optimization of Machine Learning Algorithms

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jasper Snoek、Hugo Larochelle、Ryan P. Adams
- 年份与版本：NIPS 2012 论文集第 25 卷；预印本首发于 2012-06-13，v2 更新于 2012-08-29。按会议年份归档。
- 原始来源：[论文页面](https://proceedings.neurips.cc/paper/2012/hash/05311655a15b75fab86956663e1819cd-Abstract.html)
- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2012-practical-bayesian-optimization.pdf)（NIPS 2012 会议论文集版，9 页）。
- 官方代码：[第一作者的 Spearmint 仓库](https://github.com/JasperSnoek/spearmint)。本次核对仓库说明，未运行实验。

## 解决的问题

一次训练可能占用数小时。已经知道几组超参数的验证误差后，下一次训练该试哪里？如果不同配置的耗时相差很大，怎样让同样的机器时间带来更多改进？

## 主要方法

用高斯过程描述超参数到验证误差的函数，根据已有试验更新均值与不确定性，再用期望改进选择下一组配置。论文还讨论按预计运行时间衡量改进，以及并行试验中如何把尚未返回的结果纳入决策。

## 贡献与局限

论文把代理模型的核函数、核参数的不确定性和训练耗时放进同一套实验比较。作者在包括卷积网络在内的任务上报告了收益。阅读这些结果时，应核对预算单位：固定试验次数与固定墙钟时间回答的是不同的问题。

## 前置知识与阅读重点

先掌握验证集误差、高斯过程后验和期望改进。读并行策略时，可以设想两台机器中已有一台正在训练：第二台应如何利用这个仍未完成的试验？

## 收录理由

补齐历史清单中的贝叶斯优化方法。配合随机搜索阅读，可以比较独立抽样与利用历次验证结果选点各自需要什么信息。

## 相关主题与版本

[随机搜索导读](2012-random-search.md) · [arXiv 版本记录](https://arxiv.org/abs/1206.2944)。
