<div class="compare-group">
{% assign booklist = "SSB SSR SSG SSE STB SCB SCE SOB SMK GGY" | split: " " %}
{% for book in booklist %}
{% include compare/compare.md noo=include.number from=include.from map=book %}
{% endfor %}
</div>
