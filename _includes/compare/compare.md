
<!--원문인용 시작. 상위에서 include.from, include.map 지정 필요-->
{% if (include.datatype) and (include.datatype == "auto") %}
{% assign itemms = site.data.compare.similartext_auto | where: include.from, include.noo %}
{% else %}
{% assign itemms = site.data.compare.similartext | where: include.from, include.noo %}
{% endif %}

{% assign targets = itemms | map: include.map %}

{% if targets.size > 0 %}

<div class="compare-book-{{ include.map }}" markdown="1">
{% for ts in targets %}
{% for t in ts %}

{% if (include.noo != t) %}
<div class="ORG-{{include.noo}}-vs-TRG-{{t}}" markdown="1">
{% include clause.md noo=t %}
</div>
{% endif %}

{% endfor %}
{% endfor %}
</div>

{% endif %}
<!--원문인용 끝-->
