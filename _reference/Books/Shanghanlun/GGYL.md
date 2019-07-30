---
layout: reference
title: "금궤요략"
desc: "등진본 금궤요략〔조문번호 '조문순서' 기준〕"
tags: [상한금궤원문, 금궤요략]
conf:
  book: "GGYL"
---

{{ page.desc }}

***

{% assign data_src = site.data.clause[ page.conf.book ] %}

{% for t in data_src %}

{% include clause.md book=page.conf.book noo=t.NOO %}

{% endfor %}
