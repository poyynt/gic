---
layout: default
title: Blog
---
# Blog Latest Posts  

{% for post in site.posts %}
{% capture url %}{{ page.url }}/../{{ post.url }}{% endcapture %}
* [{{ post.title}}]({{ url }})
{% endfor %}
