import os
from collections import Counter

from ruamel.yaml import YAML

######################################

filename = "formulas.yml"
basepath = os.path.join( "..", "..", "_data", "formula" )
cnt_min = 4

def chdir2cwd( file=__file__ ):
    # print( os.getcwd() )
    excute_file_path = os.path.dirname(os.path.realpath( file ))
    os.chdir( excute_file_path )

def get_data_from_yaml( filepath ):
    ym = YAML( typ='safe' )
    ym.default_flow_style = None
    with open( filepath, 'r', encoding="utf-8" ) as fl:
        data = ym.load( fl )
    return data

def mx_zero( row_n, col_n ):
    return [ [ 0 for i in range( col_n ) ] for j in range( row_n ) ]

######################################

def main():
    chdir2cwd( __file__ )

    filepath = os.path.join( basepath, filename )
    data = get_data_from_yaml( filepath )

    fm = data.get( 'formulas' )
    fm_names = list( fm )
    fm_org = [ list( fm.get( f ).get( 'ingOrg' ) ) for f in fm_names ]
    herb_cnt = Counter( sum( fm_org, [] ) )
    herb_lst = [ h for h, c in herb_cnt.most_common() if c >= cnt_min ]

    n = len( herb_lst )
    mx = mx_zero(n, n)
    for f in fm_org:
        for h1 in f:
            if h1 not in herb_lst : continue
            i1 = herb_lst.index( h1 )
            for h2 in f:
                if h2 not in herb_lst : continue
                i2 = herb_lst.index( h2 )
                mx[i1][i2] += 1
    with open( "herb_cooccurrence_matrix.tsv", 'w', encoding="utf-8") as fl:
        for k, ls in enumerate( mx):
            fl.write( herb_lst[k] + "\t" + "\t".join( [ str(c) for c in ls ] ) + "\n" )

if __name__ == '__main__':
    main()

# herb_h = Hash.new
#
# cutup = 5
#
# fs.each do | f|
# 	f.each do |h|
#
# 		herb_h[h] ||= 0
# 		herb_h[h] += 1
# 	end
# end
#
# herbs = herb_h.to_a.select{ |e| e[1] > cutup }.map{ |x| x[0] }
#
# rst = Array.new
#
# herbs.each_with_index do |herb1, i|
#
# 	rst[i] = Array.new
#
# 	herbs.each_with_index do |herb2, j|
#
# 		c = 0
#
# 		fs.each do | f |
#
# 			if ( f.include? herb1 ) and ( f.include? herb2 )
# 				c += 1
# 			end
#
# 		end
#
# 		rst[i][j] = c
#
# 	end
# end
#
#
# record = File.open('shanghan_herb_cooccurrence_matrix.tsv', 'w')
#
# herbs.each_with_index do | h, i |
#
# 	record.puts h + "\t" + rst[i].join("\t")
# end
