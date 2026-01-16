# 📐 数学公式模块 (`math`)

`math` 模块集成了主流的数学排版包，并针对不同的编译引擎和文档类进行了智能切换。

---

## 1. 加载的宏包

- `amsmath`: 基础数学公式环境。
- `mathtools`: `amsmath` 的增强补丁。
- `amsthm`: 定理基础支持。
- **智能选择**：
  - **XeLaTeX/LuaLaTeX (推荐)**：加载 `unicode-math`，设置数学字体风格为 ISO。
  - **pdfTeX 或 冲突类**：加载传统的 `amssymb`。

## 2. 提供的命令

- `\square`: 提供统一的正方形符号支持。
- `\boxtimes`: 提供统一的乘号框符号支持。

## 3. 配置选项

- `math`: (Boolean) 是否加载此模块，默认为 `true`。

## 4. 使用示例

```latex
% 开启了 math 模块后即可直接使用环境
\begin{equation}
    E = mc^2
\end{equation}

\begin{align}
    a + b &= c \\
    d + e &= f
\end{align}
```

---
[返回模块总览](README.md)
