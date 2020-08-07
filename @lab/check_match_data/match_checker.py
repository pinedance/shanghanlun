import os

from collections import Counter
from ruamel.yaml import YAML


######################################

basepath = os.path.join( "..", "..", "_data", "compare" )
filename = "similartext.yaml"

######################################

def chdir2cwd( file=__file__ ):
    # print( os.getcwd() )
    excute_file_path = os.path.dirname(os.path.realpath( file ))
    os.chdir( excute_file_path )

def flatten( lst ):
    return sum( lst, [] )

def uniq( lst ):
    return list( dict.fromkeys( lst ) )


######################################

def main():

    chdir2cwd( __file__ )

    ym = YAML( typ='safe' )
    ym.default_flow_style = None

    filepath = os.path.join( basepath, filename )
    with open( filepath, 'r', encoding="utf-8" ) as fl:
        data = ym.load( fl )

    keys = uniq( flatten( [ list(d) for d in data ] ) )
    print( keys )

    rst = {}
    for k in keys:
        q = flatten( [ d.get(k, []) for d in data ] )
        q_cnt = Counter( q )
        q_items = q_cnt.most_common()
        q_gt1 = [ t for t, n in q_items if n > 1 ]
        rst[k] = sorted( q_gt1, reverse=True )

    with open( "duplicated_claus.yml", 'w', encoding="utf-8") as fl:
        # ym.dump( sim_report_group, fl, transform=tr )
        ym.dump( rst, fl )

if __name__ == '__main__':
    main()
