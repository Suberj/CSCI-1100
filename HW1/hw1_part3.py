# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:20:51 2022

@author: suber

This makes a frame with any character and size
"""

#input statements
frame_character = str(input("Enter frame character ==> ")).strip()
print(frame_character)
height = input("Height of box ==> ").strip()
print(height)
width = input("Width of box ==> ").strip()
print(width)

height = int(height)
width = int(width)

#creating frame
w = frame_character * width
h = (frame_character + " " * (width - 2) + frame_character + "\n") * (((height -2)-1) // 2)
h_1 = (frame_character + " " * (width - 2) + frame_character + "\n") * (((height -2)) // 2)
d = "{}X{}".format(width, height)
l = len(d)
#dimensions centered
gap = ((width - 2)-l)//2
gap = int(gap)
gap_1 = ((width - 2)-l) - gap
gap_1 = int(gap_1)


m = frame_character + (" " * gap) + "{}x{}".format(width, height) + (" " * gap_1) + frame_character

#print statements
print("\nBox:")
print(w+"\n"+h+m+"\n"+h_1+w)













 








