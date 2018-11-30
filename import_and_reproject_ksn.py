#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:08:00 2018

@author: charlie

Script for importing and reprojecting the ksn (normalized steepness index)
dataset of Bennett et al (2016).
"""
from grass.pygrass.modules.shortcuts import vector as v

#first, import while creating a new location in the projection that the ksn 
#dataset currently has:
path_to_input_vector = '/home/charlie/Documents/research/mendocino/mendocino/GIS/Eel_river/chan_segs_with_litho.shp'
new_loc_name = 'chan_segs_loc'
temp_vector_name = 'chan_segs_with_litho_newloc'
v.in_ogr(input=path_to_input_vector,
         output=temp_vector_name, 
         location=new_loc_name,
         snap=-1,
         min_area=0.0001)

#then, reproject the vector by bringing it from the location that was just 
#created into the working location
path_to_folder_containing_new_location = '/home/charlie/Documents/research/mendocino/mendocino/GIS'
reprojected_vector_name = 'chan_segs_with_litho_proj'
v.proj(location=new_loc_name, mapset='PERMANENT', input=temp_vector_name,
       dbase = path_to_folder_containing_new_location,
       output = reprojected_vector_name)