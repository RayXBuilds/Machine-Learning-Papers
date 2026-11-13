---
id: sempair
primary_topic: applications
tags: [remote-sensing, multimodal, pretraining, semantic-pairing]
type: paper
added: 2026-11-13
verified: 2026-11-13
source: https://arxiv.org/abs/2611.13807
status: summary
---

# Relaxing Cross-Modal Correspondence for Multimodal Remote Sensing Pretraining

- 作者：Xianping Ma、Yu Zhang、Mingzhe Jiang、Wanxin Xie、Qing Zhu、Nan Xu、Xiaokang Zhang、Yuanxin Ye。
- 年份与版本：2026 按 arXiv v1 年份。首次提交于 2026-11-10（UTC），核对时为 v1。预印本，未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目页](https://arxiv.org/abs/2611.13807) · [v1 正文](https://arxiv.org/html/2611.13807v1)。
- 官方代码：截至核对日，未在上述原始来源中找到本论文的官方代码链接。

## 解决的问题

遥感多模态预训练常依赖逐实例配对的数据。论文考察放宽配对粒度后，表示能否仍然迁移到下游任务。[摘要](https://arxiv.org/abs/2611.13807)

## 主要方法

SemPair 将另一模态的搭档换成同类别的不同实例。MixPair 调节精确配对的比例，在固定模型、目标和训练预算下比较迁移效果。潜变量分析区分共享语义与实例相关性。[方法](https://arxiv.org/html/2611.13807v1)

## 贡献与局限

作者报告四个遥感分割基准上的表现与精确配对相近，增加精确配对比例也未带来单调改善。实验仍依赖类别标签，在已知 RGB 与伪深度配对的数据中重采样，下游光学影像与 DSM 仍对齐。独立采集档案、配准等任务的适用性尚待验证。[实验与讨论](https://arxiv.org/html/2611.13807v1)

## 前置知识与阅读重点

建议了解多模态融合、迁移学习与语义分割。重点检查训练标签如何决定搭档，以及预训练和下游阶段各自保留了哪些对应关系。

## 收录理由

补充遥感领域的数据组织问题，为审视配对成本与迁移目标提供阅读案例。

## 相关主题与版本

- arXiv ID：`2611.13807`。书目页列 DOI `10.48550/arXiv.2611.13807`，并注明待注册。
- 主文件归入[领域应用](README.md)，相关方向为[多模态学习](../multimodal/README.md)。
- 本条核对书目、方法和局限，属原创简短导读，未进行全文精读或实验复现。
