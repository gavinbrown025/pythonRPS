from random import randint

#basket of choices ARRAY - index 0, 1, 2.
choices=["rock", "paper", "scissors"]

#let AI make a choice 
computer=choices[randint(0,2)]

#set up a game loop here so we have to keep restarting
player = False

while player is False:
	player=input("Choose Rock, Paper, or Scissors \n")

	#Statrt doing some logic and condition checking	
	print("computer:", computer, "player:", player)


	#always check a breaking condition first
	if player == computer:
		#we have a tie, no pint in going any further
		print("tie, no one wins! Try again!")
	
	elif player == "quit":
		print("you chose to quit quitter")
		exit()
		
	else:
		print("not a tie. now we can check the other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer =choices[randint(0,2)]