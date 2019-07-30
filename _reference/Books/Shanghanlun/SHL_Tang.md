---
layout: reference
title: "상한론"
desc: "당본 상한론〔千金翼方 卷第九-十〕"
tags: [상한금궤원문, 당본]
---

{{ page.desc }}

***

{% assign data_src = site.data.clause.SHL_Tang %}

{% for t in data_src %}

{% include clause.md book="SHL_Tang" noo=t.NOO %}

{% endfor %}
