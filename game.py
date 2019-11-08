from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("========================================")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("========================================")	
	print("Choose Your Weapon")
	
	player=input("Choose Rock(R), Paper(P), or Scissors(S) \n")
		# if player == "R" or player == "r" or player == "rock"
		# 	player = rock
		# elif player ==
		# if choice == "Y" or choice == "y":

	#Start doing some logic and condition checking
	print("========================================")	
	print("Computer:", gameVars.computer,)
	print("Player:", player)
	print("========================================")
	

	#now we want to run comparison
	
	compare.compare(player)

	#end of compare stuff
	


	if gameVars.player_lives is 0:
		winlose.winorlose("LOST ALL YOUR LIVES")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("BEAT THE COMPUTER")

	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]