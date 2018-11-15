#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:41:36 2018

@author: charlie

using r.watershed to calculate flow accumulation raster

"""
from grass.pygrass.modules.shortcuts import raster as r

input_elev_map = 'small_crop_buffer'
direction_output_raster = 'small_crop_buffer_flowdir'
accum_output_raster = 'small_crop_buffer_accum'

max_memory_usage = 28000 #mb = 28 gb out of 31.2 available

#run r.watershed to calc flow accumulation
r.terraflow(flags='sm', elevation=input_elev_map,
            direction=direction_output_raster,
            accumulation=accum_output_raster,
            memory=max_memory_usage)