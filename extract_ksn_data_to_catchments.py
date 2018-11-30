#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:28:49 2018

@author: charlie

script to extract statistics of ksn, channel segment length, and %kjf
to study subcatchments. See also "extract_raster_data_to_catchments.py"
for extraction of slope and local relief data
"""
from grass.pygrass.modules.shortcuts import vector as v

#first, define which statistics we want.
#stupidly, v.vect.stats doesnt take all the same stats
#as v.rast.stats.
stats_list = ['minimum',
              'maximum',
              'range',
              'average',
              'stddev',
              'variance',
              'median',
              ]

#names for columns of stats
column_names_list = ['ksn_min',
                     'ksn_max',
                     'ksn_range',
                     'ksn_mean',
                     'ksn_stddev',
                     'ksn_variance',
                     'ksn_median']

#convert stats list to a single string because for some reason this method 
#won't accept a list like v.rast.stats does
#stats_string = ",".join(stats_list)

#basins file in which to store stats
basins = 'all_unique_wsheds_info'

#ksn points to use
ksn_points = 'chan_segs_points_trimmed'

#unfortunately, the v.vect.stats module only allows one method to be
#used at a time, as opposed to r.rast.stats. This is very frustrating.
#so we loop through the methods list and do them one-by-one.
for run in range(len(stats_list)):
    v.vect_stats(points = ksn_points, areas=basins, type='point', 
                 points_layer=1, areas_layer=1, method=stats_list[run],
                 points_column='ksn', count_column='ksn_points_count', 
                 stats_column=column_names_list[run])
