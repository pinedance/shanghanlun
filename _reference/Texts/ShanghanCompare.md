---
layout: reference
title: "상한론 조문 비교"
desc: "상한론 조문 비교〔송본 기준〕"
tags: [상한론, 원문]
src_path: template_shanghanlun.md
---


송본상한론
---------

조문번호 001 - 398 ("상한론수책" 기준)

<br>

{% for idx in (1..398) %}

{% assign noo = idx | prepend: '000' | slice: -3, 3 %}


<div class="origin" markdown="1">

{% assign notype = "NOO.NoA" %}
{% include {{page.src_path}} %}

<div class="compared" markdown="1">

{% include template_shanghanlun_text_compare.md %}

</div>

</div>

{% endfor %}
