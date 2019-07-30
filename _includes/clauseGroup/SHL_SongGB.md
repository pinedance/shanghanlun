
<!--원문인용 시작.  상위에서 classname 지정 필요-->

{% assign noos = site.data.clause.SHL_SongGabu | where: "CTG", include.classname | map: 'NOO' %}

{% for noo in noos %}
{% include clause.md book="SHL_SongGabu" noo=noo %}
{% endfor %}
