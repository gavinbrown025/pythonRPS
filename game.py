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
	print("Computer:", computer, "\n","Player:", player)


	#always check a breaking condition first
	if player == computer:
		#we have a tie, no pint in going any further
		print("tie, no one wins! Try again!")
	
	elif player == "quit":
		print("you chose to quit quitter")
		exit()
		
	elif player == "rock":
		if computer == "paper":
			print("you Lose!", computer, "covers", player, "\n")
		else:
			print("You Won!", player, "smashes", computer)

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
		else:
			print("You Won!", player, "covers", computer)

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
		else:
			print("You Won!", player, "cuts", computer)

		

	player = False
	computer=choices[randint(0,2)]