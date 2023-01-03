# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:46:12 2022

@author: suber

This file tells you how many gumballs you should put in the machine per week
according to the gumball radius and the weekly sales
"""
#imports
from math import pi
from math import ceil
#functions
def find_volume_sphere(radius):
    volume = (4/3) * pi * radius**3
    return volume
def find_volume_cube(side):
    volume = side**3
    return volume
#inputs
radius = input("Enter the gum ball radius (in.) => ")
print(radius)
radius = float(radius)
weekly_sales = input("Enter the weekly sales => ")
print(weekly_sales)
weekly_sales = int(weekly_sales)
#calculate 
#how many gumballs need to fit in machine
need_to_fit = ceil(1.25 * weekly_sales)
#target sales
target = str(need_to_fit)
#gumballs per dimension
per_dimension = ceil(need_to_fit**(1/3))
#find the side length
diameter = radius * 2
side = per_dimension * diameter
#extra gumballs
tot_gumballs = per_dimension**3
extra = ceil(tot_gumballs - need_to_fit)
#finds wasted space
#target wasted space
tot_vol = find_volume_cube(side)
one_gumball = find_volume_sphere(radius)
tot_vol_gumballs = one_gumball * need_to_fit
wasted = tot_vol - tot_vol_gumballs
#full wasted space
full_wasted = wasted - (extra * one_gumball)
#final print statement
print("\nThe machine needs to hold",per_dimension,"gum balls along each edge.")
print("Total edge length is {:.2f}".format(side),"inches.")
print("Target sales were",target+", but the machine will hold",extra,"extra gum balls.")
print("Wasted space is {:.2f}".format(wasted),"cubic inches with the target number of gum balls,")
print("or {:.2f}".format(full_wasted),"cubic inches if you fill up the machine.")
