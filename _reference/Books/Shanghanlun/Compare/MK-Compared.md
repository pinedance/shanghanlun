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
{% include compare.md noo=number from=page.conf.from map='Song' book="SHL_Song" %}
{% include compare.md noo=number from=page.conf.from map='SongRule' book="SHL_SongRule" %}
{% include compare.md noo=number from=page.conf.from map='SongGabu' book="SHL_SongGabu" %}
{% include compare.md noo=number from=page.conf.from map='SongEtc' book="SHL_SongEtc" %}

{% include compare.md noo=number from=page.conf.from map='Tang' book="SHL_Tang" %}
{% include compare.md noo=number from=page.conf.from map='Chunhe' book="SHL_Chunhe" %}
{% include compare.md noo=number from=page.conf.from map='Ogham' book="SHL_Ogham" %}

{% include compare.md noo=number from=page.conf.from map='GGYL' book="GGYL" %}
</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
