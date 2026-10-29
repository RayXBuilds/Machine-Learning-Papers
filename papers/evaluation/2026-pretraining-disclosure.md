---
id: pretraining-disclosure
primary_topic: evaluation
tags: [transparency, documentation, language-models]
type: paper
added: 2026-10-29
verified: 2026-10-29
source: https://arxiv.org/abs/2610.37465
status: summary
---

# What Carries Forward? Pretraining Disclosure Across Language Model Releases

- 作者：Md Sakib Ul Islam、S M Mehedi Zaman。
- 年份与版本：2026-10-27 首次提交，arXiv v1；预印本，未核实正式接收信息。日期沿用 arXiv 页面，收录日期另按北京时间记录。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.37465) · [正文与附录](https://arxiv.org/html/2610.37465v1)。
- 官方代码：所核论文页面未找到本研究的独立作者代码入口；文中被审计模型和 FMTI 的链接不作为本论文官方实现。

## 解决的问题

语言模型不断发布新版本，但关于预训练数据、处理过程和算力的披露是否得到延续？总分能否掩盖具体信息的缺失？

## 主要方法

用 FMTI 的 24 项预训练指标审计 17 个家族的 41 个模型条目，并在家族内比较相邻版本的逐项增减。证据来自公开文档，沿用旧版本说明须确认其适用关系。[方法与附录](https://arxiv.org/html/2610.37465v1)

## 贡献与局限

研究提醒读者：总分持平或提高，仍可能伴随某类披露丢失。它测量文档披露，不直接证明数据质量、可复现性或实际训练实践；等权二元评分会丢失细节，顺序复核也不提供独立标注一致性估计。已核对书目、相关方法及限制，未重做审计。

## 前置知识与阅读重点

了解模型卡、预训练流程和指标设计。关注版本继承证据、信息缺失与实践变化的区别，以及单项分数如何被总分掩盖。

## 收录理由

扩展评估目录中的文档审计方法，为判断模型版本之间哪些信息可以沿用提供参考。

## 相关主题与版本

arXiv ID：`2610.37465`；年份采用首次预印本年份。论文模型文档检索截止 2026-08-29，不能将结果当作收录当日模型披露状态。
