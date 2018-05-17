### 관련 본초

{% for herb in page.anchor.herbs %}
* [{{ herb }}]({{ site.herburl}}/{{ herb }})
{% endfor %}


### 관련 처방

{% for formula in page.anchor.formulas %}
* [{{ formula }}]({{ site.formulaurl}}/{{ formula }})
{% endfor %}
