---
id: hinted-scaling-laws
primary_topic: evaluation
tags: [scaling-laws, benchmark-design, nlp, model-ranking]
type: paper
added: 2026-11-07
verified: 2026-11-07
source: https://arxiv.org/abs/2611.02270
status: summary
---

# Hinted Scaling Laws

- 作者为 Suze van Adrichem、Luke Bailey、Rohith Kuditipudi、Christine Ye、Neil Band、Ahmed Ahmed、John Duchi、Percy Liang、Tatsunori Hashimoto。
- 年份采用预印本 v1 的 2026 年，首次提交于 2026-11-01（UTC），当前核对版本为 v1。状态为 arXiv 预印本，正式会议或期刊接收信息待核实。[书目页](https://arxiv.org/abs/2611.02270)
- 原始正文提供方法、实验及讨论章节。[arXiv HTML](https://arxiv.org/html/2611.02270v1)
- 官方代码由原文链接确认，已核对 README 中的结果重绘和数据生成入口，实验运行待开展。[tatsu-lab/hinted-scaling-laws](https://github.com/tatsu-lab/hinted-scaling-laws)

## 解决的问题

困难基准上，小模型准确率接近零，直接从这些得分外推大模型表现容易缺少有效信号。论文研究如何让低计算量实验提供下游准确率的预测依据。[摘要](https://arxiv.org/abs/2611.02270)

## 主要方法

通过提供部分参考解答、遮蔽解答词语或混合教师模型 logits，连续调节提示强度 H。用小模型在各强度下的表现拟合规模 C 与提示 H 的联合函数，再取 H=0 预测大模型在原基准上的准确率。logit 混合要求师生共享词表。[方法](https://arxiv.org/html/2611.02270v1)

## 贡献与局限

作者在 GSM8K、AIME 和 HLE 的所测模型族上报告，预测绝对误差的中位数由基线的 21 个百分点降至 4.3 个百分点。该结果限定于论文实验组合。[摘要](https://arxiv.org/abs/2611.02270)

方法连接了基准难度调节与规模外推，也研究低采样预算下的模型排序。局限包括对可靠参考解答的依赖，以及所测五个模型族中仅 Delphi 使用统一数据配方构建规模阶梯。简单联合函数的外推适用范围仍需检验。[讨论](https://arxiv.org/html/2611.02270v1)

## 前置知识与阅读重点

先了解 sigmoid 拟合、缩放定律、抽样误差与排序相关性。重点核查参考解答的答案泄漏处理、保留大模型的验证方式，以及不同提示形式的教师成本。代码提供已发布结果的绘图脚本与重新生成采样结果的入口，复现时可从结果文件及拟合参数开始核对。[代码说明](https://github.com/tatsu-lab/hinted-scaling-laws/blob/main/README.md)

## 收录理由

扩展评估维护队列中低预算性能估计的方向，提供在零分附近设计测量信号的具体案例。编者建议结合已有 FAQ 导读比较各自的预测目标与假设。

## 相关主题与版本

主主题为[评估与实验方法](README.md)，相关方向为[NLP 与大语言模型](../nlp/README.md)，可对照 [FAQ 导读](2026-factorized-active-querying.md)。唯一标识为 arXiv:2611.02270，页面列出的 DOI 为 `10.48550/arXiv.2611.02270`，标记待注册。已核对书目、相关方法、讨论和官方代码 README，阅读状态为导读，实验复现待开展。
