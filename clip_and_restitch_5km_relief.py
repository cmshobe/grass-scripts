#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:57:52 2018

@author: charlie

This script will clip and stitch together the 5 km relief tiles.
This involves clipping the unnecessary overlap for each tile
and then using r.mosaic to put all of them together into one map.
"""
import grass.script as grass
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import raster as r

#store present region
grass.use_temp_region()

#parameters
#n_cells_to_cut = 5000 #m #number of cells to get rid of to cut spurious overlap
output_base_name = '5km_tile'
input_elev_tiles = [output_base_name + '-000-000',
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
input_relief_tiles = ["'000-000_5km_relief'",
                "'000-001_5km_relief'",
                "'001-000_5km_relief'",
                "'001-001_5km_relief'",
                "'001-002_5km_relief'",
                "'001-003_5km_relief'",
                "'002-000_5km_relief'",
                "'002-001_5km_relief'",
                "'002-002_5km_relief'",
                "'002-003_5km_relief'",
                "'003-001_5km_relief'",
                "'003-002_5km_relief'",
                "'003-003_5km_relief'",
                "'004-001_5km_relief'",
                "'004-002_5km_relief'",
                "'004-003_5km_relief'"]

output_relief_tiles = ["'clipped_000-000_5km_relief'",
                "'clipped_000-001_5km_relief'",
                "'clipped_001-000_5km_relief'",
                "'clipped_001-001_5km_relief'",
                "'clipped_001-002_5km_relief'",
                "'clipped_001-003_5km_relief'",
                "'clipped_002-000_5km_relief'",
                "'clipped_002-001_5km_relief'",
                "'clipped_002-002_5km_relief'",
                "'clipped_002-003_5km_relief'",
                "'clipped_003-001_5km_relief'",
                "'clipped_003-002_5km_relief'",
                "'clipped_003-003_5km_relief'",
                "'clipped_004-001_5km_relief'",
                "'clipped_004-002_5km_relief'",
                "'clipped_004-003_5km_relief'"]


for i in range(len(input_elev_tiles)):
    elevation_tile = input_elev_tiles[i]

    #first, set region of the tile of interest to its 2.5 km dem 
    #tile raster
    print('setting region for tile ' + elevation_tile)
    g.region(flags='p', raster=elevation_tile)

    #then, shrink it by 2500 meters on every side
    print('shrinking region for tile '+ elevation_tile + ' to discard overlap')
    g.region(flags='p', n='n-10000', s='s+10000', 
             w='w+10000', e='e-10000')

    #next, export the smaller RELIEF TILE (not the elevation tile)
    #hopefully this will have a size and res matching the comp region
    input_relief_tile_name = input_relief_tiles[i]
    output_relief_tile_name = output_relief_tiles[i]
    mapcalc_expression = output_relief_tile_name + '=' + input_relief_tile_name
    print('exporting relief tile without border: ' + output_relief_tile_name)
    r.mapcalc(expression=mapcalc_expression)

print('16 tiles clipped')

#restore region as it was before script
grass.del_temp_region()
print('Temporary region restored (see below):')
g.region(flags='p')

#finally, mosaic all rasters together to make 5 km window relief map
output_relief_tiles = ['clipped_000-000_5km_relief',
                'clipped_000-001_5km_relief',
                'clipped_001-000_5km_relief',
                'clipped_001-001_5km_relief',
                'clipped_001-002_5km_relief',
                'clipped_001-003_5km_relief',
                'clipped_002-000_5km_relief',
                'clipped_002-001_5km_relief',
                'clipped_002-002_5km_relief',
                'clipped_002-003_5km_relief',
                'clipped_003-001_5km_relief',
                'clipped_003-002_5km_relief',
                'clipped_003-003_5km_relief',
                'clipped_004-001_5km_relief',
                'clipped_004-002_5km_relief',
                'clipped_004-003_5km_relief']

mosaic_name = 'mosaic_5km_relief'

r.patch(input=output_relief_tiles, output=mosaic_name)