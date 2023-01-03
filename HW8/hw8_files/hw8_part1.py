# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:46:26 2022

@author: suber

Part one of Homework 8
"""

import json
import BerryField
import Bear
import Tourist


if __name__ == "__main__":
    #getting file name from user
    file = input("Enter the json file name for the simulation => ")
    #file = "bears_and_berries_1.json"
    print(file)
    
    
    #opening the file and getting the data
    f = open(file)
    data = json.loads(f.read())
    berry_field = (data["berry_field"])
    active_bears = (data["active_bears"])
    reserved_bears =(data["reserve_bears"])
    active_tourists = (data["active_tourists"])
    reserved_tourists = (data["reserve_tourists"])
    
    
    #creating a list for the bears to make the grid
    bears = []
    for i in range(len(active_bears)):
        bears.append(Bear.Bear(active_bears[i][0],active_bears[i][1],active_bears[i][2]))
    
    
    #creating a list for the tourists to make the grid
    tourists = []
    for i in range(len(active_tourists)):
        tourists.append(Tourist.Tourist(active_tourists[i][0],active_tourists[i][1]))
        
    
    #all print statements
    grid = BerryField.BerryField(berry_field, bears, tourists)
    
    #prints out the grid
    print("\nField has {} berries.".format(grid.berry_total()))
    print(grid)
    
    #print bears locations and dirrections
    print("Active Bears:")
    
    for i in range(len(bears)):
        print(bears[i])
        
    #printing the locations of the tourists
    print("\nActive Tourists:")
    
    for i in range(len(tourists)):
        print(tourists[i])
