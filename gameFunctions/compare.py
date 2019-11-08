from random import randint
from gameFunctions import gameVars

#Need to create function
#Figure out what you need to pass into the function, what are you comparing
def compare(player):
	if player == gameVars.computer:
		#we have a tie, no pint in going any further
		print("Tie, no one wins! Try again!")
	
	elif player == "quit":
		print("You chose to quit quitter")
		exit()
		
	elif player == "rock":
		if gameVars.computer == "paper":
			print("You Lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You Won!", player, "smashes", gameVars.computer)
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You Lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You Won!", player, "covers", gameVars.computer)
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You Lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You Won!", player, "cuts", gameVars.computer)
			gameVars.computer_lives = gameVars.computer_lives -1

	

	