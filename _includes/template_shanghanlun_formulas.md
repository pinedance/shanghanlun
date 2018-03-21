{% assign formulas = site.data.shanghanlun_formulas | where: "NameK", page.title %}

{% if formulas.size > 0 %}

## 상한론

{% assign formula = formulas[0] %}

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

{% if formula.Formula.Explanation %}

참고

> {{ formula.Formula.Explanation }}

{% endif %}

### 상한론 조문

{% for nn in formula.NoA %}

{% assign noo = nn %}{% assign notype = "NOO.NoA" %}
{% include template_shanghanlun.md %}

{% endfor %}



{% endif %}
