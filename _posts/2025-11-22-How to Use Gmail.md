---
layout: post
title: 'How to Use Gmail'
date: 2025-11-22
author: pepper
tags: [Services, Gmail, Tips]
comments: true
toc: true
pinned: false
---

这篇博客介绍了 利用 Gmail 邮箱别名获取无限 Gmail 邮箱。
<!-- more -->

## 利用 Gmail 邮箱别名获取无限 Gmail 邮箱


最近 [Cursor AI 编程工具](https://link.zhihu.com/?target=https%3A//www.cursor.com/) 的火爆，导致在 X（Twitter）信息流基本上是炫没有编程的我用 Cursor 写了一个 XX 项目的帖子。但 Cursor 每月 20 美金的订阅费用对众多人是不小开支。

由于 Cursor 对新用户注册会有 2 周的免费 Pro 体验期，因此有很多人用不同的邮箱注册来注册新用户，持续白嫖 Cursor，但怎样获取众多免费的邮箱是个大问题。

有人琢磨出利用 [Gmail 邮箱别名](https://zhida.zhihu.com/search?content_id=247931467&content_type=Article&match_order=1&q=Gmail%E9%82%AE%E7%AE%B1%E5%88%AB%E5%90%8D&zhida_source=entity) 获取无限 Gmail 邮箱的方案。这里介绍一下 Gmail 邮箱别名的用法。

**需要强调一下：不鼓励此类利用别人善意恶意白嫖的行为，经济条件许可的尽量开 Pro 版支持一下，良性的生态需要大家支持和奉献。**

---

### Gmail 邮箱别名的规则

Gmail 邮箱为了避免用户误输入用户名导致用户无法收到邮件的常见问题，对邮箱用户名的一些特殊字符做了处理，包括：`.`、`+`、`@` 等，以及 `gmail.com` 等价于 `googlemail.com`。

下面以 `myusername@gmail.com` 为例说明：

1. **gmail.com 等价于 googlemail.com**

  对 Gmail 邮箱，邮箱后缀使用 `gmail.com` 和使用 `googlemail.com` 是相同的，往 `myusername@googlemail.com` 发邮件，`myusername@gmail.com` 会正常收到。

2. **用户名之间加 `.`**

  Gmail 邮箱中，在邮箱用户名中加 `.` 会被省略掉，也即 `myusername@gmail.com` 和如下的邮箱其实是一样的：

  - `my.username@gmail.com`
  - `my.user.name@gmail.com`
  - `my.user.n.ame@gmail.com`

3. **用户名加 `+` 任意字符**

  例如：

  - `myusername+111@gmail.com`
  - `myusername+222@gmail.com`
  - `myusername+aa@gmail.com`
  - `myusername+bb@gmail.com`

  以上邮箱都是 `myusername@gmail.com` 的别名。

  > 注意：有很多网站在注册时检查邮箱格式，如果使用 `+`，会提示邮箱格式错误。但 Cursor 对邮箱用户名包含的 `+` 不做检查。

4. **以上三种用法的结合**

  例如：

  - `my.username@googlemail.com`
  - `my.username+111@gmail.com`
  - `my.username+abc@gmail.com`

---

### Gmail 邮箱别名的一些用法

1. **不同的网站注册使用不同的别名，方便跟踪哪个网站泄露了个人资料**

2. **临时邮箱**

  许多提供 Gmail 临时邮箱的服务都使用了此技术，包括：

  - [Smailpro](https://link.zhihu.com/?target=https%3A//smailpro.com/)
  - [Emailnator](https://link.zhihu.com/?target=https%3A//www.emailnator.com/)
  - [22.Do](https://link.zhihu.com/?target=https%3A//22.do/)

3. **邮件分流**

  典型应用场景：[Newsletter 订阅](https://zhida.zhihu.com/search?content_id=247931467&content_type=Article&match_order=1&q=newsletter%E8%AE%A2%E9%98%85&zhida_source=entity)

  使用常用邮箱订阅 Newsletter 最大的问题是与正常邮件混在一起，每天处理很麻烦。用邮件别名 + 过滤器可以将不同的订阅自动路由到不同的 Label 标签文件夹下。

  **方法：**

  a. 在 Gmail 选择 “Settings → Labels”，“Create a new label” 栏填写 “News1”，单击 “Create” 按钮。

  b. 切换到 “Filters” 标签，单击 “Create a new filter” 链接，在 “To” 栏中填写 `myusername.news1@gmail.com`，单击 “Next Step” 按钮。在打开的页面中勾选 “Skip the Inbox (Archive it)” 和 “Apply the label” 并在下拉列表中选择 `myusername.news1@gmail.com`，单击 “Create Filter” 按钮。

  c. 借助 [Creating a ‘full fat’ RSS feed for Google Gmail labels with Google Apps Script](https://link.zhihu.com/?target=https%3A//pulse.appsscript.info/p/2022/03/creating-a-full-fat-rss-feed-for-google-gmail-labels-enabling-some-dark-social-judo/) 可以将 Label 转为 RSS feed，然后用 RSS 阅读器订阅。



### Outlook 如何实现无限别名

与 Gmail 类似，Outlook 邮箱也支持别名功能，可以通过以下方法实现无限别名：

1. **用户名加 `+` 任意字符**

  Outlook 邮箱支持在用户名后加 `+` 和任意字符来创建别名。例如：

  - `myusername+111@outlook.com`
  - `myusername+abc@outlook.com`
  - `myusername+xyz@outlook.com`

  以上邮箱都会被视为 `myusername@outlook.com` 的别名，邮件会正常接收。

2. **创建多个别名**

  Outlook 提供了直接创建多个别名的功能。具体操作步骤如下：

  a. 登录 [Outlook 邮箱](https://outlook.live.com/) 后，点击右上角的设置图标，选择 “View all Outlook settings”。

  b. 在设置页面中，选择 “Email → Sync email”，然后点击 “Manage or choose a primary alias”。

  c. 在打开的页面中，选择 “Add email”，输入新的别名并保存。

  通过这种方式，可以为一个 Outlook 账户创建多个独立的别名。

3. **邮件规则和分类**

  借助 Outlook 的邮件规则功能，可以对不同别名接收到的邮件进行分类。例如：

  a. 在设置页面中，选择 “Email → Rules”，点击 “Add new rule”。

  b. 设置规则名称，例如 “Newsletter 分类”，在条件中选择 “To”，填写对应的别名邮箱地址，例如 `myusername+news@outlook.com`。

  c. 在操作中选择 “Move to”，并指定一个文件夹，例如 “Newsletter”。

  d. 保存规则后，所有发往该别名的邮件都会自动分类到指定文件夹。

通过以上方法，Outlook 用户也可以轻松实现无限别名的功能，用于注册、分类邮件或其他用途。

  ---