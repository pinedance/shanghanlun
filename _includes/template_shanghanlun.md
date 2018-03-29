

<!--원문인용 시작.  상위에서 notype, noo 지정 필요-->
{% unless notype %}
	{% assign notype = "NOO.NoA" %}
{% endunless %}



{% assign items = site.data.shanghanlun | where:notype, noo %}

> {{noo}}	{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl }}

{% assign anns = items | map: 'ANN'  %}
{% assign ann_test = anns | join: "" | replace: "；", "" %}
{% if ann_test != ""  %}
{% assign annd = anns | join: "；" | replace: "；", "  <sup>¶</sup>" %}

<p class="ann"><sup>¶</sup>{{annd}}</p>

{% endif %}


<!--원문인용 끝-->
