---
title: 'how_to_ScatterPlots_onMap'
date: 2025-02-28
permalink: /posts/2025/02/how_to_ScatterPlots_onMap/
tags:
  - Rearch
  - Papper
---

这篇博客撰写了编写相应的代码，将经纬度信息以图形化的方式呈现出来。

---

Scatter Plots on Mapbox with \`plotly\` Express in Python & How to Embed Them
 [100DaysOfCode](https://isabella-b.com/category/100daysofcode/), [python](https://isabella-b.com/category/python/), [tutorial](https://isabella-b.com/category/tutorial/), [mapbox](https://isabella-b.com/category/mapbox/), [plotly](https://isabella-b.com/category/plotly/)

[code](https://github.com/isabellabenabaye/los-angeles-police-killings/blob/master/LA-police-killings-map.ipynb) [source](https://github.com/datadesk/los-angeles-police-killings-data)[](https://twitter.com/_isabellamb/status/1272769156941668352?s=20)[](https://dev.to/isabellabenabaye/scatter-plots-on-mapbox-with-plotly-express-in-python-how-to-embed-them-1l8m)
  <Center>
  <img src='/images/blog/02/map.jpg' style='zoom:50%'>
  </Center>
  
Last week I was exploring the Los Angeles Times’ [database](https://github.com/datadesk/los-angeles-police-killings-data) of police killings in L.A. County, trying to learn more about the Black and Latino communities that have been disproportionately affected by police violence based on data since 2000. I made a simple graphic about it that you can find in my [blog post](https://isabella-b.com/blog/los-angeles-police-killings).

I also used that data to practice some EDA and data visualization in python. The data includes the latitude and longitude of where each person killed by police died, so one of the things I tried was mapping them with Mapbox and `plotly` Express. This map shows the places of death of the people killed who were Black.

To make this Mapbox map with Plotly you’ll need a Mapbox account and a public Mapbox access token. This is easy to get, and the code to create the map is fairly simple. I will go through the whole process.

First, import `plotly` Express:

    import plotly.express as px
    

Next, you’ll have to set your Mapbox access token and call it from a file in your directory called `.mapbox_token` that contains your Mapbox access token.

If you don’t have one yet, to get a token you have to create a Mapbox account, go to > `Account` > `+ Create a token`, name your token, then `Create token`. Copy the token and paste it to your `.mapbox_token` file in your directory.

Now we’ll set it:

    px.set_mapbox_access_token(open(".mapbox_token").read())
    

To create the plot, use `px.scatter_mapbox()`, and input your data frame and latitude & longitude fields to be used:

    fig = px.scatter_mapbox(data_frame=black_killings, lat='y', lon='x', 
      opacity=0.5, 
      hover_name="full_name", 
      hover_data=["year","neighborhood","cause"], 
      zoom=10)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},  # remove the white gutter between the frame and map
            # hover appearance
            hoverlabel=dict( 
            bgcolor="white",     # white background
            font_size=16,        # label font size
            font_family="Inter") # label font
    )
    fig.show()
    

**Optional settings:**  
`opacity` - the opacity of the dots  
`hover_name` - controls which column is displayed in bold as the tooltip title  
`hover_data` - list of columns whose values will be displayed in the body of the tooltip `zoom` - set the map’s initial zoom level

The details of `update_layout` are commented above.

## Embed the plot

To embed a `plotly` plot on a website, the easiest way if your data source is small, is by hosting it in `plotly`'s Chart Studio then embedding its `<iframe>`. Alternatively, you can generate an HTML file of the visualization, host it somewhere like GitHub pages (free) or your personal website, then call that page in the `<iframe>` to embed it. In this post I’ll use the Chart Studio route, and it’s applicable to any `plotly` visualization you create.

If you don’t have the Chart Studio python package yet, you can install it using the package manager **pip** in your terminal with `pip install chart_studio`. You will need a [`plotly` Chart Studio](https://chart-studio.plotly.com/feed/#/) account and your API key.

To get your API key: Click your username in the top right > `Profile` > `API Keys` > `Regenerate Key`

Now import `chart_studio` and set your credentials:

    import chart_studio
    username = 'your-username' 
    api_key = '' 
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
    

Save your plot to your Chart Studio cloud account with `py.plot()`. It creates a unique URL for your plot that `plotly` uses in the `<iframe>` it generates that you will use to embed your visualization on a website.

    import chart_studio.plotly as py
    py.plot(fig, filename = 'file-name', auto_open=True)
    

Running that should open the plot in Chart Studio in your browser. In the bottom right there is an icon where `plotly` provides the code to the `<iframe>` you can use.

Now you can use the `<iframe>` to embed your interactive `plotly` visualization on any website!

<!-- I hope you found this helpful. If you have any questions, feel free to comment below or [tweet/DM me](https://twitter.com/_isabellamb). -->



---