---
id: evalalloc
primary_topic: evaluation
tags: [evaluation-budget, agents, adaptive-sampling]
type: paper
added: 2026-10-30
verified: 2026-10-30
source: https://arxiv.org/abs/2610.37276
status: summary
---

# Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?

- 作者：Sichun Luo、Yi Huang、Mukai Li、Haochen Luo、Guanzhi Deng、Haibo Wang、Jian Xu、Zefa Hu、Junlan Feng、Qi Liu。
- 年份与版本：2026-10-27 首次提交，arXiv v1；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.37276) · [v1 正文](https://arxiv.org/html/2610.37276v1)。
- 官方代码：本次核对的书目页与正文未提供作者代码入口；未验证可运行实现。

## 解决的问题

智能体工作流迭代时，评估既用于引导搜索，又用于选出最终候选。对所有候选执行完整测试很昂贵，如何分配有限评估预算？

## 主要方法

EvalAlloc 先完整评估少量预热候选，建立共享的信息性题目集合和响应模型；搜索阶段用稀疏反馈维持可比评分，最后复用已有观测，通过配对逐次减半筛选候选，只补做缺失评估。[方法第 5 节](https://arxiv.org/html/2610.37276v1)

## 贡献与局限

将搜索反馈和最终确认拆开分配预算，并关注候选之间的公平比较。作者在四个基准、两个演化框架中报告多数设置下更好的平均性能与更少评估单元。编者提醒：评估单元数不等于 token 费用或实际耗时，节省比例也不能直接套用到其他工作流。已核对方法与实验概述，未复现。

## 前置知识与阅读重点

了解候选搜索、抽样误差和逐次减半。阅读时检查共享题目如何选取、稀疏分数如何校准，以及搜索集与独立测试集的边界。

## 收录理由

补充评估成本控制方法，强调搜索过程中可用的反馈与最终选择所需证据具有不同精度要求。

## 相关主题与版本

arXiv ID：`2610.37276`；年份采用首次预印本年份。正文方法名为 EvalAlloc，摘要中的未展开排版宏不作为方法名。主文件归评估，以 agents 标签连接智能体方向。
