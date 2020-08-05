<!-- 약징 -->
<!-- herb 지정 필요-->

{% assign items = site.data.clause.EYJ | where: 'name_kr', include.herb %}
{% if items[0] and items[0].text !="" %}

> [{{ items[0].name }}]({{site.herburl}}/{{include.herb}}) {{ items[0].text }}

{% endif %}
