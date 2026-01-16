# otex 技术文档

欢迎查阅 **otex** 技术文档。本手册详细介绍了如何配置、扩展以及在复杂模板中使用 otex 包。

## 🗺️ 文档导航

### 1. [🌍 兼容性深度解析](compatibility/README.md)

深入了解 otex 如何在不同平台和语言环境中保持一致的表现。

- [🖋️ 字体系统与跨平台配置](compatibility/fonts.md)
- [💻 跨平台差异处理 (Win/Linux/Mac)](compatibility/cross-platform.md)
- [🇨🇳 多语言自动本地化](compatibility/localization.md)

### 2. [🚀 快速入门指南](getting-started.md)

从安装到编写第一个文档，快速掌握 otex 的基本用法。

### 3. [⚙️ 全量选项参考](options.md)

otex 提供了数十个配置参数，本章节提供详尽的 API 说明和默认值查询。

### 4. [🧩 子模块功能详解](modules/README.md)

otex 由 19 个功能模块组成，你可以深入了解每个模块加载了哪些包、提供了哪些命令。

- 数学公式 (`math`)、定理环境 (`theorems`)、代码高亮 (`code`)、表格 (`tables`) 等。

### 5. [🛠️ 故障排除与常见问题](troubleshooting.md)

遇到编译错误或字体缺失？在这里查找解决方案。

---

## 🏗️ 核心设计理念

1. **LaTeX3 驱动**：底层使用 `expl3` 编写，逻辑严密，变量命名规范。
2. **非侵入性**：尽可能通过钩子（Hook）和智能包检测来工作，减少对用户代码的干扰。
3. **防御性编程**：在加载任何宏包前都会检查冲突，确保在各种第三方模板（如 `hithesis`）中都能稳定运行。

---
[返回项目主页](../../README.md)
