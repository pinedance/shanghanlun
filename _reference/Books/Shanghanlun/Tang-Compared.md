---
layout: reference
title: "상한론 조문 비교"
desc: "〔당본 기준〕"
tags: [상한론, 원문]
conf:
  template: template_shanghanlun-others.md
  bookinit: "唐翼"
---

{% assign data_src = site.data.shanghanlun-tang %}
{% assign bookinit = page.conf.bookinit %}

{{ page.desc }}
--------------------

<br>

{% for t in data_src %}
{% assign number = t.NOO %}

{% if number contains "-00" %}
{% else %}
<div id="{{bookinit}}{{number}}" class="compare-set">
{% endif %}

<div class="origin" markdown="1">
{% assign data_src = site.data.shanghanlun-tang %}
{% assign bookinit = page.conf.bookinit %}
{% assign noo = number %}{% include {{ page.conf.template }} %}
</div>

<div class="compared" markdown="1">
{% assign from = "Tang" %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Song.md %}
{% assign noo = number %}{% include template_shanghanlun_text_compare_with_Chunhe.md %}
</div>

{% if number contains "-00" %}
{% else %}
</div>
{% endif %}

{% endfor %}
