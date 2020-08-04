import os
from time import time
from difflib import SequenceMatcher

from ruamel.yaml import YAML
import regex as re
from tqdm import tqdm
# from fuzzywuzzy import fuzz

######################################

cutoff = 0.85

filenames = ["SHL_Song", "SHL_SongGabu", "SHL_SongRule", "SHL_SongEtc",\
    "SHL_Tang", "SHL_Chunhe", "SHL_ChunheEtc", "SHL_Ogham", "MK", "GGYL"]

basepath = os.path.join( "..", "..", "_data", "clause" )

cjk_range = "[\p{Han}]"
CJK = re.compile( cjk_range, re.UNICODE)


######################################

def chdir2cwd( file=__file__ ):
    # print( os.getcwd() )
    excute_file_path = os.path.dirname(os.path.realpath( file ))
    os.chdir( excute_file_path )

def extract_han( text, cjk=CJK ):
    return "".join( re.findall( cjk, text  ) )

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
    rst = { "MK": [], "Song": [], "SongEtc": [], "SongRule": [], "SongGabu": [], "Tang": [], "Chunhe": [], "ChunheEtc": [], "Ogham": [], "GGYL": [] }
    for e in lst:
        _book, noo = e.split("@")
        book = _book.split("_")[1] if "_" in _book else _book
        rst[book].append( noo)
    return rst

def build_ridx( lst ):
    ridx = {}
    for i, em in enumerate( lst ):
        for k in em:
            if ridx.get( k ): ridx[k].append( i )
            else: ridx[k] = [ i ]
    return ridx

def flatten( lst ):
    return sum( lst, [] )

def uniq( lst ):
    return list( dict.fromkeys( lst ) )

def pair2group( lst ):                # lst : [[a,b], [a,c], [a,d,u], [c,d] ... ]
    ridx = build_ridx( lst )            # ridx : { 'a': [0,1,2], 'b':[0] ... }
    idx_list_of_pair = [ uniq( flatten( [ ridx.get( e ) for e in pair ] ) ) for pair in lst ]
    new_lst_ = [ uniq( flatten( [ lst[i] for i in idx_arr ] ) ) for idx_arr in idx_list_of_pair ]
    new_lst_ = uniq( [ tuple(item) for item in new_lst_ ] )
    new_lst = [ list(item) for item in new_lst_ ]
    if len( lst ) ==  len( new_lst):
        return new_lst
    else:
        return pair2group( new_lst )

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
    for filename in filenames:
        filepath = os.path.join( basepath, filename + '.yml' )
        with open( filepath, 'r', encoding="utf-8" ) as fl:
            tmp = ym.load( fl )

        for d in tmp:
            n = d.get("NOO", "")
            if type(n) is not str:
                n = n.get("NoA")
                if type(n) is not str:
                    n = n[1]

            if ( "-00-" in n ) or ( "-000" in n ): continue
            data.append(  ( filename + "@" + n, extract_han( d.get("TXT") ), d.get("TXT")  ) )

    print( "...", time()-t )


    print( "# Check Similarity "); t = time()
    # For test ###########
    # data = data[:800]
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
            if sim_dic.get(i):
                try:
                    sim_dic[i] = sim_dic[i].append( j )
                except ImportError:
                    print( sim_dic[i], j, r )
            else:
                sim_dic[i] = [i, j]

    data_report = [ { "src": [ data[ s[0] ][0], data[ s[0] ][2] ] , "trg": [ data[ s[1] ][0], data[ s[1] ][2] ] , "score": s[2] } for s in sim ]
    with open("report.yml", 'w', encoding="utf-8") as fl:
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
    sim_report_group = ( [ add_code( [ data[x][0] for x in sim ] ) for sim in sim_group ] )

    with open( "similartext_auto.yml", 'w', encoding="utf-8") as fl:
        # ym.dump( sim_report_group, fl, transform=tr )
        ym.dump( sim_report_group, fl )

    print( "...", time()-t )


if __name__ == '__main__':
    main()
