# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:45:50 2022

@author: suber

this file asks the user for a grid number, loops until a proper range is inputed, 
and asks the user if they want to print the grid
"""
import hw5_util


#this function returns the neighboring coordinates for the starting values of a grid
def get_nbrs(grid, start):
    rows = len(grid) - 1
    columns = len(grid[0]) - 1
    
    x = start[0]
    y = start[1]
    
    if x < rows and x > 0 and y < columns and y > 0:
        neighbors = "({}, {}) ({}, {}) ({}, {}) ({}, {})".format(x-1, y, x, y-1, x, y+1, x+1, y)
    if x == 0 and y < columns and y > 0:
        neighbors = "({}, {}) ({}, {}) ({}, {})".format(x, y-1, x, y+1, x+1, y)
    if x < rows and x > 0 and y == 0:
        neighbors = "({}, {}) ({}, {}) ({}, {})".format(x, y+1, x+1, y, x-1, y)
    if x < rows and x > 0 and y == columns:
        neighbors = "({}, {}) ({}, {}) ({}, {})".format(x-1, y, x, y-1, x+1, y)
    if x == rows and y < columns and y > 0:
        neighbors = "({}, {}) ({}, {}) ({}, {})".format(x-1, y, x, y-1, x, y+1)
    if x == 0 and y == 0:
        neighbors = "({}, {}) ({}, {})".format(x, y+1, x+1, y)
    if x == 0 and y == columns:
        neighbors = "({}, {}) ({}, {})".format(x, y-1, x+1, y)
    if x == rows and y == columns:
        neighbors = "({}, {}) ({}, {})".format(x-1, y, x, y-1)
    if x == rows and y == 0:
        neighbors = "({}, {}) ({}, {})".format(x-1, y, x, y+1)
    
        
    return neighbors

#this function takes a lists of lists and prints it in a formated grid
def format_grid(l):
    for lists in l:
        for i in lists:
            if len(str(i)) == 2:
                print("  "+str(i),end='')
            elif len(str(i)) == 1:
                print("   "+str(i),end='')
        print()
         
#inputs for the grid index and if the user wants the grid to be print or not
n = input("Enter a grid index less than or equal to 3 (0 to end): ")
print(n)
n = int(n)

#loops until an index in range is inputed
i = 1
while i == 1:  
    if n <= 0:
        n = input("Enter a grid index less than or equal to 3 (0 to end): ")
        print(n)
        n = int(n)
    elif n > 3:
        n = input("Enter a grid index less than or equal to 3 (0 to end): ")
        print(n)
        n = int(n)
    else: 
        i = 2

#if the user inputs y then the grid is printed     
printed = input("Should the grid be printed (Y or N): ")
print(printed)
printed = printed.lower()

#assigning grid values
grid = hw5_util.get_grid(n)
rows = len(grid)
columns = len(grid[0])

#printing the grid if the user inputs y
if printed == 'y':
    print("Grid {}".format(n))
    format_grid(grid)
#prints how many rows and columns are in the grid    
print("Grid has {} rows and {} columns".format(rows, columns))

#getting starting location coordinates
start = hw5_util.get_start_locations(n)
#prints starting location coordinates and neighboring points
for i in range(len(start)):
    
    print("Neighbors of {}: {}".format(start[i], get_nbrs(grid, start[i])))

#printing out the path     
path = hw5_util.get_path(n)

grid_path = []
#adds all numbers in path to list grid_path
for i in range(len(path)):
    grid_path.append(grid[path[i][0]][path[i][1]])
    
upward = 0
downward = 0
#finds values for upward and downward 
for i in range(len(grid_path) - 1):
    if grid_path[i] < grid_path[i+1]:
        upward += grid_path[i+1] - grid_path[i]
    if grid_path[i] > grid_path[i+1]:
        downward += grid_path[i] - grid_path[i+1]
#finding if the path is valid if the count is 0 then path is valid
count = 0
index = []
for i in range(len(path) - 1):
    x1 = path[i][0]
    x2 = path[i + 1][0]
    y1 = path[i][1]
    y2 = path[i + 1][1]
    
    if x1 == x2:
        if y1 == (y2 + 1):
            count += 0
        elif y1 == (y2 -1):
            count += 0
        elif y1 == y2:
            count += 0
    elif y1 == y2:
        if x1 == (x2 + 1):
            count += 0
        elif x1 == (x2 -1):
            count += 0
        elif x1 == x2:
            count += 0
    else:
        count += 1
        index.append(i)
#printing if path is valid or not if it is valid upward and downward movement is printed as well
if count == 0:
    print("Valid path")
    print("Downward {}".format(downward))
    print("Upward {}".format(upward))
else:
    n = index[0]
    x = path[n][0]
    x1 = path[n+1][0]
    y = path[n][1]
    y1 = path[n+1][0]
    print("Path: invalid step from ({}, {}) to ({}, {})".format(x,y,x1,y1))
    