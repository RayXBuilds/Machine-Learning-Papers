---
id: lista
primary_topic: deep-learning
tags: [sparse-coding, optimization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://icml.cc/2010/papers/449.pdf
status: summary
catalog_year: 2010
subtopic: "表征与自监督"
updated: 2026-11-21
---

# Learning Fast Approximations of Sparse Coding

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Karol Gregor、Yann LeCun
- 年份与版本：ICML 2010。
- 原始来源：[论文入口](https://icml.cc/2010/papers/449.pdf)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

## 解决的问题

每来一个样本都要迭代求解带 L1 惩罚的重构问题，在线提取稀疏特征的成本很高。

## 主要方法

把迭代软阈值步骤展开成固定层数的编码器，用求解器给出的编码训练层间映射。论文还给出从坐标下降构造的另一种网络。

## 贡献与局限

固定深度让推理成本可预估，也可以用预测值初始化后续求解。编者判断，换字典或换数据分布时，应重新测量近似误差。

## 前置知识与阅读重点

先掌握稀疏字典与软阈值算子。按相同近似误差比较计算量，区分两种网络各自的加速结果。

## 收录理由

可从一次迭代更新直接读懂一层网络如何设计。

## 相关主题与版本

[主主题：深度学习与表征学习](README.md) · [延伸主题：数学、学习理论与概率模型](../foundations/README.md)

本条依据原始书目和论文内容整理，未复现实验。
