# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:26:28 2022

@author: suber
"""

class Tourist(object):
    
    def __init__(self, r, c):
        #r is row, and c is column
        self.r = r
        self.c = c
        
        #killed is if the tourist was killed by bear
        #turns is how many turns they have not seen a bear
        #scared is if they see 3 or more bears at the same time
        #bored is if they have not seen a bear in 3 turns
        self.killed = False
        self.turns = 0
        self.scared = False
        self.bored = False
        
    def __str__(self):
        #makes the string to print the tourists location and how many turns since they have last seen a bear
        
        return "Tourist at ({},{}), {} turns without seeing a bear.".format(self.r, self.c, self.turns)
    
    def last_seen(self,bears):
        
        bear = 0
        for i in range(len(bears)):
            col = bears[i].c - self.c
            col = abs(col)
            
            row = bears[i].r - self.r
            row = abs(row)
            
            #this uses the distance formula to figure out if they are within 4 units of a bear
            dist = ((col**2) + (row**2))**0.5
            
            if dist <= 4:
                bear += 1
                
        return bear