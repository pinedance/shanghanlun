{% if include.classname %}
{% assign clauses = site.data.clause[ include.book ] | where: "CTG", include.classname %}
{% else %}
{% assign clauses = site.data.clause[ include.book ] %}
{% endif %}

{% for c in clauses %}

{% assign n = c.NOO | first %}

{% if n == lastnoo %}
{% continue %}
{% endif %}

{% include clause.md noo=n %}
{% assign lastnoo = n %}
{% endfor %}
