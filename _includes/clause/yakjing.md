<!--hb 지정 필요-->

{% assign items = site.data.clause.yakjing | where: 'name_kr', hb %}
{% if items[0] and items[0].text !="" %}

> [{{ items[0].name }}]({{site.herburl}}/{{hb}}) {{ items[0].text }}

{% endif %}
