import os, sys
from time import time
from collections import Counter
import math

from ruamel.yaml import YAML
import regex as re
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

from mylib import chdir2cwd, extract_han, preprocess, n_gram, flatten, uniq, pair2group
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

FILENAMES = "SSB SSR SSG SSE STB SCB SOB GGY SMK".split()
BASEPATH = os.path.join( "..", "..", "_data", "clause" )
MAX_PARARING_TOPN = 3    # or None

USE_IDF = False
N_GRAM = 3
MIN_DF = 5
DEFAULT_R = 0.1
CUTOFF = 0.2
USE_WEIGHT_FN = False

report_file = "report2.yml"
result_file = "similartext_auto2.yml"

######################################

def g_fn0( r, size ):
    if size < 2: return DEFAULT_R
    return r

# BAD result
def g_fn1( r, size ):
    if size < 2: return DEFAULT_R
    return r ** ( 1 / (size-1) )

# BAD result
def g_fn2( r, size ):
    if size < 2: return DEFAULT_R
    return r ** ( 1 / math.sqrt(size-1) )

# BAD result
def g_fn3( r, size ):
    if size < 2: return DEFAULT_R
    return r ** ( 1 / math.log( size ) )

######################################
WEIGHT_FN = g_fn0
######################################

def match_ratio( ngram_src, ngram_trg, idf={}, weight_fn=None ):
    # 결과가 비대칭이다.
    default_val = 1
    set_t1g, set_t2g = set( ngram_src ), set( ngram_trg )
    intersection = list( set_t1g & set_t2g )
    # 분모 ( gram의 idf 가중치 합계 )
    denominator = sum( [ idf.get(g, default_val) for g in ngram_src ] )
    # 분자 ( 교집합 gram의 idf 가중치 합계 )
    numerator = sum( [ min( ngram_src.count( g ), ngram_trg.count(g) ) * idf.get(g, default_val) for g in intersection ] )
    r = numerator / denominator
    if weight_fn:
        return weight_fn( r, len(ngram_src) )
    else:
        return r

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
        filepath = os.path.join( BASEPATH, filename + '.yml' )
        with open( filepath, 'r', encoding="utf-8" ) as fl:
            tmp = ym.load( fl )

        for d in tmp:
            n = d.get("NOO", "")
            if type(n) is not str: n = n[0]
            if ( "-00-" in n ) or ( "-000" in n ): continue
            txt = d.get("TXT").strip()
            hanzi_only = extract_han( preprocess( txt ) )
            hanzi_only_gram = n_gram( hanzi_only, N_GRAM )
            _data.append(  ( n, hanzi_only, txt, hanzi_only_gram ) )
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
    # data_size = len( data_textonly )
    # data_gram, data_corpus = [], []
    # for text in data_textonly:
    #     tmp_gram = n_gram( text, 2 )
    #     data_gram.append( tmp_gram )
    #     data_corpus.append( " ".join(tmp_gram) )

    vectorizer = TfidfVectorizer( analyzer='char', ngram_range=(N_GRAM, N_GRAM), min_df=MIN_DF )
    """
    * "min_df": exclude rare term
    """
    data_vector = vectorizer.fit_transform( data_textonly )
    uniq_grams = list( vectorizer.vocabulary_ )
    idf = {}
    for g in uniq_grams:
        i = vectorizer.vocabulary_[g]
        idf[g] = round( vectorizer.idf_[i], 3 )

    # print( idf )
    idf_items = sorted( idf.items(), key=lambda x: x[1] )
    print( "* IDF min:", idf_items[:5] )
    print( "* IDF max:", idf_items[-5:] )
    print( "...", time()-t )


    print( "# Check Similarity "); t = time()
    # For test ###########
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        data = data[:800]
    ######################
    max_n = MAX_PARARING_TOPN
    for i, item1 in enumerate( tqdm( data ) ):
        tmp_sim = []
        for j in range( len(data) ):
            if i == j : continue
            item2 = data[j]
            ngram_src, ngram_trg = item1[3], item2[3]
            try:
                if USE_IDF:
                    if USE_WEIGHT_FN:
                        r = match_ratio( ngram_src, ngram_trg, idf, weight_fn=WEIGHT_FN )
                    else:
                        r = match_ratio( ngram_src, ngram_trg, idf )
                else:
                    if USE_WEIGHT_FN:
                        r = match_ratio( ngram_src, ngram_trg, weight_fn=WEIGHT_FN )
                    else:
                        r = match_ratio( ngram_src, ngram_trg )
            except Exception as ex:
                print( item1[2], item2[2], ex, "\n\n" )
                r = 0
            if r < CUTOFF: continue
            # sim.append( (i, j, r) )
            tmp_sim.append( (i, j, r) )

        if len( tmp_sim ) == 0 : continue
        tmp_sim_sorted = sorted( tmp_sim, key=lambda x: -x[2] )
        if max_n:
            if len( tmp_sim ) <= max_n :
                sim += tmp_sim
                continue
            # max_n 순위까지 더하기
            sim += tmp_sim_sorted[:max_n]
        else:
            sim += tmp_sim_sorted

    # print( sim )
    sim_sorted = sorted( sim, key=lambda x: x[2] )
    sim_report = [ { "src": [ data[ s[0] ][0], data[ s[0] ][2] ] , "trg": [ data[ s[1] ][0], data[ s[1] ][2] ] , "score": format(s[2], "0.3f") } for s in sim_sorted ]
    with open( report_file, 'w', encoding="utf-8") as fl:
        ym.dump( sim_report, fl )

    print( "...", time()-t )

    print( "# Build Report"); t = time()
    # print( sim )
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
