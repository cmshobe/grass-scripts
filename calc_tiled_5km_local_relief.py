#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:57:52 2018

@author: charlie

This version works such that new jobs get spawned as old ones finish,
instead of having to wait for all previously assigned jobs to finish
before new ones will start.

note: this is the 5km radius script. because more overlap is required,
this results in an extra tile for 16 total jobs instead of 15.
"""
import time
import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r
from grass.pygrass.modules.shortcuts import general as g
import multiprocessing

def work(i):
    input_raster = input_rasters[i]
    window_size = 1001
    output_name = output_names[i]
    # Insert job into dictinoary to keep track of it
    #set computational region to the current tile
    time.sleep(i*5)
    print('setting region for tile ' + input_raster)
    g.region(flags='p', raster=input_raster, zoom=input_raster)
    print('starting to process tile ' + input_raster)
    grass.run_command('r.neighbors', #use run_command instead of start_command
            flags='c', 
            input=input_raster, 
            output=output_name, 
            method='range',
            size=window_size)

max_n_processes = 12
total_tasks = 16

#store present region
grass.use_temp_region()

aoi_dem = 'small_crop_buffer'

#tile parameters: want 10 tiles; 5 rows x 2 columns
#assume for the moment that you dont need to include overlap in width/height

width_of_tiles = 4135 #16540/4
height_of_tiles = 7208 #36040/5
overlap = 1000 #cells; 5000 m / 10 m per cell = 500 cells * 2

#then, tile the raster
#for some reason this gives 3 columns but I don't need the third
output_base_name = '5km_tile'
r.tile(input=aoi_dem, output=output_base_name, 
       width=width_of_tiles, height=height_of_tiles, 
       overlap=overlap)

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
                 output_base_name + '-004-001',
                 output_base_name + '-004-002',
                 output_base_name + '-004-003']

#make list of output names
output_names = ['000-000_5km_relief',
                '000-001_5km_relief',
                '001-000_5km_relief',
                '001-001_5km_relief',
                '001-002_5km_relief',
                '001-003_5km_relief',
                '002-000_5km_relief',
                '002-001_5km_relief',
                '002-002_5km_relief',
                '002-003_5km_relief',
                '003-001_5km_relief',
                '003-002_5km_relief',
                '003-003_5km_relief',
                '004-001_5km_relief',
                '004-002_5km_relief',
                '004-003_5km_relief']

pool = multiprocessing.Pool(processes=max_n_processes)
tasks = range(total_tasks)
results = pool.map(work, tasks, chunksize=1) #not map_async #this is where the magic happens
pool.close()
pool.join()

#restore region as it was before script
grass.del_temp_region()
print('SCRIPT COMPLETE: TEMPORARY REGION RESTORED (see below)')
g.region(flags='p')