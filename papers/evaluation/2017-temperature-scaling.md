---
id: temperature-scaling
primary_topic: evaluation
tags: [calibration, temperature-scaling, deep-learning]
type: paper
added: 2026-10-26
verified: 2026-10-26
source: https://proceedings.mlr.press/v70/guo17a.html
status: summary
---

# On Calibration of Modern Neural Networks

[主题目录](README.md) · [首页](../../README.md)

- 作者：Chuan Guo、Geoff Pleiss、Yu Sun、Kilian Q. Weinberger。
- 年份与版本：2017 · ICML，PMLR 70:1321–1330；按正式会议版年份收录。
- 原始来源：[原文入口](https://proceedings.mlr.press/v70/guo17a.html)。
- 官方代码：[作者实现](https://github.com/gpleiss/temperature_scaling)；作者标注已停止维护，适合作为方法示例。
- 核对日期：2026-10-26；本条为摘要与指定章节导读，未宣称全文精读。

## 解决的问题

分类准确率高，并不代表输出概率能反映真实正确率。本文研究神经网络的置信度校准。

## 主要方法

比较多种训练因素与后处理校准方法；Temperature Scaling 在验证集上拟合一个温度参数，调整 softmax 前的 logits。方法实现以负对数似然为拟合目标。

## 贡献与局限

提供简洁、可对照的校准基线。论文结果来自当时的图像与文本分类实验；编者提醒：这些结果不能直接保证任意分布偏移下的校准效果。

## 前置知识与阅读重点

先了解 softmax、交叉熵和独立验证集；重点区分分类正确率与概率可靠性，思考为何调温度可能改变置信度却不改变类别排序。

## 收录理由

补齐仓库概率校准基础，作为本日三篇近期研究的入门阅读。

## 相关主题与版本

相关主题：深度学习、模型评估。原文与作者代码均已核对；本文是方法导读，未复现实验。
