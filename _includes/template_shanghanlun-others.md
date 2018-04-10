

<!--원문인용 시작.  상위에서 data_src, noo 지정 필요-->


{% assign items = data_src | where: 'NOO', noo %}

> {{noo}}	{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}

{% assign anns = items | map: 'ANN' | where_exp: "item", "item"  %}

{% if anns.size > 0  %}

{% assign annd = anns | join: "；" | replace: "；", "  <sup>¶</sup>" %}

<p class="ann" markdown="1">
	<sup>¶</sup>{{ annd }}
</p>

{% endif %}


<!--원문인용 끝-->
