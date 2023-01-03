# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:18:07 2022

@author: suber

This files takes a string and then describes its happiness level and the tone
"""
#inputs
sentence = input("Enter a sentence => ")
print(sentence)
sentence = str(sentence)
#making sentence all lowercase so it matches the words in the happy/sad tuple
sentence = sentence.lower()
#this function counts the number of times happy words show up
def number_happy(sentence):
    happy = ('laugh','happiness','love','excellent','good','smile')
    count = 0
    for happy_words in happy:
        count += sentence.count(happy_words)
    return count
#this function counts the number of times sad words show up
def number_sad(sentence):
    sad = ('bad','sad','horrible','problem','hate','terrible')
    count = 0
    for sad_words in sad:
        count += sentence.count(sad_words)
    return count
#final print statements
sentiment = "+" * number_happy(sentence) + "-" * number_sad(sentence)
print("Sentiment:",sentiment)
#prints whether the sentence is happy, sad, or neutral
if number_happy(sentence) > number_sad(sentence):
    print("This is a happy sentence.")
if number_happy(sentence) < number_sad(sentence):
    print("This is a sad sentence.")
if number_happy(sentence) == number_sad(sentence):
    print("This is a neutral sentence.")