# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:50:12 2022

@author: suber

This file reads an inputed password and tells the user if it is strong or not
"""

import hw4_util

#input password
pw = input("Enter a password => ")
print(pw)

#points based on length
l = len(pw)
length = 0
if l == 6 or l == 7:
    length =+ 1
if l >= 8 and l <= 10:
    length =+2
if l > 10:
    length =+ 3
  
#points based on upper and lower case
lower = sum(map(str.islower, pw))
upper = sum(map(str.isupper, pw))
cases = 0

if lower >= 2 and upper >= 2:
    cases =+ 2
if lower == 1 or upper == 1:
    cases =+ 1

#points based on digits
digits = sum(map(str.isnumeric, pw))
digit = 0

if digits >= 2:
    digit =+ 2
if digits == 1:
    digit =+ 1
    
#points based on punctuation
a = pw.count('!')
b = pw.count('@')
c = pw.count('#')
d = pw.count('$')
e = pw.count('%')
f = pw.count('^')
g = pw.count('&')
h = pw.count('*')

x = a + b + c + d
y = e + f + g + h

puncuation_1 = 0
puncuation_2 = 0

if x >= 1:
    puncuation_1 =+ 1
if y >= 1:
    puncuation_2 =+ 1

licenses = 0
    
#points based on license
if l == 7:
    if pw[0].isalpha() and pw[1].isalpha() and pw[2].isalpha() and pw[3].isnumeric() and pw[4].isnumeric() and pw[5].isnumeric() and pw[6].isnumeric():
        licenses =+ 2

#points based on common passwords
common = hw4_util.part1_get_top()
count = 0 
commons = 0
for i in range(len(common)):
    if pw.lower() == common[i]:
        count =+ 1
        
if count >= 1:
    commons =+ 3

#final score
score = length + cases + digit + puncuation_1 + puncuation_2 - licenses - commons

#final print statements
if length > 0:
    print("Length: +{}".format(length))
if cases > 0:
    print("Cases: +{}".format(cases))
if digit > 0:
    print("Digits: +{}".format(digit))
if puncuation_1 > 0:
    print("!@#$: +{}".format(puncuation_1))
if puncuation_2 > 0:
    print("%^&*: +{}".format(puncuation_2))
if licenses > 0:
    print("License: -{}".format(licenses))
if commons > 0:
    print("Common: -{}".format(commons))
    
print("Combined score: {}".format(score))

if score <= 0:
    print("Password is rejected")
if score == 1 or score == 2:
    print("Password is poor")
if score == 3 or score == 4:
    print("Password is fair")
if score == 5 or score == 6:
    print("Password is good")
if score >= 7:
    print("Password is excellent")
    


