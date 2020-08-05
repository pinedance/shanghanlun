## 참고자료

{% if sh_fm_names_kr.size > 0 %}

	{% if gg_fm_names_kr.size > 0 %}
		{% assign kr_names = sh_fm_names_kr | concat: gg_fm_names_kr | uniq %}
	{% else %}
		{% assign kr_names = sh_fm_names_kr | uniq %}
	{% endif %}

{% else %}

	{% if gg_fm_names_kr.size > 0 %}
		{% assign kr_names = gg_fm_names_kr | uniq %}
	{% else %}
		{% assign kr_names = [ page.title ] %}
	{% endif %}

{% endif %}

<!-- 처방 명칭 -->

{% if kr_names.size > 0 %}
{% for name1_kr in kr_names %}

{% assign frm = site.data.clause.EBK | where: "name_kr", name1_kr %}
{% if frm.size > 0 %}
### [{{ name1_kr }} <small>방극/방극산정</small>]( {{site.baseurl}}/reference/Books/Etc/bangk#{{ name1_kr }})

> {{ frm[0].bangk }}

> {{ frm[0].bangksj }}

{% endif %}

{% endfor %}
{% endif %}



<!-- 내용 정리

## 정리

{% assign formulas = site.data.formula.SSB | where: "NameK", page.title %}
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
