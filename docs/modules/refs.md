# 🔗 交叉引用模块 (`refs`)

`refs` 模块通过超链接和智能引用增强了文档的交互性。

---

## 1. 加载的宏包

- `hyperref`: 提供超链接、PDF 书签和元数据设置。
- `cleveref`: 提供"智能引用"功能（如自动生成"图 1"字样）。

## 2. 提供的功能

- **自动化配置**：自动设置超链接颜色为深蓝/深绿/深红，提升阅读体验。
- **元数据填充**：根据 `pdf-title` 和 `pdf-author` 选项自动填充 PDF 属性。
- **中英文本地化**：在中文模式下，`\cref` 会自动识别并输出"图"、"表"、"定理"等中文前缀。

## 3. 配置选项

- `hyperref`: (Boolean) 是否加载超链接支持，默认为 `true`。
- `cleveref`: (Boolean) 是否加载智能引用支持，默认为 `true`。

## 4. 使用示例

### 4.1 传统引用 (`\ref` 系列)

传统引用是 LaTeX 内置的引用方式，需要手动添加引用类型前缀。

```latex
% 基本引用 - 只输出编号
如第 \ref{sec:intro} 节所示。          % 输出: 如第 1 节所示。
见图 \ref{fig:example}。              % 输出: 见图 1。

% 公式引用 - 自动添加括号
由公式 \eqref{eq:einstein} 可知...    % 输出: 由公式 (1) 可知...

% 页码引用
详见第 \pageref{sec:appendix} 页。    % 输出: 详见第 42 页。

% 组合使用
参见图 \ref{fig:arch} (第 \pageref{fig:arch} 页)。
```

**完整示例**：

```latex
\section{实验结果} \label{sec:results}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{result.pdf}
    \caption{实验结果对比} \label{fig:result}
\end{figure}

\begin{table}[htbp]
    \centering
    \caption{性能指标} \label{tab:perf}
    \begin{tabular}{cc}
        方法 & 准确率 \\
        A    & 95\%
    \end{tabular}
\end{table}

\begin{equation}
    E = mc^2 \label{eq:einstein}
\end{equation}

% 引用示例
如图 \ref{fig:result} 和表 \ref{tab:perf} 所示，
根据公式 \eqref{eq:einstein}，
在第 \ref{sec:results} 节中...
```

---

### 4.2 智能引用 (`\cref` 系列) - 推荐

智能引用由 `cleveref` 宏包提供，能够**自动识别引用类型并添加正确的前缀**。在中文模式下，会自动输出"图"、"表"、"定理"等中文前缀。

#### 基本用法

```latex
% 自动识别类型并添加前缀
\cref{fig:example}       % 中文输出: 图 1      | 英文输出: Figure 1
\cref{tab:data}          % 中文输出: 表 2      | 英文输出: Table 2
\cref{eq:maxwell}        % 中文输出: 式 3      | 英文输出: Equation 3
\cref{sec:intro}         % 中文输出: 节 1      | 英文输出: Section 1
\cref{thm:main}          % 中文输出: 定理 1    | 英文输出: Theorem 1
\cref{lem:aux}           % 中文输出: 引理 2    | 英文输出: Lemma 2
```

#### 句首大写

```latex
% 句首使用大写形式
\Cref{fig:example} shows the result.   % 输出: Figure 1 shows the result.
\Cref{sec:method} describes...         % 输出: Section 2 describes...
```

#### 多重引用

```latex
% 一次引用多个标签 (自动用逗号和"和"连接)
\cref{fig:a,fig:b,fig:c}       % 中文输出: 图 1, 2 和 3
                                % 英文输出: Figures 1, 2 and 3

\cref{eq:1,eq:2}               % 中文输出: 式 1 和 2
                                % 英文输出: Equations 1 and 2

% 混合类型引用
\cref{fig:demo,tab:data}       % 输出: 图 1 和 表 2
```

#### 范围引用

```latex
% 引用连续编号的对象
\crefrange{fig:a}{fig:d}       % 中文输出: 图 1 到 4
                                % 英文输出: Figures 1 to 4

\crefrange{eq:start}{eq:end}   % 中文输出: 式 1 到 5
                                % 英文输出: Equations 1 to 5

% 句首大写版本
\Crefrange{sec:intro}{sec:conclusion}  % 输出: Sections 1 to 5
```

#### 仅输出类型名

```latex
% 只输出类型名称，不含编号
\namecref{fig:example}         % 中文输出: 图 | 英文输出: figure
\nameCref{fig:example}         % 中文输出: 图 | 英文输出: Figure

% 复数形式
\namecrefs{fig:example}        % 英文输出: figures
\nameCrefs{fig:example}        % 英文输出: Figures
```

#### 完整示例

```latex
\section{方法} \label{sec:method}

\begin{theorem} \label{thm:convergence}
    该算法收敛。
\end{theorem}

\begin{lemma} \label{lem:bound}
    误差有界。
\end{lemma}

\begin{figure}[htbp]
    \centering
    \subfloat[情况 A]{\label{fig:case-a} ...}
    \subfloat[情况 B]{\label{fig:case-b} ...}
    \caption{实验对比} \label{fig:comparison}
\end{figure}

% 智能引用示例
\Cref{thm:convergence} 证明了算法的收敛性。
根据 \cref{lem:bound}，我们可以得出...
\cref{fig:case-a,fig:case-b} 分别展示了两种情况。
更多细节见 \crefrange{sec:method}{sec:conclusion}。
```

---

### 4.3 标签命名建议

为了保持一致性和可读性，建议使用以下前缀命名标签：

| 类型 | 前缀 | 示例 |
|------|------|------|
| 章节 | `sec:` | `\label{sec:introduction}` |
| 图片 | `fig:` | `\label{fig:architecture}` |
| 表格 | `tab:` | `\label{tab:comparison}` |
| 公式 | `eq:` | `\label{eq:maxwell}` |
| 定理 | `thm:` | `\label{thm:main}` |
| 引理 | `lem:` | `\label{lem:auxiliary}` |
| 代码 | `lst:` | `\label{lst:algorithm}` |
| 算法 | `alg:` | `\label{alg:quicksort}` |
| 附录 | `app:` | `\label{app:proofs}` |

## 5. 兼容性策略 (Compatibility Mode)

为了适应不同期刊模板对 `hyperref` 加载时机的不同要求，otex 实现了双模式加载机制：

### 5.1 主动模式 (Active Mode)

- **适用场景**：标准文档类（如 `article`, `report`）以及大多数一般模板。
- **行为**：otex 会在导言区**立即加载** `hyperref`。
- **日志**：`Hyperref loading mode: ACTIVE`

### 5.2 被动模式 (Passive Mode)

- **适用场景**：已知与早期 `hyperref` 加载冲突的复杂模板（**MDPI**, **acmart**, **beamer**）。
- **行为**：otex **不加载** `hyperref`，而是等待文档类自行加载。配置逻辑会被推迟到 `\AtBeginDocument` 执行。
- **日志**：`Hyperref loading mode: PASSIVE`

> **注意**：如果您的自定义模板出现 `LaTeX hooks Error`，可能说明它需要被加入被动模式列表。目前的黑名单包括：`mdpi`, `acmart`, `beamer`。

---
[返回模块总览](README.md)
