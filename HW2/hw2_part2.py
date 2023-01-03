# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:39:26 2022

@author: suber

This file determines a simple substitution code is reversible given a string
It encrypts the message, decrypts it, and also tells you whether it is reversible or not
and the difference in length of the original message compared to the encrypted message
"""
#inputs
string = input("Enter a string to encode ==> ")
print(string)
#defining encyption
def encrypt(word):
    word = string.replace(' a','%4%').replace('he','7!').replace('e','9(*9(').replace('y','*%$').replace('u','@@@').replace('an','-?').replace('th','!@+3').replace('o','7654').replace('9','2').replace('ck','%4')
    return word
#printing encryption output
print("\nEncrypted as ==>",encrypt(string))
#difference in length
length_input = len(string)
length_encryption = len(encrypt(string))
difference_length = abs(length_input - length_encryption)
print("Difference in length ==>",difference_length)
#defining decryption
def decrypt(word):
    word = encrypt(string).replace('%4','ck').replace('2','9').replace('7654','o').replace('!@+3','th').replace('-?','an').replace('@@@','u').replace('*%$','y').replace('9(*9(','e').replace('7!','he').replace('%4%',' a')
    return word
#printing decryption output
print("Deciphered as ==>",decrypt(string))
#stating whether it is reversible or not
if string == decrypt(string):
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")