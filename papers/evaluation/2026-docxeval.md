---
id: docxeval
primary_topic: evaluation
tags: [explainability, multimodal, document-understanding]
type: paper
added: 2026-10-30
verified: 2026-10-30
source: https://arxiv.org/abs/2610.36929
status: summary
---

# DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding

- 作者：Saifullah Saifullah、David Dembinsky、Stefan Agne、Andreas Dengel、Sheraz Ahmed（按 arXiv 书目记录）。
- 年份与版本：2026-10-27 首次提交，arXiv v1；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.36929) · [v1 正文](https://arxiv.org/html/2610.36929v1)。
- 官方代码：[作者仓库](https://github.com/saifullah3396/docxeval/)，已见源码、实验脚本和环境说明；本次未安装或执行。

## 解决的问题

文档模型同时利用文本、版面与图像，单看解释热图难以判断归因是否可信。如何在统一流程中比较解释方法及其评价指标？

## 主要方法

DocXEval 将解释方法和指标适配到多模态文档输入，并支持实体识别等多目标任务。研究比较 13 种解释方法和 17 项指标，还检查指标之间的一致性，分析不同模态及空间位置的归因。[框架与实验](https://arxiv.org/html/2610.36929v1)

## 贡献与局限

提供统一比较与诊断流程，扩展本库可解释性专题。作者报告遮挡法在其设置下总体表现较好，但并非所有指标一致；实验仅覆盖四个 Transformer 模型，其中两个为文档专用多模态模型，结论不宜推广到所有架构。已核对相关正文与限制章节，未复现实验。

## 前置知识与阅读重点

了解特征归因、输入扰动和文档模型。重点检查特征分组、扰动基线与目标选择，区分解释是否忠实于模型和解释是否符合人的直觉。

## 收录理由

补充解释方法本身的验证工具，避免仅凭可视化效果选择解释器。

## 相关主题与版本

arXiv ID：`2610.36929`；年份采用首次预印本年份。主文件归评估；多模态与文档理解通过标签关联。作者列表按论文书目页核对，仓库 README 的简略署名不替代论文署名。
