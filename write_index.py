
import pyproj
import fiona
import fiona.crs

import rtree

input_file = 'se_england_clean.shp' #put the input file here

def populate_index(idx, name_file_in):
    count =0
    with fiona.open(name_file_in, 'r') as shp_input :
        for building in shp_input:
            idx.insert(count, Polygon(building['geometry']['coordinates'][0]).bounds)
            count=count+1



idx = rtree.index.Index('Rtree_index_east')
populate_index(idx,input_file)
print "Index populated"
