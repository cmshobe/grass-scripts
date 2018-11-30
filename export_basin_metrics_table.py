#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:35:44 2018

@author: charlie

Script to export study subcatchment attribute table to .csv
"""
from grass.pygrass.modules.shortcuts import database as db

basins = 'all_unique_wsheds_info'
csv_name = 'basins_data.csv'

db.out_ogr(input=basins, output=csv_name)
