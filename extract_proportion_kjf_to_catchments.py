#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:45:42 2018

@author: charlie

This script will calculate the proportion of the kjf unit in each subcatchment
by the following steps:
    1) convert the kjf_new_proj vector (supplied by G. Bennett) to a raster
    2) set null values of that raster (non-kJf areas) equal to zero
    3) use v.rast.stats to calculate the average value of the raster in each
    polygon, which is conveniently also the proportion kjf in each polygon.
"""
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import raster as r


#first step: convert vector to raster
kjf_vector = 'kjf_new_proj'
kjf_raster = 'kjf_new_rast'
v.to.rast(input=kjf_vector, layer=1, type='area', output=kjf_raster, use='cat')

#second step: convert null values of the raster to zeros
r.null(map=kjf_raster, null=0)

#third step: extract the average value of the raster in each basin polygon
#and populate those values in a field called 'prop_kjf'
basins_vector = 'all_unique_wsheds_info'
new_field_name = 'prop_kjf'
v.rast_stats(map=basins_vector, layer=1, raster=kjf_raster, 
             column_prefix=new_field_name, method='average')