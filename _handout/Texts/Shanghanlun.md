---
layout: handout
title: "상한론 조문"
desc: "송본〔조문번호 '상한론수책' 기준〕"
tags: 상한론, 원문
src_path: template_shanghanlun.md
---


송본상한론
---------

조문번호 001 - 398 ("상한론수책" 기준)

<br>

{% for idx in (1..398) %}

{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{page.src_path}} %}


{% endfor %}
