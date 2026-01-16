# 🗂️ 索引管理模块 (`index`)

`index` 模块为文档提供术语索引（Index）支持。

---

## 1. 加载的宏包

- `imakeidx`: 一个现代的索引生成包，支持在编译时自动调用 `makeindex`。

## 2. 默认配置

- 启用双列布局 (`columns=2`)。
- 索引标题设置为 "Index"。
- 自动将索引页加入目录 (`intoc`)。

## 3. 配置选项

- `index`: (Boolean) 是否加载此模块，默认为 `false` (需要手动开启)。

## 4. 使用示例

```latex
% 在正文中标记索引项
这是一个术语\index{术语}。

% 在结尾生成索引
\printindex
```

---
[返回模块总览](README.md)
