{% assign formulas = site.data.shanghanlun_formulas | where: "NameK", page.title %}

{% if formulas.size > 0 %}

## 상한론

{% assign formula1 = formulas[0] %}

### 명칭

이름：__{{ formula1.Name }}__

한글명：{{ formula1.NameK | join: '；'}}

{% if formula1.NameS %}
이명：{{ formula1.NameS | join: '；'}}
{% endif %}

{% assign sh_fm_names_kr = formula1.NameK %}

### 처방 내용

처방 구성

> {{ formula1.Formula.Ingredients }}

제법

> {{ formula1.Formula.Directions }}

{% if formula1.Formula.Treat %}

처치

> {{ formula1.Formula.Treat }}

{% endif %}

{% if formula1.Formula.Explanation %}

참고

> {{ formula1.Formula.Explanation }}

{% endif %}

### 상한론 조문

{% for nn in formula1.NoA %}

{% assign noo = nn %}{% assign notype = "NOO.NoA" %}
{% include template_shanghanlun.md %}

{% endfor %}



{% endif %}
