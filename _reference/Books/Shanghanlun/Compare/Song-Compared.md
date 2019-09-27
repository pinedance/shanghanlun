---
layout: reference
title: "상한론 조문 비교"
desc: "〔송본 기준〕"
tags: [송본, 조문비교]
conf:
  from: "Song"
---

{{ page.desc }}
---------

<br>

{% for idx in (1..398) %}
{% assign number = idx | prepend: '000' | slice: -3, 3 %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md noo=number %}
</div>

<div class="compared" markdown="1">
{% include compared.md from=page.conf.from %}
</div>


{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
