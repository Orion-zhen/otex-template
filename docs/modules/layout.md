# 📐 布局管理模块 (`layout`)

`layout` 模块定义了文档的纸张大小、面边距以及页眉页脚样式。

---

## 1. 加载的宏包

- `geometry`: 用于设置物理页面边距。
- `fancyhdr`: 用于自定义页眉和页脚。

## 2. 默认设置

- **纸张大小**：A4 (a4paper)。
- **页边距**：上下左右均为 2.5cm。
- **页眉页脚**：
  - 左页眉：当前章节名 (`\leftmark`)。
  - 右页眉：页码。
  - 页脚：清空。

## 3. 配置选项

- `layout`: (Boolean) 是否加载此模块，默认为 `true`。

## 4. 覆盖默认页边距配置

加载 `otex` 后，可以通过 `\geometry{...}` 命令覆盖默认的页边距设置：

```latex
\documentclass{article}
\usepackage{otex}

% 覆盖默认页边距
\geometry{
  left=3cm,
  right=3cm,
  top=2cm,
  bottom=2cm
}

\begin{document}
% 内容
\end{document}
```

### 常用页边距配置示例

```latex
% 窄边距（适合草稿或多内容页面）
\geometry{left=1.5cm, right=1.5cm, top=1.5cm, bottom=1.5cm}

% 宽边距（适合正式文档或批注）
\geometry{left=4cm, right=2cm, top=3cm, bottom=3cm}

% 非对称边距（适合装订）
\geometry{inner=3cm, outer=2cm, top=2.5cm, bottom=2.5cm}
```

## 5. 覆盖默认页眉页脚配置

加载 `otex` 后，可以通过 `fancyhdr` 命令覆盖默认的页眉页脚设置：

```latex
\documentclass{article}
\usepackage{otex}

% 清除 otex 默认的页眉页脚设置
\fancyhf{}

% 自定义页眉
\lhead{我的文档}          % 左页眉
\chead{}                  % 中页眉
\rhead{\today}            % 右页眉

% 自定义页脚
\lfoot{作者：张三}        % 左页脚
\cfoot{\thepage}          % 中页脚（页码）
\rfoot{版本 1.0}          % 右页脚

\begin{document}
% 内容
\end{document}
```

### 页眉页脚样式选项

```latex
% 使用 plain 样式（仅中页脚显示页码）
\pagestyle{plain}

% 使用 empty 样式（无页眉页脚）
\pagestyle{empty}

% 恢复 fancy 样式
\pagestyle{fancy}

% 修改页眉页脚分隔线
\renewcommand{\headrulewidth}{0.4pt}  % 页眉线宽度
\renewcommand{\footrulewidth}{0pt}    % 页脚线宽度（0 表示无线）
```

### 章节标记自定义

```latex
% 自定义 \leftmark 和 \rightmark 的格式
\renewcommand{\sectionmark}[1]{\markboth{第 \thesection 节\quad #1}{}}
\renewcommand{\subsectionmark}[1]{\markright{#1}}

% 使用自定义标记
\lhead{\leftmark}
\rhead{\rightmark}
```

## 6. 综合配置示例

以下是一个完整的覆盖配置示例：

```latex
\documentclass{article}
\usepackage{otex}

% === 页边距配置 ===
\geometry{
  a4paper,
  left=3cm,
  right=2.5cm,
  top=2.5cm,
  bottom=2.5cm,
  headheight=14pt,
  headsep=20pt,
  footskip=30pt
}

% === 页眉页脚配置 ===
\fancyhf{}
\lhead{\nouppercase{\leftmark}}
\rhead{页 \thepage}
\cfoot{\footnotesize 我的文档 -- 机密}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.4pt}

\title{我的第一个 otex 文档}

\begin{document}
\maketitle

\newpage

\section{引言}
这是一个使用自定义布局的文档。
\end{document}
```

## 7. 封面页配置 (`titlepage` 环境)

`otex` 自动为 `titlepage` 环境配置了以下特性：

- **移除页码**：封面页不显示页眉页脚。
- **重置页码计数**：封面后的第一页从 1 开始计数。

### 基本用法

使用 `titlepage` 环境而非 `\maketitle` 可以完全控制封面布局：

```latex
\begin{document}

\begin{titlepage}
  \centering
  \vspace*{\fill}  % 将内容推向垂直中心
  
  {\Huge\bfseries 文档标题 \par}
  \vspace{1cm}
  {\Large 作者姓名 \par}
  \vspace{0.5cm}
  {\large \today \par}
  
  \vspace*{\fill}  % 底部填充，实现垂直居中
\end{titlepage}

\tableofcontents  % 目录从第 1 页开始
\end{document}
```

### 布局调整技巧

#### 垂直对齐

```latex
% 垂直居中（使用 \vspace*{\fill}）
\vspace*{\fill}
% 内容
\vspace*{\fill}

% 偏上布局（底部填充更多）
\vspace*{2cm}
% 内容
\vspace*{\fill}

% 偏下布局（顶部填充更多）
\vspace*{\fill}
% 内容
\vspace*{3cm}
```

#### 添加摘要

```latex
\begin{titlepage}
  \centering
  \vspace*{\fill}
  
  {\Huge\bfseries 论文标题 \par}
  \vspace{1cm}
  {\Large 作者 \par}
  \vspace{0.5cm}
  {\large \today \par}
  
  \vspace{2cm}
  \begin{minipage}{0.85\textwidth}
    \textbf{摘要：} 这里是摘要内容...
  \end{minipage}
  
  \vspace*{\fill}
\end{titlepage}
```

#### 添加封面图片

```latex
\begin{titlepage}
  \centering
  \vspace*{2cm}
  
  \includegraphics[width=0.4\textwidth]{logo.png}
  
  \vspace{2cm}
  {\Huge\bfseries 项目报告 \par}
  \vspace{1cm}
  {\Large 团队名称 \par}
  
  \vfill
  {\large 2026 年 1 月 \par}
  \vspace{2cm}
\end{titlepage}
```

> **注意**：`\vfill` 等价于 `\vspace{\fill}`，但 `\vspace*{\fill}` 在页面顶部时不会被忽略。

## 8. 配置选项

- `layout`: (Boolean) 是否加载此模块，默认为 `true`。

---
[返回模块总览](README.md)
