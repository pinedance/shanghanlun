

<!--원문인용 시작.  상위에서 notype, noo 지정 필요-->


{% assign items = site.data.shanghanlun_text_compare | where: "Song", noo %}

{% assign tang = items | map: 'Tang' %}

{% for ts in tang %}
{% for t in ts %}
{% if t %}

{% assign data_src = site.data.shanghanlun-tang %}
{% assign noo = t %}
{% include template_shanghanlun-others.md %}

{% endif %}
{% endfor %}
{% endfor %}

{% assign chun = items | map: 'Chun' %}

{% for cs in chun %}
{% for c in cs %}
{% if c %}

{% assign data_src = site.data.shanghanlun-chunhe %}
{% assign noo = c %}
{% include template_shanghanlun-others.md %}

{% endif %}
{% endfor %}
{% endfor %}




<!--원문인용 끝-->
