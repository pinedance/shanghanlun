<!--원문인용 시작-->

{% assign noo = include.noo %}

{% case include.book %}


<!-- 상한론 -->
{% when "SHL" %}

{% include clause/SHL_Song.md notype=include.notype noo=include.noo kor=include.kor %}

<!-- 상한론 -->
{% when "SHL-Song" %}

{% include clause/SHL_Song.md notype=include.notype noo=include.noo kor=include.kor %}

<!-- 변맥법 -->
{% when "SHL_SongBM" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongEtc bookinit="全書/辨脈" noo=include.noo %}

<!-- 평맥법 -->
{% when "SHL_SongPM" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongEtc bookinit="全書/平脈" noo=include.noo %}

<!-- 상한례 -->
{% when "SHL_SongL" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongEtc bookinit="全書/例" noo=include.noo %}

<!-- 치습갈 -->
{% when "SHL_SongCSG" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongEtc bookinit="全書/痓濕暍" noo=include.noo %}

<!-- 가불가 -->
{% when "SHL_SongGabu" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongGabu bookinit="全書/可不" noo=include.noo %}

<!-- 법 -->
{% when "SHL_SongRule" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_SongRule bookinit="全書/法" noo=include.noo %}

<!-- 순화본 -->
{% when "SHL_Chunhe" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_Chunhe bookinit="淳和" noo=include.noo %}

<!-- 당본 -->
{% when "SHL_Tang" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_Tang bookinit="唐翼" noo=include.noo %}

<!-- 금궤옥함경 -->
{% when "SHL_Ogham" %}

{% include clause/SHL_other.md data_src=site.data.clause.SHL_Ogham bookinit="玉函" noo=include.noo %}


<!-- 금궤요략 -->
{% when "GGYL" %}

{% include clause/SHL_other.md data_src=site.data.clause.GGYL bookinit="金匱" noo=include.noo %}

<!-- 맥경 -->
{% when "MK" %}

{% include clause/SHL_other.md data_src=site.data.clause.MK bookinit="脈經" noo=include.noo %}

<!-- 상한론 -->
{% else %}

{% include clause/SHL_Song.md notype=include.notype noo=include.noo kor=include.kor %}

{% endcase %}

<!--원문인용 끝-->
