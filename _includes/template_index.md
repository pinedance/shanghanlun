{% assign sites_with_tag = site.handout | where: "tags", page.index_subject %} 
{% for item in sites_with_tag %}

{% if item.desc %}

  [ {{ item.title }} _{{ item.desc }}_ ]( {{site.baseurl}}{{ item.url }} )
  
{% else %}

  [ {{ item.title }} ]( {{site.baseurl}}{{ item.url }} )
  
{%endif%}
  
{% endfor %}
