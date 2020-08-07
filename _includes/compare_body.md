{{ page.desc }}

***

{% assign data_src = site.data.clause[ include.bookcode ] %}
{% for t in data_src %}
{% assign number = t.NOO | first %}

{% if number contains "-000" %}
{% else %}
<div id="{{number}}" class="compare-set">
{% endif %}

<div class="compare-source" markdown="1">
{% include clause.md noo=number %}
</div>

<div class="compare-targets" markdown="1">
{% include compare/compareGroup.md number=number from=include.bookcode %}
</div>

{% if number contains "-000" %}
{% else %}
</div>

{% endif %}

{% endfor %}
