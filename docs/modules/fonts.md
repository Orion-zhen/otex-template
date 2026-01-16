# 🖋️ 字体配置模块 (`fonts`)

`fonts` 模块利用 `fontspec` 系统实现了跨平台、高度可定制的字体加载逻辑。

---

## 1. 加载的宏包

- `fontspec`: 用于调用系统 OpenType/TrueType 字体。

## 2. 核心功能

- **三套预设方案**：`windows`, `linux`, `adobe`。
- **自动检测系统**：默认尝试匹配当前操作系统的最佳字体方案。
- **自定义路径**：支持 `fonts-dir` 选项，让字体随项目分发，无需安装到系统。

## 3. 配置选项

- `fonts`: (Boolean) 是否加载此模块，默认为 `true`。
- `font-set`: 指定字体预设。
- `fonts-dir`: 指定项目内的字体搜索目录。
- `main-font`, `sans-font`, `mono-font`: 手动覆盖西文字体名。
- `cjk-main-font`, `cjk-sans-font`, `cjk-mono-font`: 手动覆盖中文字体名。
- `math-font`: 手动覆盖数学公式字体（需 unicode-math 支持）。

---
详细的字体配置方案与手动绕过指南请参阅：[🖋️ 字体系统与跨平台配置](../compatibility/fonts.md)

---
[返回模块总览](README.md)
