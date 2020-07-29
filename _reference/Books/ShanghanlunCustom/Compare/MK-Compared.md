---
layout: reference
title: "상한론 조문 비교"
desc: "〔맥경 기준〕"
tags: [맥경, 조문비교]
conf:
  from: "MK"
---

{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause.MK %}
{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md book="MK" noo=number %}
</div>

<div class="compared" markdown="1">
{% include compared.md number=number from=page.conf.from %}
</div>


{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
