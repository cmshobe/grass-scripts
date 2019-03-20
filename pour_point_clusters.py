#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:51:39 2019

@author: charlie

try using clustering to delineate groups of points
"""
#import grass.script as grass
#from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import vector as v
#from grass.pygrass.modules.shortcuts import raster as r


pours='cleaned_pour_points'
dist_4point5km = 4500 #m
output_4point5km_window = 'pour_clusters_4point5km'
v.cluster(input=pours, output=output_4point5km_window, 
          distance = dist_4point5km,
          min = 1, method = 'dbscan')
