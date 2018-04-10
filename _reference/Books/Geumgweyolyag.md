---
layout: reference
title: "금궤요략"
desc: "등진본 금궤요략〔조문번호 '조문순서' 기준〕"
tags: [금궤요략, 원문]
conf:
  template: template_shanghanlun-others.md
  bookinit: "金匱"
---

{% assign data_src = site.data.geumgweyolyag %}
{% assign bookinit = page.conf.bookinit %}


{{ page.desc }}
--------------------

<br> 

{% for t in data_src %}

{% assign noo = t.NOO %}
{% include {{ page.conf.template }} %}

{% endfor %}
