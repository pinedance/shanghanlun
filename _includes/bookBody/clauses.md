{% assign data_src = site.data.clause[ include.book ] %}

{% for t in data_src %}

{% include clause.md noo=t.NOO %}

{% endfor %}
