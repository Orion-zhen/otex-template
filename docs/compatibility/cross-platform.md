# 💻 跨平台差异处理

otex 在设计时充分考虑了 Windows, Linux 和 macOS 之间的细微差别，特别是在文件路径和外部程序调用方面。

---

## 1. 编译引擎与环境建议

| 特性 | Windows | Linux / macOS |
| :--- | :--- | :--- |
| **推荐引擎** | XeLaTeX | XeLaTeX |
| **备选引擎** | LuaLaTeX | LuaLaTeX |
| **推荐发行版** | MikTeX / TeX Live | TeX Live / MacTeX |

### 为什么推荐 XeLaTeX？

otex 的核心功能（如字体加载和中文支持）对 XeLaTeX 的依赖度最高。虽然我们也支持 LuaLaTeX，但在复杂的 `xeCJK` 适配和 `fontspec` 调用上，XeLaTeX 往往能提供更稳定、更快的编译速度。

---

## 2. 文件路径处理

LaTeX 的 `\RequirePackage` 虽然在大多数情况下能自动处理路径，但 otex 内部通过 LaTeX3 的路径合并逻辑确保了跨平台的健壮性。

- **自动斜杠转换**：无论你在 Windows 下指定 `fonts-dir=fonts\myfont` 还是在 Linux 下指定 `fonts-dir=fonts/myfont`，otex 内部都会统一处理。
- **相对路径优先**：建议始终使用相对于项目根目录的路径，以确保项目分发后的可移植性。

---

## 3. Shell-escape 与外部程序

如果你使用了 `minted` 模块，otex 会检测编译时是否开启了 `--shell-escape`（通过内置的 `pdftexcmds` 逻辑）。

- **Windows 警告**：在 Windows + MikTeX 环境下，由于安全策略，`shell-escape` 往往需要手动在编译器设置中全局开启。
- **Linux 支持**：在 Linux 下，`latexmk` 通常能很好地通过配置文件自动开启。

---

## 4. 文件编码强制要求

**otex 强制要求所有源文件使用 UTF-8 编码。**

- otex 内部加载了 `inputenc` (仅补丁) 或直接在 XeLaTeX 下假设 UTF-8 流。
- 如果你的项目包含旧有的 GBK 编码文件，建议使用命令行工具（如 `iconv`）进行转换后再配合 otex 使用。

---
[返回兼容性首页](README.md) | [返回文档首页](../README.md)
