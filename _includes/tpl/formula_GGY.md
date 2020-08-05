{% assign formulas = site.data.formula.GGY | where: "NameK", page.title %}

{% if formulas.size > 0 %}

{% assign gg_fm_names_kr = [] %}

## 금궤요략

{% for formula2 in formulas %}

### 명칭： __{{ formula2.Name }}__

한글명：{{ formula2.NameK | join: '；'}}

{% if formula2.NameS %}
이명：{{ formula2.NameS | join: '；'}}
{% endif %}

{% assign gg_fm_names_kr = gg_fm_names_kr | concat: formula2.NameK %}

### 처방 내용

처방 구성

> {{ formula2.Formula.Ingredients  | replace: "HERBURL", site.herburl | replace: "¶", "<sup>¶</sup>" | replace: "（", "<small>（"  | replace: "）", "）</small>" }}

제법

> {{ formula2.Formula.Directions }}

{% if formula2.Formula.Treat %}

처치

> {{ formula2.Formula.Treat }}

{% endif %}

{% if formula2.Indications %}

목표

> {{ formula2.Indications }}

{% endif %}


{% if formula2.Formula.Explanation %}

참고

> {{ formula2.Formula.Explanation }}

{% endif %}

{% if formula1.Formula.Ann %}

<p class="ann"><sup>¶</sup>{{ formula1.Formula.Ann | join: " <sup>¶</sup>"}} </p>

{% endif %}


### 금궤요략 조문

{% if formula2.NoA.size > 0 %}

{% for noo in formula2.NoA %}

{% include clause.md noo=noo %}

{% endfor %}

{% else %}

없음

{% endif %}

{% if formula2.NoA.size > 1 %}

***
{% endif %}

{% endfor %}


{% endif %}
