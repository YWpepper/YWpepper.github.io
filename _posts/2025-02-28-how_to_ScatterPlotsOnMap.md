---
title: 'how_to_ScatterPlotsOnMap'
date: 2025-02-28
author: pepper
permalink: /posts/2025/02/how_to_ScatterPlots_onMap/
pinned: false
toc: true
tags:
  - Rearch
  - Papper
---

这篇博客撰写了编写相应的代码,将经纬度信息以图形化的方式呈现出来。

<!-- more -->

---

## 使用英文版本的中国地图

```python
fig.update_layout(
    mapbox={
        'style': "carto-positron",  # 使用国际版OSM配置
        'zoom': 10,
        'center': {'lon': 116.25, 'lat': 40.12},
        'accesstoken': None
    },
    width=1200,
    height=800,
    margin={"r":0, "t":40, "l":0, "b":0},
    title="China Traffic Prediction Error Heatmap (English Labels)"
)
```

## 在 Python 中使用 Plotly Express 在 Mapbox 上绘制散点图

本教程参考自 [Isabella Benabaye](https://isabella-b.com) 的文章。

**相关链接:**

- [代码仓库](https://github.com/isabellabenabaye/los-angeles-police-killings/blob/master/LA-police-killings-map.ipynb)
- [数据来源](https://github.com/datadesk/los-angeles-police-killings-data)

<Center>
  <img src="https://images.weserv.nl/?url=cdn.nlark.com/yuque/0/2025/png/40742019/1762870316241-305be9e7-b868-4e58-b5e9-d398f22186a0.png?x-oss-process=image%2Fformat%2Cwebp" style="zoom:50%">
</Center>

### 背景介绍

上周我在探索洛杉矶时报关于洛杉矶县警察杀人事件的[数据库](https://github.com/datadesk/los-angeles-police-killings-data),试图根据 2000 年以来的数据了解更多受警察暴力不成比例影响的黑人和拉丁裔社区。我制作了一个简单的图表,你可以在我的[博客文章](https://isabella-b.com/blog/los-angeles-police-killings)中找到。

我还使用这些数据在 Python 中练习了一些探索性数据分析和数据可视化。数据包含每个被警察杀害的人死亡地点的经纬度,所以我尝试的一件事是使用 Mapbox 和 Plotly Express 绘制地图。这张地图显示了被杀害的黑人的死亡地点。

### 准备工作

要使用 Plotly 制作这个 Mapbox 地图,你需要一个 Mapbox 账户和一个公共 Mapbox 访问令牌。这很容易获得,创建地图的代码也相当简单。我将介绍整个过程。

首先,导入 Plotly Express:

```python
import plotly.express as px
```

### 设置 Mapbox 访问令牌

接下来,你需要设置 Mapbox 访问令牌,并从目录中名为 `.mapbox_token` 的文件中调用它,该文件包含你的 Mapbox 访问令牌。

如果你还没有令牌,要获取令牌,你必须创建一个 Mapbox 账户,转到 `Account` > `+ Create a token`,命名你的令牌,然后点击 `Create token`。复制令牌并将其粘贴到目录中的 `.mapbox_token` 文件中。

现在我们来设置它:

```python
px.set_mapbox_access_token(open(".mapbox_token").read())
```

### 创建散点图

要创建图表,使用 `px.scatter_mapbox()`,并输入你的数据框和要使用的经纬度字段:

```python
fig = px.scatter_mapbox(
    data_frame=black_killings, 
    lat='y', 
    lon='x', 
    opacity=0.5, 
    hover_name="full_name", 
    hover_data=["year","neighborhood","cause"], 
    zoom=10
)

fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},  # 移除框架和地图之间的白色间隙
    # 悬停外观
    hoverlabel=dict( 
        bgcolor="white",      # 白色背景
        font_size=16,         # 标签字体大小
        font_family="Inter"   # 标签字体
    )
)

fig.show()
```

**可选参数:**

- `opacity` - 点的不透明度
- `hover_name` - 控制哪一列以粗体显示为工具提示标题
- `hover_data` - 值将显示在工具提示正文中的列列表
- `zoom` - 设置地图的初始缩放级别

### 嵌入图表

要在网站上嵌入 Plotly 图表,如果你的数据源很小,最简单的方法是将其托管在 Plotly 的 Chart Studio 中,然后嵌入其 `<iframe>`。或者,你可以生成可视化的 HTML 文件,将其托管在 GitHub Pages(免费)或你的个人网站等地方,然后在 `<iframe>` 中调用该页面来嵌入它。在这篇文章中,我将使用 Chart Studio 路线,它适用于你创建的任何 Plotly 可视化。

#### 安装 Chart Studio

如果你还没有 Chart Studio Python 包,可以在终端中使用包管理器 **pip** 安装它:

```bash
pip install chart_studio
```

你需要一个 [Plotly Chart Studio](https://chart-studio.plotly.com/feed/#/) 账户和你的 API 密钥。

**获取 API 密钥:**
点击右上角的用户名 > `Profile` > `API Keys` > `Regenerate Key`

#### 设置凭据

现在导入 `chart_studio` 并设置你的凭据:

```python
import chart_studio

username = 'your-username' 
api_key = 'your-api-key' 
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
```

#### 上传图表

使用 `py.plot()` 将你的图表保存到你的 Chart Studio 云账户。它会为你的图表创建一个唯一的 URL,Plotly 在生成的 `<iframe>` 中使用该 URL,你将使用它在网站上嵌入你的可视化。

```python
import chart_studio.plotly as py

py.plot(fig, filename='file-name', auto_open=True)
```

运行该命令应该会在浏览器中的 Chart Studio 中打开图表。在右下角有一个图标,Plotly 在那里提供了你可以使用的 `<iframe>` 代码。

现在你可以使用 `<iframe>` 在任何网站上嵌入你的交互式 Plotly 可视化!

---
