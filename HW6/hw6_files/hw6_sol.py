# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:03:38 2022

@author: suber

This takes two files and compares the words in those files
It finds the average word length, distincted words and word sets
"""

"""
This function takes a string and turns it into a list where 
every word is a new index in the list.
"""
def string_list(s):
    new_list = []
    #making s into a list where it breaks at every space
    l = s.strip().lower().replace(" ", '|').split("|")
    
    import re
    #goes through the list and takes anything out that is not a letter
    for i in range(len(l)):
        x = re.sub("[^a-zA-Z]+", "", l[i])
        if len(x) > 0:
            new_list.append(x)
    
    
    return new_list

"""
This function takes in a list of words and sorts them into a list of lists
sorted by the length of the word. The length of the word is the index in the list (minus one).
It then prints those out in the form for the assignment.
"""
def sorting_length(l, m):
    #making a list of lists to append our words to
    x = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    #appending words based on length
    for i in range(len(l)):
        length = len(l[i])
        x[length-1].append(l[i])
    #sorting every list in the list x    
    for i in range(len(x)):
        x[i].sort()
    #printing out all the words sorted by length    
    for i in range(m):
        #prints out the format if no words have that length
        if len(x[i]) == 0:
            if i + 1 < 10:
                print("   {}:   0:".format(i+1))
            elif i + 1 >= 10:
                print("  {}:   0:".format(i+1))
        else:
            #prints out if 6 or under words have that length
            if len(x[i]) <= 6:
                str1 = ''
                for j in range(len(x[i])):
                    str1 = str1 + ' ' + x[i][j]
                if i + 1 < 10:    
                    print("   {}:{:>4}:{}".format(i+1,len(x[i]),str1))
                elif i + 1 >= 10:
                    print("  {}:{:>4}:{}".format(i+1,len(x[i]),str1))
            #prints out if over 6 words have that length
            else:
                str1 = ''
                x[i].sort()
                str1 = str1 + x[i][0] + " " + x[i][1] + " " + x[i][2] + " " + '...' + " " + x[i][-3] + " " + x[i][-2] + " " + x[i][-1]
                if i + 1 < 10:
                    print("   {}:{:>4}: {}".format(i+1,len(x[i]),str1))
                elif i + 1 >= 10:
                    print("  {}:{:>4}: {}".format(i+1,len(x[i]),str1))
                    
    
"""
This function takes in a list and the seperation of the list and then outputs
a list of tuples with all the unique tuples within the max list seperation. 
It also returns every pair to be used later when comparing the two files.
"""
def distinct_pairs(l,step):
    pairs = []
    distinct = []
    step = int(step)
    
    #finding all pairs
    for i in range(len(l)-step):
        for j in range(1,step+1):
            pairs.append([l[i],l[i+j]])
    if step == 2:
        pairs.append([l[-2],l[-1]])
    elif step == 3:
        pairs.append([l[-3],l[-2]])
        pairs.append([l[-3],l[-1]])
        pairs.append([l[-2],l[-1]])
    #finding distinct pairs
    for k in range(len(pairs)):
        pairs[k].sort()
        distinct.append(pairs[k])
    #removing multiple occurances of tuples    
    distinct = {tuple(x) for x in distinct}
    distinct = list(distinct)
    
    return pairs, distinct 
        
#makes every word in the file stop.txt and adds it to set 
stop_list = []
for line in open('stop.txt'):
    y = string_list(line)
    str1 = ''
    str1 = str1 + y[0]
    stop_list.append(str1)

#user will input the two files and the max seperation of words
file1 = input("Enter the first file to analyze and compare ==> ")
print(file1)
file2 = input("Enter the second file to analyze and compare ==> ")    
print(file2)
seperation = input("Enter the maximum separation between words in a pair ==> ")
print(seperation)
seperation = int(seperation)

#getting everyword in a list for each file
#making the list for the first file
file1_lol = [] #this will be a list of lists
file1_l = [] #making the list of lists into one list
for line in open(file1, encoding='utf-8'):
    y = string_list(line)
    file1_lol.append(y)
for i in range(len(file1_lol)):
    for j in range(len(file1_lol[i])):
        file1_l.append(file1_lol[i][j])
        
#making the list for the second file
file2_lol = [] #this will be a list of lists
file2_l = [] #making the list of lists into one list
for line in open(file2, encoding='utf-8'):
    y = string_list(line)
    file2_lol.append(y)
for i in range(len(file2_lol)):
    for j in range(len(file2_lol[i])):
        file2_l.append(file2_lol[i][j])        
    
#removing the words from stop.txt from the word lists

l1 = []
for i in range(len(file1_l)):
    if not file1_l[i] in stop_list:
        l1.append(file1_l[i]) 
        
l2 = []
for i in range(len(file2_l)):
    if not file2_l[i] in stop_list:
        l2.append(file2_l[i]) 
        
#calculating the average word length
#for list 1
tot_length1 = 0

for i in range(len(l1)):
    tot_length1 += len(l1[i])
avg1 = tot_length1/len(l1)

#for list 2
tot_length2 = 0

for i in range(len(l2)):
    tot_length2 += len(l2[i])      
avg2 = tot_length2/len(l2) 
    
#find distinct words for both lists
set1 = set(l1)
set2 = set(l2)

distinct1 = len(set1)/len(l1)
distinct2 = len(set2)/len(l2)

#sorting each word in the list by length
length1 = []
for i in range(len(l1)):
    length1.append(len(l1[i]))
    
length2 = []
for i in range(len(l2)):
    length2.append(len(l2[i]))
    
#finding the length of the largest word    
m1 = max(length1)
m2 = max(length2)

m = []
m.append(m1)
m.append(m2)
ma = max(m)
mi = min(m)
#making sorted list as s1 and s2
s1 = []
s2 = []
for i in range(len(l1)):
    s1.append(l1[i])
for i in range(len(l2)):
    s2.append(l2[i])

l1s = list(set1)
l2s = list(set2)
s1.sort()
s2.sort()

#finding all pairs and distinct pairs
pairs1 = distinct_pairs(l1,seperation)[0]
dpairs1 = distinct_pairs(l1, seperation)[1]
pairs2 = distinct_pairs(l2,seperation)[0]
dpairs2 = distinct_pairs(l2, seperation)[1]
dpairs1.sort()
dpairs2.sort()

#finding the ratio of distinct pairs to total pairs
ratio_pairs1 = len(dpairs1)/len(pairs1)
ratio_pairs2 = len(dpairs2)/len(pairs2)

#compairing the two documents
inter = set1 & set2
union = set1.union(set2)
J = len(inter)/len(union)

  
#final print statements
#file 1
print("\nEvaluating document {}".format(file1))
print("1. Average word length: {:.2f}".format(avg1))
print("2. Ratio of distinct words to total words: {:.3f}".format(distinct1))
print("3. Word sets for document {}:".format(file1))
sorting_length(l1s, m1) 
print("4. Word pairs for document {}".format(file1))
print("  {} distinct pairs".format(len(dpairs1)))

#loop to print the distinct pairs
if len(dpairs1) < 10:
    for i in range(len(dpairs1)):
        print("  {} {}".format(dpairs1[i][0],dpairs1[i][1]))
else:
    for i in range(5):
        print("  {} {}".format(dpairs1[i][0],dpairs1[i][1]))
    print("  ...")
    x = dpairs1[-5:-1:1]
    for i in range(len(x)):
        print("  {} {}".format(x[i][0],x[i][1]))
    print("  {} {}".format(dpairs1[-1][0],dpairs1[-1][1]))
    
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio_pairs1))
    
#file 2
print("\nEvaluating document {}".format(file2))
print("1. Average word length: {:.2f}".format(avg2))
print("2. Ratio of distinct words to total words: {:.3f}".format(distinct2))
print("3. Word sets for document {}:".format(file2))
sorting_length(l2s, m2) 
print("4. Word pairs for document {}".format(file2))
print("  {} distinct pairs".format(len(dpairs2)))

#loop to print the distinct pairs
if len(dpairs2) < 10:
    for i in range(len(dpairs2)):
        print("  {} {}".format(dpairs2[i][0],dpairs2[i][1]))
else:
    for i in range(5):
        print("  {} {}".format(dpairs2[i][0],dpairs2[i][1]))
    print("  ...")
    y = dpairs2[-5:-1:1]
    for i in range(len(y)):
        print("  {} {}".format(y[i][0],y[i][1]))
    print("  {} {}".format(dpairs2[-1][0],dpairs2[-1][1]))
    
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratio_pairs2))

#comparing the two files
print("\nSummary comparison")

#deciding which file had a larger avg word len
if avg1 > avg2:
    print("1. {} on average uses longer words than {}".format(file1,file2))
else:
    print("1. {} on average uses longer words than {}".format(file2,file1))
    
print("2. Overall word use similarity: {:.3f}".format(J))
print("3. Word use similarity by length:")

#finding word use similarity
#making a list of lists to append our words to
x = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#appending words based on length
for i in range(len(l1s)):
    length = len(l1s[i])
    x[length-1].append(l1s[i])
#taking all empty strings in the back out
word_sim1 = []
for i in range(m1):
    word_sim1.append(x[i])
    
x1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#appending words based on length
for i in range(len(l2s)):
    length = len(l2s[i])
    x1[length-1].append(l2s[i])
#taking all empty strings in the back out
word_sim2 = []
for i in range(m2):
    word_sim2.append(x1[i])
    
#comparing both word lists
#making every list inside the word lists a set so we can compare the two easily and quickly
set_sim1 = []
set_sim2 = []

for i in range(len(word_sim1)):
    if not len(word_sim1[i]) == 0:
        set_sim1.append(set(word_sim1[i]))
    else:
        set_sim1.append(set())
    
for i in range(len(word_sim2)):
    if not len(word_sim2[i]) == 0:
        set_sim2.append(set(word_sim2[i]))
    else:
        set_sim2.append(set())
    

#printing all the values    
for i in range(mi):
    both = set_sim1[i] & set_sim2[i]
    un = set_sim1[i].union(set_sim2[i])
    if not len(un) == 0:
        J = len(both)/len(un)
    else:
        J = 0
    print(" {:>3}: {:.4f}".format(i+1,J))

dif = ma - mi
if dif > 0:
    for i in range(dif):
        print(" {:>3}: 0.0000".format(i+1+(mi)))

#finding word pair similarity
ds1 = {tuple(x) for x in dpairs1}
ds2 = {tuple(x) for x in dpairs2}
inter = ds1 & ds2
union = ds1.union(ds2)
J = len(inter)/len(union)

print("4. Word pair similarity: {:.4f}".format(J))