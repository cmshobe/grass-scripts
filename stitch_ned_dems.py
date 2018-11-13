#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to stitch together the 10 relevant DEMS into one.
"""
import sys
import os
#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r

in_names = ['n39w123_tile', 'n39w124_tile', 'n40w123_tile', 'n40w124_tile', 
         'n40w125_tile', 'n41w123_tile', 'n41w124_tile', 'n41w125_tile', 
         'n42w124_tile', 'n42w125_tile']
out_name = 'study_area_mosaic'

r.patch(input=in_names, output=out_name)