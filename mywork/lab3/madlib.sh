#!/bin/bash

#clear the screen
clear
echo "Let's build a mad-lib!"

#prompt user for words and then assign to variables
read -p "1. Please give me an name: " NAME
read -p "2. Please give me a sport activity(verb): " SPORT
read -p "3. Please give me a location(noun): " LOCATION
read -p "4. Please give me any noun: " NOUN
read -p "5. Please give me another noun: " NOUN2
read -p "5. Please give me a positive emotion(adjective): " EMOTION
read -p "6. Please give me a verb: " VERB 
read -p "7. Please give me a resteraunt(noun): " RESTERAUNT
read -p "8. Please give me a food(noun): " FOOD

#telling story
echo ""
echo "$NAME was having a good day, while playing $SPORT with some friends at the $LOCATION. When suddenly a giant $NOUN came out of nowhere and attacked $NAME. $NAME quickly grabbed a $NOUN2 to scare off the $NOUN. $NAME and friends felt $EMOTION after succeeding in scaring off the $NOUN. $NAME and friends then started to $VERB in celebration. They then decided to go to $RESTERAUNT to eat their favorite $FOOD."