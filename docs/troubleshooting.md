# 🛠️ 故障排除与常见问题 FAQ

这里记录了在使用 **otex** 过程中可能遇到的常见问题及其解决方案。

---

## 1. 字体缺失 (Font Not Found)

**现象**：编译时报错 `fontspec error: "font-not-found"`。

**解决方案**：

1. **检查预设**：虽然 otex 能够自动检测并匹配 `windows`/`linux`/`adobe` 预设，但如果你的系统环境非标准（如在不支持 Noto 的精简版 Linux 上），可能仍会报错。请手动指定 `font-set=linux` 或使用手动模式。
2. **使用 fonts-dir**：将所需字体放入项目 `fonts/` 文件夹，并配置 `\usepackage[fonts-dir=fonts]{otex}`。
3. **手动安装**：在 Windows 下右键安装字体；在 Linux 下将字体放入 `~/.local/share/fonts` 并执行 `fc-cache -fv`。

---

## 2. 宏包冲突 (Package Conflict)

**现象**：

- 报错 `Command \XXX already defined` 或 `Option clash for package XXX`。
- 或者，您可能会看到 otex 的智能警告（非错误）：
  - `Package 'xxx' conflict: symbol 'yyy' defined. Skipping load.`
  - `Conflict detected: Package 'xxx' conflicts with loaded package 'yyy'. Skipping.`

**解决方案**：

1. **相信 otex 的判断**：如果 otex 提示因为冲突而跳过了某个包的加载（如因 `mathpazo` 而跳过 `unicode-math`），这通常是保护性措施，避免编译崩溃。
2. **调整加载顺序**：尝试将 `\usepackage{otex}` 放在导言区的最后面，即恰好在 `\begin{document}` 之前，以让 otex 来管理包的加载顺序和选项平衡。
3. **极致手段**：如果某个模块冲突严重，请禁用它。例如 `\usepackage[notheorems]{otex}`。

---

## 3. minted 获取 Python 失败

**现象**：`minted` 报错 `-shell-escape` 未开启或找不到 `pygmentize`。

**解决方案**：

1. **确认安装**：确保你的电脑安装了 Python 和 Pygments (`pip install pygments`)。
2. **开启权限**：编译命令必须包含 `-shell-escape` 参数。
3. **回退方案**：如果不想折腾 Python，可以使用 `nominted` 选项，otex 会自动回退到基于原生 LaTeX 的 `listings` 模块。

---

## 4. 参考文献 (BibLaTeX) 报错

**现象**：报错 `File 'xxx.bbl' not created by biblatex`。

**解决方案**：

- 确认后端设置。otex 默认使用 `biblatex`。
- 如果你的环境不支持 `biber`，请尝试改用 `bibtex` 后端：
  `\usepackage[bib-backend=bibtex]{otex}`

---

## 5. 项目分发后他人无法编译

**现象**：你自己能编，同学考回去编不了。

**建议方案**：

- 采用 `fonts-dir` 将字体随项目分发。
- 确保对方也使用了兼容的编译器（推荐 XeLaTeX）。
- 将 `otex.sty` 和 `otex/` 模块文件夹一并打包发送。

---
[返回文档首页](README.md)
