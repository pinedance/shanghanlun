---
layout: reference
title: "금궤요략 조문"
desc: "등진본 〔조문번호 '조문순서' 기준〕"
tags: [금궤요략, 원문]
src_path: template_geumgweyolyag.md
---


금궤요략
---------


<br>

{% for line in site.data.geumgweyolyag %}

{% if line.LVL == "AA" %}

## {{ line.NOO }} {{ line.TXT }}

{% else %}

> {{ line.NOO }}	{{ line.TXT | replace: "URI", site.formulaurl }}

{% endif %}

{% endfor %}
