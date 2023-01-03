# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:09:10 2022

@author: suber

This module allows you to move pikachu around and fight pokemon
"""
#function that is used to move pikachu
def move_pokemon(position_tuple, direction, steps):
    row, column = position_tuple
    
    #used for moving pikachu
    if direction.upper() == 'N':
        new_posistion = (row - steps,column)
    elif direction.upper() == 'S':
        new_posistion = (row + steps,column)
    elif direction.upper() == 'W':
        new_posistion = (row,column - steps)   
    elif direction.upper() == 'E':
        new_posistion = (row,column + steps)
    else:
        new_posistion = (row, column)
    return new_posistion

#inputs to get number of turns, name, and how ofter you see pokemon
turns = input("How many turns? => ").strip()
print(turns)
turns = int(turns)
name = input("What is the name of your pikachu? => ").strip()
print(name)
battle = input("How often do we see a Pokemon (turns)? => ").strip()
print(battle)
battle = int(battle)

#sets the starting location and win/loss list
position = (75,75)
new_row, new_column = position
Win_Loss = []
    
#inital print statement to start the simution
print("\nStarting simulation, turn 0 {} at ({}, {})".format(name,new_row,new_column))
#while loop that allows you to move pikachu and battle
i = 1
while i < turns + 1:
    direction = input("What direction does {} walk? => ".format(name)).strip()
    print(direction)
    
    #changing position for next time through the loop
    position = (new_row,new_column)
    new_row, new_column = move_pokemon(position, direction, 5) 
    
    #boundries
    if new_row > 150:
        new_row = 150
    elif new_column > 150:
        new_column = 150
    elif new_row < 0:
        new_row = 0
    elif new_column < 0:
        new_column = 0
        
    #this controls the battle portion of the code
    if i % battle == 0: #this makes it so the loop does not work unless it is a multiple of battle
        print("Turn {}, {} at ({}, {})".format(i,name,new_row,new_column))
        pokemon = input("What type of pokemon do you meet (W)ater, (G)round? => ").strip()
        print(pokemon)
        direction = direction.upper()
        #this changes the position based on the users input
        if pokemon.upper() == 'G':
            #moves pikachu in 10 steps in the opposite direction it was headed
            if direction == 'N':
                new_row = new_row + 10
            elif direction == 'S':
                new_row = new_row - 10
            elif direction == 'W':
                new_column = new_column + 10
            elif direction == 'E':
                new_column = new_column - 10
                
            #boundries
            if new_row > 150:
                new_row = 150
            elif new_column > 150:
                new_column = 150
            elif new_row < 0:
                new_row = 0
            elif new_column < 0:
                new_column = 0    
                
            Win_Loss.append('Lose')
            print("{} runs away to ({}, {})".format(name,new_row,new_column))
            
        elif pokemon.upper() == 'W':
            #moves pikachu 1 step forward
            if direction == 'N':
                new_row = new_row - 1
            elif direction == 'S':
                new_row = new_row + 1
            elif direction == 'W':
                new_column = new_column - 1
            elif direction == 'E':
                new_column = new_column + 1
                
            #boundries
            if new_row > 150:
                new_row = 150
            elif new_column > 150:
                new_column = 150
            elif new_row < 0:
                new_row = 0
            elif new_column < 0:
                new_column = 0  
                
            Win_Loss.append('Win')
            print("{} wins and moves to ({}, {})".format(name,new_row,new_column))
            
        #happens when other input is inputed
        else:
            Win_Loss.append('No Pokemon')
    i += 1 

#final print statement
print("{} ends up at ({}, {}), Record: {}".format(name,new_row,new_column,Win_Loss))