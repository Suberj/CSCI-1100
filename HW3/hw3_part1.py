# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:07:25 2022

@author: suber

This module takes in a paragraph from a user and then tells the user the avg sentence length, 
the percent of hard words, the ASYL and the readablility. 
It also tells the reader what the hard words are.
"""
#Imports the module syllables.py that was given to us as s (makes it shorter to type)
import syllables as s

#input statement to ask user for a paragraph
paragraph = input("Enter a paragraph => ")
print(paragraph)

#calculates the avg sentence length
sentences = paragraph.count(".")
split = paragraph.split()
ASL = len(split) / sentences

#find the number of words that have three or more syllables without -, ed, or es

HW = []
for i in range(len(split)):
    #this loop goes through every index in the split and adds words 3 syllables or over that do not contain a '-' into the new list HW
    if s.find_num_syllables(split[i]) >= 3:
        if not split[i].__contains__('-'):
            HW.append( split[i] )
            
#removing words ending in ed and es
for word in HW:
    if word.endswith('ed'):
        HW.remove(word)
    if word.endswith('es'):
        HW.remove(word)
        
#calculates the percent of hard words in paragraph
hard_wrds = len(HW)
PHW = (hard_wrds / len(split)) * 100
            
#calculates the avg num of syllables
syllables = 0 
for i in range(len(split)):
    #this loop goes through every word in the paragraph and adds all of the syllables
    x = s.find_num_syllables(split[i])
    syllables += x
    
ASYL = syllables / len(split)

#calculates GFRI
GFRI = 0.4 * (ASL + PHW)
    
#calculates FKRI
FKRI = 206.835 - 1.015 * ASL - 86.4 * ASYL

#Final print statements
print("Here are the hard words in this paragraph:")
print(HW)
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(ASL, PHW, ASYL))
print("Readability index (GFRI): {:.2f}".format(GFRI))
print("Readability index (FKRI): {:.2f}".format(FKRI))