---
layout: reference
title: "방극/방극산정"
desc:
tags: [관련원문, 방극, 방극산정]
src_path: template_shanghanlun.md
---



{% for idx in (1..204) %}

{% assign frms = site.data.bangk | where: "noo", idx %}

{% for frm in frms %}

<div id="{{ frm.name_kr }}"></div>
### [ {{ frm.name }} <small>{{ frm.name_kr }}</small> ]({{ site.formulaurl }}/{{ frm.name_kr }})

> {{ frm.bangk }}

> {{ frm.bangksj }}

{% endfor %}

{% endfor %}
