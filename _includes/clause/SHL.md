<!--송본 상한론 본문 조문 이외의 모든 것-->
<!--원문인용 시작.  상위에서 noo, bookinit 지정 필요-->

{% assign bookinit = include.bookinit %}
{% assign noo = include.noo %}

{% assign data = site.data.clause[ include.bookcode ] %}
{% assign items = data | where: 'NOO', noo %}

{% assign compared_path = site.baseurl | append: "/reference/Books/ShanghanlunCustom/Compare/" | append: include.linkfile | append: "#" | append: noo %}

{% if include.bookcode == "SSB" %}
<div id="{{noo}}" class="shanghanlun text song">
{% else %}
<div id="{{noo}}" class="shanghanlun text others">
{% endif %}

{% if noo contains "-00-" %}

<h2 markdown="1">{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}</h2>

{% elsif noo contains "-000" %}

<h3 markdown="1">{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}</h3>

{% else  %}

<p class="clause-head">
<a href="{{compared_path}}" target="{{site.data.theme.a.target}}">
<span class="book-label">《{{bookinit}}》</span>
<span class="clause-idx">{{noo}}</span>
</a>
</p>

<blockquote>
<p class="clause-body" markdown="1">{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "¶", "<sup>¶</sup>"}}</p>
</blockquote>

{% endif %}

{% assign anns = items | map: 'ANN' | where_exp: "item", "item"  %}

{% if anns.size > 0  %}

{% assign annd = anns | join: "；" | replace: "；", "  <sup>¶</sup>" %}

<p class="ann" markdown="1"><sup>¶</sup>{{ annd }}</p>

{% endif %}

{% if include.kor  %}

{% assign kor = items | map: 'KOR' | join: " "  %}

<p class="kor" markdown="1"><sup>§</sup>{{ kor | replace: "URI", site.formulaurl }}</p>

{% endif %}

</div>

<!--원문인용 끝-->
