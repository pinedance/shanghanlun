

<!--원문인용 시작. 상위에서 from, noo 지정 필요-->

{% assign items = site.data.shanghanlun_text_compare | where: from, noo %}

{% assign targets = items | map: 'Song' %}

{% for ts in targets %}
{% for t in ts %}
{% if t %}

{% assign noo = t %}
{% assign bookinit = "全書" %}

{% include template_shanghanlun.md %}

{% endif %}
{% endfor %}
{% endfor %}




<!--원문인용 끝-->
