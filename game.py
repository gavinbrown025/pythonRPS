from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("==================================================")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==================================================")	
	print("Choose Your Weapon")
	
	player=input("Choose Rock(R), Paper(P), or Scissors(S) \n")
	## LETS YOU PUT IN SHORTFORMS 
	if player == "R" or player == "r" or player == "Rock" or player == "rock":
		player=("Rock")	
	
	elif player == "P" or player == "p" or player == "Paper" or player == "paper":
		player=("Paper")	
	
	elif player == "S" or player == "s" or player == "Scissors" or player == "scissors":
		player=("Scissors")
	
	elif player == "quit" or player == "q" or player == "Q":
		player=("quit")
		print("You left the Battle, QUITTER")
		exit()

	else:
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("Make a valid choice!")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		gameVars.player = False
		gameVars.computer=gameVars.choices[randint(0,2)]

	#Start doing some logic and condition checking
	print("==================================================")	
	print("Computer:", gameVars.computer,)
	print("Player:", player)
	print("==================================================")
	
	#now we want to run comparison	
	compare.compare(player)
	#end of compare stuff

	if gameVars.player_lives is 0:
		winlose.winorlose("WERE MURDERED BY THE MACHINE OVERLORDS")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("BEAT SKYNET AND SAVED THE WORLD")

	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)] 