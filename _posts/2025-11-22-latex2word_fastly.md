---
layout: post
title: "latex2word_fastly"
date: 2025-11-22
author: pepper
tags: [tool]
comments: true
toc: true
pinned: false
---

这篇博客关于使用 Pandoc 将 LaTeX 转换为 Word (DOCX) 的指南整理.

<!-- more -->

## 🚀 使用 Pandoc 将 LaTeX (TEX) 转换为 Word (DOCX)

---

### 🛠️ 前置条件：安装 Pandoc

首先，您需要下载并安装 Pandoc 工具。

请在官方 GitHub Release 页面下载：
[Pandoc 3.4 Release](https://github.com/jgm/pandoc/releases/tag/3.4)

安装完成后，打开命令行工具（如 Command Prompt, PowerShell 或 Terminal），输入以下命令进行验证：

```bash
pandoc -v
```

如果出现类似的版本信息（如截图所示），则说明安装成功。

### ✍️ 基础用法：

简单的文件转换

1. 打开命令行工具。
2. 切换到您的 `.tex` 文件（例如 `main.tex`）所在的目录。
3. 输入以下命令：

```bash
pandoc main.tex -o main.docx
```

如果命令执行后没有报错，说明转换成功。您可以直接在当前文件夹下找到生成的 `main.docx` 文件。

#### 格式进阶：

附带预设样式的转换如果您希望转换后的 `.docx` 文件（例如投稿论文）具有特定的预设样式（如期刊模板样式），您需要使用一个**参考文档** (`reference-doc`) 来指定样式。

步骤一：生成自定义参考文件首先，在您的 `.tex` 所在目录，输入以下命令生成一个基础的 `custom-reference.docx` 文件：

```bash
pandoc -o custom-reference.docx --print-default-data-file reference.docx
```

步骤二：修改样式接下来，您需要修改新生成的 `custom-reference.docx` 文件中的样式（标题、正文、列表等），使其符合您目标模板的要求。

- 如果您已经有一个模板，您需要将 `custom-reference.docx` 文件的**样式**更改为与目标模板一致。
- 关于如何修改 DOCX 样式，可以参考此外部链接（例如，将样式从一个文件导入到另一个文件）：
  [CSDN 博客：Word 样式修改参考](https://blog.csdn.net/symoriaty/article/details/80290838)

步骤三：使用参考文件进行转换修改完成后，使用 `--reference-doc` 参数将 `.tex` 文件转换为带有预设样式的 `.docx` 文件：

```bash
pandoc main.tex --reference-doc=custom-reference.docx -o main.docx
```

> **💡 注意：**
> Pandoc 官方推荐的方案是**新建**一个 `custom-reference.docx` 并在此文件上修改样式，而不是直接使用期刊给的模板文件作为参考文档。在实际使用中，直接使用模板通常无法达到修改格式的目的。

### 参考文献处理

（附带 `bib` 文件）
如果您的 LaTeX 文件使用了 `bib` 文件（例如 `ref.bib`）来管理参考文献，并希望转换时自动生成参考文献列表，您需要使用 `--bibliography`、`--citeproc` 和 `--csl` 参数。

```bash
pandoc --bibliography=ref.bib -o main.docx main.tex --citeproc --csl=nature.csl
```

- `--bibliography=ref.bib`: 指定您的参考文献数据库文件。
- `--citeproc`: 启用 Pandoc 的引文处理器。
- `--csl=[style.csl]`: 指定引文样式文件（CSL，Citation Style Language），例如 `nature.csl`。

---

📚 更多资源\* **Pandoc 官方手册：** 查阅更多命令行参数和用法
[https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)

- **关键参考博客：**
  [Medium: How to convert from LaTeX to MS Word with Pandoc](https://medium.com/@zhelinchen91/how-to-convert-from-latex-to-ms-word-with-pandoc-f2045a762293)

## 常见报错总结

- Pandoc 内置的数学公式转换引擎（texmath）不支持 `\xrightarrow` 这个命令

  `\xrightarrow` 是 LaTeX 中 amsmath 宏包提供的增强型箭头（可以随文字长度伸缩），但在转换为 Word 的 Office Math 格式（OMML）时，Pandoc 无法识别它。

  解决方法：使用兼容性更好的替代方案。将包含 `\xrightarrow` 替换成`\overset`。

```latex
\hat{G} = \{e_0 \xrightarrow{r_1} e_1 \xrightarrow{r_2} \dots \xrightarrow{r_k} e_k\} \in G
```

修改为：

```latex
\hat{G} = \{e_0 \overset{r_1}{\rightarrow} e_1 \overset{r_2}{\rightarrow} \dots \overset{r_k}{\rightarrow} e_k\} \in G
```

---
