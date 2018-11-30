#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:30:27 2018

@author: charlie

This is a script to import and reproject the "KJf_new" poygons, which show the
locations where the Franciscan Melange unit crops out on the surface.
"""
from grass.pygrass.modules.shortcuts import vector as v

#first, import while creating a new location in the projection that the KJf_new 
#dataset currently has:
path_to_input_vector = '/home/charlie/Documents/research/mendocino/mendocino/GIS/Eel_river/commondata/geology/KJf_new.shp'
new_loc_name = 'kjf_loc'
temp_vector_name = 'kjf_newloc'
v.in_ogr(input=path_to_input_vector,
         output=temp_vector_name, 
         location=new_loc_name,
         snap=-1,
         min_area=0.0001)

#then, reproject the vector by bringing it from the location that was just 
#created into the working location
path_to_folder_containing_new_location = '/home/charlie/Documents/research/mendocino/mendocino/GIS'
reprojected_vector_name = 'kjf_new_proj'
v.proj(location=new_loc_name, mapset='PERMANENT', input=temp_vector_name,
       dbase = path_to_folder_containing_new_location,
       output = reprojected_vector_name)
