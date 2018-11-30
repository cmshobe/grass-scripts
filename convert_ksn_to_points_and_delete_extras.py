#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:39:29 2018

@author: charlie

This script does two main things:
    1) turns the ksn line segments into points (each segment into 3 points)
    2) deletes the excess points such that each line segment is only 
    identified by a single midpoint, which holds the same attribute values
    that the ksn lines held.
"""
import numpy as np
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import vector as v
from grass.pygrass.modules.shortcuts import database as db

#first, use v.to.points to convert ksn segments to points (there will be a
#point at the beginning, middle, and end of each segment)
chan_segs_lines = 'chan_segs_with_litho_proj'
v.to.points(flags='p', input=chan_segs_lines, type='line', dmax=100)

#then, copy chan_segs_points so we keep a pristine version in case we mess up
g.copy(vector='chan_segs_points,chan_segs_points_trimmed')

#then, loop through an iterable, deleting two out of the three
#ksn points for each segment knowing that there are three points for each 
#segment: one has "along"=0, one has "along"=n, and the one we want to keep
#has "along"=n/2

#we use v.edit with the "delete" function
#so I will be selecting the points I want to delete
#THE BELOW LOOP SUCCESSFULLY DELETES ALL ZERO VALUES BUT NOT THE MAXIMA
points_file = 'chan_segs_points'
expression = '"along" = 0'
v.edit(map=points_file, layer=2, type='point', tool='delete',
   where=expression)
    
#NOW NEED A SECOND LOOP TO TAKE CARE OF DELETING THE MAXIMUM VALUES
points_file = 'chan_segs_points'
num_chan_segs = 102318
catlist = []
for chan_seg in range(num_chan_segs):
    lcat = chan_seg + 1 #lcats start at 1, not 0.
    expression_2 = 'SELECT cat,MAX("along") FROM chan_segs_points_2 WHERE "lcat" = ' + str(lcat)
    #use db.select to find the cat of the point I want to delete
    filename = 'sql_out.txt'
    db.select(overwrite=True, sql=expression_2, separator='comma', 
              output=filename) #this will select the point I want to 
    #delete and write it out to line 2 of a csv file. So in Numpy speak
    #the way to access the cat is now [0,0] of that csv as long as the
    #header row is skipped on import.
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    cat = data[0] #this gives me the category I want to delete!!
    catstr = str(int(cat))
    catlist.append(catstr)
    #turn the list into a format v.edit can understand
    catstringall = ",".join(catlist)
    
#now outside the loop, delete 
v.edit(map=points_file, layer=2, type='point', tool='delete',
   cats=catstringall)