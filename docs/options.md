# ⚙️ 全量选项配置手册

otex 通过 LaTeX3 的 `keys` 机制提供了一套非常直观的参数配置系统。

---

## 1. 模块开关 (Boolean Options)

大部分选项默认为 `true`，你可以显式设置为 `false` 或使用 `no` 前缀的别名。

| 选项名 | 别名 (禁用) | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| `layout` | `nolayout` | `true` | 页边距、行间距等基础布局 |
| `fonts` | `nofonts` | `true` | 加载 fontspec 并配置系统字体 |
| `ctex` | `noctex` | `true` | 中文支持 |
| `theorems` | `notheorems` | `true` | 定理环境 (Theorem, Lemma 等) |
| `math` | `nomath` | `true` | 数学宏包 (amsmath, unicode-math 等) |
| `graphics` | `nographics` | `true` | 图片支持 (graphicx, tikz 等) |
| `code` | - | `true` | 代码块支持 (由 listings 和 minted 开关控制) |
| `minted` | `nominted` | `true` | 使用 minted (Pygments) 进行代码高亮 |
| `bib` | `nobib` | `true` | 参考文献支持 |
| `english` | - | `false` | 是否开启全英文模式 (界面本地化) |

---

## 2. 功能配置 (Value Options)

| 选项名 | 默认值 | 示例 / 可选值 | 说明 |
| :--- | :--- | :--- | :--- |
| `bib-backend` | `biblatex` | `bibtex`, `biber` | 参考文献处理后端 |
| `bib-style` | `ieee` | `gb7714-2015`, `nature` | 参考文献引用样式 |
| `font-set` | `auto` | `windows`, `linux`, `adobe`, `none` | 字体预设方案 (auto 模式下会自动检测操作系统) |
| `fonts-dir` | (空) | `fonts` | 自定义字体搜索路径 |
| `pdf-title` | `Generated Document` | `{我的论文}` | 自动设置 PDF Meta 属性 |
| `pdf-author` | `Orion` | `{张三}` | 自动设置 PDF Meta 属性 |

---

## 3. 字体微调 (Font Tuning)

当 `font-set=none` 或需要覆盖预设时使用：

- `main-font`: 西文正文字体
- `sans-font`: 西文无衬线字体
- `mono-font`: 西文等宽字体
- `cjk-main-font`: 中文正文字体（宋体类）
- `cjk-sans-font`: 中文无衬线字体（黑体类）
- `cjk-mono-font`: 中文等宽字体（仿宋类）
- `math-font`: 数学公式字体（需配合 unicode-math）

---

## 4. 示例：综合配置

```latex
\usepackage[
    english=true,      % 英文模式
    bib-style=nature,  % Nature 风格引文
    nominted,          % 禁用需要外部 Python 的 minted，回退到 listings
    font-set=adobe,    % 使用 Adobe 字体方案
    pdf-title={Advanced Optimization Methods}
]{otex}
```

---
[返回文档首页](README.md)
