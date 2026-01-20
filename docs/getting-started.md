# 🚀 快速入门指南

本章节通过五个简单的步骤，带你从零开始在项目中使用 **otex**。

---

## 1. 复用与安装

### 方式一：项目内安装（推荐新手）

将 `otex.sty` 文件和 `otex/` 模块文件夹复制到你的 `.tex` 源码同级目录下：

```text
my-project/
├── otex.sty
├── otex/ (文件夹)
└── main.tex
```

### 方式二：全局安装（推荐长期使用）

通过 `git clone` 将 otex 安装到用户目录下的 `TEXMFHOME`，使其全局可用并可通过 `git pull` 轻松更新。

**步骤 1：查找你的 TEXMFHOME 路径**

```bash
kpsewhich -var-value=TEXMFHOME
```

通常输出为 `~/texmf`（Linux/macOS）或 `C:/Users/<用户名>/texmf`（Windows）。

**步骤 2：克隆仓库到 TEXMFHOME**

LaTeX 查找包的标准路径规则是 `TEXMFHOME/tex/latex/包名/`。注意文件结构：放置后的目录结构应该看起来像这样（这对 LaTeX 找到依赖文件很重要）：

```text
~/texmf/
└── tex/
    └── latex/
        └── otex/
            ├── otex.sty
            └── otex/
                ├── otex-algo.sty
                └── ...
```

```bash
# Linux/macOS
git clone https://github.com/Orion-zhen/otex-template.git $(kpsewhich -var-value=TEXMFHOME)/tex/latex/otex
```

```pwsh
# Windows (PowerShell)
git clone https://github.com/Orion-zhen/otex-template.git "$env:USERPROFILE\texmf\tex\latex\otex"
```

**步骤 3：（可选）刷新 TeX 文件名数据库**

```bash
texhash ~/texmf  # 或 mktexlsr，部分发行版需要
```

打开终端，使用 `kpsewhich` 命令检查系统能否找到 otex 包：

```bash
kpsewhich otex.sty
```

如果输出了诸如 `~/texmf/tex/latex/otex/otex.sty` 的完整路径，说明配置成功。

> [!TIP]
> 安装完成后，任何项目都可以直接使用 `\usepackage{otex}`，无需再复制文件。

**通过 git 更新 otex：**

```bash
cd $(kpsewhich -var-value=TEXMFHOME)/tex/latex/otex
git pull
```

---

## 2. 第一个文档：快速上手示例

创建一个名为 `main.tex` 的文件，填入以下内容：

```latex
\documentclass{article}
\usepackage{otex} % 默认开启全功能

% 可选：设置 PDF 属性
\hypersetup{
    pdftitle={我的第一个 otex 文档},
    pdfauthor={Orion}
}

\title{我的第一个 otex 文档}

\begin{document}
\maketitle

\section{数学与定理}
这里有一个定理：
\begin{theorem}
    勾股定理：$a^2 + b^2 = c^2$。
\end{theorem}

\section{代码展示}
\begin{listing}[H]
\begin{minted}{python}
def hello():
    print("Hello from otex!")
\end{minted}
\end{listing}

\end{document}
```

---

## 3. 编译推荐

推荐使用 `XeLaTeX` 引擎和 `latexmk` 工具，因为它们能自动处理交叉引用和参考文献。

**命令：**

```bash
latexmk -xelatex -shell-escape main.tex
```

*注：`-shell-escape` 是 `minted` 代码高亮模块正常工作所必须的。*

---

## 4. 常见轻量级定制

如果你不需要某些功能，或者需要微调语言，可以在加载包时传递参数：

- **切换为英文模式**：`\usepackage[english=true]{otex}`
- **禁用特定功能**（如不需要数学模块）：`\usepackage[nomath]{otex}`
- **指定文献样式**：`\usepackage[bib-style=gb7714-2015]{otex}`

---

## 5. 接下来做什么？

- 深入了解 [🌍 字体与跨平台兼容性](compatibility/fonts.md)。
- 查看 [⚙️ 全量选项配置手册](options.md)。
- 了解 [🧩 19 个子模块](modules/README.md) 的具体用法。

---
[返回文档首页](README.md)
