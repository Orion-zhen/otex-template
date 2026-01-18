# otex

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![LaTeX3](https://img.shields.io/badge/LaTeX-expl3-brightgreen.svg)](https://ctan.org/pkg/expl3)

**otex** 是一个基于 LaTeX3 (expl3) 开发的模块化 LaTeX 配置框架。它旨在为各种 LaTeX 模板提供统一、健壮且易于扩展的基础配置，自动处理复杂的宏包冲突，并提供极致的跨平台、多语言兼容性。

## ✨ 核心特性

- 🧩 **模块化设计**：包含 120 个独立功能模块，支持按需加载。
- 🌍 **全球化驱动**：内置完美的中英文双语支持，一键切换。
- 🔧 **智能冲突解析**：自动检测并修正与第三方模板（如各个大学学位论文模板）的宏包冲突。
- 🖋️ **极致字体兼容**：支持 Windows/Linux/macOS 预设，并提供 `fonts-dir` 免安装分发方案。
- 🚀 **开箱即用**：集成了数学、定理、代码高亮、算法、参考文献等常用配置。

> [!IMPORTANT]
> otex 应该是你的文档中 **最后一个** 加载的包！otex 需要检查其它模板和包的加载情况来解析冲突并智能加载。

## 🚀 快速开始

### 1. 安装

将 `otex.sty` 文件和 `otex/` 文件夹复制到你的 LaTeX 项目根目录下。

### 2. 最小示例

在你的 `.tex` 文件中使用：

```latex
\documentclass{article}
\usepackage[english=false]{otex} % 默认开启中文支持

\begin{document}
\section{你好 otex}
这是一段使用 otex 配置的文字。
\end{document}
```

### 3. 编译要求

- **引擎**：推荐使用 `XeLaTeX` 或 `LuaLaTeX`。
- **命令**：推荐使用 `latexmk`。

  ```bash
  latexmk -xelatex -shell-escape main.tex
  ```

- **LaTeX Workshop**：仓库中附带了 VS Code 的 LaTeX Workshop 插件的相关配置，在 `latex-worksop.jsonc` 中。可以复制到自己的 VS Code 中使用。

### 4. 示例文档

本仓库提供了 `article.tex` 文件以供验证 otex 的构建情况。

## 🖥️ 环境配置

如需在 Windows 系统上使用 otex 的全部功能，请按顺序安装以下软件：

### 1. TeX 发行版

安装 **TeX Live** (推荐) 或 **MiKTeX**：

- [TeX Live](https://tug.org/texlive/)：选择完整安装 (Full Scheme)，包含所有必要的宏包和工具
- [MiKTeX](https://miktex.org/)：首次编译时会自动下载缺失的宏包

> [!TIP]
> TeX Live 完整安装约需 8GB 磁盘空间，但可避免宏包缺失问题。

### 2. 编辑器

推荐使用 **VS Code** + **LaTeX Workshop** 插件：

1. 安装 [VS Code](https://code.visualstudio.com/)
2. 在扩展商店搜索安装 `LaTeX Workshop`
3. 将本仓库的 `latex-workshop.jsonc` 配置复制到 VS Code 设置中

### 3. Python (可选，代码高亮功能需要)

`minted` 代码高亮模块需要 Python 和 Pygments：

1. 安装 [Python](https://www.python.org/downloads/)（勾选 "Add to PATH"）
2. 命令行执行：`pip install Pygments`

### 4. 字体 (可选)

otex 在 Windows 上默认使用系统自带字体 (中易宋体、Times New Roman 等)。如需使用其他字体预设，请参考 [字体配置文档](docs/compatibility/fonts.md)。

---

## 📚 详细文档

为了保持简洁，完整的技术手册和方案详解请参阅 `docs/` 目录：

- [📖 文档首页](docs/README.md)
- [🌍 兼容性深度解析 (字体/跨平台/多语言)](docs/compatibility/README.md)
- [⚙️ 全量选项配置参考](docs/options.md)
- [🧩 子模块功能详解](docs/modules/README.md)
- [📦 快速入门指南](docs/getting-started.md)

## ⚖️ 许可证

Internal Project. Released under [GPL-3.0](LICENSE).
