

Required libraries (install them in this order on a clean environment (using Python 2.7))

- matplotlib (install it via Anaconda)
- basemap (install it via Anaconda)
- shapely (`conda install -c scitools shapely `)
- fiona (`conda install -c conda-forge fiona=1.6 `)
- Rtree (`conda install -c conda-forge rtree`)


# Combine shapefile and Rtree

### Writing an RTree index

The Rtree index provided with the repository has been computed with the script stored in `write_index.py`. Take a look at the script:

- the index is created with `idx = rtree.index.Index('Rtree_index_east')`. By default if you provide a string as input the index will be written on a file with the same name

- the index is populated with the function `populate_index` where:

  - the shapefile is opened with fiona `with fiona.open(name_file_in, 'r') as shp_input :`

  - for each building an entry is inserted in the index. Notice that for each entry we need:
    - the bounding box of the object we are inserting in the Rtree (`Polygon(building['geometry']['coordinates'][0]).bounds`)
    - the element associated with such bounding box (`count`). In this case we are using the index of the building in the shapefile (this will provide a quick access to the building without having to store the entire geometry).


### Reading an RTree index

For this part use `read_index.py`

Here you will try to load and visualize building from a shapefile by using the Rtree index for searching the buildings efficiently.

- Start by visiting this [website](http://boundingbox.klokantech.com). Zoom consistently on the London city and pick a bounding box enclosing part of its center. Copy  (by selecting the CSV format) the lat and long coordinates of the bounding box in `coords`.

- Set the correct file names:

  - `input_file` is the shapefile (download from this [link](https://www.dropbox.com/s/yuqstvcmc3877vc/buildings.zip?dl=0))
  - `out_file` is the file on which you will write the clipped buildings to visualize
  - `file_index` is the file containing the Rtree index (download from this [link](https://www.dropbox.com/s/z0mxzlzy47dj4v3/spatial_index.zip?dl=0)).


At this point you can go on implementing the function `write_clipped_file`.

- start by opening a new index from the Rtree file.
- then select all the buildings which bounding box intersect with the `query_box`. (Look at the function intersection of the documentation of rtree). The returned value will be a list of indices of the buildings that we want to visualize.

- open with Fiona the input shapefile and the new (clipped) shapefile that we want to produce in output. By cycling on the list of indices select the desired buildings and write them in the new file 'out_file'.

The result should be a set of buildings covering the region selected. Save the image produced and upload it on GitHub.
