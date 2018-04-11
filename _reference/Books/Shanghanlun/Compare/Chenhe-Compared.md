---
layout: reference
title: "상한론 조문 비교"
desc: "〔순화본 기준〕"
tags: [순화본, 조문비교]
conf:
  template: template_shanghanlun-others.md
  bookinit: "淳和"
---

{% assign data_src = site.data.shanghanlun-chunhe %}
{% assign bookinit = page.conf.bookinit %}

{{ page.desc }}
--------------------

<br>

{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-00" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% assign data_src = site.data.shanghanlun-chunhe %}
{% assign bookinit = page.conf.bookinit %}
{% assign noo = number %}{% include {{ page.conf.template }} %}
</div>

<div class="compared" markdown="1">
{% assign from = "Chun" %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Tang.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Song.md %}
</div>

{% if number contains "-00" %}
{% else %}
</div>
{% endif %}

{% endfor %}
