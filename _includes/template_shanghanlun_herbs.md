{% if page.imgs %}

{% for img in page.imgs %}

![ {{ img.title }} ]( {{site.baseurl}}/img/Herbs/{{img.ref}}/{{img.name}} )
*{{img.ref}}*  

{% endfor %}

{%endif%}
