# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:30:45 2022

@author: suber

This is the class for berry field for HW8

This class creates the string to print and counts all the berries in the field
"""

import copy

class BerryField(object):
    
    def __init__(self, grid, bears, tourists):
        #grid is the grid vales, bears is the list of bears and tourists is the list of tourists
        self.grid = grid
        self.bears = bears
        self.tourists = tourists
        
    def __str__(self):
        #prints a grid from the data given
        
        #making data into array
        l = copy.deepcopy(list(self.grid))
        
        
        #putting bears and tourists into list
        for i in range(len(self.bears)):
            x = self.bears[i].r
            y = self.bears[i].c
            
            l[x][y] = "B"
            
        for i in range(len(self.tourists)):
            x = self.tourists[i].r
            y = self.tourists[i].c
            
            if l[x][y] == "B":
                l[x][y] = "X"
            else:
                l[x][y] = "T"
        
        
        #creating the string
        str1 = ""
        for i in range(len(l)):
            for j in range(len(l[i])):
                str1 += "{:>4}".format(l[i][j])
                
            str1 += "\n"
            
        return str1
            
                        
    def berry_total(self):
        #returns the total amount of berries in the field
        total = 0
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                
                total += self.grid[i][j]
                
        return total
    
    def grow(self):
        #this grows the berry every turn
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                
                if self.grid[i][j] > 0 and self.grid[i][j] < 10:
                    self.grid[i][j] += 1
        
    
    
    def spread(self):
        #this spreads the berries every turn
        
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                
                if self.grid[x][y] == 10:
                    

                    if (y == 0 and x != len(self.grid[x])-1 and x != 0):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x-1][y+1] == 0):
                            self.grid[x-1][y+1] = 1
                        if (self.grid[x+1][y+1] == 0):
                            self.grid[x+1][y+1] = 1
                            
                            
                    if (x == 0 and x != len(self.grid[x])-1 and x != 0):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                        if (self.grid[x+1][y-1] == 0):
                            self.grid[x+1][y-1] = 1
                
                        if (self.grid[x+1][y+1] == 0):
                            self.grid[x+1][y+1] = 1
                            
                            
                    if(x != len(self.grid[x])-1 and x != 0 and  y != len(self.grid[x])-1 and y != 0):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                       
                        if (self.grid[x+1][y-1] == 0):
                            self.grid[x+1][y-1] = 1
                        if (self.grid[x-1][y+1] == 0):
                            self.grid[x-1][y+1] = 1
                        if (self.grid[x+1][y+1] == 0):
                            self.grid[x+1][y+1] = 1
                        if (self.grid[x-1][y-1] == 0):
                            self.grid[x-1][y-1] = 1   
                            
                            
                    if (y == len(self.grid[x])-1 and x != len(self.grid[x])-1 and x != 0):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                        if (self.grid[x+1][y-1] == 0):
                            self.grid[x+1][y-1] = 1
                        if (self.grid[x-1][y-1] == 0):
                            self.grid[x-1][y-1] = 1
                    if (x == len(self.grid[x])-1 and y != len(self.grid[x])-1 and y != 0):
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                        if (self.grid[x-1][y+1] == 0):
                            self.grid[x-1][y+1] = 1
                        if (self.grid[x-1][y-1] == 0):
                            self.grid[x-1][y-1] = 1
                    if (x==0 and y==0):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x+1][y+1] == 0):
                            self.grid[x+1][y+1] = 1
                    if (x == 0 and y == len(self.grid[x])-1):
                        if (self.grid[x+1][y] == 0):
                            self.grid[x+1][y] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                        if (self.grid[x+1][y-1] == 0):
                            self.grid[x+1][y-1] = 1  
                    if (x == len(self.grid[x])-1 and y == 0):
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y+1] == 0):
                            self.grid[x][y+1] = 1
                        if (self.grid[x-1][y+1] == 0):
                            self.grid[x-1][y+1] = 1
                    if (x == len(self.grid[x])-1 and y == len(self.grid[x])-1):
                        if (self.grid[x-1][y] == 0):
                            self.grid[x-1][y] = 1
                        if (self.grid[x][y-1] == 0):
                            self.grid[x][y-1] = 1
                        if (self.grid[x-1][y-1] == 0):
                            self.grid[x-1][y-1] = 1        
                            
                            
    def grid_list(self):
        return list(self.grid)        