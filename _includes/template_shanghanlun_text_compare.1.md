

<!--원문인용 시작.  상위에서 noo 지정 필요-->


{% assign items1 = site.data.shanghanlun_text_compare | where: "Song", noo %}

{% assign tang = items1 | map: 'Tang' %}


{% for ts in tang %}
{% for t in ts %}
{% if t %}

{% assign noo = t %}
{% assign bookinit = "唐翼" %}
{% assign data_src = site.data.shanghanlun-tang %}
{% include template_shanghanlun-others.md %}

{% endif %}
{% endfor %}
{% endfor %}





{% assign items2 = site.data.shanghanlun_text_compare | where: "Song", noo %}

{% assign chun = items2 | map: 'Chun' %}

{% for cs in chun %}
{% for c in cs %}
{% if c %}

{% assign noo = c %}
{% assign bookinit = "淳和" %}
{% assign data_src = site.data.shanghanlun-chunhe %}
{% include template_shanghanlun-others.md %}

{% endif %}
{% endfor %}
{% endfor %}




<!--원문인용 끝-->
