---
layout: reference
title: "상한론"
desc: "송본 상한론 〔法〕"
tags: [상한금궤원문, 송본]
---

{{ page.desc }}

***


{% assign data_src = site.data.clause.SHL_SongRule %}

{% for t in data_src %}

{% include clause.md book="SHL_SongRule" noo=t.NOO %}

{% endfor %}
