#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to clip mosaiced DEM to study basins
PLUS A 5 KM BUFFER ON EVERY SIDE so that local relief is appropriately 
calculated.
"""
import sys
import os
#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r
from grass.pygrass.modules.shortcuts import vector as v

#first buffer the subcatchments layer by 5 km 
#(largest relief window extent I will need)
vector_to_be_buffered = 'subcatchments_vector'
output_name = 'subcatchments_buffer'
buffer_distance = 5000 #map units are m, so this is 5 km

v.buffer(input=vector_to_be_buffered, output=output_name,
         distance=buffer_distance, minordistance=buffer_distance,
         type='area')

#then use the basins to mask the mosaiced raster
mosaic_name = 'study_area_mosaic'
vector_mask_extent = 'subcatchments_buffer'
r.mask(vector=vector_mask_extent)

#then use mapcalc
r.mapcalc(expression="cropped_with_buffer=study_area_mosaic")

#then to transfer color table:
r.colors(map='cropped_with_buffer', raster=mosaic_name) # may be required to transfer the color table