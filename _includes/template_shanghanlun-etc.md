
<!--원문인용 시작.  상위에서 bookinit, data_src, classname 지정 필요-->

{% assign noos = data_src | where: "CTG", classname | map: 'NOO' %}
{% for noo in noos %}
{% include template_shanghanlun-others.md %}
{% endfor %}
