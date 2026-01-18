# 📑 标题格式模块 (`titlesec`)

`titlesec` 模块负责章节标题的格式化与间距控制，基于 `titlesec` 宏包构建。

---

## 1. 加载的宏包

- `titlesec`: 提供 `\titleformat` 和 `\titlespacing` 命令。

## 2. 核心逻辑：兼容性检测

本模块会自动检测运行环境：

- ✅ **标准文档类**（`article`, `report`, `book`）：正常加载并应用学术风格的标题格式。
- ⛔ **不兼容类**（如 `beamer`）：自动跳过加载，因为这些类没有定义 `\l@section` 等命令。

## 3. 默认标题样式

### 英文模式（`english` 选项启用）

```latex
\titleformat{\section}
  {\normalfont\large\bfseries}
  {\thesection.}{0.5em}{}
```

### 中文模式（默认）

```latex
\titleformat{\section}
  {\normalfont\large\bfseries}
  {\chinese{section}、}{0em}{}
```

## 4. 自定义标题格式

要覆盖默认样式，在 `\usepackage{otex}` **之后** 使用 `\titleformat`：

```latex
\usepackage{otex}

% 自定义 section 格式：居中、大字号
\titleformat{\section}[block]
  {\centering\Large\bfseries}
  {\thesection}{1em}{}

% 自定义间距
\titlespacing*{\section}{0pt}{3ex}{2ex}
```

## 5. 配置选项

- `titlesec`: (Boolean) 是否加载此模块，默认为 `true`。

> [!NOTE]
> 本模块由 `otex-chinese.sty` 自动调用，无需手动加载。

---
[返回模块总览](README.md)
