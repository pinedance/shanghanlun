## 약재 모습

### 현대 이미지

<!-- 현대이미지 -->
{% if page.imgsNew %}

{% for img in page.imgsNew %}
![{{ img.ref.title }}]({{ img.src }})
_출처： [{{ img.ref.title }}]({{ img.ref.address }})_

{% endfor %}

{% endif %}

<!-- 포털이미지 -->
{% if page.notations %}
포털이미지
* <a href="https://www.google.com/search?tbm=isch&q={{page.notations[0]}}" target="_blank">Google Image 보기</a>
* <a href="http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word={{page.notations[0]}}" target="_blank">Baidu Image 보기</a>

{% else %}
포털이미지
* <a href="https://www.google.com/search?tbm=isch&q={{page.title}}" target="_blank">Google Image 보기</a>
* <a href="http://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word={{page.title}}" target="_blank">Baidu Image 보기</a>
{% endif %}


{% if page.imgs %}
### 고의서 도상

{% include herb_img.html %}

{% endif %}
