---
layout: reference
title: "상한금궤 조문 비교"
desc: "〔금궤요략 기준〕"
tags: [금궤요략, 조문비교]
conf:
  from: "GGYL"
---

{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause.GGY %}
{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md noo=number %}
</div>

<div class="compared" markdown="1">
{% include compared.md number=number from=page.conf.from %}
</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
