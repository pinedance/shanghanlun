## 참고자료

{% assign frm = site.data.bangk | where: "name_kr", page.title %}

{% if frm.size > 0 %}

### [방극/방극산정]( {{site.baseurl}}/reference/Books/bangk#{{page.title}})

> {{ frm[0].bangk }}

> {{ frm[0].bangksj }}

{% endif %}

<!-- 내용 정리

## 정리

{% assign formulas = site.data.shanghanlun_formulas | where: "NameK", page.title %}
{% assign formula = formulas[0] %}

#### 효능

{{  formula.Features }}

#### 적응증

{{ formula.Indications }}


#### 설명

{{ formula.Commentary }}


## 외부자료

Ref : {{ formula.Page }}

-->
