---
layout: reference
title: "상한론"
desc: "宋本 傷寒論1 〔서문 ∽ 辨痓濕暍〕"
tags: [상한금궤원문, 송본]
---



[刻《仲景全書》序]({{site.baseurl}}/reference/Books/Shanghanlun/Foreword/송본_조개미_서)

[《傷寒論》序]({{site.baseurl}}/reference/Books/Shanghanlun/Foreword/송본_임억_서)

[《傷寒卒病論》集]({{site.baseurl}}/reference/Books/Shanghanlun/Foreword/송본_상한잡병론_집론)

[醫林列傳]({{site.baseurl}}/reference/Books/Shanghanlun/Foreword/송본_의림열전)

[國子監]({{site.baseurl}}/reference/Books/Shanghanlun/Foreword/송본_국자감_상서)


## 辨脈法第一

{% for idx in (1..37) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "01-" | append: nooTail %}
{% include clause.md book="SHL_SongEtc" noo=noo %}

{% endfor %}



## 平脈法第二

{% for idx in (1..50) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "02-" | append: nooTail %}
{% include clause.md book="SHL_SongEtc" noo=noo %}

{% endfor %}

## 傷寒例第三

{% for idx in (1..43) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "03-" | append: nooTail %}
{% include clause.md book="SHL_SongEtc" noo=noo %}

{% endfor %}


## 辨痓濕暍脈證第四 <small>痓音◍又作痓去郢切下同</small>

{% for idx in (1..16) %}

{% assign nooTail = idx | prepend: '000' | slice: -3, 3 %}
{% assign noo = "04-" | append: nooTail %}
{% include clause.md book="SHL_SongEtc" noo=noo %}

{% endfor %}
