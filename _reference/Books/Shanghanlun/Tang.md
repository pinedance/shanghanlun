---
layout: reference
title: "상한론"
desc: "당본 상한론〔千金翼方 卷第九-十〕"
tags: [상한론, 원문, 당본]
conf:
  template: template_shanghanlun-others.md
  bookinit: "唐翼"
---

{% assign data_src = site.data.shanghanlun-tang %}
{% assign bookinit = page.conf.bookinit %}


{{ page.desc }}
--------------------

<br>

{% for t in data_src %}

{% assign noo = t.NOO %}
{% include {{ page.conf.template }} %}

{% endfor %}
