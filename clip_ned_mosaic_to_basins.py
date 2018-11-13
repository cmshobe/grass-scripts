#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to clip mosaiced DEM to study basins.
"""
import sys
import os
#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r

mosaic_name = 'study_area_mosaic'
vector_mask_extent = 'subcatchments_vector'

#first, use the basins to mask the mosaiced raster
r.mask(vector=vector_mask_extent)

#then use mapcalc
r.mapcalc(expression="cropped=study_area_mosaic")

#then to transfer color table:
r.colors(map='cropped', raster=mosaic_name) # may be required to transfer the color table