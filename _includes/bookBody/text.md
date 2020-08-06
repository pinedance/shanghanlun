{% assign sites_with_tag = site.reference | where: "tags", "text" %}

{% assign raw_items = sites_with_tag | where: "tags", include.book %}

{% assign items = raw_items | where: "tags", include.position %}

{% for item in items %}

{% if item.desc %}

### [ {{ item.title }} _{{ item.desc }}_ ]( {{site.baseurl}}{{ item.url }} )

{% else %}

### [ {{ item.title }} ]( {{site.baseurl}}{{ item.url }} )

{% endif %}

<!-- {{ item.content }} -->

{% endfor %}
