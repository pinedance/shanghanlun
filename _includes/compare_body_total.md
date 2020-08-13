{{ page.desc }}
--------------------

{% assign files = "SSB SSR SSG SSE STB SCB SOB GGY SMK" | split: " " %}
{% assign books = "SSB SSR SSG SSE STB SCB SOB GGY SMK" | split: " " %}
{% assign book_cnt = books | size | minus: 1 %}

{% assign data_compared = site.data.compare[ include.data_src ] %}
{% for pair in data_compared %}

<div class="compare-set" markdown="1">
{% for i in ( 0..book_cnt ) %}

{% assign file = files[i] %}
{% assign book = books[i] %}
{% assign noos = pair[book] %}

{% if noos and noos.size != 0 %}

{% for noo in noos %}
{% include clause.md noo=noo %}
{% endfor %}

{% endif %}
{% endfor %}
</div>

{% endfor %}
