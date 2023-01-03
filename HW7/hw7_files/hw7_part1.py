# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:07:27 2022

@author: suber

Part one for homework 7: autocorrect words and checks if it is in a dictionary
"""

if __name__ == "__main__":
    #inputs for the files
    dictionary = input("Dictionary file => ").strip()
    print(dictionary)
    
    input_file = input("Input file => ").strip()
    print(input_file)
    
    keyboard = input("Keyboard file => ").strip()
    print(keyboard)

    #creating a list of all the words in the dictionary
    all_words = []
    freq = dict()
    for lines in open(dictionary):
        line = lines.split(",")
        all_words.append(line[0])
        freq[line[0]] = line[1].strip()
    #creating a list of all the inputed words
    input_words = []
    for lines in open(input_file):
        line = lines.strip()
        input_words.append(line)
        
    #creating a list for the letters to replace
    replacements = []
    for lines in open(keyboard):
        line = lines.strip().split(" ")
        replacements.append(line)
    
    #turning the replacement list into a dictionary
    keyboard_dict = dict()
    keys = []
    for i in range(len(replacements)):
        key = replacements[i][0]
        keys.append(key)
        replacements[i].pop(0)
        keyboard_dict[key] = replacements[i]
        
    for i in range(len(input_words)):
        word = input_words[i]
        autocorrect = []
        
        #finds words that do not need autocorrect
        if word in all_words:
            print("{:>15} -> FOUND".format(word))
        
        else:
            #DROP type
            for j in range(len(word)):
                drop = list(word)
                drop.pop(j)
                drop = "".join(drop)
                
                if drop in all_words:
                    autocorrect.append(drop)
             
                #INSERT TYPE
                for q in range(len(keys)):
                    insert = word[:j] + keys[q] + word[j:]
                    
                    if insert in all_words:
                        autocorrect.append(insert)
                #adding letter to end of word        
                for z in range(len(keys)):
                    insert2 = word + keys[z]
                    
                    if insert2 in all_words:
                        autocorrect.append(insert2)
                        
                        
            #SWAP TYPE
            for x in range(len(word)-1):
                swap = list(word)
                swap[x], swap[x+1] = swap[x+1], swap[x]
                swap = "".join(swap)
                    
                if swap in all_words:
                    autocorrect.append(swap)
                        
            #REPLACE type
            """To do this I am changing replace to a list because if I use .replace
            then if the word has multiple of the same letter it changes both letters giving me wrong answers"""
            replace = list(word)
            
            for z in range(len(replace)):
                for q in range(len(keys)):
                    if replace[z] == keys[q]:
                        lst = keyboard_dict[keys[q]]
                for l in range(len(lst)):
                    replace[z] = lst[l]
                    r = "".join(replace)
                    if r in all_words:
                        autocorrect.append(r)
                    replace = list(word)
                
                
        #sorting autocorrected words
        sort_auto = []
        autocorrect = set(autocorrect)
        autocorrect = list(autocorrect)
        for a in range(len(autocorrect)):
            f = freq[autocorrect[a]]
            sort_auto.append([f,autocorrect[a]])            
                
        sort_auto.sort(reverse=True)     
        
        autocorrect1 = []
        for z in range(len(sort_auto)):
            autocorrect1.append(sort_auto[z][1])
            
        #prints the autocorrect words in the format the HW gives
        #prints if less then 3 possible words           
        if len(autocorrect1) <= 3 and len(autocorrect1) > 0:
            string = ''
            for x in autocorrect1:
                
                string += ' ' + x
            string.strip()
            print("{:>15} -> FOUND{:>3}: {}".format(word, len(autocorrect1), string))
        
        #if there is more than 6 possible words this prints out only the top 3
        elif len(autocorrect1) > 3:
            autocorrect2 = [autocorrect1[0],autocorrect1[1],autocorrect1[2]]
            
            string = ''
            for x in autocorrect2:
                
                string += ' ' + x
            string.strip()
            print("{:>15} -> FOUND{:>3}: {}".format(word, len(autocorrect1), string))
            
        #if not words were found then it prints NOT FOUND
        elif word not in all_words and len(autocorrect1) == 0:
            print("{:>15} -> NOT FOUND".format(word))