---
layout: reference
title: "상한론"
desc: "순화본 상한론〔太平聖惠方 卷第八〕"
tags: [상한금궤원문, 순화본]
conf:
  book: "SHL_Chunhe"
---

{{ page.desc }}
--------------------

<br>

{% assign data_src = site.data.clause[ page.conf.book ] %}

{% for t in data_src %}

{% include clause.md book=page.conf.book noo=t.NOO %}

{% endfor %}
