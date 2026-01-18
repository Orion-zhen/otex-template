# 🇨🇳 中文支持模块 (`chinese`)

`chinese` 模块是 otex 处理中西文混排的核心，基于 `ctex` 宏包构建。

---

## 1. 加载的宏包

- `ctex`: 智能加载，根据 `english` 选项自动设置 `scheme=chinese` 或 `scheme=plain`。
- `otex-titlesec`: 本模块会自动加载 [titlesec 模块](titlesec.md) 来管理标题格式。

## 2. 核心逻辑：Heading 委托

> [!IMPORTANT]
> **otex 始终使用 `heading=false` 加载 ctex**，将标题格式的管理权完全委托给 `titlesec` 模块。

这意味着：
- ❌ **不要使用** `\ctexset{section/format = ...}` 等 ctex 标题配置
- ✅ **应该使用** `titlesec` 的 `\titleformat` 和 `\titlespacing` 命令

这样设计的好处：
1. 避免 `ctex` 与 `titlesec` 的冲突
2. 提供更强大的标题自定义能力
3. 保证与第三方模板的兼容性

## 3. 配置选项

- `ctex`: (Boolean) 是否加载此模块，默认为 `true`。
- `english`: 决定了 `ctex` 的预设方案（Scheme）。

---
详细的本地化逻辑请参阅：[🌍 多语言自动本地化](../compatibility/localization.md)

---
[返回模块总览](README.md)
