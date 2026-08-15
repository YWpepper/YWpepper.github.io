---
layout: post
title: "工具-Mac-M系列ACE驱动安装问题笔记"
date: 2026-08-15
author: pepper
tags: [tool, mac]
comments: true
toc: true
pinned: false
---

这篇博客介绍了在M系列Mac上安装ACE驱动时遇到的问题，以及两种解决方案：一种是修改安全策略以允许内核扩展，另一种是使用替代方案如OBS Studio来捕获音频而无需修改系统设置。

<!-- more -->

# Mac M系列 ACE驱动安装问题笔记

## 现状

- 无法使用mac原生态的 QuickTime Playerl 来录制本地的声音🔊？

- 安装Movavi Screen Recorder/ AudioHijack / Loopback软件 软件后无法安装ACE音频内核扩展?

  ![image.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151340206.png)

- M系列Mac点击【启用系统扩展】弹窗提示：**需要恢复模式修改安全设置**，普通系统设置无法直接开启。

  ![image.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151340813.png)

> ⚠️「任何来源」选项仅控制普通App，**对内核扩展Kext无效**。

## 方案一：修改安全策略，正常使用ACE（需要进恢复模式）

### 进入恢复模式操作步骤

1. 完全关机Mac

   ![image.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151340590.png)

2. 长按电源键，直到出现「选项⚙️」，松开电源键 → 点击【选项】→【继续】进入恢复模式

   ![image.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151341248.png)

3. 顶部菜单：实用工具 → **启动安全性实用工具**

4. 选中系统磁盘(Macintosh HD) →【安全策略】

5. 设置为**降低安全性**，勾选「允许用户管理内核扩展」，输入密码确认

   ![image.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151341780.png)

6. 顶部菜单打开【实用工具-终端】，输入放行开发者命令：

   ```
   spctl kext-consent add 7266XEXAPM
   ```

7. 输入`reboot`重启回到正常系统

8. 回到桌面，重新触发ACE安装，在「安全性与隐私」允许该系统扩展，再次重启Mac。

   ![Snipaste_2026-08-15_12-55-19.png](https://virginia-pepper.oss-cn-guangzhou.aliyuncs.com/img/blog/202608151341802.png)

### ⚠️恢复模式&降低安全性风险说明

1. **仅仅进入恢复模式，不修改任何选项，电脑完全无变化，不会删除任何文件**。不要执行抹掉磁盘、重装系统操作。
2. 修改为【降低安全性】的实际影响
   - ✅效果：可以加载ACE等第三方内核扩展
   - ⚠️理论风险：系统允许加载内核级驱动，若安装来路不明驱动，恶意程序可获取系统最高权限。**只使用官网正版软件，日常几乎无实际风险**。
   - FileVault磁盘加密不受影响，可以正常接收macOS系统更新。
   - macOS大版本更新后，安全策略**可能被重置，ACE会失效，需要重新配置**。
   - 开机进度条会短暂变长，属于正常现象。
3. 可以随时复原：再次进入恢复模式，安全策略切回【完整安全性】，关闭内核扩展权限。

## 方案二：不修改安全策略，替代方案（推荐，不用进恢复模式）

> 不想改动系统安全策略，就放弃ACE驱动，更换音频捕获方案

| 方案                      | 是否要恢复模式 | 能力                         | 成本       | 备注                                                 |
| ------------------------- | -------------- | ---------------------------- | ---------- | ---------------------------------------------------- |
| ACE(Loopback/AudioHijack) | ✅必须         | 可单独抓取某一个App声音      | 付费       | M芯片必须降低安全策略                                |
| BlackHole虚拟声卡         | ❌否           | 抓取全部系统混音，不能分应用 | 免费开源   | AU插件，非内核扩展                                   |
| OBS‑macOS音频捕获         | ❌否           | ✅支持单独捕获单个App声音    | 免费       | 使用苹果ScreenCaptureKit新接口，**零驱动，优先推荐** |
| 硬件对录线                | ❌否           | 录制全部系统声音             | 需要买线材 | 音质损耗，占用耳机口                                 |

### ✅首选替代：OBS Studio（最简）

1. 下载新版OBS Studio(30版本以上)
2. 来源→添加→**macOS音频捕获**
3. 直接选择要录制的软件，即可捕获该程序内部声音，无需任何虚拟声卡与内核驱动。

### 选择建议

1. 轻度录制声音：直接用OBS，不碰恢复模式，维持出厂完整安全防护。
2. 重度需要音频路由、分软件音频处理：选择方案一，恢复模式修改安全策略，只安装官网来源软件。
3. 后续不再使用ACE相关软件：记得切回完整安全性。

### ⚠️ 退出恢复模式后 ACE 插件状态

ACE 会失效的场景

- 你手动二次进入恢复模式，把安全策略切回完整安全性。
- **macOS 大版本系统升级（例如 Sonoma 升级 Sequoia）**：部分更新会重置安全策略，自动变回完整安全性，ACE 就不能用，需要再次进恢复模式重新设置降低安全性**Rogue Amoe...**
