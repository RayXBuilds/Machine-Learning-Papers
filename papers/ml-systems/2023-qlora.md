---
id: qlora
primary_topic: ml-systems
tags: [quantization, low-rank-adaptation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html
status: summary
catalog_year: 2023
subtopic: "高效训练与环境接口"
updated: 2026-11-21
---

# QLoRA: Efficient Finetuning of Quantized LLMs

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Tim Dettmers、Artidoro Pagnoni、Ari Holtzman、Luke Zettlemoyer。
- 年份与版本：NeurIPS 2023。arXiv 首版提交于 2023-05-23。
- 原始来源：[NeurIPS 2023 书目](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html) · [arXiv 版本记录](https://arxiv.org/abs/2305.14314)。
- 官方代码：已核对[作者项目仓库](https://github.com/artidoro/qlora)。

## 解决的问题

微调大模型时，单卡显存究竟被基础权重、可训练参数还是优化器占用？

## 主要方法

冻结以 NF4 存储的基础权重，让梯度经反量化计算传到低秩适配器。双重量化压缩量化常数，分页优化器处理显存峰值。

## 贡献与局限

作者报告单张 48 GB 显卡可微调 65B 模型。该预算依赖训练设置，不能直接当作任意上下文长度的容量承诺。

## 前置知识与阅读重点

先读 LoRA，再画出权重存储精度与乘法计算精度；查看改变适配层范围后任务表现如何变化。

## 收录理由

补上从低秩微调到量化训练的显存账本。

## 相关主题与版本

arXiv:2305.14314。[正式 DOI 10.52202/075280-0441](https://doi.org/10.52202/075280-0441)。可对读 [LoRA](../nlp/2021-lora.md)。本导读依据原始书目与摘要整理，未复现实验。
