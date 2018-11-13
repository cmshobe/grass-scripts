#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to reproject my 11 NED 10m DEM rasters into UTM zone
10N.
"""
import sys
import os
#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r

from_location='ned_tiles'
from_mapset='PERMANENT'
dbase_path = os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/')

names = ['n39w123_tile', 'n39w124_tile', 'n40w123_tile', 'n40w124_tile', 
         'n40w125_tile', 'n41w123_tile', 'n41w124_tile', 'n41w125_tile', 
         'n42w123_tile', 'n42w124_tile', 'n42w125_tile'] #list of raster names

for name in names:
    r.proj(location=from_location, mapset=from_mapset, input=name, 
           dbase=dbase_path, output=name, resolution=10.0)