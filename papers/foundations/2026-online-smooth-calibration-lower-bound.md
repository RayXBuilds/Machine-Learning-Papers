---
id: online-smooth-calibration-lower-bound
primary_topic: foundations
tags: [calibration, online-learning, minimax, probability]
type: paper
added: 2026-11-14
verified: 2026-11-14
source: https://arxiv.org/abs/2611.16097
status: summary
---

# A Matching Lower Bound for Online Smooth Calibration

- 作者：Kaixuan Ji、Quanquan Gu。
- 年份与版本：2026 按预印本 v1 年份。首次提交于 2026-11-11 23:13 UTC，核对时为 v1。未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.16097) · [v1 正文](https://arxiv.org/html/2611.16097v1)。
- 官方代码：未在上述原始来源中找到本论文的官方代码链接。

## 解决的问题

序贯二元预测中，平滑校准误差用 Lipschitz 测试函数度量预测残差。论文研究面对自适应对手时，任何预测器都无法避免多大的误差。[摘要](https://arxiv.org/abs/2611.16097)

## 主要方法

构造随累计残差调整伯努利均值的对手，残差到阈值后固定后续结果。结合常数与仿射测试，分析预测器抵消历史残差所付出的代价。[第 4 节](https://arxiv.org/html/2611.16097v1)

## 贡献与局限

作者给出期望平滑校准误差的 Ω(√T) 下界，与已知上界匹配，并推出两种校准距离的对应下界。结论采用累计误差口径，限于双方依据历史同时行动的二元预测协议。编者提醒：不能直接用它解释独立同分布测试集上的分箱 ECE。[定理与协议](https://arxiv.org/html/2611.16097v1)

## 前置知识与阅读重点

建议了解条件期望、停时和极小极大分析。重点核对对手可见的信息、误差是否除以轮数，以及早停后残差为何无法抵消。

## 收录理由

补充概率校准专题的理论边界，连接指标定义与在线学习中的不可能性结果。

## 相关主题与版本

- arXiv ID：`2611.16097`。书目页列 DOI `10.48550/arXiv.2611.16097`，注明待注册。
- 主文件归入[数学、学习理论与概率模型](README.md)，相关主题为[评估与实验方法](../evaluation/README.md)。
- 本条核对书目、协议及主定理陈述，未独立验证完整证明或复现实验。
