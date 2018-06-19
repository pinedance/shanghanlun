<!--원문인용 시작.  상위에서 data_src, noo, bookinit 지정 필요-->

<div id="{{bookinit}}{{noo}}" class="shanghanlun text others" markdown="1">

{% assign items = data_src | where: 'NOO', noo %}

{% if noo contains "-000" %}

### {{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}

{% else  %}

> <sup>《{{bookinit}}》{{noo}}</sup>	{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}

{% endif %}

{% assign anns = items | map: 'ANN' | where_exp: "item", "item"  %}

{% if anns.size > 0  %}

{% assign annd = anns | join: "；" | replace: "；", "  <sup>¶</sup>" %}

<p class="ann" markdown="1">
	<sup>¶</sup>{{ annd }}
</p>

{% endif %}

</div>

<!--원문인용 끝-->
