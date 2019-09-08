---
layout: reference
title: "상한론 조문 비교"
desc: "〔금궤요략 기준〕"
tags: [금궤요략, 조문비교]
conf:
  from: "GGYL"
---

{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause.GGYL %}
{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% include clause.md book="GGYL" noo=number %}
</div>

<div class="compared" markdown="1">
{% include compare.md noo=number from=page.conf.from map='Song' book="SHL_Song" %}
{% include compare.md noo=number from=page.conf.from map='SongRule' book="SHL_SongRule" %}
{% include compare.md noo=number from=page.conf.from map='SongGabu' book="SHL_SongGabu" %}
{% include compare.md noo=number from=page.conf.from map='SongEtc' book="SHL_SongEtc" %}

{% include compare.md noo=number from=page.conf.from map='Tang' book="SHL_Tang" %}
{% include compare.md noo=number from=page.conf.from map='Chunhe' book="SHL_Chunhe" %}
{% include compare.md noo=number from=page.conf.from map='Ogham' book="SHL_Ogham" %}
{% include compare.md noo=number from=page.conf.from map='MK' book="MK" %}

</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
