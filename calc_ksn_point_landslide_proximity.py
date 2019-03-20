#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:09:11 2019

@author: charlie
"""

from grass.pygrass.modules.shortcuts import vector as v
from grass.script import run_command

#create new column in points map to hold lithology
ksn_points_map = 'chan_segs_points_trimmed'
new_col_name = 'lith_label varchar(10)'
v.db_addcolumn(map=ksn_points_map,
               columns=new_col_name)

#ask of all points: what is your lithology?
geologic_map = 'cageol_poly_dd'
lithology_column = 'ORIG_LABEL'
extract_to='lith_label'
v.what_vect(map=ksn_points_map,
            column=extract_to,
            query_map=geologic_map,
            query_column=lithology_column)

#ask of all points: how far are you from the nearest failure polygon?
failures_map = 'all_hillslope_failures'
lines_output='lines_from_channel_points_to_failures'
new_col_name2 = 'dist_to_failure double'
v.db_addcolumn(map=ksn_points_map,
               columns=new_col_name2)
new_col_name3 = 'cat_of_failure double'
v.db_addcolumn(map=ksn_points_map,
               columns=new_col_name3)
things_to_extract = ['dist','cat']
cols_to_extract_to = ['dist_to_failure', 'cat_of_failure']

#v.distance(from_=ksn_points_map,
#           from_type='point',
#           to=failures_map,
#           to_type='area',
#           output=lines_output,
#           upload=things_to_extract,
#           column=cols_to_extract_to)

#had to use the run_command structure because 'from' is a reserved keyword
run_command('v.distance', from_=ksn_points_map,
           from_type='point',
           to=failures_map,
           to_type='area',
           output=lines_output,
           upload=things_to_extract,
           column=cols_to_extract_to)