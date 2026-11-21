---
id: phipict
primary_topic: applications
tags: [scientific-machine-learning, differentiable-simulation, flow-control, inverse-design]
type: paper
added: 2026-11-18
verified: 2026-11-18
source: https://arxiv.org/abs/2611.18008
status: summary
catalog_year: 2026
subtopic: "科学计算与遥感"
updated: 2026-11-21
---

# Sample-Efficient Control of Magnetoconvective Flows via Differentiable Simulation

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jannis Becktepe、Dmitry Krasnov、Nils Thuerey、Jörg Schumacher、Sebastian Peitz。
- 年份与版本：2026 按预印本 v1 年份，首次提交于 2026-11-13（UTC），核对时为 v1。未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.18008) · [v1 正文](https://arxiv.org/html/2611.18008v1)。
- 官方代码：[φ-PICT](https://github.com/upb-sciml/phiPICT)，作者提供的可微流体求解器，集成 FluidGym。本库未运行代码。

## 解决的问题

液态金属磁流体的控制与逆向设计需要大量仿真。论文研究能否利用求解器梯度降低优化的样本需求。[摘要](https://arxiv.org/abs/2611.18008)

## 主要方法

φ-PICT 在可微流体求解框架中加入电势、电流和洛伦兹力耦合及相应梯度，使用 GPU 加速，并在 FluidGym 中比较闭环控制与逆向设计方法。[方法](https://arxiv.org/html/2611.18008v1)

## 贡献与局限

作者通过磁流体基准验证求解器，展示梯度用于传热控制及壁面缺陷识别。模型采用磁场不受流体影响的准静态近似，当前执行限于支持 CUDA 的单 GPU，高分辨率三维仿真仍昂贵。编者提醒：仿真中的优化收益尚不能直接视为实际冷却装置的部署效果。[设定与局限](https://arxiv.org/html/2611.18008v1)

## 前置知识与阅读重点

建议了解流体数值模拟、自动微分与策略优化。重点检查梯度验证、控制观测与奖励，以及仿真步数和实际计算时间是否采用一致预算。

## 收录理由

补充科学机器学习的可微仿真案例，连接物理求解器、控制学习和逆问题。

## 相关主题与版本

- arXiv ID：`2611.18008`。书目页列 DOI `10.48550/arXiv.2611.18008`，注明待注册。
- 主文件归入[领域应用](README.md)，相关方向为[强化学习与决策](../reinforcement-learning/README.md)。
- 本条核对书目、方法、局限及官方仓库，未进行全文精读或实验复现。
