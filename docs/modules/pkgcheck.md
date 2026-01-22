# 🛡️ 智能包检查器 (`pkgcheck`)

`pkgcheck` 是 otex 的技术核心，它是一套基于 LaTeX3 和现代 LaTeX Hook 机制（LaTeX 2020/10/01+）的防御性宏包管理逻辑。

---

## 1. 核心 API：`\otex_safe_require:nnnn`

otex 的所有子模块都不会直接调用标准的 `\RequirePackage`，而是使用这个智能接口：

```latex
\otex_safe_require:nnnn {包名} {选项} {守卫符号} {配置代码}
```

### 混合策略工作流 (Hybrid Strategy)

该函数执行一种“混合检测”策略，结合了**Hook机制**、**符号检测**和**预加载保护**：

1. **预加载检查**：首先通过 `\IfPackageLoadedTF` 询问 LaTeX 内核该包是否已被加载。
    * **如果是**：标记 `\l_otex_pkg_preloaded_bool` 为真，并立即执行 `{配置代码}`（通过 Hook）。
    * **如果否**：进入符号检测阶段。

2. **符号冲突检测**：检查 `{守卫符号}`（如 `\newlist` 之于 `enumitem`）是否已存在。
    * **冲突**：如果包未加载但符号已存在，说明有冲突的包（如 `paralist`）占据了生态位。此时 otex **跳过加载**并发出警告（Backoff）。
    * **安全**：如果符号不存在，说明安全。此时 otex 加载该包，标记 `\l_otex_pkg_preloaded_bool` 为假，并注册 `{配置代码}`。

---

## 2. 安全合并与增量配置 (Safe Merging)

otex 遵循“不破坏”原则。当一个包已经被模板或用户预加载时，otex 会采取**增量配置**策略。

### 机制：`\l_otex_pkg_preloaded_bool`

在 `{配置代码}` 中，模块开发者可以使用此布尔标志来区分“加载者”：

* **False (由 otex 加载)**：此时 otex 拥有该包的控制权，应用所有**默认配置**（包括侵入性的样式修改，如字体大小、章节格式等）。
* **True (被预加载)**：此时 otex 仅作为“客人”。模块应当**跳过**默认样式配置，仅应用**无副作用的增强**（如设置 PDF 元数据、定义辅助命令等）。

### 示例 (`otex-caption`)

```latex
\otex_safe_require:nnnn { caption } {} { \captionsetup } 
{
  % 1. 只有当 otex 亲自加载 caption 时，才修改字体样式
  \bool_if:NF \l_otex_pkg_preloaded_bool
  {
    \captionsetup{ font=small, labelfont=bf, labelsep=colon }
  }
  
  % 2. 其他无副作用的逻辑（如果有）可以始终执行
}
```

这种设计确保了 otex 即便引入了 `caption` 模块，也不会覆盖用户在导言区手动设置的 `\captionsetup{font=Large}`。

---

## 3. 它的意义

这个模块是 otex 高兼容性的基石。它解决了两大难题：

1. **冲突避免**：通过符号检测防止加载冲突包。
2. **配置共存**：通过预加载保护，实现了 otex 配置与模板/用户配置的和平共存与智能合并。

---
[返回模块总览](README.md)
