from random import randint
from gameFunctions import gameVars

def winorlose(status):
	#print("called win or lose", status)
	print("================================================")
	print("YOU" ,status,"!")
	print("Would you like to battle again?")
	print("================================================")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		#reset the game and start again
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You left the Battle, QUITTER")
		exit()

	else:
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		print("Make a valid choice!")
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
		#recursion => calling a function from within itslef
		winorlose(status)

