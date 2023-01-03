# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:16:29 2022

@author: suber
This file takes in a series of inputs and print a story with those inputs
"""

#inital print statements
print("Let's play Mad Libs for Homework 1")
print("Type one word responses to the following:\n")

#input statements
proper_name = input("proper_name ==> ").strip()
print(proper_name)
adjective0 = input("adjective ==> ").strip()
print(adjective0)
noun0 = input("noun ==> ").strip()
print(noun0)
verb0 = input("verb ==> ").strip()
print(verb0)
verb1 = input("verb ==> ").strip()
print(verb1)
noun1 = input("noun ==> ").strip()
print(noun1)
emotion0 = input("emotion ==> ").strip()
print(emotion0)
verb2 = input("verb ==> ").strip()
print(verb2)
noun2 = input("noun ==> ").strip()
print(noun2)
season = input("season ==> ").strip()
print(season)
adjective1 = input("adjective ==> ").strip()
print(adjective1)
emotion1 = input("emotion ==> ").strip()
print(emotion1)
team_name = input("team-name ==> ").strip()
print(team_name)
noun3 = input("noun ==> ").strip()
print(noun3)
adjective2 = input("adjective ==> ").strip()
print(adjective2)

#final mad lib
print("\nHere is your Mad Lib...\n\nGood morning",proper_name+"!")
print("\n  This will be a/an",adjective0,noun0+"!","Are you",verb0,"forward to it?")
print("  You will",verb1,"a lot of",noun1,"and feel",emotion0,"when you do.")
print("  If you do not, you will",verb2,"this",noun2+".")
print("\n  This",season,"was",adjective1+".","Were you",emotion1,"when",team_name,"won")
print("  the",noun3+"?")
print("\n  Have a/an",adjective2,"day!")


