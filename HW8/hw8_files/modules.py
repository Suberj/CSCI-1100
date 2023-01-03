# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:53:06 2022

@author: suber

This is the berry class module for homework 8
"""

import copy

class berry_field(object):
    
    def __init__(self, grid, bL, tL):
        self.grid = grid
        self.original = copy.deepcopy(grid)
        self.bL = bL
        self.tL = tL
    
    #prints out the berry data into a grid
    def __str__(self):
        
        #putting bears in list
        for i in range(len(self.bL)):
            self.grid[self.bL[i][0]][self.bL[i][1]] = "B"
        
        #putting tourist in list
        for i in range(len(self.tL)):
            if self.grid[self.tL[i][0]][self.tL[i][1]] != "B":
                self.grid[self.tL[i][0]][self.tL[i][1]] = "T"
            else:
                self.grid[self.tL[i][0]][self.tL[i][1]] = "X"
                    
        #creating list of strings for final grid to be printed
        final_grid = []
            
        for i in range(len(self.grid)):
            str1 = "   "
            for j in range(len(self.grid[i])):
                if len(str(self.grid[i][j])) == 1:
                    str1 = str1 + str(self.grid[i][j]) + "   "
                else:
                    str1 = str1 + str(self.grid[i][j]) + "  "
            final_grid.append(str1.rstrip())
        
        #printing
        for i in range(len(final_grid)-1):
            print(final_grid[i])
        return final_grid[-1]
    
    #way to grow berries
    def grow(self):
        
        for i in range(len(self.grid)):
            
            for j in range(len(self.grid[i])):
                
                if self.grid[i][j] >= 1 and self.grid[i][j] < 10:
                    self.grid[i][j] += 1
                    
        return self.grid
    
    #allows berries to spread
    def spread(self):
        
        #finding adjacent indices
        #i and j are the indices of the point, r is the tot rows and c is the tot columns
        def get_adjacent_indices(i, j, r, c):
            adjacent_indices = []
            if i > 0:
                adjacent_indices.append([i-1,j])
            if i+1 < r:
                adjacent_indices.append([i+1,j])
            if j > 0:
                adjacent_indices.append([i,j-1])
            if j+1 < c:
                adjacent_indices.append([i,j+1])
            return adjacent_indices
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                
                if self.grid[i][j] == 0:
                    adj_ind = get_adjacent_indices(i, j, len(self.grid), len(self.grid[i]))
                    
                    for k in range(len(adj_ind)):
                        x = int(adj_ind[k][0])
                        y = int(adj_ind[k][1])
                       
                        
                        if self.grid[x][y] == 10:
                            self.grid[i][j] = 1
                            
                            continue
        return self.grid
    
    def original(self):
        return self.original
                        
                
                            
                   
                        
                        
                        
 
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:53:18 2022

@author: suber

This is the bear class module for hw 8 
"""

class bear(object):
    
    #r is row, c is column, and d is direction
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        
    
    #prints out the location of the bear and the dirrection it is traveling
    def __str__(self):
        return "Bear at ({},{}) moving {}".format(self.r, self.c, self.d)
    
    #eats berries till it is full
    def eat(self, grid):
   
        eat_count = 0
        
        while eat_count <= 30:
                
            berry_amount = grid[self.r][self.c]
                
            if eat_count + berry_amount <= 30:
                eat_count += berry_amount
                grid[self.r][self.c] = 0
                
                return True
                    
            else:
                rest = 30 - eat_count
                eat_count = 30
                berry_amount = berry_amount - rest
                grid[self.r][self.c] = berry_amount
                
                return False
                    
    def alseep(self, t_loc):
        
        return [self.r,self.c] in t_loc
        
    
                
    def move(self, grid):
        #moving the bear
        if self.d == 'N' and self.r > 0:
            self.r -= 1
            
        elif self.d == 'S' and self.r < len(grid):
            self.r += 1
            
        elif self.d == 'E' and self.c < len(grid[0]):
            self.c += 1
            
        elif self.d == 'W' and self.c > 0:
            self.c -= 1
            
        elif self.d == 'NE' and self.c < len(grid[0]) and self.r > 0:
            self.c += 1
            self.r -= 1
            
        elif self.d == 'NW' and self.c > 0 and self.r > 0:
            self.c -= 1
            self.r -= 1
            
        elif self.d == 'SE' and self.c < len(grid[0]) and self.r < len(grid):
            self.c += 1
            self.r += 1
            
        elif self.d == 'SW' and self.c > 0 and self.r < len(grid):
            self.c -= 1
            self.r += 1
            
    #gets bears coordinates
    def coords(self):
        return [self.r,self.c]

    
            



# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:53:28 2022

@author: suber

This is the tourist class module for HW8
"""

class tourist(object):
    
    #r is row and c is column and bL is the bear list
    def __init__(self, r, c, bL):
        self.r = r
        self.c = c
        self.bL = bL
        self.turn = 0
        self.leave = False
    
    def seen(self):
        for i in range(len(self.bL)):
            bx = self.bL[i][0]
            by = self.bL[i][1]
            if self.r + 4 >= bx and self.r - 4 <= bx and self.c + 4 >= by and self.r - 4 <= bx:
                
                return True
            
        
    def __str__(self):
        
        if not self.seen():
            count = self.turn
            self.turn += 1
        else:
            count = 0
        return "Tourist at ({},{}), {} turns without seeing a bear.".format(self.r, self.c, count)
    
    def leave(self):
        pass
        
        
    
    
        