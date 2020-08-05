<!--원문인용 시작-->

{% assign book = include.noo | split: "-" | first %}

{% case book %}

<!-- 상한론 -->
{% when "SSB" %}
{% include clause/SSB.md notype=include.notype noo=include.noo kor=include.kor %}

<!-- 상한례 -->
{% when "SSE" %}
{% assign chp = include.noo | slice: 4, 6 %}

<!-- sub case -->
{% case chp %}

<!-- 변맥법 -->
{% when "01" %}
{% include clause/SHL.md data_src=site.data.clause.SSE bookinit="全書〔辨脈〕" noo=include.noo %}

<!-- 평맥법 -->
{% when "02" %}
{% include clause/SHL.md data_src=site.data.clause.SSE bookinit="全書〔平脈〕" noo=include.noo %}

<!-- 상한례 -->
{% when "03" %}
{% include clause/SHL.md data_src=site.data.clause.SSE bookinit="全書〔例〕" noo=include.noo %}

<!-- 치습갈 -->
{% when "04" %}
{% include clause/SHL.md data_src=site.data.clause.SSE bookinit="全書〔痓濕暍〕" noo=include.noo %}

{% else %}
{% include clause/SHL.md data_src=site.data.clause.SSE bookinit="全書〔外〕" noo=include.noo %}
{% endcase %}
<!-- sub case end -->

<!-- 가불가 -->
{% when "SSG" %}
{% include clause/SHL.md data_src=site.data.clause.SSG bookinit="全書〔可不〕" noo=include.noo %}

<!-- 법 -->
{% when "SSR" %}
{% include clause/SHL.md data_src=site.data.clause.SSR bookinit="全書〔法〕" noo=include.noo %}

<!-- 순화본 -->
{% when "SCB" %}
{% include clause/SHL.md data_src=site.data.clause.SCB bookinit="淳和" noo=include.noo %}

<!-- 순화본 기타 -->
{% when "SCE" %}
{% include clause/SHL.md data_src=site.data.clause.SCE bookinit="淳和" noo=include.noo %}

<!-- 당본 -->
{% when "STB" %}
{% include clause/SHL.md data_src=site.data.clause.STB bookinit="千翼" noo=include.noo %}

<!-- 금궤옥함경 -->
{% when "SOB" %}
{% include clause/SHL.md data_src=site.data.clause.SOB bookinit="玉函" noo=include.noo %}


<!-- 금궤요략 -->
{% when "GGY" %}
{% include clause/SHL.md data_src=site.data.clause.GGY bookinit="金匱" noo=include.noo %}

<!-- 맥경 -->
{% when "SMK" %}
{% include clause/SHL.md data_src=site.data.clause.SMK bookinit="脈經" noo=include.noo %}

<!-- 상한론 -->
{% else %}
{% include clause/SSB.md notype=include.notype noo=include.noo kor=include.kor %}

{% endcase %}

<!--원문인용 끝-->
