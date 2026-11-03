---
id: imrouter
primary_topic: data-mining
tags: [time-series, imbalanced-learning, mixture-of-experts]
type: paper
added: 2026-11-03
verified: 2026-11-03
source: https://arxiv.org/abs/2610.39246
status: summary
---

# IMRouter: Imbalance-aware Temporal Pattern Routing for LLM-based Time Series Forecasting

- 作者：Xin Yang、Cai Xu、Haishun Chen、Ying Liu、Jie Zhao、Wei Zhao、Ziyu Guan。
- 年份与版本：2026-10-29 首次提交，arXiv v1；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.39246) · [v1 正文](https://arxiv.org/html/2610.39246v1)。
- 官方代码：原始书目与正文未发现作者实现入口，补充检索亦未核实官方仓库；未运行实现。

## 解决的问题

平均预测误差可能掩盖低频时序模式上的较大误差。IMRouter 研究不同局部模式出现频率不均时，如何减少高频模式对表示学习及语言模型对齐过程的支配。

## 主要方法

PATR 通过梯度冲突与局部梯度密度引导专家路由，降低不兼容片段共用专家的倾向，并提高低密度优化信号的权重。RGSA 用互信息目标将路由中的模式信息传递到时序与文本原型的对齐表示。[方法第 4 节](https://arxiv.org/html/2610.39246v1)

## 贡献与局限

将模式不平衡同时联系到专家分工和跨模态对齐。作者在七个长期预测基准及其他设置中报告效果，并在 Traffic 的模式分组中比较误差。

编者判断：用于分析的模式簇是表示与聚类产生的代理标签，结论应结合模式划分方式理解；低频模式也不等同于异常值或极端事件。基准上的平均改进不保证所有预测跨度、低频模式或真实部署均受益，新增路由机制的成本仍需实践核查。

已核对摘要、方法及实验范围，未精读全部推导或复现实验。

## 前置知识与阅读重点

了解滑动窗口预测、均方误差、混合专家和跨注意力。重点区分用于分析的模式聚类与训练时的梯度路由，比较整体误差、分组误差及去除密度加权后的消融结果。

## 收录理由

补齐数据挖掘主题的时序预测导读，提供从样本频率分布审视预测误差的近期方法案例。

## 相关主题与版本

arXiv ID：`2610.39246`；文件年份采用首次预印本年份。主要任务为时序预测，归数据挖掘；通过 mixture-of-experts 标签关联深度学习，不复制主文件。
