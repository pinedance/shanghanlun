---
layout: reference
title: "상한금궤 처방 목록 (유취방 순서)"
tags: [index, 처방]
order: 5
index:
  category: reference
  subject: 처방
---

{% assign formulas = site.data.clause.EBK %}

{% for fml in formulas %}

### <small>{{ fml.noo }}</small> [{{ fml.name }} <small>（{{ fml.name_kr }}）</small>]({{site.formulaurl}}/{{fml.name_kr}})

> {{ fml.bangksj}}

* {{ fml.compose }}

{% endfor %}
