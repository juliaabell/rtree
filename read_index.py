import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap

import fiona
import fiona.crs

import rtree


input_file = #put the input file here
out_file = #put the name of the output file here
file_index = #put the name of the file storing the RTree Index here

query_box = [,,,] #put the coordinates of the box you want to visualize here in this order:
#lat of the lowest left corner
#long of the lowest left corner
#lat of the upper right corner
#long of the upper right corner


input_file = 'C:\\Users\\Julia Bell\\Documents\\UMD Senior Year\\GEOG476\\buildings\\se_england_clean.shp'

out_file = 'C:\\Users\\Julia Bell\\Documents\\UMD Senior Year\\GEOG476\\buildings\\se_england_clipped.shp'
file_index = 'C:\\Users\\Julia Bell\\Documents\\UMD Senior Year\\GEOG476\\Rtree_index_east'

query_box = [-0.1333165169,51.5046555989,-0.121986866,51.5100245354] 



def write_clipped_file(name_file_in, out_file, file_index):
    idx = rtree.index.Index(file_index)
    #idx.insert(0,query_box)
    
    with fiona.open(input_file, 'r') as shp_input :
        
        schema= shp_input.schema.copy()
            
            
        with fiona.open(out_file, 'w', 'ESRI Shapefile', schema) as out_file :
            test=list(idx.intersection(query_box))
           
            for index in test:
                print index
                
                        
                building=(shp_input[int(index)])
                
                #print building
                out_file.write(building)
            
write_clipped_file(input_file,out_file,file_index)

map = Basemap(llcrnrlon=query_box[0],
              llcrnrlat=query_box[1],
              urcrnrlon=query_box[2],
              urcrnrlat=query_box[3],
             resolution='c', projection='tmerc', lat_0 = 0, lon_0 = 0)

map.readshapefile(out_file, 'buildings', drawbounds = True, color='red')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='white',lake_color='aqua')
map.drawcoastlines()
