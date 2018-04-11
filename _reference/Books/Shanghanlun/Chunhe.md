---
layout: reference
title: "상한론"
desc: "순화본 상한론〔太平聖惠方 卷第八〕"
tags: [상한금궤원문, 순화본]
conf:
  template: template_shanghanlun-others.md
  bookinit: "淳和"
---

{% assign data_src = site.data.shanghanlun-chunhe %}
{% assign bookinit = page.conf.bookinit %}


{{ page.desc }}
--------------------

<br>

{% for t in data_src %}

{% assign noo = t.NOO %}
{% include {{ page.conf.template }} %}

{% endfor %}
