<div id="Song{{noo}}" class="shanghanlun text song" markdown="1">

<!--원문인용 시작.  상위에서 notype, noo, kor 지정 필요-->
{% assign notype = include.notype %}
{% assign noo = include.noo %}
{% assign kor = include.kor %}

{% unless notype %}
	{% assign notype = "NOO.NoA" %}
{% endunless %}

{% assign compared_path = site.baseurl | append: "/reference/Books/Shanghanlun/Compare/Song-Compared#" | append: noo %}

{% assign items = site.data.clause.SHL_Song | where:notype, noo %}

> <sup><a href="{{compared_path}}" target="{{site.data.theme.a.target}}">《全書》{{noo}}</a></sup>	{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}

{% assign anns = items | map: 'ANN' | where_exp: "item", "item"  %}

{% if anns.size > 0  %}

{% assign annd = anns | join: "；" | replace: "；", "  <sup>¶</sup>" %}

<p class="ann" markdown="1">
	<sup>¶</sup>{{ annd }}
</p>

{% endif %}

{% if kor  %}

{% assign kor = items | map: 'KOR' | join: " "  %}

<p class="kor" markdown="1">
	<sup>§</sup>{{ kor | replace: "URI", site.formulaurl }}
</p>

{% endif %}

</div>
<!--원문인용 끝-->
