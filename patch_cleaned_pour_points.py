#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:34:58 2018

@author: charlie

patch together the cleaned pour points from the 38 subcatchments into one pour 
points vector.
"""

from grass.pygrass.modules.shortcuts import vector as v

file_names = ['subcatchment_1_pour_points',
              'subcatchment_2_pour_points',
              'subcatchment_3_pour_points',
              'subcatchment_4_pour_points',
              'subcatchment_5_pour_points',
              'subcatchment_6_pour_points',
              'subcatchment_7_pour_points',
              'subcatchment_8_pour_points',
              'subcatchment_9_pour_points',
              'subcatchment_10_pour_points',
              'subcatchment_11_pour_points',
              'subcatchment_12_pour_points',
              'subcatchment_13_pour_points',
              'subcatchment_14_pour_points',
              'subcatchment_15_pour_points',
              'subcatchment_16_pour_points',
              'subcatchment_17_pour_points',
              'subcatchment_18_pour_points',
              'subcatchment_19_pour_points',
              'subcatchment_20_pour_points',
              'subcatchment_21_pour_points',
              'subcatchment_22_pour_points',
              'subcatchment_23_pour_points',
              'subcatchment_24_pour_points',
              'subcatchment_25_pour_points',
              'subcatchment_26_pour_points',
              'subcatchment_27_pour_points',
              'subcatchment_28_pour_points',
              'subcatchment_29_pour_points',
              'subcatchment_30_pour_points',
              'subcatchment_31_pour_points',
              'subcatchment_32_pour_points',
              'subcatchment_33_pour_points',
              'subcatchment_34_pour_points',
              'subcatchment_35_pour_points',
              'subcatchment_36_pour_points',
              'subcatchment_37_pour_points',
              'subcatchment_38_pour_points',]
output_file_name = 'cleaned_pour_points'

v.patch(flags='ne', input=file_names, output=output_file_name)
v.build(map=output_file_name)
