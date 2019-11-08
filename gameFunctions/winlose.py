from random import randint
from gameFunctions import gameVars

def winorlose(status):
	#print("called win or lose", status)
	print("================================================")
	print("YOU" ,status, "! Would you like to play again?")
	print("================================================")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		#reset the game and start again
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit quitter")
		exit()

	else:
		print("Make a valid choice. Yes or No!" )
		#recursion => calling a function from within itslef
		winorlose(status)

