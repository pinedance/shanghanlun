{% assign formulas = site.data.geumgweyolyag_formulas | where: "NameK", page.title %}

{% if formulas.size > 0 %}

## 금궤요략

{% for formula in formulas %}

### 명칭

이름：__{{ formula.Name] }}__

한글명：{{ formula.NameK | join: '；'}}

{% if formula.NameS %}
이명：{{ formula.NameS | join: '；'}}
{% endif %}

### 처방 내용

처방 구성

> {{ formula.Formula.Ingredients }}

제법

> {{ formula.Formula.Directions }}

{% if formula.Formula.Treat %}

처치

> {{ formula.Formula.Treat }}

{% endif %}

{% if formula.Formula.Indications %}

목표

> {{ formula.Formula.Indications }}

{% endif %}


{% if formula.Formula.Explanation %}

참고

> {{ formula.Formula.Explanation }}

{% endif %}

### 금궤요략 조문

{% for noo in formula.NoA %}

{% include template_geumgweyolyag.md %}

{% endfor %}

***

{% endfor %}


{% endif %}
