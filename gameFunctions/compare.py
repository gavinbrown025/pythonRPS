from random import randint
from gameFunctions import gameVars

#Need to create function
#Figure out what you need to pass into the function, what are you comparing
def compare(player):
	if player == gameVars.computer:
		#we have a tie, no pint in going any further
		print("Tie, no one wins! Try again!")
		
	elif player == "Rock":
		if gameVars.computer == "Paper":
			print("XXXXXXXXXX You Lose! XXXXXXXXX")
			print ("XXXXX" ,gameVars.computer, "SUFFOCATES", player,"XXXXX")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("+++++++++ You Won! +++++++++"), 
			print("+++++",player, "BLUDGEONS", gameVars.computer, "+++++")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Paper":
		if gameVars.computer == "Scissors":
			print("XXXXXXXXXX You Lose! XXXXXXXXX")
			print ("XXXXX" ,gameVars.computer, "STABS", player,"XXXXX")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("+++++++++ You Won! +++++++++"), 
			print("+++++",player, "SUFFOCATES", gameVars.computer, "+++++")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Scissors":
		if gameVars.computer == "Rock":
			print("XXXXXXXXXX You Lose! XXXXXXXXX")
			print ("XXXXX" ,gameVars.computer, "BLUDGEONS", player,"XXXXX")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("+++++++++ You Won! +++++++++"), 
			print("+++++",player, "STABS", gameVars.computer, "+++++")
			gameVars.computer_lives = gameVars.computer_lives -1

	

	