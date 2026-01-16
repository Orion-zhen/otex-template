# ⚓ 浮动体模块 (`floats`)

`floats` 模块优化了图片和表格在页面中的位置策略。

---

## 1. 加载的宏包

- `float`: 提供 `[H]` 强制位置选项。
- `flafter`: 确保浮动体总是出现在其被定义的位置之后。
- `placeins`: 当开启 `floats-in-section` 选项时，确保浮动体不跨越章节边界。

## 2. 优化参数

该模块对 LaTeX 默认的极度保守的浮动参数进行了优化：

- 提高了单一页面中图片/表格的覆盖上限（`topfraction` = 0.85）。
- 增加了页面总浮动体数量限制。
- 调整了浮动体前后的空隙（`textfloatsep` 等）。

## 3. 配置选项

- `floats`: (Boolean) 是否加载此模块，默认为 `true`。
- `floats-in-section`: (Boolean) 是否开启章节锁定，防止图片乱跑。

---
[返回模块总览](README.md)
