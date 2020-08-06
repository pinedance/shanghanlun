import os, sys
import glob

#####################################

PREFIX = "GGY-15-"
BEGIN, END = "022", "003"
STEP = 2



######################################

excute_file_path = os.path.dirname( os.path.realpath( __file__ ) )
project_file_path = os.path.join( excute_file_path, "..", ".." )

os.chdir( project_file_path )

cwd = os.getcwd()
print( cwd )

# onlyfiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk( cwd ) for f in filenames if os.path.isfile( os.path.join(dp, f) )]

target_files = ['*.yml', '*.yaml', '*.md', '*.txt']
onlyfiles = []
for t in target_files:
    onlyfiles += list( glob.iglob( os.path.join(cwd, '**', t), recursive=True ) )

# print( "\n".join( onlyfiles ) )

def replace_text_infile( a, b, filepath ):
    try:
        with open( filepath, 'r', encoding="utf-8" ) as fl:
            text = fl.read()
    except Exception as ex:
        print( "!!Read Fail", filepath, ex )
        return False

    text_new = text.replace( a, b )

    try:
        with open( filepath, 'w', encoding="utf-8" ) as fl:
            fl.write( text_new )
    except Exception as ex:
        print( "!!Write Fail", filepath, ex )
        return False

    return True

def padding( num, l, pad="0" ):
    raw = ( pad * l ) + str( num )
    start = -1 * l
    return raw[start:]

def get_queue( prefix, begin, end, step=1 ):
    idxlen = len( begin )
    queue = []
    if int( begin ) < int( end ):
        rg = range( int( begin ), int( end )+1, 1 )
    else:
        rg = range( int( begin ), int( end )-1, -1 )
    for i in rg:
        bf = prefix + padding( i, idxlen )
        af = prefix + padding( i+step, idxlen )
        queue.append( (bf, af) )
    return queue

def main():

    queue = get_queue( PREFIX, BEGIN, END, STEP )
    print( queue )

    if len(sys.argv) > 1 and sys.argv[1] == "exe":
        for a, b in queue:
            print( "*", a, "=>", b)
            for filepath in onlyfiles:
                status = replace_text_infile( a, b, filepath )

    print("# End")

if __name__ == '__main__':
    main()
