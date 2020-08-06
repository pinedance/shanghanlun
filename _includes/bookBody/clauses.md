{% if include.classname %}

{% assign clauses = site.data.clause[ include.book ] | where: "CTG", include.classname %}

{% else %}

{% assign clauses = site.data.clause[ include.book ] %}

{% endif %}

{% for c in clauses %}

{% assign n = c.NOO | first %}

{% include clause.md noo=n %}

{% endfor %}
