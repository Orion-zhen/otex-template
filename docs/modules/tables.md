# 📊 表格模块 (`tables`)

`tables` 模块加载了构建学术规范表格所需的核心宏包。采用**符号存在性检测**避免与模板冲突。

---

## 1. 加载的宏包

以下包仅在其代表性符号不存在时加载：

- `booktabs` (检测 `\toprule`): 提供 `\toprule`, `\midrule`, `\bottomrule` 等绘制专业三线表所需的命令。
- `multirow` (检测 `\multirow`): 支持跨行单元格。
- `array`: 增强版的表格列定义。
- `longtable` (检测 `longtable` 环境): 支持跨页的长表格。
- `wrapfig` (检测 `\wrapfigure`): 支持文字环绕的表格和图片。

## 2. 配置选项

- `tables`: (Boolean) 是否加载此模块，默认为 `true`。

## 3. 使用示例

```latex
\begin{table}[ht]
    \centering
    \caption{三线表示例}
    \begin{tabular}{ccc}
        \toprule
        参数 & 数值 & 单位 \\
        \midrule
        温度 & 300 & K \\
        压力 & 1.0 & atm \\
        \bottomrule
    \end{tabular}
\end{table}
```

---
[返回模块总览](README.md)
