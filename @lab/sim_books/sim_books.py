import os, sys
from time import time
from collections import Counter
import math

from ruamel.yaml import YAML
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

from mylib import chdir2cwd, extract_han, preprocess, n_gram, flatten, uniq, pair2group
# from fuzzywuzzy import fuzz

"""
책들 사이에 유사도를 구해보자.
"""

######################################

FILENAMES = "SSE SSB SSG STB SCB SOB GGY SMK".split()
BASEPATH = os.path.join( "..", "..", "_data", "clause" )

USE_IDF = True

result_file = "sim_matrix.tsv"
report_file = "report.tsv"
######################################

def match_ratio( ngram_src, ngram_trg, idf={} ):
    # 결과가 비대칭이다.
    default_val = 1
    t1g_cnt, t2g_cnt = Counter(ngram_src), Counter(ngram_trg)
    t1g_set, t2g_set = set( list( t1g_cnt)  ), set( list( t2g_cnt)  )
    inter = list( t1g_set & t2g_set )
    union = list( t1g_set | t2g_set )
    # 분모 ( 합집합 gram의 idf 가중치 합계 )
    denominator \
    = sum( [ max( t1g_cnt.get(g,0), t2g_cnt.get(g,0) ) * idf.get(g, default_val) for g in union ] )
    # 분자 ( 교집합 gram의 idf 가중치 합계 )
    numerator \
    = sum( [ min( t1g_cnt.get(g,0), t2g_cnt.get(g,0) ) * idf.get(g, default_val) for g in inter ] )
    r = numerator / denominator
    return r

######################################

def main():

    chdir2cwd( __file__ )
    data, data_gram = {}, {}
    data_textonly = []
    sim = []

    ym = YAML( typ='safe' )
    ym.default_flow_style = None

    print( "# Build Data "); t = time()

    for filename in FILENAMES:
        filepath = os.path.join( BASEPATH, filename + '.yml' )
        with open( filepath, 'r', encoding="utf-8" ) as fl:
            tmp = ym.load( fl )

        data[filename], data_gram[filename] = [], []
        for d in tmp:
            n = d.get("NOO", "")
            if type(n) is not str: n = n[0]
            if ( "-00-" in n ) or ( "-000" in n ): continue
            txt = d.get("TXT").strip()
            hanzi_only = extract_han( txt )
            hanzi_only_gram = n_gram( hanzi_only, 2 )
            data[filename].append( hanzi_only )
            data_gram[filename].append( hanzi_only_gram )
            data_textonly.append( hanzi_only )

    data['SSA'] = sum( [ data['SSE'], data['SSB'], data['SSG'] ], [] )
    data_gram['SSA'] = sum( [ data_gram['SSE'], data_gram['SSB'], data_gram['SSG'] ], [] )

    # print(data, len(data))
    print( "...", time()-t )

    print( "# Build Meta-Data (idf) "); t = time()

    vectorizer = TfidfVectorizer( analyzer='char', ngram_range=(2, 2), min_df=4 )
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

    nodes = ['SSA'] + FILENAMES
    rst = np.zeros( [len(nodes), len(nodes)] )

    for i, node1 in enumerate( tqdm( nodes ) ):
        data1 = data[node1]
        data1_gram = data_gram[node1]
        data1_allgram = sum( data1_gram, [] )
        for j in range( len( nodes ) ):
            if i == j:
                r = 1
            else:
                node2 = nodes[j]
                data2 = data[node2]
                data2_gram = data_gram[node2]
                data2_allgram = sum( data2_gram, [] )
                try:
                    if USE_IDF:
                        r = match_ratio( data1_allgram, data2_allgram, idf )
                    else:
                        r = match_ratio( data1_allgram, data2_allgram )
                except Exception as ex:
                    print( data1_allgram, data2_allgram, ex, "\n\n" )
                    r = 0
            sim.append( (i, j, r) )
            rst[i][j] = r

    # print( sim )
    delimiter="\t"
    eol="\n"

    report_sim = [ s for s in sim if s[2] != 1 ]
    report_sim = sorted( report_sim, key=lambda x: -x[2] )
    with open( report_file, 'w', encoding="utf-8") as fl:
        for i,j,r in report_sim:
            fl.write( "{0}\t{1}\t{2:0.3f}".format(nodes[i],nodes[j],r) + eol )

    with open( result_file, 'w', encoding="utf-8") as fl:
        for i in range(len(nodes)):
            q = [ format(e, ".3f") for e in list( rst[i] ) ]
            txt = nodes[i] + delimiter + delimiter.join(q) + eol
            fl.write( txt )

    print( "...", time()-t )

if __name__ == '__main__':
    main()
