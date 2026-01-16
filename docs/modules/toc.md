# 📖 目录管理模块 (`toc`)

`toc` 模块负责文档目录（Table of Contents）的样式定制与深度设置。

---

## 1. 加载的宏包

- `tocloft` (检测 `\cftbeforetoctitleskip`): 用于定制目录、插图清单和表格清单的样式。仅在代表性符号不存在时加载。

## 2. 核心功能

- **深度控制**：自动将 `tocdepth` 和 `secnumdepth` 设置为 3（即显示并编号到 subsubsection）。
- **符号存在性检测**：通过检测 `\cftbeforetoctitleskip` 符号判断 tocloft 功能是否已存在，避免与模板冲突。

## 3. 配置选项

- `toc`: (Boolean) 是否加载此模块，默认为 `true`。

---
[返回模块总览](README.md)
