<!--송본 상한론 가불가 조문 -->
<!--원문인용 시작.  상위에서 classname 지정 필요-->

{% assign noos = site.data.clause.SSG | where: "CTG", include.classname | map: 'NOO' %}

{% for noo in noos %}
{% include clause.md noo=noo %}
{% endfor %}
