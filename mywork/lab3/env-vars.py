#!/usr/bin/python3

import os

#prompt user with questions and assign to input variable
FAV_COLOR = input("What is your favorite color? ")
FAV_SHOW = input("What is your favorite TV Show? ")
FAV_SONG = input("What is your favorite song? ")

#set input variables to environment variables
os.environ['FAV_COLOR'] = FAV_COLOR
os.environ['FAV_SHOW'] = FAV_SHOW
os.environ['FAV_SONG'] = FAV_SONG

#print out env variables
print("Favorite color: ", os.getenv("FAV_COLOR"))
print("Favorite show: ", os.getenv("FAV_SHOW"))
print("Favorite Song: ", os.getenv('FAV_SONG'))