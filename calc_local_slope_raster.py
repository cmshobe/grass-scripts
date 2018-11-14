#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:25:07 2018

@author: charlie

GRASS script to calculate a local slope map
"""
from grass.pygrass.modules.shortcuts import raster as r

elev_raster = 'small_crop_buffer'
output_slope_map = 'small_crop_buffer_slope'
r.slope.aspect(elevation=elev_raster, slope=output_slope_map)