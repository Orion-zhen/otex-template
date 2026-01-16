# 🖋️ 字体系统与跨平台配置

otex 的字体系统设计目标是：**在不改变源码的情况下，自动适配主流系统字体，同时允许极高的手动定制自由度。**

---

## 1. 自动预设方案 (Presets)

otex 默认会检测你的载入类 (document class) 以及 **操作系统 (OS)**。如果是标准的 `article`/`book` 等，且没有指定 `font-set`，它会根据当前系统智能选择预设：

- **Windows**: 自动切换到 `windows` 预设。
- **Linux**: 自动切换到 `linux` 预设 (使用 Liberation 和 Noto 字体)。
- **macOS (Darwin)**: 自动切换到 `adobe` 预设 (使用 Source 家族字体)。

你也可以手动指定：

| 选项名 | 适用场景 | 对应的西文字体 (Main/Sans/Mono) | 对应的中文字体 (Main/Sans/Mono) |
| :--- | :--- | :--- | :--- |
| `font-set=windows` | Windows 环境 | Times New Roman, Arial, Courier New | 中易宋体 (SimSun), 黑体 (SimHei), 仿宋 (FangSong) |
| `font-set=linux` | Linux (Ubuntu/Debian等) | Liberation Serif, Sans, Mono | Noto Serif CJK SC, Noto Sans CJK SC, Noto Sans Mono CJK SC |
| `font-set=adobe` | 专业出版/开源 | Source Serif Pro, Source Sans Pro, Source Code Pro | Source Han Serif CN, Source Han Sans CN, Source Han Sans CN |
| `font-set=none` | **手动模式** | 不加载任何预设，仅保留宏包环境 | 不加载任何预设 |

---

## 2. 绕过默认配置的手动方案 (高级)

如果你不希望使用 otex 自动挑选的字体，我们提供了以下三种层进式的控制方案：

### 方案 A：使用 otex 包参数直接指定

这是最简单的方法，直接在引入 otex 时通过参数指定字体名。

```latex
\usepackage[
    main-font = {Inter},
    sans-font = {Roboto},
    mono-font = {Fira Code},
    cjk-main-font = {Source Han Serif SC},
    cjk-sans-font = {Source Han Sans SC},
    cjk-mono-font = {Source Han Mono SC},
    math-font = {STIX Two Math}
]{otex}
```

*注：此方案依然受 otex 内部逻辑管理，会自动设置给 fontspec/xeCJK。*

### 方案 B：解耦模式 (`font-set=none`)

如果你希望保留 otex 自动加载 `fontspec` 和 `xeCJK` 的便利，但想完全用标准 LaTeX 命令设置字体：

```latex
\usepackage[font-set=none]{otex}

% 在导言区手动配置，otex 不会覆盖这些设置
\setmainfont{Crimson Pro}
\setCJKmainfont{Microsoft YaHei}
```

### 方案 C：彻底禁用字体模块 (`fonts=false`)

如果你正在使用的模板（如某些学位论文模板）已经有了极其复杂的字体配置，且与 otex 冲突：

```latex
\usepackage[fonts=false]{otex}
```

此时 otex **完全不会** 加载 `fontspec` 和 `xeCJK`，也不会进行任何字体相关的操作。

---

## 3. 零安装分发：`fonts-dir` 选项

为了让你的文档能在任何人的电脑上编译（即使对方没有安装特定字体），你可以将字体文件放在项目子目录中。

1. 在项目根目录创建 `fonts/` 文件夹。
2. 放入字体文件（如 `MyFont.otf`）。
3. 配置 otex：

```latex
\usepackage[fonts-dir=fonts]{otex}
\setmainfont{MyFont.otf} % 现在可以通过文件名直接引用
```

**内部机制**：otex 会自动为 `fontspec` 添加 `Path` 特性，使得所有后续的字体调用都会优先查看该目录。

---

## 4. 数学字体

otex 默认加载 `unicode-math` 并尝试配置 `DejaVu Math TeX Gyre` 作为数学字体。

- 如果检测到系统中没有该字体，它会回退到 TeX 默认的数学字体。
- 你也可以通过手动禁用 `math` 模块来阻止这一行为。

---
[返回兼容性首页](README.md) | [返回文档首页](../README.md)
