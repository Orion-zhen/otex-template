# 🧠 智能动态兼容性 (Dynamic Intelligent Compatibility)

otex 引入了全新的**动态智能兼容性**机制。不再依赖硬编码的文档类名称检测（如 `mdpi`, `acmart`），而是通过分析 LaTeX 环境中的**特征**（如已加载的包、当前字体设置）来自动调整自身行为。

这种设计确保了 otex 能够即插即用地适配几乎任何第三方 LaTeX 模板，而无需手动修改配置。

## 核心机制

### 自动退避 (Auto-Backoff)

当 otex 检测到环境已经被其他模板“接管”时，它会自动让出控制权，进入**退避模式 (Backoff Mode)**。

#### 1. 字体系统自动退避

**检测逻辑**：在加载字体设置前，otex 会检查 `\rmdefault`（默认罗马字体族）是否已被修改。

- 如果 `\rmdefault` 仍为标准的 `cmr` (Computer Modern) 或 `lmr` (Latin Modern)，otex 将按计划应用其字体配置。
- 如果检测到非标准字体（例如 MDPI 模板加载了 `mathpazo` 导致字体变为 `ppl`），或者检测到已加载了 `fontspec`/`mathpazo`/`times` 等字体包，otex 将自动设置 `font-set=none`。

**效果**：otex 不会覆盖模板原有的字体设计，从而避免 `bad native font flag` 等底层冲突。

#### 2. 标题系统自动退避

**检测逻辑**：otex (通过 `ctex` 模块) 通常会接管中文文档的标题样式。但在加载前，otex 会检查是否加载了 `titlesec` 宏包。

- `titlesec` 是许多定制模板（如 MDPI, ACM）用于深度定制标题的工具。
- 如果检测到 `titlesec`，otex 将强制 `ctex` 使用 `scheme=plain` 和 `heading=false`。

**效果**：`ctex` 不会重置或干扰模板精心设计的标题样式。

#### 3. 数学符号包自动退避

**检测逻辑**：otex 默认倾向于使用现代的 `unicode-math`。但在加载前，它会通过**冲突知识库**扫描当前的包列表。

- 如果检测到注册表中的冲突数学字体包（如 `mathpazo`, `newtxmath`, `fourier`, `stix`, `txfonts`, `pxfonts` 等），otex 会自动禁用 `unicode-math` 模块。
- 对于 `amssymb` 包，otex 还会叠加使用**符号存在性检测**：检查 `\Bbbk` 符号是否已定义。

**效果**：避免了 `unicode-math` 与传统数学包并存时的致命冲突，以及 `amssymb` 与 `newtxmath` 等包的 `Command already defined` 错误。

#### 4. Hyperref 加载自动退避 (Hyperref Backoff)

**检测逻辑**：otex 维护了一个**显式黑名单 (Explicit Blocklist)**，包含已知无法处理外部 `hyperref` 加载的复杂文档类（目前为 `mdpi`, `acmart`, `beamer`）。

- **被动模式 (Passive Mode)**：若检测到当前文档类在黑名单中，otex 将**放弃加载** `hyperref`，完全依赖文档类自行加载，仅在 `\AtBeginDocument` 阶段尝试补充配置。
- **主动模式 (Active Mode)**：对于其他标准或未知文档类，otex 默认采用主动加载策略，以确保最佳兼容性。

**效果**：解决了 MDPI 等模板因 `hyperref` 加载时机过晚导致的 `LaTeX hooks Error` 或 `Missing \begin{document}` 错误。

### 安全配置合并 (Safe Configuration Merging)

除了“退避”，otex 还引入了**增量合并**机制。当检测到某个包（如 `caption`, `titlesec`）已被模板预加载时：

1. **跳过破坏性配置**：otex 会自动停止应用其默认的、具有主观意见的样式（如字体大小、间距）。
2. **保留增强性配置**：otex 依然会运行那些必要的、无副作用的钩子（如元数据设置、兼容性补丁）。

**示例**：

如果您在导言区预先加载了 `\usepackage{caption}` 并设置了 `font=Large`，otex 识别到后，将不会强行将字体重置为 `small`，不仅消除了“选项冲突”错误，更完美保留了您的个性化设置。

### 符号存在性检测 (Symbol Safeguard)

作为知识库冲突检测的补充，otex 依然保留了**符号存在性检测**作为兜底策略（Fallback）。这种方式比单纯的包名检测更加通用，能捕捉隐式冲突。

**原理**：在加载某个包之前，检测该包提供的代表性符号是否已存在。如果存在，即使包名未列入黑名单，otex 也会跳过加载。

| 模块 | 包 | 代表性符号 |
| ---- | --- | --------- |
| `math` | `amssymb` | `\Bbbk` |
| `tables` | `booktabs` | `\toprule` |
| `tables` | `multirow` | `\multirow` |
| `tables` | `longtable` | `longtable` 环境 |
| `graphics` | `graphicx` | `\includegraphics` |
| `graphics` | `tikz` | `\tikz` |
| `floats` | `float` | `\newfloat` |
| `algo` | `algorithm2e` | `\SetKwInput` |
| `caption` | `caption` | `\captionsetup` |
| `toc` | `tocloft` | `\cftbeforetoctitleskip` |
| `base` | `siunitx` | `\SI` |

**优势**：

- 无需枚举所有可能冲突的包
- 直接检测本质条件（符号是否已存在）
- 适用于任何提供等效功能的第三方包

## 🕵️ 如何确认功能状态 (Verification)

由于 otex 会并在后台静默调整，您可以通过以下方式确认当前哪些功能已开启或被禁用：

### 1. 检查编译日志 (Log)

otex 在触发退避机制时，会向控制台和 `.log` 文件输出 `Package otex Warning` 信息。

**示例输出：**

```text
Package otex Warning: Non-standard font family 'ppl' detected. Preserving external font settings.
Package otex Warning: Package 'titlesec' detected. Disabling ctex heading modification and fontset.
Package otex Warning: Legacy math package 'mathpazo' detected. Disabling unicode-math.
```

如果您看到这些警告，说明 otex 已为了兼容性自动关闭了对应模块的“侵入式”功能，这通常是预期的良好行为。

### 2. 人工确认

- **字体**：若文档中的字体与您预期的一致（例如 MDPI 使用了 Palatino），则说明 otex 正确地退避了。
- **数学**：若 `\boldsymbol` 命令能正常工作且不想使用 `unicode-math` 的特性，则说明兼容模式生效。

## 开发者指南

如果你是模板开发者，或者希望强制覆盖这种自动行为，可以通过显式选项控制：

```latex
% 强制使用 otex 字体（忽略检测）
\usepackage[font-set=linux]{otex}

% 强制禁用 otex 字体
\usepackage[font-set=none]{otex}
```
