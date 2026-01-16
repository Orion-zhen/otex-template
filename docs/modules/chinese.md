# 🇨🇳 中文支持模块 (`chinese`)

`chinese` 模块是 otex 处理中西文混排的核心，基于 `ctex` 宏包构建。

---

## 1. 加载的宏包

- `ctex`: 智能加载，根据 `english` 选项自动设置 `scheme=chinese` 或 `scheme=plain`。

## 2. 核心逻辑：智能 Heading 避让

本模块会检测当前加载的文档类（document class）：

- 如果是标准类（如 `article`, `report`），则开启完整的 `ctex` 标题支持。
- 如果是冲突类或未知类，则自动回退到 `heading=false` 模式，并禁用 `ctex` 的标题接管，以保证原有模板样式的完整性。

## 3. 配置选项

- `ctex`: (Boolean) 是否加载此模块，默认为 `true`。
- `english`: 决定了 `ctex` 的预设方案（Scheme）。

---
详细的本地化逻辑请参阅：[🌍 多语言自动本地化](../compatibility/localization.md)

---
[返回模块总览](README.md)
