<!--송본 상한론 본문 조문 이외의 모든 것-->
<!--원문인용 시작.  상위에서 noo, bookinit 지정 필요-->

{% assign bookinit = include.bookinit %}
{% assign noo = include.noo %}

{% assign data = site.data.clause[ include.bookcode ] %}
{% assign items = data | where: 'NOO', noo %}

{% assign compared_path = site.baseurl | append: "/reference/Books/ShanghanlunCustom/Compare/" | append: include.bookcode | append: "#" | append: "SRC-" | append: noo %}

{% assign origin_path = site.baseurl | append: "/reference/Books/Shanghanlun/Clause/" | append: include.bookcode | append: "#" | append: noo %}

{% assign clause_body = items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl | replace: "｛", '<span class="subtext t1">'  | replace: "｝", '</span>'  | replace: "〈", '<span class="subtext t2">'  | replace: "〉", '</span>' | replace: "（", '<span class="subtext t0">'  | replace: "）", '</span>' | replace: "¶", '<sup class="sym-ann"></sup>' | replace: "，", '<span class="sym-comma"></span>' | replace: "。", '<span class="sym-period"></span>' | replace: "「", '<span class="sym-open"></span>' | replace: "」", '<span class="sym-close"></span>' %}

{% if include.bookcode == "SSB" %}
<div id="{{noo}}" class="shanghanlun text song">
{% else %}
<div id="{{noo}}" class="shanghanlun text others">
{% endif %}

{% if noo contains "-00-" %}

<h2 id="h2-{{noo}}" markdown="1">{{ clause_body }}</h2>

{% elsif noo contains "-000" %}

<h3 id="h3-{{noo}}" markdown="1">{{ clause_body }}</h3>

{% else  %}

<p class="clause-head">
<a href="{{origin_path}}" target="{{site.data.theme.a.target}}">
<span class="book-label">《{{bookinit}}》</span>
<span class="clause-idx">{{noo}}</span>
</a>
<a href="{{compared_path}}" target="{{site.data.theme.a.target}}">
<span class="compare-link">☞diff</span>
</a>
</p>

<blockquote>
<p class="clause-body" markdown="1">{{ clause_body }}</p>
</blockquote>

{% endif %}

{% assign anns = items | map: 'ANN' | where_exp: "item", "item"  %}

{% if anns.size > 0  %}

<p class="ann">
{% for ann in anns %}
{% if ann.size > 0 %}
{% for a in ann %}
<span markdown="1"><sup>¶</sup>{{ a }}</span>
{% endfor %}
{% endif %}
{% endfor %}
</p>

{% endif %}

{% if include.kor  %}

{% assign kor_body = items | map: 'KOR' | join: " " | replace: "URI", site.formulaurl | replace: "｛", '<span class="subtext t1">'  | replace: "｝", "</span>"  | replace: "〈", '<span class="subtext t2">'  | replace: "〉", "</span>" | replace: "（", '<span class="subtext t0">'  | replace: "）", "</span>" | replace: "¶", '<sup class="sym-ann"></sup>' | replace: "，", '<span class="sym-comma"></span>' | replace: "。", '<span class="sym-period"></span>' | replace: "「", '<span class="sym-open"></span>' | replace: "」", '<span class="sym-close"></span>' %}

<p class="kor" markdown="1"><sup>§</sup>{{ kor_body }}</p>

{% endif %}

</div>

<!--원문인용 끝-->
