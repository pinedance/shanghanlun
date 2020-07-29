---
layout: reference
title: "상한론 조문 비교"
desc: "〔자동 생성〕"
tags: [자동, 조문비교]
conf:
  from: "Auto"
---

{{ page.desc }}
--------------------

<br>

{% assign files = "SHL_Song SHL_SongRule SHL_SongGabu SHL_SongEtc SHL_Tang SHL_Chunhe SHL_ChunheEtc SHL_Ogham GGYL MK" | split: " " %}
{% assign books = "Song SongRule SongGabu SongEtc Tang Chunhe ChunheEtc Ogham GGYL MK" | split: " " %}
{% assign book_cnt = book.size | minus: 1 %}

{% assign data_compared = site.data.compare.similartext_auto %}
{% for pair in data_compared %}

* {{ books }}
* {{ files }}
* {{ book_cnt }}

<div class="compared" markdown="1">
{% for i in ( 0..book_cnt ) %}

{{i}}

{% assign file = files[i] %}
{% assign book = books[i] %}
{% assign noos = pair[book] %}

* {{file}} ; {{book}} ; {{noos}}

{% if noos and noos.size != 0 %}

{% for noo in noos %}
{% include clause.md book=file noo=noo %}
{% endfor %}

{% endif %}
{% endfor %}
</div>

{% endfor %}
