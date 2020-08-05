<!--원문인용 시작-->

{% assign noo = include.noo %}
{% assign book = include.noo | split: "-" | first %}

{% case include.book %}

<!-- 상한론 -->
{% when "SHL" %}
{% include clause.SSB_Song.md notype=include.notype noo=include.noo kor=include.kor %}

<!-- 상한론 -->
{% when "SHL_Song" %}
{% include clause.SSB_Song.md notype=include.notype noo=include.noo kor=include.kor %}


<!-- 상한례 -->
{% when "SHL_SongEtc" %}
{% assign chp = include.noo | slice: 0, 2 %}

<!-- sub case -->
{% case chp %}

<!-- 변맥법 -->
{% when "01" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSE_SongEtc bookinit="全書〔辨脈〕" noo=include.noo %}

<!-- 평맥법 -->
{% when "02" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSE_SongEtc bookinit="全書〔平脈〕" noo=include.noo %}

<!-- 상한례 -->
{% when "03" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSE_SongEtc bookinit="全書〔例〕" noo=include.noo %}

<!-- 치습갈 -->
{% when "04" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSE_SongEtc bookinit="全書〔痓濕暍〕" noo=include.noo %}

{% else %}
{% include clause/SHL_other.md data_src=site.data.clause.SSE_SongEtc bookinit="全書〔外〕" noo=include.noo %}
{% endcase %}
<!-- sub case end -->

<!-- 가불가 -->
{% when "SHL_SongGabu" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSG_SongGabu bookinit="全書〔可不〕" noo=include.noo %}

<!-- 법 -->
{% when "SHL_SongRule" %}
{% include clause/SHL_other.md data_src=site.data.clause.SSR_SongRule bookinit="全書〔法〕" noo=include.noo %}

<!-- 순화본 -->
{% when "SHL_Chunhe" %}
{% include clause/SHL_other.md data_src=site.data.clause.SCB_Chunhe bookinit="淳和" noo=include.noo %}

<!-- 순화본 기타 -->
{% when "SHL_ChunheEtc" %}
{% include clause/SHL_other.md data_src=site.data.clause.SCE_ChunheEtc bookinit="淳和" noo=include.noo %}

<!-- 당본 -->
{% when "SHL_Tang" %}
{% include clause/SHL_other.md data_src=site.data.clause.SHL_Tang bookinit="千翼" noo=include.noo %}

<!-- 금궤옥함경 -->
{% when "SHL_Ogham" %}
{% include clause/SHL_other.md data_src=site.data.clause.SOB_Ogham bookinit="玉函" noo=include.noo %}


<!-- 금궤요략 -->
{% when "GY" %}
{% include clause/SHL_other.md data_src=site.data.clause.GGY_GGYL bookinit="金匱" noo=include.noo %}

<!-- 맥경 -->
{% when "MK" %}
{% include clause/SHL_other.md data_src=site.data.clause.SMK_MK bookinit="脈經" noo=include.noo %}

<!-- 상한론 -->
{% else %}
{% include clause.SSB_Song.md notype=include.notype noo=include.noo kor=include.kor %}

{% endcase %}

<!--원문인용 끝-->
