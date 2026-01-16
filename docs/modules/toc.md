# 📖 目录管理模块 (`toc`)

`toc` 模块负责文档目录（Table of Contents）的样式定制与深度设置。

---

## 1. 加载的宏包

- `tocloft`: 用于定制目录、插图清单和表格清单的样式。

## 2. 核心功能

- **深度控制**：自动将 `tocdepth` 和 `secnumdepth` 设置为 3（即显示并编号到 subsubsection）。
- **智能避让**：如果检测到文档类（如 `IEEEtran`, `acmart`）已经有了严格的目录样式，该模块将自动跳过，以免破坏原有排版。

## 3. 配置选项

- `toc`: (Boolean) 是否加载此模块，默认为 `true`。

---
[返回模块总览](README.md)
