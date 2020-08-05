{% assign formulas = site.data.formula.SSB | where: "NameK", page.title %}

{% if formulas.size > 0 %}

## 상한론

{% assign formula1 = formulas[0] %}

### 명칭： __{{ formula1.Name }}__

한글명：{{ formula1.NameK | join: '；'}}

{% if formula1.NameS %}
이명：{{ formula1.NameS | join: '；'}}
{% endif %}

{% assign sh_fm_names_kr = formula1.NameK %}

### 처방 내용

처방 구성

> {{ formula1.Formula.Ingredients | replace: "HERBURL", site.herburl | replace: "¶", "<sup>¶</sup>" | replace: "（", "<small>（"  | replace: "）", "）</small>" }}

<br>

제법

> {{ formula1.Formula.Directions | replace: "¶", "<sup>¶</sup>" }}

{% if formula1.Formula.Treat  %}

<br>

처치

> {{ formula1.Formula.Treat | replace: "¶", "<sup>¶</sup>" }}

{% endif %}

{% if formula1.Formula.Explanation %}

<br>

참고

> {{ formula1.Formula.Explanation | replace: "¶", "<sup>¶</sup>" }}

{% endif %}


{% if formula1.Formula.Ann %}

<p class="ann"><sup>¶</sup>{{ formula1.Formula.Ann | join: " <sup>¶</sup>"}} </p>

{% endif %}



### 상한금궤 조문

{% for noo in formula1.NoA %}

{% include clause.md noo=noo %}

{% endfor %}



{% endif %}
