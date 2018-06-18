---
layout: reference
title: "상한론"
desc: "송본 상한론〔조문번호 '상한론수책' 기준〕"
tags: [상한금궤원문, 송본]
conf:
  template: template_shanghanlun.md
  data_src: site.data.shanghanlun
  bookinit: "全書"
---

※ 조문번호 001 - 398 ("상한론수책" 기준)

[刻《仲景全書》序]({{site.baseurl}}/reference/Books/Sinipets/조개미_중경전서_서)

[《傷寒論》序]({{site.baseurl}}/reference/Books/Sinipets/임억_상한론_서)

[《傷寒卒病論》集]({{site.baseurl}}/reference/Books/Sinipets/상한잡병론_집론)

[醫林列傳]({{site.baseurl}}/reference/Books/Sinipets/상한잡병론_집론)

[國子監]({{site.baseurl}}/reference/Books/Sinipets/국자감_상서)


## 辨脉法第一

{% assign data_src = site.data.shanghanlun-etc %}
{% assign bookinit = "辨脉" %}

{% for idx in (1..38) %}

{% assign noo1 = idx | prepend: '00' | slice: -2, 2 %}
{% assign noo = "변맥" | append: '-' | append: noo1  %}
{% include template_shanghanlun-others.md %}

{% endfor %}


## 平脉法第二

{% assign data_src = site.data.shanghanlun-etc %}
{% assign bookinit = "平脉" %}

{% for idx in (1..49) %}

{% assign noo1 = idx | prepend: '00' | slice: -2, 2 %}
{% assign noo = "평맥" | append: '-' | append: noo1  %}
{% include template_shanghanlun-others.md %}

{% endfor %}

## 傷寒例第三

{% assign data_src = site.data.shanghanlun-etc %}
{% assign bookinit = "傷寒例" %}

{% for idx in (1..68) %}

{% assign noo1 = idx | prepend: '00' | slice: -2, 2 %}
{% assign noo = "상한례" | append: '-' | append: noo1  %}
{% include template_shanghanlun-others.md %}

{% endfor %}


## 辨痓濕暍脉證第四 <small>痙音◍又作痙去郢切下同</small>

{% assign data_src = site.data.shanghanlun-etc %}
{% assign bookinit = "痓濕暍" %}

{% for idx in (1..16) %}

{% assign noo1 = idx | prepend: '00' | slice: -2, 2 %}
{% assign noo = "치습갈" | append: '-' | append: noo1  %}
{% include template_shanghanlun-others.md %}

{% endfor %}


## 辨太陽病脉證幷治上第五 <small>合一十六法 方一十四首</small>

{% for idx in (1..30) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}


## 辨太陽病脉證幷治中第六 <small>合六十六法 方三十九首 幷見太陽陽明合病法</small>

{% for idx in (31..127) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}



## 辨太陽病脉證幷治下第七 <small>合三十九法 方三十首 幷見太陽少陽合病法</small>

{% for idx in (128..178) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}

## 辨陽明病脉證幷治第八 <small>合四十四法 方一十首一方附 幷見陽明少陽合病法</small>

{% for idx in (179..262) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}

## 辨少陽病脉證幷治第九 <small>方一首 幷見三陽合病法</small>

{% for idx in (263..272) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}

## 辨太陰病脉證幷治第十 <small>合三法 方三首</small>

{% for idx in (273..280) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}

## 辨少陰病脉證幷治第十一 <small>合二十三法 方一十九首</small>

{% for idx in (281..325) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}

## 辨厥陰病脉證幷治第十二 <small>厥利嘔噦附 合一十九法 方一十六首</small>

{% for idx in (326..381) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}


## 辨霍亂病脉證幷治第十三 <small>合六法 方六首</small>

{% for idx in (382..391) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}


## 辨陰陽易差後勞復病脉證幷治第十四 <small>合六法 方六首</small>

{% for idx in (392..398) %}
{% assign noo = idx | prepend: '000' | slice: -3, 3 %}
{% assign notype = "NOO.NoA" %}
{% include {{ page.conf.template }} %}
{% endfor %}


## 辨不可發汗病脉證幷治第十五 <small>一法 方本闕</small>

> 夫以爲疾病至急, 倉卒尋按, 要者難得, 故重集諸可與不可方治, 比之三陰三陽篇中, 此易見也. 又時有不止是三陽三陰, 出在諸可與不可中也.

{% assign noo = "285" %}{% include {{ page.conf.template }} %}

{% assign noo = "050" %}{% include {{ page.conf.template }} %}

{% assign noo = "286A" %}{% include {{ page.conf.template }} %}

> 脉濡而弱, 弱反在關, 濡反在巔, 微反在上, 濇反在下. 微則陽氣不足, 濇則無血, 陽氣反微, 中風汗出, 而反躁煩, 濇則無血, 厥而且寒. 陽微發汗, 躁不得眠.

動氣在右, 不可發汗. 發汗則衂而渴, 心苦煩, 飲即吐水.

動氣在左, 不可發汗. 發汗則頭眩, 汗不止, 筋惕肉瞤.

動氣在上, 不可發汗. 發汗則氣上衝, 正在心端.

動氣在下, 不可發汗. 發汗則無汗, 心中大煩, 骨節苦疼, 目運惡寒, 食則反吐, 穀不得前.

咽中閉塞, 不可發汗. 發汗則吐血, 氣微絕, 手足厥冷, 欲得踡臥, 不能自溫.

諸脉得數動微弱者, 不可發汗. 發汗則大便難, 腹中乾, <small>一云:小便難, 胞中乾.</small> 胃躁而煩, 其形相象, 根本異源.

脉濡而弱, 弱反在關, 濡反在巔, 弦反在上, 微反在下. 弦爲陽運, 微爲陰寒, 上實下虛, 意欲得溫. 微弦爲虛, 不可發汗, 發汗則寒慄, 不能自還.

欬者則劇, 數吐涎沫, 咽中必乾, 小便不利, 心中飢煩, 晬時而發, 其形似瘧, 有寒無熱, 虛而寒慄, 欬而發汗, 踡而苦滿, 腹中復堅. 厥, 脉緊, 不可發汗. 發汗則聲亂, 咽嘶舌萎, 聲不得前.

諸逆發汗, 病微者難差, 劇者言亂, 目眩者死, <small>一云: 讝言目眩, 睛亂者死,</small> 命將難全.

太陽病, 得之八九日, 如瘧狀, 發熱惡寒, 熱多寒少, 其人不嘔, 清便續自可, 一日二三度發, 脉微而惡寒者, 此陰陽俱虛, 不可更發汗也.

* {% assign noo = "023" %}{% include {{ page.conf.template }} %}

太陽病, 發熱惡寒, 熱多寒少, 脉微弱者, 無陽也, 不可發汗.

* {% assign noo = "027" %}{% include {{ page.conf.template }} %}

{% assign noo = "083" %}{% include {{ page.conf.template }} %}

{% assign noo = "087" %}{% include {{ page.conf.template }} %}

{% assign noo = "086" %}{% include {{ page.conf.template }} %}

{% assign noo = "088" %}{% include {{ page.conf.template }} %}

{% assign noo = "084" %}{% include {{ page.conf.template }} %}

{% assign noo = "085" %}{% include {{ page.conf.template }} %}

下利不可發汗, 汗出必脹滿.

* {% assign noo = "364" %}{% include {{ page.conf.template }} %}

欬而小便利, 若失小便者, 不可發汗, 汗出則四肢厥逆冷.

{% assign noo = "335" %}{% include {{ page.conf.template }} %}

傷寒脉弦細, 頭痛發熱者, 屬少陽, 少陽不可發汗.

* {% assign noo = "265" %}{% include {{ page.conf.template }} %}

傷寒頭痛, 翕翕發熱, 形象中風, 常微汗出, 自嘔者, 下之益煩, 心懊憹如飢. 發汗則致痓, 身強難以伸屈. 熏之則發黃, 不得小便, 久則發欬唾.

太陽與少陽倂病, 頭項強痛, 或眩冒, 時如結胸, 心下痞鞕者, 不可發汗.

* {% assign noo = "142" %}{% include {{ page.conf.template }} %}

太陽病發汗, 因致痓.

{% assign noo = "284" %}{% include {{ page.conf.template }} %}

{% assign noo = "294" %}{% include {{ page.conf.template }} %}


## 辨可發汗病脉證幷治第十六 <small>合四十一法 方一十四首</small>

大法, 春夏宜發汗.

凡發汗, 欲令手足俱周, 時出似漐漐然, 一時閒許, 益佳. 不可令如水流離. 若病不解, 當重發汗. 汗多者必亡陽, 陽虛不得重發汗也.

凡服湯發汗, 中病便止, 不必盡劑也.

凡云:可發汗, 無湯者, 丸散亦可用. 要以汗出爲解, 然不如湯, 隨證良驗.

{% assign noo = "042" %}{% include {{ page.conf.template }} %}

脉浮而數者, 可發汗, 屬桂枝湯證. <small>二 用前第一方, 一法:用麻黃湯.</small>

* {% assign noo = "052" %}{% include {{ page.conf.template }} %}

{% assign noo = "234" %}{% include {{ page.conf.template }} %}

夫病脉浮大, 問病者, 言但便鞕耳. 設利者, 爲大逆. 鞕爲實, 汗出而解. 何以故? 脉浮當以汗解.












## 辨發汗後病脉證幷治第十七 <small>合二十五法 方二十四首</small>






## 辨不可吐第十八 <small>合四證</small>

## 辨可吐第十九 <small>合二法 五證</small>

## 辨不可下病脉證幷治第二十 <small>合四法 方六首</small>

## 辨可下病脉證幷治第二十一 <small>合四十四法 方一十一首</small>

## 辨發汗吐下後病脉證幷治第二十二 <small>合四十八法 方三十九首</small>


***

[傷寒論後序]({{site.baseurl}}/reference/Books/Sinipets/상한론_후서)
