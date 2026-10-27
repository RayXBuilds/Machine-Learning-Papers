---
id: em-algorithm
primary_topic: foundations
tags: [latent-variables, maximum-likelihood, probabilistic-models]
type: paper
added: 2026-10-27
verified: 2026-10-27
source: https://academic.oup.com/jrsssb/article-abstract/39/1/1/7027539
status: summary
---

# Maximum Likelihood from Incomplete Data Via the EM Algorithm

- 作者：A. P. Dempster、N. M. Laird、D. B. Rubin。
- 年份与版本：1977 年，Journal of the Royal Statistical Society: Series B (Methodological)，39(1)：1–22，正式期刊论文。出版页另列 2018-12-05 在线发布日，文件年份采用原卷期年份 1977。
- 原始来源：[出版方书目与摘要](https://academic.oup.com/jrsssb/article-abstract/39/1/1/7027539) · [DOI](https://doi.org/10.1111/j.2517-6161.1977.tb01600.x)。
- 官方代码：本次核对的出版页未提供作者代码。

## 解决的问题

存在缺失数据或潜变量时，如何系统地计算最大似然估计？

## 主要方法

EM 用迭代方式处理不完整数据的估计问题。理解算法时可从两步入手：在当前参数下对完整数据对数似然取条件期望，再最大化该目标以更新参数。出版摘要列举了混合模型、缺失值及因子分析等应用。

## 贡献与局限

原文摘要讨论似然的单调性与收敛性，给出统一算法框架。本次仅核对书目与摘要，未核对全文证明或复现。编者阅读提醒：似然单调改进不能直接等同于任意初值都得到全局最优，需结合具体假设阅读。

## 前置知识与阅读重点

先掌握条件期望、似然与潜变量。建议用两成分混合模型理解隐变量，再检查每一步优化的对象和停止条件。

## 收录理由

补齐维护队列中的 EM，为概率模型和含缺失观测的学习问题建立原始文献入口。

## 相关主题与版本

DOI：`10.1111/j.2517-6161.1977.tb01600.x`。页码采用出版方正文记录 1–22，不与后续讨论混为一篇；在线上线日期不替代原始发表年份。
