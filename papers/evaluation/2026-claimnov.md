---
id: claimnov
primary_topic: evaluation
tags: [novelty-evaluation, scientific-discovery, retrieval]
type: paper
added: 2026-10-29
verified: 2026-10-29
source: https://arxiv.org/abs/2610.36511
status: summary
---

# Do AI Scientists Know What's New?

- 作者：Miri Liu、Xiayu Zhao、Encheng Xie、ChengXiang Zhai。
- 年份与版本：2026-10-27 首次提交，arXiv v1；预印本，未核实正式接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.36511) · [正文](https://arxiv.org/html/2610.36511v1)。
- 官方代码：[ClaimNov 作者仓库](https://github.com/emmatliu/claimnov)，已见源码、数据与评估目录；本次未安装运行。

## 解决的问题

AI 科研系统如何识别重复想法，同时保留含有新贡献的研究提案？整篇判定容易把局部已有成果误当作整项研究缺乏新意。

## 主要方法

ClaimNov 按贡献主张拆解提案，检索相关工作、判断主张蕴含关系，再汇总新颖性。作者构建覆盖整篇和主张层面的四组评估数据，以时间关系辅助界定先前工作。[方法与评估](https://arxiv.org/html/2610.36511v1)

## 贡献与局限

把新颖性检查变成可追踪到具体主张和文献的判断。论文报告在其测试集上改善重复识别与误拒之间的权衡；但仅研究英文 AI 文献，先前文献池固定，不能据此确认开放网络检索能力。标签也含启发式与模型辅助判断。已核对方法概述和限制章节，未复现。

## 前置知识与阅读重点

理解信息检索、文本蕴含与假阳性。重点检查时间截断、候选文献池以及“部分新颖”标签，区分检索失败和判断失败。

## 收录理由

补充科研智能体评估方法，强调发现重复与保留有效新贡献需要同时衡量。

## 相关主题与版本

arXiv ID：`2610.36511`；年份采用首次预印本年份。主主题为评估，语言模型与检索作为跨主题标签。
