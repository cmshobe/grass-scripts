#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:49:37 2018

@author: charlie

Hopefully a GRASS script to to calculate 100 m,
1 km, 2.5 km, and 5 km radius local relief on my AOI DEM buffered by 5km
to ensure that all points have full data availability.

Note that ocean-adjacent points will have a lot of zeros, but
that seems perfectly realistic.

THIS SCRIPT WILL WORK IN PARALLEL SUCH THAT EACH LOCAL RELIEF CALCULATION
RUNS ON A DIFFERENT CORE IN PARALLEL. THIS MEANS AT LEAST FOUR CORES ARE
REQUIRED FOR THIS SCRIPT TO WORK!

NOTE: THIS SCRIPT DOES NOT WORK. GRASS DOESN'T TALK WITH JOBLIB.
"""
#stuff needed for parallelization
from joblib import Parallel, delayed
#import multiprocessing

#import grass.script as grass
from grass.pygrass.modules.shortcuts import raster as r

#INPUTS################################################################
#input DEM is buffered AOI DEM
aoi_dem = 'cropped_with_buffer'

#DEFINE FUNCTION THAT WILL BE RUN ON EACH CORE INDEPENDENTLY################
indices = range(4)
def calc_local_relief(i):
    #going from biggest job to smallest is generally good practice
    output_names = ['buffered_5km_relief', 
                    'buffered_2point5km_relief', 
                    'buffered_1km_relief', 
                    'buffered_100m_relief']
    window_sizes = [1001, 501, 201, 21]
    output_name = output_names[i]
    window_size = window_sizes[i]
    r.neighbors(flags='c', input=aoi_dem, output=output_name, method='range',
                size=window_size)
    
    #return i+2
num_cores = 4

results = Parallel(n_jobs=num_cores, verbose=11)(delayed(calc_local_relief)(i) for i in indices)
print(results)
#100 m local relief
#c flag is for a circular rather than square moving window
#size is neighborhood size in number of cells so 21 = 10 cells
#on each side summing to 100m radius
#win_size_100m = 21
#output_100m = 'buffered_100m_radius_relief'
#r.neighbors(flags='c', input=aoi_dem, output=output_100m, method='range', 
#            size=win_size_100m)
#
##1 km local relief
##window is 201, 100 cell radius x 10m for 1 km
#win_size_1km = 201
#output_1km = 'buffered_1km_radius_relief'
#r.neighbors(flags='c', input=aoi_dem, output=output_1km, method='range', 
#            size=win_size_1km)
#
##2.5 km local relief
##window is 501, 250 cell radius x 10m for 2.5 km
#win_size_2point5km = 501
#output_2point5km = 'buffered_2point5km_radius_relief'
#r.neighbors(flags='c', input=aoi_dem, output=output_2point5km, method='range', 
#            size=win_size_2point5km)
#
##5 km local relief
##window is 1001, 500 cell radius x 10m for 5 km
#win_size_5km = 1001
#output_5km = 'buffered_5km_radius_relief'
#r.neighbors(flags='c', input=aoi_dem, output=output_5km, method='range', 
#            size=win_size_5km)
