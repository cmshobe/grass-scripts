#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:57:29 2018

@author: charlie

create watersheds from pour point shapefile 'cleaned_pour_points'
"""
import numpy as np
from grass.pygrass.modules.shortcuts import vector as v

#first, export all pour points to ascii file  to be read in for wshed creation

cleaned_pour_points = 'cleaned_pour_points'
out_file = 'cleaned_pour_points.csv'

v.out.ascii(input=cleaned_pour_points, layer=1, type='point', 
            output=out_file, format='point', separator=',')

#now, loop through those pour points and create a watershed for each one
