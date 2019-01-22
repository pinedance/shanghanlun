---
layout: reference
title: "상한금궤 처방 목록(유취방 순서)"
tags: [index, 처방]
index:
  category: reference
  subject: 처방
---

{% assign formulas = site.data.bangk %}

{% for fml in formulas %}

### {{ fml.noo }} [{{ fml.name }} （{{ fml.name_kr }}）]({{site.formulaurl}}/{{fml.name_kr}})

> {{ fml.bangksj}}

* {{ fml.compose }}

{% endfor %}
