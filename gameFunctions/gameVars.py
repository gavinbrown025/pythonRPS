from random import randint


#basket of choices ARRAY - index 0, 1, 2.
choices=["Rock", "Paper", "Scissors"]

#adding lives -> 
#when one or the other gets to 0, win / lose
player_lives = 5
computer_lives = 5

total_lives = 5

#let AI make a choice 
computer=choices[randint(0,2)]


#set up a game loop here so we have to keep restarting
player = False