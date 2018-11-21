#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:57:29 2018

@author: charlie

create watersheds from pour point shapefile 'cleaned_pour_points'
"""
import numpy as np
import grass.script as grass
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import raster as r

grass.use_temp_region() #save the region so I can zoom in on rasters

#first, export all pour points to ascii file  to be read in for wshed creation

cleaned_pour_points = 'cleaned_pour_points'
out_file = 'cleaned_pour_points.csv'

v.out_ascii(input=cleaned_pour_points, layer=1, type='point', 
            output=out_file, format='point', separator=',')

#now, loop through those pour points and create a watershed for each one
points = np.genfromtxt(out_file, delimiter=',') #import csv
x_coords = points[:, 0]
y_coords = points[:, 1]
n_points = len(x_coords)

#set input flow direction map
flow_dir_map = 'small_crop_buffer_flowdir'
unique_names_list = []#use this later for patching
for point in range(n_points):#n_points
    #dynamically set output name to avoid overwriting wsheds
    wshed_name = 'wshed_' + str(point) 
    print('Extracting watershed ' + str(point + 1) + ' of ' + str(n_points))

    #get coordinates into right form
    x_coord = x_coords[point]
    y_coord = y_coords[point]
    coords = [x_coord, y_coord]
    
    #extract one watershed
    r.water_outlet(input=flow_dir_map, output=wshed_name, 
                   coordinates=coords)
    
    #temporarily zoomthe computational region to the raster of interest
    g.region(flags='p', raster=wshed_name, zoom=wshed_name)
    
    #use r.null as an intermediate step to creating vector watersheds
    r.null(map=wshed_name, setnull=0) 
    
    #now use r.recode to give each raster a unique value
    #write a rules file
    rules_file = 'wshed_' + str(point) + '_recode_rules.txt'
    file = open(rules_file, "w")
    file.write('1:1:' + str(point) + ':' + str(point))
    file.close()
    
    #use r.recode to find the rules file and recode the basin
    recoded_name = 'wshed_' + str(point) + '_unique'
    r.recode(overwrite=True, input=wshed_name, output=recoded_name, 
             rules=rules_file)
    
    #save unique name for patching outside of the loop
    unique_names_list.append(recoded_name)
    
    grass.del_temp_region() #revert to full region
    
#now once they've all been extracted, nulled, and recoded, we patch the basins
patched_raster = 'all_unique_wsheds_rast'
r.patch(input=unique_names_list, output=patched_raster)

#now turn them into a vector areas file
uncleaned_vector = 'all_unique_wsheds_vect'
r.to_vect(input=patched_raster, output=uncleaned_vector, type='area')

#now clean the vector polygons file to get ride of weird tiny basins
cleaned_vector = 'all_unique_wsheds_cleaned'
v.clean(input=uncleaned_vector, output=cleaned_vector, tool='rmarea',
        threshold=1000000)

#now add a column to the attribute table to hold drainage area in square km
column_name_and_type = 'drainage_area_sqkm DOUBLE PRECISION'
v.db_addcolumn(map=cleaned_vector, columns=column_name_and_type)

#finally, calculate polygon areas and use them to populate the new column
column_name = 'drainage_area_sqkm'
v.to_db(map=cleaned_vector, option='area', columns=column_name, 
        units='kilometers')

#and we're done!