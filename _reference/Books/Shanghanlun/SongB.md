---
layout: reference
title: "상한론"
desc: "송본 상한론〔조문번호 '상한론역전' 기준〕"
tags: [상한론, 원문]
conf:
  template: template_shanghanlun.md
  data_src: site.data.shanghanlun
  bookinit: "全書"
---


{{ page.desc }}
---------

조문번호 001 - 398 ("상한론수책" 기준)

<br>

{% for idx in (1..406) %}

{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoB" %}
{% include {{ page.conf.template }} %}


{% endfor %}


