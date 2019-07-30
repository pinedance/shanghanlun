---
layout: reference
title: "맥경"
desc: "권7, 권8, 권9"
tags: [상한금궤원문, 맥경]
conf:
  book: "MK"
---

{{ page.desc }}

***

{% assign data_src = site.data.clause[ page.conf.book ] %}

{% for t in data_src %}

{% include clause.md book=page.conf.book noo=t.NOO %}

{% endfor %}
