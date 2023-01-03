# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:46:26 2022

@author: suber

Part two of Homework 8
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
    print("\nStarting Configuration")
    print("Field has {} berries.".format(grid.berry_total()))
    print(grid)
    
    #print bears locations and dirrections
    print("Active Bears:")
    
    for i in range(len(bears)):
        print(bears[i])
        
    #printing the locations of the tourists
    print("\nActive Tourists:")
    
    for i in range(len(tourists)):
        print(tourists[i])
    
    
    """
    This is where part two starts
    The code aboove is the initial state from part one
    """
    
    
    for i in range(5):
        print("\nTurn: {}".format(i+1))
        
        """
        This section deals with the tourists that are killed or left
        
        It finds the tourists, prints them out, and then removes them from the list
        """
        #killed
        #num_left is to make it so I can remove the tourists without messing the loop up
        num_left = 0
        for j in range(len(tourists)):
            for k in range(len(bears)):
                
                if tourists[j - num_left].r == bears[k].r and tourists[j - num_left].c == bears[k].c:
                    bears[k].kill = True
                    
                    print(tourists[j - num_left],"- Left the Field")
                    
                    tourists.remove(tourists[j - num_left])
                    num_left += 1
                    
        
        """
        This section deals with moving the bears around
        
        It sees if the bears are asleep, moves the bears, 
        has them eat berries and tourists, and sees if they leave the grid
        """
        
        #finding bears that leave
        num_left = 0
        for j in range(len(bears)):
            
            if bears[j - num_left].left(grid.grid_list()) == False:
                print(bears[j - num_left],"- Left the Field")
            
                bears.remove(bears[j - num_left])
                num_left += 1
         
        #finding bears that are asleep        
        for j in range(len(bears)):
            
            if bears[j].kill == True:
                bears[j].sleep = True
                bears[j].turns = 4
                bears[j].kill = False
                
            if bears[j].sleep == True:
                bears[j].turns -= 1
                
            if bears[j].turns == 0:
                bears[j].sleep = False
                
        #growing and spreading berries
        grid.grow()
        grid.spread()
        
        #moving the bears and having them eat
        for j in range(len(bears)):
            
            if bears[j].sleep == False and bears[j].left(grid.grid_list()) == True:
                
                bears[j].berries = 0
                while True:
                    
                    bears[j].berries += grid.grid_list()[bears[j].r][bears[j].c]
                    grid.grid_list()[bears[j].r][bears[j].c] = 0
                    bears[j].move()
                    
                    #checking if tourists got killed
                    for k in range(len((tourists))):
                        if bears[j].r == tourists[k].r and bears[j].c == tourists[k].c:
                            tourists[k].killed = True
                            bears[j].kill = True
                            break
                    
                    #checking if bear left the grid
                    if bears[j].left(grid.grid_list()) == False:
                        break
                    
                    #bear eats the berries
                    bears[j].berries += grid.grid_list()[bears[j].r][bears[j].c]
                    grid.grid_list()[bears[j].r][bears[j].c] = 0
                    
                    #if bear eats over 30 berries
                    if bears[j].berries >= 30:
                        grid.grid_list()[bears[j].r][bears[j].c] = bears[j].berries - 30
                        break
                    
                    
        #seeing if bear killed tourist on the final turn
        for k in range(len(bears)):
            for j in range(len(tourists)):
                
                if tourists[j - num_left].r == bears[k].r and tourists[j - num_left].c == bears[k].c:
                    bears[k].kill = True
                    
                    print(tourists[j - num_left],"- Left the Field")
                    
                    tourists.remove(tourists[j - num_left])
                    num_left += 1
                 
                    grid.grid_list()[bears[k].r][bears[k].c] = 10    
                 
        #finding bears that are asleep        
        for j in range(len(bears)):
            
            if bears[j].kill == True:
                bears[j].sleep = True
                bears[j].kill = False
            
            if i == 4:
                if bears[j].sleep == True:
                    bears[j].turns = 3
            
            if bears[j].turns == 0:
                bears[j].sleep = False
                
        #finding bears that leave
        num_left = 0
        for j in range(len(bears)):
            
            if not bears[j - num_left].left(grid.grid_list()):
                print(bears[j - num_left],"- Left the Field")
            
                bears.remove(bears[j - num_left])
                num_left += 1
        
        #scared and bored
        num_left = 0
        for j in range(len(tourists)):
            count = tourists[j - num_left].last_seen(bears)
            if count == 0:
                tourists[j - num_left].turns += 1
            
            if count >= 3:
                print(tourists[j - num_left],"- Left the Field")
                
                tourists.remove(tourists[j - num_left])
                num_left += 1   
            
            if tourists[j - num_left].turns >= 3:
                print(tourists[j - num_left],"- Left the Field")
                
                tourists.remove(tourists[j - num_left])
                num_left += 1    
        
                
        #prints new grid
        print("Field has {} berries.".format(grid.berry_total()))
        print(grid)
    
        #print bears locations and dirrections
        print("Active Bears:")
    
        for j in range(len(bears)):
            
            if bears[j].sleep == False or bears[j].turns == 1:
                print(bears[j])
                
            else:
                print(bears[j],"- Asleep for {} more turns".format(bears[j].turns - 1))
                    
            
        #printing the locations of the tourists
        print("\nActive Tourists:")
    
        for j in range(len(tourists)):
            print(tourists[j])
    
        print("")        
            
            
            
            
            
            
    
            
    
