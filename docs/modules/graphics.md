# 🖼️ 图形处理模块 (`graphics`)

`graphics` 模块集成了标准的图片加载功能和彩色盒子支持。采用**符号存在性检测**避免与模板冲突。

---

## 1. 加载的宏包

以下包仅在其代表性符号不存在时加载：

- `graphicx` (检测 `\includegraphics`): 标准图片加载包。
- `tcolorbox` (检测 `\tcbox`): 用于创建美观的彩色文本框。

## 2. 配置选项

- `graphics`: (Boolean) 是否加载此模块，默认为 `true`。

## 3. 使用示例

### 插入图片

```latex
\includegraphics[width=0.8\textwidth]{figure.png}
```

---
[返回模块总览](README.md)
