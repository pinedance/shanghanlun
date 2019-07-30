---
layout: reference
title: "상한론"
desc: "송본 상한론〔조문번호 '상한론역전' 기준〕"
tags: [상한금궤원문, 송본]
---


{{ page.desc }}
---------

조문번호 001 - 398 ("상한론수책" 기준)

<br>

{% for idx in (1..406) %}

{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% include clause.md notype="NOO.NoB" noo=noo %}

{% endfor %}
