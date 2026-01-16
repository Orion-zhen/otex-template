# 💻 代码高亮模块 (`code`)

`code` 模块负责文档中的行内代码和代码块排版，支持强大的 `minted` (Pygments) 和经典的 `listings`。

---

## 1. 加载的宏包

- **`minted`**：当启用且开启 `--shell-escape` 时作为首选高亮引擎。
- **`listings`**：作为 `minted` 的回退方案或主代码包。

## 2. 提供的命令与环境

- `\code{text}`: 智能行内代码。开启 `minted` 时使用 `\mintinline`，否则回退到 `\texttt` 并带背景色。
- `listing` (环境): 代码块包装容器。
- `minted` (环境): 需要指定语言，如 `\begin{minted}{python}`。

## 3. 配置选项

- `listings`: (Boolean) 是否开启 `listings` 支持。
- `minted`: (Boolean) 是否尝试开启 `minted` 支持，默认为 `true`。

## 4. 使用示例

```latex
% 行内代码
使用 \code{print("hello")} 打印。

% 代码块 (minted)
\begin{listing}[H]
    \begin{minted}{python}
    def fib(n):
        return n if n < 2 else fib(n-1) + fib(n-2)
    \end{minted}
\end{listing}
```

---
[返回模块总览](README.md)
