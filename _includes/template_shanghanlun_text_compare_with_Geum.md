

<!--원문인용 시작. 상위에서 from, noo 지정 필요-->

{% assign itemms = site.data.shanghanlun_text_compare | where: from, noo %}

{% assign targets = itemms | map: 'Geum' %}

{% for ts in targets %}
{% for t in ts %}
{% if t %}

{% assign noo = t %}
{% include template_geumgweyolyag.md %}

{% endif %}
{% endfor %}
{% endfor %}

<!--원문인용 끝-->
