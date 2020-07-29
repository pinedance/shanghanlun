---
layout: reference
title: "方極〔方極刪定〕"
desc: "吉益東洞"
tags: [관련원문, 방극, 방극산정]
---

{% for idx in (1..204) %}
{% assign frms = site.data.clause.bangk | where: "noo", idx %}
{% for frm in frms %}

<div id="{{ frm.name_kr }}" markdown="1">

### [ {{ frm.name }} <small>{{ frm.name_kr }}</small> ]({{ site.formulaurl }}/{{ frm.name_kr }})

> {{ frm.bangk }}

> {{ frm.bangksj }}

</div>

{% endfor %}
{% endfor %}
