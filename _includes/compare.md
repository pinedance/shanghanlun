

<!--원문인용 시작. 상위에서 from, noo 지정 필요-->

{% assign itemms = site.data.compare.SHLtext | where: include.from, include.noo %}

{% assign targets = itemms | map: include.map %}

{% for ts in targets %}
{% for t in ts %}

{% if (include.from == include map) and (t! = include.noo) %}

{% include clause.md book=include.book noo=t %}

{% else %}

{% if t %}
{% include clause.md book=include.book noo=t %}
{% endif %}

{$ endif $}

{% endfor %}
{% endfor %}

<!--원문인용 끝-->
