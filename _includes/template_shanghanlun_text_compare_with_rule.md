

<!--원문인용 시작. 상위에서 from, noo 지정 필요-->

{% assign itemms = site.data.shanghanlun_text_compare | where: from, noo %}

{% assign targets = itemms | map: 'SongRule' %}

{% for ts in targets %}
{% for t in ts %}
{% if t %}

{% assign noo = t %}
{% assign bookinit = "全書/法" %}
{% assign data_src = site.data.shanghanlun-rule %}
{% include template_shanghanlun-others.md %}

{% endif %}
{% endfor %}
{% endfor %}

<!--원문인용 끝-->
