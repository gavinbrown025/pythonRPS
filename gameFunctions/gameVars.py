from random import randint


#basket of choices ARRAY - index 0, 1, 2.
choices=["rock", "paper", "scissors"]

#adding lives -> 
#when one or the other gets to 0, win / lose
player_lives = 1
computer_lives = 1

total_lives = 1

#let AI make a choice 
computer=choices[randint(0,2)]


#set up a game loop here so we have to keep restarting
player = False