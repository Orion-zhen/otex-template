# 🧩 子模块功能详解

otex 将不同的 LaTeX 功能抽象为 20 个独立的子模块。这些模块位于 `otex/` 目录下，由 `otex.sty` 根据用户的选项自动管理加载。

---

## 1. 核心基础设施

- [**`otex-pkgcheck.sty`**](pkgcheck.md)：全包最核心的智能包检查器，负责处理宏包冲突。
- [**`otex-base.sty`**](base.md)：基础工具包，包括颜色 (`xcolor`)、单位 (`siunitx`) 和跨平台检测。
- [**`otex-commands.sty`**](commands.md)：提供常用的便捷命令，如更简洁的表格绘制和特殊字符。

## 2. 文本与布局

- [**`otex-layout.sty`**](layout.md)：控制页边距、行间距和段落样式。
- [**`otex-fonts.sty`**](fonts.md)：字体系统核心，通过 `fontspec` 实现。
- [**`otex-chinese.sty`**](chinese.md)：CTEX 深度集成与中文环境适配。
- [**`otex-titlesec.sty`**](titlesec.md)：章节标题格式化与间距控制。
- [**`otex-toc.sty`**](toc.md)：目录与页码样式定制。
- [**`otex-index.sty`**](index.md)：索引与术语表支持。

## 3. 数学与定理

- [**`otex-math.sty`**](math.md)：加载 `amsmath`, `mathtools` 及符号包。
- [**`otex-theorems.sty`**](theorems.md)：提供 11+ 种预定义的定理环境。

## 4. 图形、表格与浮动体

- [**`otex-graphics.sty`**](graphics.md)：图片插入 (`graphicx`) 与彩色盒子 (`tcolorbox`)。
- [**`otex-tables.sty`**](tables.md)：增强型表格支持 (`tabularx`, `booktabs`)。
- [**`otex-floats.sty`**](floats.md)：浮动体位置策略与标题 (`caption`) 定制。
- [**`otex-caption.sty`**](caption.md)：图表标题格式化与子图支持。

## 5. 代码与算法

- [**`otex-code.sty`**](code.md)：代码高亮逻辑，管理 `listings` 与 `minted` 的共存。
- [**`otex-algo.sty`**](algo.md)：算法流程图支持 (`algorithm2e` 或 `algorithmicx`)。

## 6. 其他辅助

- [**`otex-bib.sty`**](bib.md) ：参考文献引用与列表构建。
- [**`otex-refs.sty`**](refs.md) ：交叉引用与超链接 (`hyperref`, `cleveref`)。
- [**`otex-appendix.sty`**](appendix.md) ：附录环境适配。

---

## 💡 使用提示

如果你只需要特定的模块而不希望加载整个 otex，可以使用 `no[module]` 选项来排除它们。例如：
`\usepackage[nominted, nobib]{otex}`

[返回文档首页](../README.md)
