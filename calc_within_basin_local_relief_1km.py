#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:13:09 2019

@author: charlie

script to calculate 1 km local relief ONLY WITHIN each subbasin rather than
including values outside the basin.

Basically, this will:
    -iterate through each subbasin in the all_unique_wsheds_info layer
    -select each and export it to its own layer
    -use the new layer to mask the underlying elevation raster
    -use r.neighbors to calculate the local relief within only the masked area
    -then calculate the MEAN local relief within the polygon
"""
#import numpy as np
import grass.script as grass
from grass.pygrass.modules.shortcuts import general as g
#from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import raster as r

####up-front parameters
relief_window_size = 201 #100 m radius, 10 cells on each side of center
#all_wsheds = 'all_unique_wsheds_info'
#dem_name = 'small_crop_buffer'
#col_name = 'intra_10m_relief' #name of column in new basin to hold mean relief

####loop through subbasins ("value" column goes 0 to 343)
unique_names_list = []#use this later for patching
for basin in range(344): #will iterate [0,343] #344
    print('EXTRACTING ' + str(basin + 1) + ' OF 344...')
    #store present region
    grass.use_temp_region()
    #select relevant polygon
    #expression = '"value"=' + str(basin)
    out_name = 'tmp_vect_' + str(basin)
    #v.extract(input=all_wsheds, type='area', where=expression,
    #          output=out_name)
    #now make the mask that keeps everything inside the basin visible but
    #nulls everything outside
    r.mask(vector=out_name)
    #then use mapcalc
    rast_name = 'tmp_rast_' + str(basin)
    #save unique name for patching outside of the loop
    #unique_names_list.append(rast_name)
    #mc_exp=str(rast_name) + '=small_crop_buffer'#'"' + rast_name + '=small_crop_buffer"'
    #r.mapcalc(expression=mc_exp)
    #then to transfer color table:
    #r.colors(map=rast_name, raster=dem_name) # may be required to transfer the color table
    
    #now set the region to the small raster to speed computation
    g.region(zoom=rast_name)
    print('REGION SHRUNK TO RASTER ' + str(basin) + ' (see below)')
    g.region(flags='p')
    
    #now use r.neighbors to calc local relief at given scale ONLY
    #within the extracted subcatchment; all else is treated as NULL
    single_basin_relief_map = 'tmp_1km_relief_' + str(basin)
    r.neighbors(flags='c', input=rast_name, output=single_basin_relief_map,
                method='range',
                size=relief_window_size)
    r.mask(flags='r') #delete mask
    
    #restore region as it was before zoom to subbasin
    grass.del_temp_region()
    #print('FULL REGION RESTORED (see below)')
    #g.region(flags='p')
