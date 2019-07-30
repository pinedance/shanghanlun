---
layout: reference
title: "상한론 조문 비교"
desc: "〔순화본 기준〕"
tags: [순화본, 조문비교]
conf:
  from: "Chun"
---


{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause.SHL_Chunhe %}
{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md book="SHL_Chunhe" noo=number %}
</div>

<div class="compared" markdown="1">
{% include compare/SHL-Tang.md noo=number from=page.conf.from %}
{% include compare/SHL-Song.md noo=number from=page.conf.from %}
</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
