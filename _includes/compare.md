
<!--원문인용 시작. 상위에서 include.from, include.map, include.book 지정 필요-->
{% if (include.datatype) and (include.datatype == "auto") %}
{% assign itemms = site.data.compare.similartext_auto | where: include.from, include.noo %}
{% else %}
{% assign itemms = site.data.compare.similartext | where: include.from, include.noo %}
{% endif %}

{% assign targets = itemms | map: include.map %}

{% for ts in targets %}
{% for t in ts %}

{% if (include.from != include.map) or (include.noo != t) %}
{% include clause.md book=include.book noo=t %}
{% endif %}

{% endfor %}
{% endfor %}

<!--원문인용 끝-->
