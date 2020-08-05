---
layout: reference
title: "상한금궤 조문 비교"
desc: "〔자동 생성〕"
tags: [자동, 조문비교]
conf:
  method: "Auto"
  data: "similartext_auto"
---

{{ page.desc }}
--------------------

<br>

{% assign files = "SSB SSR SSG SSE STB SCB SCE SOB GGY SMK" | split: " " %}
{% assign books = "SSB SSR SSG SSE STB SCB SCE SOB GGY SMK" | split: " " %}
{% assign book_cnt = books | size | minus: 1 %}

{% assign data_compared = site.data.compare[page.conf.data] %}
{% for pair in data_compared %}

<div class="compare-set" markdown="1">
{% for i in ( 0..book_cnt ) %}

{% assign file = files[i] %}
{% assign book = books[i] %}
{% assign noos = pair[book] %}

{% if noos and noos.size != 0 %}

{% for noo in noos %}
{% include clause.md noo=noo %}
{% endfor %}

{% endif %}
{% endfor %}
</div>

<br>
{% endfor %}
