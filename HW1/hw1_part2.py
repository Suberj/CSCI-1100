# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:19:09 2022

@author: suber

This file takes in inputs for minutes, seconds, miles, and target miles
then it calculates your pace, speed, and how long it will take to run your target miles
then it prints these in a message
"""


#inputs
minutes = input("Minutes ==> ")
print(minutes)
seconds = input("Seconds ==> ")
print(seconds)
miles = input("Miles ==> ")
print(miles)
target_miles = input("Target Miles ==> ")
print(target_miles)

#making things integers and float
minutes = int(minutes)
seconds = int(seconds)
miles = float(miles)
target_miles = float(target_miles)

#calculation
pace_minutes = (((minutes*60) + seconds) / miles) // 60
pace_seconds = ((((minutes*60) + seconds) / miles) % 60) / 100
pace = pace_minutes + ((pace_seconds*100)/60)
pace_seconds1 = pace_seconds * 100
pace_seconds1 = int(pace_seconds1)
pace_minutes = int(pace_minutes)

time = ((minutes*60) + seconds) / 360
speed = (miles / time) * 10
speed_rounded = "{:.2f}".format(speed)

target_miles1 = "{:.2f}".format(target_miles)
target = pace * target_miles
target_minutes = int(target)
target_decimal= target - target_minutes
target_seconds = (target_decimal*60)
target_seconds = int(target_seconds)


#print statement
print("\nPace is",pace_minutes,"minutes and",pace_seconds1,"seconds per mile.\nSpeed is",speed_rounded,"miles per hour.\nTime to run the target distance of",target_miles1,"miles is",target_minutes,"minutes and",target_seconds,"seconds.")