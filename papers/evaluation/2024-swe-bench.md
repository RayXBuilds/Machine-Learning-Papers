---
id: swe-bench
primary_topic: evaluation
tags: [software-engineering, benchmarks]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html
status: summary
catalog_year: 2024
subtopic: "模型评审与评估预算"
updated: 2026-11-21
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Carlos E. Jimenez、John Yang、Alexander Wettig、Shunyu Yao、Kexin Pei、Ofir Press、Karthik Narasimhan。
- 年份与版本：ICLR 2024。arXiv 首版提交于 2023-10-10。正式发表在次年；此处讨论原始基准，后续子集另有版本。
- 原始来源：[ICLR 2024 书目](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) · [arXiv 版本记录](https://arxiv.org/abs/2310.06770)。
- 官方代码：已核对[作者项目仓库](https://github.com/SWE-bench/SWE-bench)。

- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2024-swe-bench.pdf)（会议论文集版（proceedings.iclr.cc））。

## 解决的问题

单函数代码题的分数能否反映修复真实代码库问题的能力？

## 主要方法

从 GitHub 问题及对应拉取请求构造任务，给定问题说明和历史代码快照，执行测试检验候选补丁。

## 贡献与局限

原始集合涵盖 12 个 Python 项目中的 2,294 个问题。测试覆盖和仓库构成限制了分数所能说明的能力。

## 前置知识与阅读重点

熟悉版本控制与回归测试即可。查看一次任务中修复前失败的测试以及修复前后均须通过的测试。

## 收录理由

把以执行结果验证的评估与文本匹配指标放在一起比较。

## 相关主题与版本

arXiv:2310.06770。本导读依据原始书目与摘要整理，未复现实验。
