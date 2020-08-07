import os, sys
from time import time
from collections import Counter

from ruamel.yaml import YAML
import regex as re
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

from mylib import chdir2cwd, extract_han, n_gram, flatten, uniq, pair2group
# from fuzzywuzzy import fuzz

"""
SequenceMatcher의 결과값(r)은
* 구절의 앞뒤가 바뀐 조문의 경우 r이 낮게 나타난다.
* 한 조문이 다른 조문을 포함하는 관계일 때도 r이 낮게 나타난다.
"""

"""
이를 보완하기 위해 text reuse를 이용하여 조문 사이에 유사도를 계산한다.
조문source와 조문target이 있을 때, 각각을 bi-gram으로 나누어 공통된 bi-gram 개수를 조문source의 bi-gram 개수로 나눈다.
이렇게 하면 포함관계를 찾아낼 수 있지만, 값이 대칭적이지 않기 때문에 조문source와 조문target이 바뀌면 결과도 달라진다.

계산된 유사도값(r)이 cutoff 이하의 조합은 버린다.
r이 가장 높은 조합을 찾아 연관된 조합으로 만든다.
연관된 조합들 사이에 공통된 조문이 있으면 이를 합쳐나간다.
더이상 합칠 것이 없게 된 조문 조합들이 결과이다.
"""

"""
이렇게 하면 문제가 생긴다. A,B,C,D,E 조합이 원하는 결과이지만
A -> B, B -> A 가 되면 [A,B], [C,D,E]가 된다.
전처럼 cutoff 이상을 모두 가져가야 하나?
"""

######################################

FILENAMES = "SSB SSR SSG SSE STB SCB SCE SOB GGY SMK".split()

basepath = os.path.join( "..", "..", "_data", "clause" )

cjk_range = "[\p{Han}]"
CJK = re.compile( cjk_range, re.UNICODE)

cutoff = 0.6
report_file = "report2.yml"
result_file = "similartext_auto2.yml"
######################################

def match_ratio( text_src, text_trg, idf, n=2 ):
    # 결과가 비대칭이다.
    text1, text2 = text_src, text_trg
    t1g, t2g = n_gram( text1, n), n_gram( text2, n)
    t1size, t2size = len( t1g ), len( t2g )
    set_t1g, set_t2g = set( t1g ), set( t2g )
    intersection = list( set_t1g & set_t2g )
    # 분모 ( gram의 idf 가중치 합계 )
    denominator = sum( [ idf.get(g, 0) for g in t1g ] )
    # 분자 ( 교집합 gram의 idf 가중치 합계 )
    numerator = sum( [ text_src.count( g ) * idf.get(g, 0) for g in intersection ] )
    return numerator / denominator

def add_code( lst ):
    uniq_list = uniq( lst )
    rst = {}
    for f in FILENAMES: rst[f] = []
    for e in uniq_list:
        book = e.split("-")[0]
        rst[book].append( e )
    return rst

def tr(s):
    return re.sub(r'^-', '\n-', s, flags=re.M )

######################################

def main():

    chdir2cwd( __file__ )
    _data, data = [], []
    data_textonly = []
    sim, sim_group = [], []
    ym = YAML( typ='safe' )
    ym.default_flow_style = None

    print( "# Build Data "); t = time()
    for filename in FILENAMES:
        filepath = os.path.join( basepath, filename + '.yml' )
        with open( filepath, 'r', encoding="utf-8" ) as fl:
            tmp = ym.load( fl )

        for d in tmp:
            n = d.get("NOO", "")
            if type(n) is not str: n = n[0]
            if ( "-00-" in n ) or ( "-000" in n ): continue
            hanzi_only = extract_han( d.get("TXT") )
            _data.append(  ( n, hanzi_only, d.get("TXT")  ) )
            data_textonly.append( hanzi_only )

    # 분할된 조문 합치기
    # noos = uniq( list( list( zip( *_data ) )[0] ) )
    # for n in noos:
    #     tmp_hanzi_only = ""
    #     tmp_TXT = ""
    #     for d in _data:
    #         if n != d[0]: continue
    #         tmp_hanzi_only += d[1]
    #         tmp_TXT += d[2]
    #     data.append( (n, tmp_hanzi_only, tmp_TXT) )
    #     data_textonly.append( hanzi_only )

    data = _data
    # print(data, len(data))
    print( "...", time()-t )

    print( "# Build Meta-Data (idf) "); t = time()
    data_size = len( data_textonly )
    data_gram, data_corpus = [], []
    for text in data_textonly:
        tmp_gram = n_gram( text, 2 )
        data_gram.append( tmp_gram )
        data_corpus.append( " ".join(tmp_gram) )

    vectorizer = TfidfVectorizer( )
    data_vector = vectorizer.fit_transform( data_corpus )
    uniq_grams = list( vectorizer.vocabulary_ )
    idf = {}
    for g in uniq_grams:
        i = vectorizer.vocabulary_[g]
        idf[g] = vectorizer.idf_[i]

    # print( idf )
    print( "...", time()-t )


    print( "# Check Similarity "); t = time()
    # For test ###########
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        data = data[:800]
    ######################
    for i, item1 in enumerate( tqdm( data ) ):
        tmp_sim, tmp_r = [], []
        for j in range( len(data) ):
            if i == j : continue
            item2 = data[j]
            text_src, text_trg = item1[1], item2[1]
            try:
                r = match_ratio( text_src, text_trg, idf )
            except Exception as ex:
                print( text_src, text_trg, ex, "\n\n" )
                r = 0
            if r < cutoff: continue
            sim.append( (i, j, r) )
        #     tmp_r.append( r )
        #     tmp_sim.append( (i, j, r) )
        #
        # if len( tmp_r ) == 0 : continue
        # max_r = max( tmp_r )
        # for i,j,r in tmp_sim:
        #     if r == max_r: sim.append( (i, j, r) )

    data_report = [ { "src": [ data[ s[0] ][0], data[ s[0] ][2] ] , "trg": [ data[ s[1] ][0], data[ s[1] ][2] ] , "score": format(s[2], "0.3f") } for s in sim ]
    with open( report_file, 'w', encoding="utf-8") as fl:
        ym.dump( data_report, fl )

    print( "...", time()-t )

    print( "# Build Report"); t = time()

    sim_group = pair2group( [ [ s[0], s[1] ] for s in sim ] )
    sim_report_group = [ add_code( [ data[x][0] for x in sim ] ) for sim in sim_group ]
    ########
    # with open( "tmp_log", 'w', encoding="utf-8") as fl:
    #     ym.dump( [ [[ data[x][0] for x in sim ], sim] for sim in sim_group ], fl )
    ########
    with open( result_file, 'w', encoding="utf-8") as fl:
        # ym.dump( sim_report_group, fl, transform=tr )
        ym.dump( sim_report_group, fl )

    print( "...", time()-t )


if __name__ == '__main__':
    main()
