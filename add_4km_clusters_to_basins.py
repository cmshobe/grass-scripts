#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:09:36 2019

@author: charlie

add column for 4km pour point clustering and populate each 
row (basin) with its cluster value
"""
import numpy as np
from grass.pygrass.modules.shortcuts import vector as v
basins_map = 'all_unique_wsheds_info'
col_to_add = 'cluster_number_4km INT'
col_name = 'cluster_number_4km'
v.db_addcolumn(map = basins_map, layer = 1, 
               columns = col_to_add)

keys = np.zeros((344, 2)) #first column will hold basin 'value',

#IMPORTANT STEP: I NEED TO POPULATE THIS ARRAY MANUALLY BECAUSE
#OF SMALL INCONSISTENCIES IN THE RELATIVE POSITION OF BASINS
#AND THEIR POUR POINTS. 

#So we go through each basin 'value' from 0-343 and get the cluster
#number for each basin
clusters = [0,
            53,
            53,
            53,
            53,
            60,
            60,
            60,
            60,
            50,
            50,
            10,
            10,
            3,
            3,
            3,
            3,
            0,
            0,
            26,
            26,
            0,
            27,
            27,
            0,
            51,
            51,
            51,
            78,
            78,
            76,
            76,
            46,
            46,
            47,
            47,
            47,
            0,
            0,
            0,
            79,
            79,
            79,
            79,
            79,
            79,
            79,
            79,
            79,
            37,
            37,
            37,
            29,
            29,
            28,
            28,
            0,
            81,
            81,
            81,
            81,
            81,
            0,
            12,
            12,
            12,
            12,
            54,
            63,
            63,
            59,
            59,
            59,
            59,
            35,
            35,
            31,
            31,
            30,
            30,
            0,
            0,
            83,
            83,
            84,
            84,
            84,
            84,
            0,
            52,
            52,
            82,
            82,
            82,
            39,
            39,
            0,
            0,
            38,
            38,
            36,
            36,
            69,
            69,
            64,
            64,
            64,
            64,
            65,
            65,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            0,
            14,
            14,
            13,
            13,
            0,
            11,
            11,
            11,
            11,
            11,
            89,
            89,
            89,
            89,
            0,
            90,
            90,
            90,
            87,
            87,
            0,
            16,
            16,
            16,
            18,
            18,
            19,
            19,
            17,
            17,
            20,
            91,
            91,
            0,
            20,
            0,
            0,
            88,
            88,
            71,
            71,
            71,
            70,
            70,
            70,
            75,
            75,
            73,
            73,
            73,
            73,
            75,
            75,
            0,
            86,
            85,
            85,
            86,
            85,
            85,
            85,
            85,
            79,
            79,
            0,
            79,
            79,
            0,
            0,
            0,
            80,
            80,
            80,
            0,
            79,
            79,
            0,
            0,
            9,
            0,
            9,
            0,
            0,
            4,
            4,
            7,
            7,
            7,
            4,
            0,
            5,
            5,
            15,
            5,
            15,
            6,
            6,
            0,
            92,
            92,
            92,
            0,
            0,
            93,
            93,
            93,
            93,
            93,
            93,
            93,
            0,
            0,
            33,
            34,
            33,
            34,
            0,
            0,
            0,
            0,
            56,
            56,
            61,
            61,
            0,
            72,
            72,
            32,
            32,
            32,
            0,
            0,
            25,
            25,
            24,
            24,
            0,
            8,
            8,
            8,
            8,
            2,
            2,
            74,
            74,
            69,
            69,
            0,
            68,
            68,
            68,
            0,
            68,
            68,
            0,
            66,
            66,
            66,
            67,
            67,
            67,
            67,
            42,
            42,
            0,
            41,
            41,
            45,
            45,
            45,
            45,
            45,
            0,
            0,
            0,
            48,
            48,
            48,
            48,
            22,
            22,
            22,
            22,
            22,
            23,
            23,
            23,
            0,
            0,
            0,
            21,
            21,
            21,
            0,
            0,
            44,
            44,
            40,
            44,
            40,
            40,
            0,
            43,
            43,
            43,
            43,
            0,
            49,
            49,
            54,
            54,
            54,
            54,
            55,
            55,
            0,
            55,
            58,
            58,
            0,
            57,
            57,
            77,
            77,
            62,
            62
            ]

#second column will hold associated cluster number
keys[:, 0] = range(344) #populate first column [0:343]
keys[:, 1] = clusters
for j in range(344):
    i = int(j)
    expression = '"value"=' + str(keys[i, 0]) #access a single basin
    v.db_update(map = basins_map, 
                layer = 1,
                column = col_name,
                value = str(keys[i, 1]),
                where = expression)

from grass.pygrass.modules.shortcuts import database as db    
csv_name = 'basins_data_with_intra_relief_and_4km_clusters.csv'
db.out_ogr(input=basins_map, output=csv_name)
