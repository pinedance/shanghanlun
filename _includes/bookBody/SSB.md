{% assign prefix = "SSB-" %}

## 辨太陽病脈證幷治上第五 <small>合一十六法 方一十四首</small>

{% for idx in (1..30) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}


## 辨太陽病脈證幷治中第六 <small>合六十六法 方三十九首 幷見太陽陽明合病法</small>

{% for idx in (31..127) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}



## 辨太陽病脈證幷治下第七 <small>合三十九法 方三十首 幷見太陽少陽合病法</small>

{% for idx in (128..178) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}

## 辨陽明病脈證幷治第八 <small>合四十四法 方一十首一方附 幷見陽明少陽合病法</small>

{% for idx in (179..262) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}

## 辨少陽病脈證幷治第九 <small>方一首 幷見三陽合病法</small>

{% for idx in (263..272) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}

## 辨太陰病脈證幷治第十 <small>合三法 方三首</small>

{% for idx in (273..280) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}

## 辨少陰病脈證幷治第十一 <small>合二十三法 方一十九首</small>

{% for idx in (281..325) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}

## 辨厥陰病脈證幷治第十二 <small>厥利嘔噦附 合一十九法 方一十六首</small>

{% for idx in (326..381) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}


## 辨霍亂病脈證幷治第十三 <small>合六法 方六首</small>

{% for idx in (382..391) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}


## 辨陰陽易差後勞復病脈證幷治第十四 <small>合六法 方六首</small>

{% for idx in (392..398) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 | prepend: prefix %}
{% include clause.md noo=noo kor=include.kor %}
{% endfor %}
