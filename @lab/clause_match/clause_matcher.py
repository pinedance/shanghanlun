import os, sys
from time import time
from difflib import SequenceMatcher

from ruamel.yaml import YAML
import regex as re
from tqdm import tqdm
# from fuzzywuzzy import fuzz

from mylib import chdir2cwd, extract_han, preprocess, n_gram, flatten, uniq, pair2group

"""
SequenceMatcher를 이용하여 조문 사이에 유사도를 계산한다.
계산된 유사도값(r)이 cutoff 이상인 조합을 서로 연관된 조합으로 본다.
연관된 조합들 사이에 공통된 조문이 있으면 이를 합쳐나간다.
더이상 합칠 것이 없게 된 조문 조합들이 결과이다.
"""

######################################

cutoff = 0.75

FILENAMES = "SSB SSR SSG SSE STB SCB SOB GGY SMK".split()

basepath = os.path.join( "..", "..", "_data", "clause" )

report_file = "report.yml"
result_file = "similartext_auto.yml"

######################################


# def match_ratio( text1, text2, metric="diff" ):
#     if metric is "fuzz":
#         r = fuzz.ratio( text1, text2 ) / 100
#     elif metric is "partial_fuzz":
#         r = fuzz.partial_ratio( text1, text2 ) / 100
#     else:
#         r = SequenceMatcher( None, text1, text2 ).quick_ratio()
#     return r

def match_ratio( text1, text2 ):
    r = SequenceMatcher( None, text1, text2 ).quick_ratio()
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
    data = []
    sim, sim_dic, sim_group = [], {}, []
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
            txt = d.get("TXT").strip()
            hanzi_only = extract_han( preprocess( txt ) )
            data.append(  ( n, hanzi_only, txt ) )

    print( "...", time()-t )


    print( "# Check Similarity "); t = time()
    # For test ###########
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        data = data[:800]
    ######################
    for i, item1 in enumerate( tqdm( data ) ):
        for j in range( i+1, len(data) ):
            item2 = data[j]
            text1, text2 = item1[1], item2[1]
            try:
                r = match_ratio( text1, text2 )
            except ImportError:
                print( text1, text2, "\n\n" )
                r = 0
            if r < cutoff: continue
            sim.append( (i, j, r) )
            # if sim_dic.get(i):
            #     try:
            #         sim_dic[i] = sim_dic[i].append( j )
            #     except ImportError:
            #         print( sim_dic[i], j, r )
            # else:
            #     sim_dic[i] = [i, j]
    sim_sorted = sorted( sim, key=lambda x: x[2] )
    data_report = [ { "src": [ data[ s[0] ][0], data[ s[0] ][2] ] , "trg": [ data[ s[1] ][0], data[ s[1] ][2] ] , "score": s[2] } for s in sim_sorted ]
    with open( report_file, 'w', encoding="utf-8") as fl:
        ym.dump( data_report, fl )

    print( "...", time()-t )

    print( "# Build Report"); t = time()
    # queue = [ 0 for i in range( len(data) ) ]
    # print( "# Merge and Report Result "); t = time()
    # for i in range( len(data) ):
    #     if sim_dic.get( i ) is None: continue
    #     if queue[i] is 1: continue
    #     trg = set( sim_dic.get( i ) )
    #     while True:
    #         new_trg = set( list( trg ) + sum( [ sim_dic.get( k ) for k in list( trg ) if sim_dic.get( k ) ], [] ) )
    #         if trg == new_trg: break
    #         else: trg = new_trg
    #     sim_group.append( sorted( list( trg ) ) )
    #     for q in trg: queue[q] = 1

    sim_group = pair2group( [ [ s[0], s[1] ] for s in sim ] )
    sim_report_group = [ add_code( [ data[x][0] for x in sim ] ) for sim in sim_group ]

    with open( result_file, 'w', encoding="utf-8") as fl:
        # ym.dump( sim_report_group, fl, transform=tr )
        ym.dump( sim_report_group, fl )

    print( "...", time()-t )


if __name__ == '__main__':
    main()
