# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:54:28 2022

@author: suber
"""

import hw5_util


"""given the grid and the coordinate this function finds
all of the neighboring coordincates and returns them """
def get_nbrs(grid, start):
    rows = len(grid) - 1
    columns = len(grid[0]) - 1
    
    x = start[0]
    y = start[1]
    
    if x < rows and x > 0 and y < columns and y > 0:
        neighbors = [(x-1,y),(x,y-1),(x,y+1),(x+1,y)]
    if x == 0 and y < columns and y > 0:
        neighbors = neighbors = [(x,y-1),(x,y+1),(x+1,y)]
    if x < rows and x > 0 and y == 0:
        neighbors = neighbors = [(x,y+1),(x+1,y),(x-1,y)]
    if x < rows and x > 0 and y == columns:
        neighbors = [(x-1,y),(x,y-1),(x+1,y)]
    if x == rows and y < columns and y > 0:
        neighbors = [(x-1,y),(x,y-1),(x,y+1)]
    if x == 0 and y == 0:
        neighbors = [(x,y+1),(x+1,y)]
    if x == 0 and y == columns:
        neighbors = [(x,y-1),(x+1,y)]
    if x == rows and y == columns:
        neighbors = [(x-1,y),(x,y-1)]
    if x == rows and y == 0:
        neighbors = [(x-1,y),(x,y+1)]
        
    return neighbors

"""given a list of lists this function returns them printed in
a grid"""
def format_grid(l):
    for lists in l:
        for i in lists:
            if len(str(i)) == 2:
                print("  "+str(i),end='')
            elif len(str(i)) == 1:
                print("   "+str(i),end='')
        print()
        
    
"""given a grid this function finds the global max
it returns the global max, and the coordinate of the global max"""
def global_max(grid):
    max_values = []
    #adds all the max values of each list inside grid to max_values
    for i in range(len(grid)):
        max_values.append(max(grid[i]))
    #finds the global max
    g_max = max(max_values)
    #finding the first index values for the global max
    index = 0
    for i in range(len(max_values)):
        if max_values[i] == g_max:
            index = i
    #finding the second index value for the global max
    for i in range(len(grid[index])):
        if grid[index][i] == g_max:
            index1 = i
    return (index,index1,g_max)
    

""" given a list of coordinates this function finds the values assosiated with 
the points in the grid"""
def nbr_values(nb):
    #nb = get_nbrs(grid, start)
    path = []
    for i in range(len(nb)):
        path.append(grid[nb[i][0]][nb[i][1]])
    return path
    
"""given a coordinate, the number grid, the step height, and the global max this function 
will find the steepest path from that coordinate untill it either gets to the global max or 
cannot move anymore"""
def steepest(start, n, max_height, g_max):
    count = 0
    
    nb = get_nbrs(grid, start)
    num = nbr_values(nb)
    location = start
    location_value = grid[location[0]][location[1]]
    nums = []
    path = []
    
    path.append(start)
    
    j = 0
    while j == 0:
    
        for i in range(len(num)):
            if num[i] < location_value:
                count += 1
            elif num[i] > location_value + max_height:
                count += 1
            else:
                nums.append(num[i])
        
        if len(nums) == 0:
            j = 1
        else:    
            location_value = max(nums)    
            location = nb[num.index(max(nums))]
            path.append(location)
        
            nb = get_nbrs(grid, location) 
            num = nbr_values(nb)
            nums = []
      
        if location_value == g_max:
            j = 1
      
    return path

"""given a coordinate, the number grid, the step height, and the global max this function 
will find the gradual path from that coordinate untill it either gets to the global max or 
cannot move anymore"""
def gradual(start, n, max_height, g_max):
    count = 0
    
    nb = get_nbrs(grid, start)
    num = nbr_values(nb)
    location = start
    location_value = grid[location[0]][location[1]]
    nums = []
    path = []
    
    path.append(start)
    
    j = 0
    while j == 0:
    
        for i in range(len(num)):
            if num[i] <= location_value:
                count += 1
            elif num[i] > location_value + max_height:
                count += 1
            else:
                nums.append(num[i])
        
        if len(nums) == 0:
            j = 1

        else:    
            location_value = min(nums)    
            location = nb[num.index(min(nums))]
            path.append(location)
        
            nb = get_nbrs(grid, location) 
            num = nbr_values(nb)
            nums = []
      
        if location_value == g_max:
            j = 1
            
        if len(path) == 12:
            j = 1
       
    return path


#functions end here  
        
#inputs for the grid index and if the user wants the grid to be print or not
n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
print(n)
n = int(n)

#loops until an index in range is inputed
i = 1
while i == 1:  
    if n <= 0:
        n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
        print(n)
        n = int(n)
    elif n > 3:
        n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
        print(n)
        n = int(n)
    else: 
        i = 2

#this takes the number, n, inputed by the user and gets the grid corresponding to that number
grid = hw5_util.get_grid(n)
rows = len(grid)
columns = len(grid[0])

#has the user input a maximum step height that will be used when making the path
step_height = input("Enter the maximum step height: ").strip()
print(step_height)
step_height = int(step_height)

#asks the users if the want the path grid to be printed(will be used later)
grid_printed = input("Should the path grid be printed (Y or N): ").strip()
print(grid_printed)

#prints how many rows and columns are in the grid    
print("Grid has {} rows and {} columns".format(rows, columns))

#this assigns g_max to the max value of the grid, as well as the location of the global max in the grid
g_max = global_max(grid)    
print("global max: ({}, {}) {}".format(g_max[0],g_max[1],g_max[2]))


#assigns start to the starting locations of the grid
start = hw5_util.get_start_locations(n)


plot = []
"""This loops prints all of the paths out and tells the user if it ends
at a global max, a local max, or neither.
Also this appends every point in every path to the array 'plot' which will
be used later when ploting how many times all the paths went through each point
This is the bulk of the program and is where most of the output comes from."""
for i in range(len(start)):
   
   print('===')
   print('steepest path')
   
   #print the coords in a line of 5
   string1 = ''
   for j in range(len(steepest(start[i], n, step_height, g_max))):
       plot.append(steepest(start[i], n, step_height, g_max)[j])
       if j % 4 != 0 or j == 0:
           string1 = string1 + str(steepest(start[i], n, step_height, g_max)[j]) + ' '
       elif j % 4 == 0 and j != 0: 
           string1 = string1 + str(steepest(start[i], n, step_height, g_max)[j]) + ' \n'    
   string1 = string1.rstrip('\n')           
   print(string1)  
   
   #finds if the ending point is global, local max or niether
   if str(steepest(start[i], n, step_height, g_max)[-1]) == '({}, {})'.format(g_max[0], g_max[1]):
       print('global maximum')
   elif grid[steepest(start[i], n, step_height, g_max)[-1][0]][steepest(start[i], n, step_height, g_max)[-1][1]] >= max(nbr_values(get_nbrs(grid, steepest(start[i], n, step_height, g_max)[-1]))):
       print('local maximum')
   else:
       print('no maximum')
   print('...')
   
   print('most gradual path')
   
   #prints the coords in a line of 5
   string2 = ''
   for k in range(len(gradual(start[i], n, step_height, g_max))):
       plot.append(gradual(start[i], n, step_height, g_max)[k])
       if k % 4 != 0 or k == 0:
           string2 = string2 + str(gradual(start[i], n, step_height, g_max)[k]) + ' '
       elif k % 4 == 0 and k != 0:  
           string2 = string2 + str(gradual(start[i], n, step_height, g_max)[k]) + ' \n'
   string2 = string2.rstrip('\n')       
   print(string2)    
   
   #finds if the ending point is global, local max or niether
   if str(gradual(start[i], n, step_height, g_max)[-1]) == '({}, {})'.format(g_max[0], g_max[1]):
       print('global maximum')
   elif grid[gradual(start[i], n, step_height, g_max)[-1][0]][gradual(start[i], n, step_height, g_max)[-1][1]] >= max(nbr_values(get_nbrs(grid, gradual(start[i], n, step_height, g_max)[-1]))):
       print('local maximum')
   else:
       print('no maximum')     
print('===')


#makes a grid that shows how many times each point was gone over in every path
plot_grid = []
plot_grid.append(columns)
count = 0
#adds count of all coordinates to plot
for i in range(rows):
    for j in range(columns):
        plot_grid.append(plot.count((i, j)))
#if it is zero replaces it with .        
for i in range(len(plot_grid)):
    if plot_grid[i] == 0:
        plot_grid[i] = '.' 
#plots the values in a grid        
plot = ''
for i in range(len(plot_grid)):
    if i % (columns) != 0:
        plot = plot + "  " + str(plot_grid[i])
    elif i % (columns) == 0 and i != 0:
        plot = plot + "  " + str(plot_grid[i]) + '\n' 
    else:
        count += 0
        
plot = plot.rstrip('\n')    

#if the user wanted the grid to be ploted then this prints out the grid
if grid_printed == 'y':
    print("Path grid")
    print(plot)