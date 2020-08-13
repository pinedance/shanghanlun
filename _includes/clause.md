<!--원문인용 시작-->

{% assign bookcode = include.noo | split: "-" | first %}

{% case bookcode %}

<!-- 상한론 -->
{% when "SSB" %}
{% assign bookinit="全書" %}


<!-- 상한례 -->
{% when "SSE" %}
{% assign chp = include.noo | slice: 4, 2 %}

<!-- sub case -->
{% case chp %}

<!-- 변맥법 -->
{% when "01" %}
{% assign bookinit="全書|辨脈" %}

<!-- 평맥법 -->
{% when "02" %}
{% assign bookinit="全書|平脈" %}

<!-- 상한례 -->
{% when "03" %}
{% assign bookinit="全書|例" %}

<!-- 치습갈 -->
{% when "04" %}
{% assign bookinit="全書|痓濕暍" %}

{% else %}
{% assign bookinit="全書|外" %}
{% endcase %}
<!-- sub case end -->

<!-- 가불가 -->
{% when "SSG" %}
{% assign bookinit="全書|可不" %}

<!-- 법 -->
{% when "SSR" %}
{% assign bookinit="全書|法" %}

<!-- 순화본 -->
{% when "SCB" %}
{% assign bookinit="淳化" %}

<!-- 당본 -->
{% when "STB" %}
{% assign bookinit="千翼" %}

<!-- 금궤옥함경 -->
{% when "SOB" %}
{% assign bookinit="玉函" %}

<!-- 금궤요략 -->
{% when "GGY" %}
{% assign bookinit="金匱" %}

<!-- 맥경 -->
{% when "SMK" %}
{% assign bookinit="脈經" %}

<!-- 상한론 -->
{% else %}
{% assign bookinit="全書" %}
{% endcase %}

{% include clause/SHL.md bookinit=bookinit bookcode=bookcode linkfile=linkfile noo=include.noo kor=include.kor %}
<!--원문인용 끝-->
