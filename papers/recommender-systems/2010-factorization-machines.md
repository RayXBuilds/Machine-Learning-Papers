---
id: factorization-machines
primary_topic: recommender-systems
tags: [feature-interactions, factorization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://doi.org/10.1109/ICDM.2010.127
status: summary
---

# Factorization Machines

- 作者：Steffen Rendle
- 年份与版本：ICDM 2010。
- 原始来源：[论文入口](https://doi.org/10.1109/ICDM.2010.127)
- 官方代码：[作者项目](https://www.libfm.org/)

## 解决的问题

用户、物品与上下文构成高维稀疏向量时，很多特征对几乎从未共同出现，怎样估计其交互？

## 主要方法

给每个特征分配隐向量，以两个隐向量的内积表示二阶交互系数。重排二重求和后可按非零特征数线性计算预测值。

## 贡献与局限

共享因子让罕见组合也能借用其他观测。编者判断，潜在维数限制模型能表达的交互结构，稀疏性本身无法保证泛化。

## 前置知识与阅读重点

先了解二次回归与矩阵分解。把一个用户和一个物品写成独热特征，再加上下文，比较新增了哪些内积项。

## 收录理由

把推荐中的用户—物品分解推广到上下文交互，便于理解后续深度推荐模型。

## 相关主题与版本

[主主题：推荐系统](README.md) · [延伸主题：传统机器学习](../classical-ml/README.md) · [DOI 10.1109/ICDM.2010.127](https://doi.org/10.1109/ICDM.2010.127)

本条依据原始书目和论文内容整理，未复现实验。
