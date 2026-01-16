# 🔗 交叉引用模块 (`refs`)

`refs` 模块通过超链接和智能引用增强了文档的交互性。

---

## 1. 加载的宏包

- `hyperref`: 提供超链接、PDF 书签和元数据设置。
- `cleveref`: 提供“智能引用”功能（如自动生成“图 1”字样）。

## 2. 提供的功能

- **自动化配置**：自动设置超链接颜色为深蓝/深绿/深红，提升阅读体验。
- **元数据填充**：根据 `pdf-title` 和 `pdf-author` 选项自动填充 PDF 属性。
- **中英文本地化**：在中文模式下，`\cref` 会自动识别并输出“图”、“表”、“定理”等中文前缀。

## 3. 配置选项

- `hyperref`: (Boolean) 是否加载超链接支持，默认为 `true`。
- `cleveref`: (Boolean) 是否加载智能引用支持，默认为 `true`。

## 5. 兼容性策略 (Compatibility Mode)

为了适应不同期刊模板对 `hyperref` 加载时机的不同要求，otex 实现了双模式加载机制：

### 5.1 主动模式 (Active Mode)

- **适用场景**：标准文档类（如 `article`, `report`）以及大多数一般模板。
- **行为**：otex 会在导言区**立即加载** `hyperref`。
- **日志**：`Hyperref loading mode: ACTIVE`

### 5.2 被动模式 (Passive Mode)

- **适用场景**：已知与早期 `hyperref` 加载冲突的复杂模板（**MDPI**, **acmart**, **beamer**）。
- **行为**：otex **不加载** `hyperref`，而是等待文档类自行加载。配置逻辑会被推迟到 `\AtBeginDocument` 执行。
- **日志**：`Hyperref loading mode: PASSIVE`

> **注意**：如果您的自定义模板出现 `LaTeX hooks Error`，可能说明它需要被加入被动模式列表。目前的黑名单包括：`mdpi`, `acmart`, `beamer`。

## 4. 使用示例

```latex
% 传统引用
如第 \ref{sec:intro} 节所示。

% 智能引用 (推荐)
如 \cref{sec:intro} 所示。（中文下自动输出“如图 1”）
```

---
[返回模块总览](README.md)
