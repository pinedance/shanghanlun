<div class="compare-group" markdown="1">
{% assign booklist = "SSB SSR SSG SSE STB SCB SCE SOB SMK GGY" | split: " " }
{% for book in booklist %}
{{ book }}
{% include compare/compare.md noo=include.number from=include.from map=book %}
{% endfor %}
</div>
