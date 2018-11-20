#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:11:26 2018

@author: charlie

Script for acquiring pour point candidates and [mostly] automatically
stripping them down to only the ones I need
"""
from grasspygrass.modules.shortcuts import raster as r
from grass.pygrass.modules.shortcuts import vector as v

#startingfrom flow accum raster
accum_raster = 'small_crop_buffer_accum'
reclassed_accum = 'reclassed_accum'
reclass_rules_file = 'reclass_rules_500max.txt'
#first, use r.reclass to isolate accums I care about (100000-500000 cells)
r.reclass(input=accum_raster, output=reclassed_accum, 
          rules = reclass_rules_file)

#then, use r.to.vect to turn every pixel with a goldilocks accumulation value
#into a point.
possible_pour_points = 'possible_pour_points'
r.to.vect(input=reclassed_accum, output=possible_pour_points, type='point')

#this results in a points file, but the points spill outside our area of 
#interest and also don't have accumulation values in the attribute table

#now, clip the points file to the AOI
clip_area = 'subcatchments_vector'
pour_points_in_aoi = 'pour_points_in_aoi'
v.clip(input=possible_pour_points, clip = clip_area, 
       output=pour_points_in_aoi)

#then use v.what.rast to extract accum values to the remaining points
v.what.rast(map=pour_points_in_aoi, type='point', raster = accum_raster, 
            column = 'accum_in_cells')

#now we want to split this points file up by the 38 subcatchments
#so that we can manually identify the real pour points.
#Then we use v.edit (see bottom of script) to get rid of points that aren't
#the real pour point.

list_of_watersheds_to_do = list(range(1,39))

watersheds_vector = 'subcatchments_vector'
candidate_pour_points = 'pour_points_in_aoi_8'

for i in range(len(list_of_watersheds_to_do)):
    sql_command = 'Catchment_ = ' + str(list_of_watersheds_to_do[i])
    single_subcatchment_name = 'subcatchment_' + str(list_of_watersheds_to_do[i]) + '_boundary'
    #first, extract the watershed to its own polygon shapefile
    v.extract(input=watersheds_vector, where=sql_command, 
              output=single_subcatchment_name)
    
    #then, clip pour points to that polygon
    subcatchment_pour_points_name = 'subcatchment_' + str(list_of_watersheds_to_do[i]) + '_pour_points'
    v.clip(input=candidate_pour_points, clip=single_subcatchment_name,
           output=subcatchment_pour_points_name)
    
#command to kill unnecessary pour point (need to manually get id's for QC purposes)
#v.edit -r map=subcatchment_xx_pour_points type=point tool=delete cats=#####,#####
#where ##### is the cat number of a point we WANT TO KEEP