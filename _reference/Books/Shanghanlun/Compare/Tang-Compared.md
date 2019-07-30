---
layout: reference
title: "상한론 조문 비교"
desc: "〔당본 기준〕"
tags: [당본, 조문비교]
conf:
  from: "Tang"
---

{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause.SHL_Tang %}
{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md book="SHL_Tang" noo=number %}
</div>

<div class="compared" markdown="1">
{% include compare/SHL-Song.md noo=number from=page.conf.from %}
{% include compare/SHL-Chunhe.md noo=number from=page.conf.from %}
</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
