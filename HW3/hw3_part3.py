# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:43:33 2022

@author: suber

This module simulates the population of bears each year based on the tourist 
population, and berries
"""
import math

#function that shows the bear and berry population every year
def find_next(bears, berries, tourists):
    bears_next = berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)
    bears_next = int(bears_next)
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - \
        (math.log(1+tourists,10)*0.05)
    #makes negatives 0
    if bears_next < 0:
        bears_next = 0
    if berries_next < 0:
        berries_next = 0
    return (bears_next, berries_next)
    

#inputs for the number of bears and size of berry area
bears = input("Number of bears => ").strip()
print(bears)
bears = int(bears)
berries = input("Size of berry area => ").strip()
print(berries)
berries = float(berries)

#list for min/max
bear_list = []
berry_list = []
tourist_list = []

#determine the starting number of tourist
if bears < 4 or bears > 15:
     tourists = 0
else:
     if bears < 10:
         tourists = 10000 * bears
     if bears > 10:
         tourists = (10000 * 10) + (20000 * (bears - 10))
     
#adding all values to lists to be used later for max/min
bear_list.append(bears)
berry_list.append(round(berries,1))
tourist_list.append(tourists)
    
#labels
print("Year      Bears     Berry     Tourists")

#finding all of the values
i = 1
while i <= 10: 
    
    #finding spacing and printing line
    space1 = " " * (10 - len(str(i)))
    space2 = " " * (10 - len(str(bears)))
    space3 = " " * (10 - len("{:.1f}".format(berries)))
    print(str(i)+space1+str(bears)+space2+"{:.1f}".format(berries)+space3+str(tourists))
    
    #adding all values to lists to be used later for max/min
    bear_list.append(bears)
    berry_list.append(round(berries,1))
    tourist_list.append(tourists)
    
    #finding pop for 10 years
    population = find_next(bears, berries, tourists)
    
    #setting new vales for next loop
    bears = population[0]
    berries = population[1]
    
    #determine the number of tourists
    if bears < 4 or bears > 15:
        tourists = 0
    else:
        if bears < 10:
            tourists = 10000 * bears
        if bears > 10:
            tourists = (10000 * 10) + (20000 * (bears - 10))
        
    i += 1
    
#printing min/max
print("\nMin:      "+str(min(bear_list))+(" " * (10 - len(str(min(bear_list)))))+str(min(berry_list))+(" " * (10 - len(str(min(berry_list)))))+str(min(tourist_list)))
print("Max:      "+str(max(bear_list))+(" " * (10 - len(str(max(bear_list)))))+str(max(berry_list))+(" " * (10 - len(str(max(berry_list)))))+str(max(tourist_list)))
