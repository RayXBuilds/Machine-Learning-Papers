---
id: auditing-ai-peer-reviewers
primary_topic: evaluation
tags: [peer-review, error-detection, benchmarks, llm-evaluation]
type: paper
added: 2026-11-17
verified: 2026-11-17
source: https://arxiv.org/abs/2611.17052
status: summary
---

# Auditing AI peer reviewers: a benchmark on real scientific papers

- 作者：Íñigo Zubeldia、Boris Bolliet、Francisco Villaescusa-Navarro、Pablo Villanueva-Domingo、Miles Cranmer。
- 年份与版本：2026 按 arXiv v1 年份，首次提交于 2026-11-12（UTC），核对时为 v1。作者书目注明已被 NeurIPS 2026 接收，正式会议出版页尚未独立核实。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.17052) · [v1 正文](https://arxiv.org/html/2611.17052v1)。
- 官方代码：[Skepthical Benchmark](https://github.com/inigozubeldia/skepthical-benchmark)，含评估流程、错误清单及裁判日志。本库未运行代码。

## 解决的问题

AI 审稿系统能否检出客观错误，又会产生多少误报？论文将审稿能力拆成可定位的缺陷检测任务。[摘要](https://arxiv.org/abs/2611.17052)

## 主要方法

向天体物理与机器学习论文注入四类、三级严重度错误，分别测量检出情况及原始副本上的误报。配套 Skepthical 使用引用检索、计算机代数与代码执行辅助核查。[基准设计](https://arxiv.org/html/2611.17052v1)

## 贡献与局限

作者发现工具收益随领域变化：强制引用检索在天体物理上的优势未在机器学习中显著重现。每领域仅 15 篇论文，裁判主要依赖 LLM，人工检查只覆盖一篇的检出任务。系统间计算预算也未匹配，不能单独归因于流程设计。基准不衡量创新性等整体审稿质量。[讨论与局限](https://arxiv.org/html/2611.17052v1)

## 前置知识与阅读重点

建议了解错误检测、误报统计与 LLM 裁判。重点检查误报率分母、严重度分组、裁判一致性及模型与工具配置的对照方式。

## 收录理由

补充科研评估专题，让审稿工具的选择建立在检出与误报证据上。

## 相关主题与版本

- arXiv ID：`2611.17052`。书目页列 DOI `10.48550/arXiv.2611.17052`，注明待注册。
- 主文件归入[评估与实验方法](README.md)，相关方向为[自然语言处理与大语言模型](../nlp/README.md)。
- 本条核对书目、基准设计、局限及官方仓库，未进行全文精读或实验复现。
