# 🖼️ 图形处理模块 (`graphics`)

`graphics` 模块集成了强大的 TikZ 绘图系统和标准的图片加载功能。

---

## 1. 加载的宏包

- `graphicx`: 标准图片加载包。
- `tcolorbox`: 用于创建美观的彩色文本框。
- `tikz`: 强大的矢量绘图宏包。
- `pgfplots`: 基于 TikZ 的函数图与数据可视化宏包。

## 2. 提供的样式 (TikZ Style)

为了方便快速绘图，该模块预定义了一些 TikZ 样式：

- `base`: 基础节点样式。
- `process`: 矩形流程节点（淡橙色）。
- `decision`: 菱形决策节点（淡蓝色）。
- `startstop`: 圆角矩形起止节点（淡红色）。
- `arrow`: 增强型箭头。

## 3. 配置选项

- `graphics`: (Boolean) 是否加载此模块，默认为 `true`。

## 4. 使用示例

### 插入图片

```latex
\includegraphics[width=0.8\textwidth]{figure.png}
```

### 使用预定义样式绘图

```latex
\begin{tikzpicture}
    \node [startstop] (start) {开始};
    \node [process, below of=start] (step1) {步骤一};
    \draw [arrow] (start) -- (step1);
\end{tikzpicture}
```

---
[返回模块总览](README.md)
