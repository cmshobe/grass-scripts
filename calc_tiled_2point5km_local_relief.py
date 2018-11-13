#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

GRASS script to calculate 2.5 km local relief.
This was taking a horribly long time on a single core so I will
segment the domain into overlapping tiles, and parse each tile 
out to a different core.
"""
import os
import multiprocessing as multi

import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r
from grass.pygrass.modules.shortcuts import general as g

#store present region
grass.use_temp_region()

aoi_dem = 'small_crop_buffer'

#tile parameters: want 10 tiles; 5 rows x 2 columns
#assume for the moment that you dont need to include overlap in width/height

width_of_tiles = 4135 #16540/4
height_of_tiles = 7208 #36040/5
overlap = 500 #cells; 2500 m / 10 m per cell = 250 cells * 2

#then, tile the raster
#for some reason this gives 3 columns but I don't need the third
output_base_name = '2point5km_tile'
r.tile(input=aoi_dem, output=output_base_name, 
       width=width_of_tiles, height=height_of_tiles, 
       overlap=overlap)

# some rasters are empty because of the shape of the AOI,
#so there are actually only 8 rasters with information in them.

# Find number of workers that can be used on system. This variable could 
# also be set manually.

# =============================================================================
workers = multi.cpu_count() #to leave one processor available
# # This is only a set of examples for r.slope.aspect jobs where the maps are
# # named serially.
jobs = 15 #number of tiles
# 
# Check if workers are already being used
if workers is 1 and "WORKERS" in os.environ:
    workers = int(os.environ["WORKERS"])
if workers < 1:
    workers = 1
# 
# Initialize process dictionary
proc = {}

#make list of input rasters
#the two left out are upper right (000-001) and lower left (004-000).
input_rasters = [output_base_name + '-000-000',
                 output_base_name + '-000-001',
                 output_base_name + '-001-000',
                 output_base_name + '-001-001',
                 output_base_name + '-001-002',
                 output_base_name + '-001-003',
                 output_base_name + '-002-000',
                 output_base_name + '-002-001',
                 output_base_name + '-002-002',
                 output_base_name + '-002-003',
                 output_base_name + '-003-001',
                 output_base_name + '-003-002',
                 output_base_name + '-003-003',
                 output_base_name + '-004-002',
                 output_base_name + '-004-003']

#make list of output names
output_names = ['000-000_2point5km_relief',
                '000-001_2point5km_relief',
                '001-000_2point5km_relief',
                '001-001_2point5km_relief',
                '001-002_2point5km_relief',
                '001-003_2point5km_relief',
                '002-000_2point5km_relief',
                '002-001_2point5km_relief',
                '002-002_2point5km_relief',
                '002-003_2point5km_relief',
                '003-001_2point5km_relief',
                '003-002_2point5km_relief',
                '003-003_2point5km_relief',
                '004-002_2point5km_relief',
                '004-003_2point5km_relief']

# Loop over jobs
for i in range(jobs):
    input_raster = input_rasters[i]
    window_size = 501
    output_name = output_names[i]
    # Insert job into dictinoary to keep track of it
    #set computational region to the current tile
    print('setting region for tile ' + input_raster)
    g.region(flags='p', raster=input_raster, zoom=input_raster)
    
    proc[i] = grass.start_command('r.neighbors', 
            flags='c', 
            input=input_raster, 
            output=output_name, 
            method='range',
            size=window_size)
    print('started processing tile ' + 'input_raster')
    # If the workers are used up, wait for all of them from the last group to
    # finish.
    if (i % (workers) is 0) and (i != 0): #and (i != 1) 
        for j in range(workers):
            print(j)
            print('PROCESS HALTED ' + 'input_raster')
            print('PROCESS ID ' + str(i))
            proc[i - j].wait()

# Make sure all workers are finished.
for i in range(jobs):
    if proc[i].wait() is not 0:
        grass.fatal(('Problem running analysis on evel_' + str(i) + '.'))
        
#restore region as it was before script
grass.del_temp_region()
print('SCRIPT COMPLETE: TEMPORARY REGION RESTORED (see below)')
g.region(flags='p')