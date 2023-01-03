# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:28:41 2022

@author: suber

Part two of homework 7
Tells you best/worst movie in a list given parameters
"""

import json

#gets move/rating dictionaries
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    #getting keys for the dictionaries into a list
    keys = list(movies.keys())
    
    
    #inputs for the min/max year, weights, and genre
    miny = input("Min year => ").strip()
    print(miny)
    miny = int(miny)
    
    maxy = input("Max year => ").strip()
    print(maxy)
    maxy = int(maxy)
    
    w1 = input("Weight for IMDB => ").strip()
    print(w1)
    w1 = float(w1)
    
    w2 = input("Weight for Twitter => ").strip()
    print(w2)
    w2 = float(w2)
    
    print("")
    
    genre = input("What genre do you want to see? ").strip()
    print(genre)
    genre = genre.lower()
    
    
    
    
    #loop starts here and will only stop if the user inputs stop for the genre
    while genre != 'stop':
        
        print("")
        
        #gets movie keys that are in the year range given by user
        mov_in_yrs = []
        for i in range(len(keys)):
        
            if movies[keys[i]]['movie_year'] >= miny and movies[keys[i]]['movie_year'] <= maxy:
                mov_in_yrs.append(keys[i])        
        
        #gets the keys of the movies in the year range that have ratings        
        ratings_keys = []
        for i in range(len(mov_in_yrs)):
            if mov_in_yrs[i] in ratings:
                ratings_keys.append(mov_in_yrs[i])
                
        #calculating the combined rating for the movies given 
        combined_rating = []
        for i in range(len(ratings_keys)):
            
            
            #getting twitter rating
            
            #if there are not at least 3 ratings the movies are skipped
            if len(ratings[ratings_keys[i]]) < 3:
                continue
            
            average_twitter_rating = sum(ratings[ratings_keys[i]])/len(ratings[ratings_keys[i]])
            
            #gettings imdb rating
            imdb_rating = movies[ratings_keys[i]]['rating']
            
            #getting combined_rating for each movie
            combined_rating.append([(w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2), movies[ratings_keys[i]]['name'], movies[ratings_keys[i]]['genre'], movies[ratings_keys[i]]['movie_year']])
        
                
        #finding all movies with ratings in the genre given
        mov_in_genre = []
        for i in range(len(combined_rating)):
            for j in range(len(combined_rating[i][2])):
                
                #making all the genres lower
                combined_rating[i][2][j] = combined_rating[i][2][j].lower()
                
            #finding if genre is the given genre
            if genre in combined_rating[i][2]:
                mov_in_genre.append(combined_rating[i])
        
        #if there is no moviese in the year range in the genre this will tell the user
        if len(mov_in_genre) == 0:
            
            print("No {} movie found in {} through {}\n".format(genre.title(), miny, maxy))
    
        #sorting the movies to find the best and the worst movies
        else:
            mov_in_genre.sort()
            mov_in_genre.sort(reverse=True)
            
            #finding best and worst movies
            best = mov_in_genre[0]
            worst = mov_in_genre[-1]
            
            #printing the movies
            print("Best:")
            print("        Released in {}, {} has a rating of {:.2f}\n".format(best[3], best[1], best[0]))
            
            print("Worst:")
            print("        Released in {}, {} has a rating of {:.2f}\n".format(worst[3], worst[1], worst[0]))
            
        #asking the user for another genre to start the loop over again or end it
        
        genre = input("What genre do you want to see? ").strip()
        print(genre)
        genre = genre.lower()
        
        

        
        
        
            