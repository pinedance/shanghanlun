

<!--원문인용 시작.  상위에서 notype, noo 지정 필요-->
{% assign items = site.data.geumgweyolyag | where: 'NOO', noo %}

> {{noo}}	{{ items | map: 'TXT' | join: " " | replace: "URI", site.formulaurl }}



<!--원문인용 끝-->
