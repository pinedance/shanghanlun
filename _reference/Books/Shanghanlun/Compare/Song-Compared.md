---
layout: reference
title: "상한론 조문 비교"
desc: "〔송본 기준〕"
tags: [송본, 조문비교]
conf:
  template: template_shanghanlun.md
  bookinit: "全書"
---

{% assign notype = "NOO.NoA" %}
{% assign bookinit = page.conf.bookinit %}

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
{% assign noo = number %}{% include {{ page.conf.template }} %}
</div>

<div class="compared" markdown="1">
{% assign from = "Song" %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_rule.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_gabu.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Tang.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Chunhe.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Geum.md %}
</div>

{% if number contains "-000" %}
{% else %}
</div>
{% endif %}

{% endfor %}
