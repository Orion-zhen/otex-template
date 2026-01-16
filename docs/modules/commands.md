# 🔡 便捷命令模块 (`commands`)

`commands` 模块提供了一系列能显著提高写作效率的“生活质量”扩展命令。

---

## 1. 加载的宏包

- `etoolbox`: 基础编程补丁。
- `tcolorbox`: 用于创建带有背景色和边框的信息框。

## 2. 提供的命令

- `\zh{text}`: 强制使用中文字体（宋体）排版。
- `\en{text}`: 强制使用西文 (Modern Roman) 字体排版。
- `\otexkeyword{text}`: 以红色加粗样式标注关键字。
- `\todo{text}`: 显眼的黄色 TODO 标记块。

## 3. 提供的彩色信息框 (Environments)

- `alertbox`: 红色警告框。
- `infobox`: 蓝色通知框。
- `tipbox`: 绿色提示框。

## 4. 使用示例

```latex
\begin{tipbox}[title=小技巧]
    使用 \otexkeyword{\string\cref} 可以实现自动带前缀的交叉引用。
\end{tipbox}

\todo{记得补全这一段的推导过程}
```

---
[返回模块总览](README.md)
