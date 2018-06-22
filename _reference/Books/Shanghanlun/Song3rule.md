---
layout: reference
title: "상한론"
desc: "송본 상한론 〔法〕"
tags: [상한금궤원문, 송본]
conf:
  template: template_shanghanlun-others.md
  bookinit: "全書"
---

{% assign data_src = site.data.site.data.shanghanlun-rule %}
{% assign bookinit = page.conf.bookinit %}


{{ page.desc }}
--------------------

<br>

{% for t in data_src %}

{% assign noo = t.NOO %}
{% include {{ page.conf.template }} %}

{% endfor %}
