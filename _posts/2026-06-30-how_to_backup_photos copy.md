---
layout: post
title: "工具-照片备份操作指南（rsync）"
date: 2026-06-30
author: pepper
tags: [tool, mac, photo]
comments: true
toc: true
pinned: false
---

这篇博客介绍了使用 rsync 命令进行照片备份的操作指南，包括日常备份、完整性校验、备份策略建议以及一键备份脚本。

<!-- more -->
# 照片备份操作指南

## 一、日常备份（推荐）

使用 `rsync` 命令，只同步新增/变化的文件，已有文件不会重复拷贝。

```bash
rsync -avh --progress \
  --exclude='.DS_Store' \
  --exclude='._*' \
  --exclude='.fseventsd/' \
  "/Volumes/源盘名称/照片/" \
  "/Volumes/备份盘名称/备份目录/照片/"
```

### 参数说明

| 参数           | 作用                                   |
| -------------- | -------------------------------------- |
| `-a`         | 归档模式（保留权限、时间戳、符号链接） |
| `-v`         | 显示详细过程                           |
| `-h`         | 人类可读的大小显示                     |
| `--progress` | 显示实时传输进度                       |
| `--exclude`  | 排除不需要的文件                       |

### 注意事项

- 源路径末尾的 `/` 不能省，表示"复制目录里的内容"
- 中途可以 `Ctrl+C` 中断，再次运行会从断点继续
- 已存在且相同的文件会自动跳过，不会重复传输

---

## 二、验证备份完整性

### 快速检查（文件存在性对比）

只对比两边文件名，几秒钟出结果：

```bash
SRC="/Volumes/源盘名称/照片"
DST="/Volumes/备份盘名称/备份目录/照片"
TMP="/tmp/photo_check"
mkdir -p "$TMP"

# 扫描两边文件列表
find "$SRC" -type f ! -name '._*' ! -name '.DS_Store' ! -path '*/.fseventsd/*' | sed "s|^$SRC/||" | sort > "$TMP/src.txt"
find "$DST" -type f ! -name '._*' ! -name '.DS_Store' ! -path '*/.fseventsd/*' | sed "s|^$DST/||" | sort > "$TMP/dst.txt"

# 对比
echo "源文件数: $(wc -l < $TMP/src.txt | tr -d ' ')"
echo "备份文件数: $(wc -l < $TMP/dst.txt | tr -d ' ')"
echo "缺失文件数: $(comm -23 $TMP/src.txt $TMP/dst.txt | wc -l | tr -d ' ')"
echo "多余文件数: $(comm -13 $TMP/src.txt $TMP/dst.txt | wc -l | tr -d ' ')"
```

如果缺失文件数 > 0，重新运行第一节的 rsync 命令即可补全。

### 深度校验（MD5 校验，可选）

对文件内容做 MD5 校验，确认没有损坏。**注意：速度慢，适合定期抽检，不建议每次都做。**

```bash
# 对两边共有文件计算 MD5 并对比
join -t'|' -1 2 -2 2 \
  <(while IFS='|' read -r size path; do
     md5 -q "$SRC/${path#./}" 2>/dev/null | tr -d '\n'
     echo "|$path"
   done < src_list.txt | sort -t'|' -k2) \
  <(while IFS='|' read -r size path; do
     md5 -q "$DST/${path#./}" 2>/dev/null | tr -d '\n'
     echo "|$path"
   done < dst_list.txt | sort -t'|' -k2) | \
  awk -F'|' '{ if ($2 != $3) print "MD5不匹配: "$1 }'
```

---

## 三、备份策略建议

### 频率

| 场景                         | 建议频率     |
| ---------------------------- | ------------ |
| 日常使用                     | 每周 1 次    |
| 大量导入新照片后             | 当天立即备份 |
| 重要活动照片（旅行、婚礼等） | 拍完立即备份 |

### 3-2-1 原则（最佳实践）

- **3** 份数据副本（原始 + 2 份备份）
- **2** 种不同存储介质（硬盘 + U 盘 / 硬盘 + 云）
- **1** 份异地存放（云端或其他地点）

建议：
- 增加一份云端备份（如 iCloud、百度网盘、阿里云盘）
- 或第三块物理硬盘放在不同地点

---

## 四、常见问题

### Q: rsync 中断了怎么办？

A: 重新运行同样的命令即可，rsync 会自动从断点继续。

### Q: 怎么知道备份完了没？

A: 运行完 rsync 后，再运行第二节的快速检查命令，缺失文件数为 0 就是完整的。

### Q: 源目录删了文件，备份里还留着？

A: 默认 rsync 只增不删。如果想让备份和源目录完全一致（源删了备份也删），加上 `--delete` 参数：

```bash
rsync -avh --progress --delete \
  --exclude='.DS_Store' \
  --exclude='._*' \
  "/Volumes/源盘名称/照片/" \
  "/Volumes/备份盘名称/备份目录/照片/"
```

⚠️ 慎用 `--delete`，先确认源目录没问题再加。

### Q: 硬盘名字变了怎么办？

A: 修改命令里的路径即可。可以在 Finder 中右键硬盘 → 显示简介，查看或修改硬盘名称。

### Q: 备份速度慢？

A:

- 用 USB 3.0/Type-C 接口
- 第一次备份会慢（全量），之后很快（只传增量）
- 大文件多的话耐心等待，正常现象

---

## 五、一键脚本（可选）

把下面的内容保存为 `backup_photos.sh`，修改前两行的路径为你自己的，以后双击或在终端运行 `bash backup_photos.sh` 即可。

```bash
#!/bin/bash
SRC="/Volumes/源盘名称/照片"
DST="/Volumes/备份盘名称/备份目录/照片"

if [ ! -d "$SRC" ]; then
  echo "❌ 源目录不存在: $SRC"
  exit 1
fi

if [ ! -d "$DST" ]; then
  echo "❌ 备份目录不存在: $DST"
  exit 1
fi

echo "🚀 开始备份照片..."
echo "源: $SRC"
echo "目标: $DST"
echo ""

rsync -avh --progress \
  --exclude='.DS_Store' \
  --exclude='._*' \
  --exclude='.fseventsd/' \
  "$SRC/" "$DST/"

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ 备份完成！"
else
  echo ""
  echo "❌ 备份过程中出现错误，请检查后重试"
  exit 1
fi
```

保存后执行 `chmod +x backup_photos.sh` 赋予执行权限。
