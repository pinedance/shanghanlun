<!--hb 지정 필요-->

{% assign items = site.data.yakjing_in | where: 'name_kr', hb %}
{% if items[0] and items[0].text !="" %}

> [{{hb}}]({{site.herburl}}/{{hb}}) {{ items[0].text }}

{% endif %}
