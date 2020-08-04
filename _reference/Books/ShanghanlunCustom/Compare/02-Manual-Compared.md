---
layout: reference
title: "상한금궤 조문 비교"
desc: "〔수동 생성〕"
tags: [수동, 조문비교]
conf:
  method: "Manual"
  data: "similartext"
---

{{ page.desc }}
--------------------

<br>

{% assign files = "SHL_Song SHL_SongRule SHL_SongGabu SHL_SongEtc SHL_Tang SHL_Chunhe SHL_ChunheEtc SHL_Ogham GGYL MK" | split: " " %}
{% assign books = "Song SongRule SongGabu SongEtc Tang Chunhe ChunheEtc Ogham GGYL MK" | split: " " %}
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
{% include clause.md book=file noo=noo %}
{% endfor %}

{% endif %}
{% endfor %}
</div>

<br>
{% endfor %}
