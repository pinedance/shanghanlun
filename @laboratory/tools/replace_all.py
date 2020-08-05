import os

#####################################

PREFIX = "TES-01-"
BEGIN, END = "007", "030"




######################################

excute_file_path = os.path.dirname( os.path.realpath( __file__ ) )
project_file_path = os.path.join( excute_file_path, "..", ".." )

os.chdir( project_file_path )

cwd = os.getcwd()
print( cwd )

onlyfiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk( cwd ) for f in filenames if os.path.isfile( os.path.join(dp, f) )]

# print( onlyfiles )

def replace_text_infile( a, b, filepath ):
    with open( filepath, 'r', encoding="utf-8" ) as fl:
        text = fl.read()

    text_new = text.replace( a, b )

    with open( filepath, 'w', encoding="utf-8" ) as fl:
        fl.write( text_new )

def padding( num, l, pad="0" ):
    raw = ( pad * l ) + str( num )
    start = -1 * l
    return raw[start:]

def get_queue( prefix, begin,end ):
    idxlen = len( begin )
    queue = []
    for i in range( int( end ), int( begin), -1 ):
        bf = prefix + padding( i, idxlen )
        af = prefix + padding( i+1, idxlen )
        queue.append( (bf, af) )
    return queue

def main():

    queue = get_queue( PREFIX, BEGIN, END )
    print( queue )


    # for a, b in queue:
    #     for filepath in onlyfiles:
    #         replace_text_infile( a, b, filepath )
    #         print( "*", a, "=>", b)
    #
    # print("# End")

if __name__ == '__main__':
    main()
