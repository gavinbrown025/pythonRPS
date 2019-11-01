from random import randint

#basket of choices ARRAY - index 0, 1, 2.
choices=["rock", "paper", "scissors"]

#adding lives -> 
#when one or the other gets to 0, win / lose
player_lives = 5
computer_lives = 5

#let AI make a choice 
computer=choices[randint(0,2)]

#set up a game loop here so we have to keep restarting
player = False

def winorlose(status):
	#print("called win or lose", status)
	print("================================================")
	print("YOU" ,status, "! Would you like to play again?")
	print("================================================")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		#reset the game and start again
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit quitter")
		exit()

	else:
		print("Make a valid choice. Yes or No!" )


while player is False:
	print("========================================")
	print("Computer Lives", computer_lives, "/5")
	print("Player Lives", player_lives, "/5")
	print("========================================")	
	print("Choose Your Weapon")
	player=input("Choose Rock, Paper, or Scissors \n")

	#Statrt doing some logic and condition checking
	print("========================================")	
	print("Computer:", computer,)
	print("Player:", player)
	print("========================================")


	#always check a breaking condition first
	if player == computer:
		#we have a tie, no pint in going any further
		print("Tie, no one wins! Try again!")
	
	elif player == "quit":
		print("You chose to quit quitter")
		exit()
		
	elif player == "rock":
		if computer == "paper":
			print("You Lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "smashes", computer)
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You Lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "covers", computer)
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print("You Lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("You Won!", player, "cuts", computer)
			computer_lives = computer_lives -1

	

	if player_lives is 0:
		# print("You Lose, Loser! Play again?")
		winorlose("LOST ALL YOUR LIVES")

	elif computer_lives is 0:
		# print("You Won! Play again?")
		winorlose("BEAT THE COMPUTER")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]

		# elif choice == "N" or choice == "n":
		# 	print("you chose to quit quitter")
		# 	exit()

		# else:
		# 	print("Make a valid choice. Yes or No!" )


	player = False
	computer=choices[randint(0,2)]