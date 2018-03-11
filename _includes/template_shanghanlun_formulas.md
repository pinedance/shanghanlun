{% assign formulas = site.data.shanghanlun_formulas | where: "NameK", page.title %}

{% assign formula = formulas[0] %}


## 명칭

이름：__{{ formula.Name] }}__

이명：{{ formula.NameS | join: '；'}}

한글명：{{ formula.NameK | join: '；'}}

## 처방 내용

처방 구성

> {{ formula.Formula.Ingredients }}

제법

> {{ formula.Formula.Directions }}

처치

> {{ formula.Formula.Treat }}

참고

> {{ formula.Formula.Explanation }}


## 사용

### 효능

{{  formula.Features }}

### 적응증

{{ formula.Indications }}


### 설명

{{ formula.Commentary }}


## 참고자료

### 관련조문

{% for nn in formula.NoA %}

{% assign noo = nn %}{% assign notype = "NOO.NoA" %}
{% include template_shanghanlun.md %}

{% endfor %}

### 관련설명

{% assign frm = site.data.bangk | where: "name_kr", page.title %}

[방극/방극산정]( {{site.baseurl}}/reference/Books/bangk#{{page.title}})

> {{ frm[0].bangk }}

> {{ frm[0].bangksj }}


### 외부자료

Ref : {{ formula.Page }}
