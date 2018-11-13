#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to import the 11 NED 10m DEMS that make up the broad
MTJ study area.
"""
import sys
import os
#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r
#import 1 of 11 rasters
path1= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n39w123/grdn39w123_13/w001001.adf')
name1='n39w123_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path1, output=name1)

#import 2 of 11 rasters
path2= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n39w124/grdn39w124_13/w001001.adf')
name2='n39w124_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path2, output=name2)


#import 3 of 11 rasters
path3= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n40w123/grdn40w123_13/w001001.adf')
name3='n40w123_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path3, output=name3)


#import 4 of 11 rasters
path4= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n40w124/grdn40w124_13/w001001.adf')
name4='n40w124_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path4, output=name4)


#import 5 of 11 rasters
path5= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n40w125/grdn40w125_13/w001001.adf')
name5='n40w125_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path5, output=name5)


#import 6 of 11 rasters
path6= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n41w123/grdn41w123_13/w001001.adf')
name6='n41w123_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path6, output=name6)


#import 7 of 11 rasters
path7= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n41w124/grdn41w124_13/w001001.adf')
name7='n41w124_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path7, output=name7)


#import 8 of 11 rasters
path8= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n41w125/grdn41w125_13/w001001.adf')
name8='n41w125_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path8, output=name8)


#import 9 of 11 rasters
path9= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n42w123/grdn42w123_13/w001001.adf')
name9='n42w123_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path9, output=name9)


#import 10 of 11 rasters
path10= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n42w124/grdn42w124_13/w001001.adf')
name10='n42w124_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path10, output=name10)


#import 11 of 11 rasters
path11= os.path.abspath('/home/charlie/Documents/research/mendocino/mendocino/GIS/ned_downloaded_tiles/n42w125/grdn42w125_13/w001001.adf')
name11='n42w125_tile'
if os.path.exists(path1):
    print('yes, path exists!')
else:
    print('no')
r.in_gdal(input=path11, output=name11)

#####################################################################