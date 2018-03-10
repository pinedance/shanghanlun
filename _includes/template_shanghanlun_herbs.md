{% if page.imgs %}

{% for img in page.imgs %}

![ {{img.ref}} {{ page.title }} {{ img.name }} ]( {{site.baseurl}}/img/Herbs/{{img.ref}}/{{img.name}} )
*{{img.ref}}*  

{% endfor %}

{%endif%}

{% include imgmodal.html %}
