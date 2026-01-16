# 📜 定理环境模块 (`theorems`)

`theorems` 模块提供了一套美观且符合学术规范的定理、定义、证明等环境。

---

## 1. 加载的宏包

- `amsthm`: 用于定义定理样式和环境。

## 2. 提供的环境

本模块会根据 `english` 选项自动翻译环境名称。

- `theorem`: 定理
- `lemma`: 引理
- `proposition`: 命题
- `corollary`: 推论
- `definition`: 定义
- `example`: 例
- `remark`: 注
- `assumption`: 假设
- `conjecture`: 猜想
- `problem`: 问题
- `solution`: 解答

## 3. 配置选项

- `theorems`: (Boolean) 是否加载此模块，默认为 `true`。
- `english`: 影响由该模块提供的环境名称语言。

## 4. 使用示例

```latex
\begin{theorem}[勾股定理]
    在一个直角三角形中，斜边的平方等于两条直角边的平方和。
\end{theorem}

\begin{proof}
    这里是证明内容...
\end{proof}
```

---
[返回模块总览](README.md)
