#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:35:45 2018

@author: charlie

script to extract statistics of slope and relief to study subcatchments .
See also "extract_vector_data_to_catchments.py"
for extraction of ksn and %kjf data
"""
from grass.pygrass.modules.shortcuts import vector as v

#first, define which statistics we want
stats_list = ['number',
              'minimum',
              'maximum',
              'range',
              'average',
              'stddev',
              'variance',
              'coeff_var',
              'sum',
              'first_quartile',
              'median',
              'third_quartile',
              ]

#now, extract the local slope info by basin
basins = 'all_unique_wsheds_info'
slope_map = 'small_crop_buffer_slope_percent'
slope_prefix = 'slope'
v.rast_stats(verbose=True, map=basins, raster=slope_map, 
             column_prefix=slope_prefix, 
             method=stats_list)

#then do the same for 100m local relief
relief_100m_map = 'buffered_100m_relief'
relief_100m_prefix = 'relief_100m'
v.rast_stats(verbose=True, map=basins, raster=relief_100m_map, 
             column_prefix=relief_100m_prefix, 
             method=stats_list)

#then do the same for 1km local relief
relief_1km_map = 'buffered_1km_relief'
relief_1km_prefix = 'relief_1km'
v.rast_stats(verbose=True, map=basins, raster=relief_1km_map, 
             column_prefix=relief_1km_prefix, 
             method=stats_list)

#then do the same for 2.5km local relief
relief_2point5km_map = 'mosaic_2point5km_relief'
relief_2point5km_prefix = 'relief_2point5km'
v.rast_stats(verbose=True, map=basins, raster=relief_2point5km_map, 
             column_prefix=relief_2point5km_prefix, 
             method=stats_list)

#then do the same for 5km local relief
relief_5km_map = 'mosaic_5km_relief'
relief_5km_prefix = 'relief_5km'
v.rast_stats(verbose=True, map=basins, raster=relief_5km_map, 
             column_prefix=relief_5km_prefix, 
             method=stats_list)

#now extract elevation statistics for each basin
elev_map = 'small_crop_buffer'
elev_prefix = 'elev'
v.rast_stats(verbose=True, map=basins, raster=elev_map,
             column_prefix=elev_prefix,
             method=stats_list)