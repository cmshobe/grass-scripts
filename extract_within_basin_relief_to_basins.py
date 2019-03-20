#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:42:16 2019

@author: charlie

Script to extract within-basin relief to watersheds shapefile.
-Relief comes from scripts: calc_within_basin_local_relief_xkm.py

How it works:
    -loop through relief windows (100m, 1km, 2.5km, 5km)
    -for each one, stitch together all individual basin relief rasters into one
    -then use v.rast.stats to average the values in each subbasin and
        extract them to 'all_unique_wsheds_info'
"""
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import raster as r

all_wsheds = 'all_unique_wsheds_info' #name of watersheds shapefile where all the info will go

list_of_column_prefixes = ['intra_100m_relief',
                           'intra_1km_relief',
                           'intra_2point5km_relief',
                           'intra_5km_relief']
#generate list of names for each relief window, then combine
#into a list of names lists

#100m
names_100m = ['tmp_relief_{}'.format(i) for i in range(344)]

#1km
names_1km = ['tmp_1km_relief_{}'.format(i) for i in range(344)]

#2.5km
names_2point5km = ['tmp_2point5km_relief_{}'.format(i) for i in range(344)]

#5km
names_5km = ['tmp_5km_relief_{}'.format(i) for i in range(344)]

list_of_names_lists = [names_100m,
                       names_1km,
                       names_2point5km,
                       names_5km]

for j in range(len(list_of_column_prefixes)):

    col_name = list_of_column_prefixes[j] #name of column in new basin to hold mean relief

    #now stitch all local relief rasters into one big one
    patched_rast = 'patched_' + col_name
    names_list = list_of_names_lists[j]
    r.patch(input=names_list, output=patched_rast)

    #now get the mean local relief 
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

    v.rast_stats(verbose=True, map=all_wsheds, raster=patched_rast, 
                 column_prefix=col_name, 
                 method=stats_list)