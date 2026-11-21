---
id: wilds
primary_topic: evaluation
tags: [distribution-shift, benchmark]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/2012.07421
status: summary
---

# WILDS: A Benchmark of in-the-Wild Distribution Shifts

- 作者：Pang Wei Koh、Shiori Sagawa、Henrik Marklund、Sang Michael Xie、Marvin Zhang、Akshay Balsubramani、Weihua Hu、Michihiro Yasunaga、Richard Lanas Phillips、Irena Gao、Tony Lee、Etienne David、Ian Stavness、Wei Guo、Berton Earnshaw、Imran Haque、Sara M Beery、Jure Leskovec、Anshul Kundaje、Emma Pierson、Sergey Levine、Chelsea Finn、Percy Liang。
- 年份与版本：按 ICML 2021 正式发表年份归档。arXiv 初稿提交于 2020 年 12 月。
- 原始来源：[ICML 会议版](https://proceedings.mlr.press/v139/koh21a) · [作者预印本](https://arxiv.org/abs/2012.07421)。
- 官方代码：[作者项目](https://github.com/p-lambda/wilds)。

## 解决的问题

随机切分得到的分数能否反映跨医院、跨地区等实际部署差异？

## 主要方法

将有自然环境标记的数据组织成十项任务，针对不同偏移设置训练测试域、组别及相应指标。

## 贡献与局限

基线在若干域外测试上明显退化。各任务的域定义、标签和指标不同，跨任务解释提升前应检查切分规则。

## 前置知识与阅读重点

先了解域泛化与子群评估。挑一项任务列出训练域、测试域、平均指标和最差组指标的适用条件。

## 收录理由

为评估目录补充由部署场景决定数据切分的基准。

## 相关主题与版本

arXiv:2012.07421。延伸阅读见 [ImageNetV2](../evaluation/2019-imagenetv2.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
