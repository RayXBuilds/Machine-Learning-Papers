---
id: listen-attend-and-spell
primary_topic: nlp
catalog_year: 2015
subtopic: "序列建模与预训练"
updated: 2026-11-27
tags: [speech-recognition, attention, sequence-to-sequence]
type: paper
added: 2026-11-27
verified: 2026-11-27
source: https://arxiv.org/abs/1508.01211v2
status: summary
---

# Listen, Attend and Spell

[主题目录](README.md) · [年份导航](../../docs/years/README.md)

- 作者：William Chan、Navdeep Jaitly、Quoc V. Le、Oriol Vinyals
- 年份与版本：按 2015 年预印本归档。arXiv 首发于 8 月 5 日，本次收录 8 月 20 日发布的 v2。
- 原始来源：[arXiv 版本页](https://arxiv.org/abs/1508.01211v2) · [Google Research 论文页](https://research.google/pubs/listen-attend-and-spell/)
- 仓库内 PDF：[预印本 v2，16 页](../../pdfs/nlp/2015-listen-attend-and-spell.pdf)
- 官方代码：上述两个来源均未列出配套实现。

## 解决的问题

一段语音有数百帧，转写却可能只有几十个字符，训练数据通常也没有标出每个字符从哪一帧开始。能否只用录音和对应文本，让模型同时学会对齐和拼写？

## 主要方法

Listener 用金字塔形双向循环网络编码声学特征。越往上，相邻时间步越多地被合并，解码器需要检索的序列也越短。Speller 每生成一个字符，就根据解码状态给各段声学表示分配权重，结合加权得到的声音信息和已经生成的字符预测下一个字符。

## 贡献与局限

在 Google 语音搜索的一个子集上，作者报告 LAS 单独解码的词错误率为 14.1%。用外部语言模型对 32 个候选转写重新排序后降至 10.3%，同一实验中的混合系统为 8.0%。因此，比较识别系统时应注明是否使用外部文本资源。双向编码还要读取后续语音，这套实验不能直接说明实时听写的延迟。

## 前置知识与阅读重点

先读[序列到序列学习](2014-seq2seq.md)和[注意力对齐](2015-bahdanau-attention.md)。阅读注意力热图时，选取一个输出字符，沿输入时间轴找出权重集中的位置，再观察下一个字符的关注点怎样移动。这些权重是模型学出的软对齐，训练时无需提供逐字符时间戳。

## 收录理由

这篇工作把库中已有的序列建模方法带到语音转写。它提供了一个具体例子，可以分别讨论三个问题：如何压缩长输入、如何学习对齐，以及如何衡量外部语言模型对最终结果的影响。

## 相关主题与版本

预印本标识为 arXiv:1508.01211。后续 ICASSP 2016 会议版题为 *Listen, attend and spell: A neural network for large vocabulary conversational speech recognition*。[会议版 DOI](https://doi.org/10.1109/ICASSP.2016.7472621)。本文数字取自预印本 v2，未做实验复现。
