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
"""
import os
import multiprocessing as multi

import grass.script as grass

# Find number of workers that can be used on system. This variable could 
# also be set manually.
aoi_dem = 'cropped_with_buffer'

workers = 4 #multi.cpu_count()
# This is only a set of examples for r.slope.aspect jobs where the maps are
# named serially.
jobs = 4

# Check if workers are already being used
if workers is 1 and "WORKERS" in os.environ:
    workers = int(os.environ["WORKERS"])
if workers < 1:
    workers = 1

# Initialize process dictionary
proc = {}

# Loop over jobs
for i in range(jobs):
    output_names = ['buffered_5km_relief', 
                    'buffered_2point5km_relief', 
                    'buffered_1km_relief', 
                    'buffered_100m_relief']
    window_sizes = [1001, 501, 201, 21]
    output_name = output_names[i]
    window_size = window_sizes[i]
    # Insert job into dictinoary to keep track of it
    proc[i] = grass.start_command('r.neighbors', 
            flags='c', 
            input=aoi_dem, 
            output=output_name, 
            method='range',
            size=window_size)
    print('started a process')
    # If the workers are used up, wait for all of them from the last group to
    # finish.
    #if i % workers is 0:
    #    for j in range(workers):
    #        proc[i - j].wait()

# Make sure all workers are finished.
for i in range(jobs):
    if proc[i].wait() is not 0:
        grass.fatal(('Problem running analysis on evel_' + str(i) + '.'))