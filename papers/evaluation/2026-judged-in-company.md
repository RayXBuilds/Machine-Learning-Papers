---
id: judged-in-company
primary_topic: evaluation
tags: [llm-as-judge, batch-prompting, robustness]
type: paper
added: 2026-11-02
verified: 2026-11-02
source: https://arxiv.org/abs/2610.40241
status: summary
---

# Judged in Company: In-Context Batching Makes LLM Verdicts Depend on Other Items

- 作者：Peng Xie、Amr Alanwar。
- 年份与版本：2026-10-29 首次提交，arXiv v1；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2610.40241) · [v1 正文](https://arxiv.org/html/2610.40241v1)。
- 官方代码：正文列出 [PX-CPS/Judged_in_company](https://github.com/PX-CPS/Judged_in_company)，并使用未来发布措辞；2026-11-02 打开仓库及读取 README 均返回 404，尚未核实公开可用实现，未复现。

## 解决的问题

将独立条目合并进同一提示词可以减少重复指令，但某条内容的评分是否会随同批内容及位置改变？整体准确率接近，并不保证逐条判断稳定。

## 主要方法

在有害评论、简答题评分和评论星级任务中，固定条目，改变批次成员、邻居顺序及条目位置，并设置改名、改写指令等对照。作者分解判断翻转的来源，另通过编辑生成中的先前判断与邻居文本检验影响渠道。

## 贡献与局限

把评价重点从汇总指标扩展到单条决策的一致性。作者在所测模型与任务上发现重分批次会改变判断，排列投票不能完全消除影响；翻转率并非错误率，单条评分也不是人工真值。[摘要与结果](https://arxiv.org/abs/2610.40241)

主要设计限于三个英文任务、特定提示模板、JSON 输出和贪心解码；较大模型只重复部分实验。潜在评分及投票预测还依赖阈值模型假设，不能直接外推至所有模型或部署方式。[局限](https://arxiv.org/html/2610.40241v1)

已核对方法、结果概述与局限，未逐项审阅证明或复现实验。

## 前置知识与阅读重点

了解 LLM 裁判、分类阈值及方差分解。重点区分提示词内合并条目与服务端独立请求批处理，并检查单条基线、数值噪声对照及投票后残留差异。

## 收录理由

补充评估流程中的上下文干扰问题，提醒低成本批量评分除汇总精度外，还应核对条目级稳定性。

## 相关主题与版本

arXiv ID：`2610.40241`；页面列出 DOI `10.48550/arXiv.2610.40241`，检索时标注 pending registration，未单独确认注册完成。文件年份采用首次预印本年份。主文件归评估，通过 llm-as-judge 标签关联 NLP。
