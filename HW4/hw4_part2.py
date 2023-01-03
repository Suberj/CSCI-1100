# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 13:36:25 2022

@author: suber
"""

import hw4_util

#function that finds the daily average cases
def daily(state):
    
    stats = hw4_util.part2_get_week(index)[i]
            
    pop = stats[1]
    tot_cases = stats[2] + stats[3] + stats[4] + stats[5] + stats[6] + stats[7] + stats[8]
    avg_per_1k = (tot_cases / 7) / (pop / 100000)
    return avg_per_1k

#function that finds the percent of cases that are positive
def pct(state):
                
    stats = hw4_util.part2_get_week(index)[i]
                        
    tot_cases = stats[2] + stats[3] + stats[4] + stats[5] + stats[6] + stats[7] + stats[8]
    tot_negatives = stats[9] + stats[10] + stats[11] + stats[12] + stats[13] + stats[14] + stats[15]
    tot_tests = tot_cases + tot_negatives
    percent = (tot_cases / tot_tests) * 100
    return percent
    
i=0
while i >= 0:

    print("...")
    #inputs for week
    index = input("Please enter the index for a week: ")
    print(index)
    index = int(index)
    
    #make sure index is in range and if it is negative it ends the loop
    if index > 29:
        print("No data for that week")
    if index < 0:
        i = -1
    if index > 0 and index <= 29:
        #index is in range for weeks it executes the rest of the code
        request = input("Request (daily, pct, quar, high): ")
        print(request)
        request = request.lower()
        
        #make sure one of the request is inputed
        if request == 'daily' or request == 'pct' or request == 'quar' or request == 'high':
            
            #if statements to determine the request
            if request == 'daily':
                        
                #input for state
                state = input("Enter the state: ")
                print(state)
                state = state.upper()
                
                states = [ 'AK' , 'AL' , 'AR' , 'AZ' , 'CA' , 'CO' , 'CT' , 'DC' , 'DE' , 'FL' , 'GA' , 'HI' , 'IA' , 'ID' , 'IL' , 'IN' , 'KS' , 'KY' , 'LA' , 'MA' , 'MD' , 'ME' , 'MI' , 'MN' , 'MO' , 'MS' , 'MT' , 'NC' , 'ND' , 'NE' , 'NH' , 'NJ' , 'NM' , 'NV' , 'NY' , 'OH' , 'OK' , 'OR' , 'PA' , 'PR' , 'RI' , 'SC' , 'SD' , 'TN' , 'TX' , 'UT' , 'VA' , 'VT' , 'WA' , 'WI' , 'WV' , 'WY']
                
                if state in states:
                    
                    #loop that adds the stats to a list for a state on a specific week
                    for i in range (len(hw4_util.part2_get_week(index))):
                        if hw4_util.part2_get_week(index)[i][0] == state:
                        
                            avg_per_1k = daily(state)
                
                            print("Average daily positives per 100K population: {:.1f}".format(avg_per_1k))
                
                else:
                    print("State {} not found".format(state))
                    
            if request == 'pct':
                        
                #input for state
                state = input("Enter the state: ")
                print(state)
                state = state.upper()
                
                states = [ 'AK' , 'AL' , 'AR' , 'AZ' , 'CA' , 'CO' , 'CT' , 'DC' , 'DE' , 'FL' , 'GA' , 'HI' , 'IA' , 'ID' , 'IL' , 'IN' , 'KS' , 'KY' , 'LA' , 'MA' , 'MD' , 'ME' , 'MI' , 'MN' , 'MO' , 'MS' , 'MT' , 'NC' , 'ND' , 'NE' , 'NH' , 'NJ' , 'NM' , 'NV' , 'NY' , 'OH' , 'OK' , 'OR' , 'PA' , 'PR' , 'RI' , 'SC' , 'SD' , 'TN' , 'TX' , 'UT' , 'VA' , 'VT' , 'WA' , 'WI' , 'WV' , 'WY']
               
                if state in states:
                    for i in range (len(hw4_util.part2_get_week(index))):
                        if hw4_util.part2_get_week(index)[i][0] == state:
                            percent = pct(state)
                            print("Average daily positive percent: {:.1f}".format(percent))
            
                else:
                     print("State {} not found".format(state))
                     
            if request == 'quar':
                states = []
                for i in range (len(hw4_util.part2_get_week(index))):
                    x = daily(hw4_util.part2_get_week(index)[i])
                    y = pct(hw4_util.part2_get_week(index)[i])
                    if x > 10 or y > 10:
                        #adds state to list if it meets the quaritine requirements
                        states.append(hw4_util.part2_get_week(index)[i][0])
                #orginizes states
                print("Quarantine states:")
                hw4_util.print_abbreviations(states)
            
            if request == 'high':
                high = []
                states = []
                for i in range (len(hw4_util.part2_get_week(index))):
                    x = daily(hw4_util.part2_get_week(index)[i])
                    #adds every value for that week into the list high
                    high.append(x)
                    #adds each state in a list
                    states.append(hw4_util.part2_get_week(index)[i][0])
                #find max value and the state that coorisponds to that value
                max_value = max(high)
                max_index = high.index(max_value)
                max_state = states[max_index]
                
                print("State with highest infection rate is {}".format(max_state))
                print("Rate is {:.1f} per 100,000 people".format(max_value))
                
                
                
        #if request is not one of the ones given then it prints this and loop restarts
        else:
            print("Unrecognized request")
                   
           
