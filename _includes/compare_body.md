{{ page.desc }}

***

{% assign clauses = site.data.clause[ include.bookcode ] %}

{% for c in clauses %}

{% assign n = c.NOO | first %}

{% if n == lastnoo %}
{% continue %}
{% endif %}

{% if n contains "-00-" or n contains "-000" %}
<!-- if Title -->
{% include clause.md noo=n %}
{% else %}
<!-- if Clause -->
<div id="SRC-{{n}}" class="compare-set">
<div class="compare-source">
{% include clause.md noo=n %}
</div>
<div class="compare-targets">
{% include compare/compareGroup.md number=n from=include.bookcode %}
</div>
</div>
{% endif %}

{% assign lastnoo = n %}

{% endfor %}
