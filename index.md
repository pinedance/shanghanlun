---
layout: default
title: Contents
---


# {{ page.title}}


## [강의 목록]({{site.baseurl}}/lecture/index)

{% assign sites_with_tag = site[ "lecture" ] | where: "tags", "강의" %}
{% for item in sites_with_tag %}
{% if item.desc %}
  [ {{ item.title }} _{{ item.desc }}_ ]( {{site.baseurl}}{{ item.url }} )
{% else %}
  [ {{ item.title }} ]( {{site.baseurl}}{{ item.url }} )
{%endif%}
{% endfor %}


## [자료 목록]({{site.baseurl}}/reference/index)

{% assign sites_with_tag = site[ "reference" ] | where: "tags", "index" %}
{% for item in sites_with_tag %}
{% if item.desc %}
  [ {{ item.title }} _{{ item.desc }}_ ]( {{site.baseurl}}{{ item.url }} )
{% else %}
  [ {{ item.title }} ]( {{site.baseurl}}{{ item.url }} )
{%endif%}
{% endfor %}
