# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:04:24 2022

@author: suber

This is the bear class for HW8

This class can create the string to print,
see if the bear is still in the grid,
and move the bear
"""

class Bear(object):
    
    def __init__(self, r, c, d):
        #r is the row, c is the column, and d is the direction
        self.r = r
        self.c = c
        self.d = d
        
        #sleep is to see if the bear is alseep
        #turns is to see how many more turns the bear is asleep
        #kill is to see if the bear killed a tourists
        #berries is how many berries the bear has eaten 
        self.sleep = False
        self.turns = 0
        self.kill = False
        self.berries = 0
        
    def __str__(self):
        #creates a string that has the bear, it's location, and the dirrection it is heading
        
        return "Bear at ({},{}) moving {}".format(self.r, self.c, self.d)
    
    def left(self, grid):
        #seeing if the bear is still in the grid
        
        h = len(grid)
        w = len(grid[0])
        
        wl = list(range(0,w))
        hl = list(range(0,h))
        
        if self.r in hl and self.c in wl:
            return True
        else:
            return False
    
    def move(self):
        #this sets the new coord for bear
        
        if self.d == "N":
            self.r -= 1
        
        elif self.d == "NE":
            self.r -= 1
            self.c += 1
        
        elif self.d == "E":
            self.c += 1
        
        elif self.d == "SE":
            self.r += 1   
            self.c += 1
        
        elif self.d == "S":
            self.r += 1
        
        elif self.d == "SW":
            self.r+= 1
            self.c-= 1
        
        elif self.d == "W":
            self.c -= 1  
        
        elif self.d == "NW":
            self.r-= 1
            self.c-= 1
        
        
        


        
