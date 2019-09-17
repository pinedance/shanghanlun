

<!--원문인용 시작. 상위에서 include.from, include.map, include.book 지정 필요-->

{% assign itemms = site.data.compare.SHLtext | where: include.from, include.noo %}

{% assign targets = itemms | map: include.map %}

{% for ts in targets %}
{% for t in ts %}
{% if t %}

{% if include.from != include.map or include.noo != t %}

{% include clause.md book=include.book noo=t %}

{% endif %}

{% endif %}
{% endfor %}
{% endfor %}

<!--원문인용 끝-->
