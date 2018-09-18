"""
This module outlines gameplay

"""


### IMPORTS ###

from time import sleep
from os import system
import shutil
import pydealer as pyd
from pydealer.const import BOTTOM
import hands
import legality


### MODULE WIDE UTILITY ###

def clear():
	_ = system('clear')


columns = shutil.get_terminal_size().columns


### CLASSES ###

class LastPlay:
	"""
	Holds information about the last play made.

	"""

	def __init__(self):
		"""
		Constructs play method
		
		"""
		
		self.card = pyd.Stack()

	def display(self):
		"""
		Displays what card and how many were played
		in the previous turn.

		"""

		if len(self.card) == 0:
			print("No previous card played.\n".center(columns))

		else:
			last = self.card[0]
			print("Last card value played: {}.\n".format(last).center(columns))
	
	def new_play(self, value):
		"""
		Adds a newly played card and amount to 
		top of the card stack. Called at end of turn.
		
		:arg single card instance value:
			Card

		"""
		
		self.card.add(value, end=BOTTOM)


### GAME PLAY FUNCTIONS ###

def start_game(num_play):
	"""
	Initiates game play. Finds player number and creates hands.

	"""
	if ( (num_play != str(2)) and (num_play != str(4)) ):
		print("That is not 2 or 4 players! Please lose or gain a friend.",
			  "Restart the game when you have it figured out.",
			  sep="\n")

		exit(0)
	
	else:
		hand = hands.hand_size(num_play)
		
		return hand


def new_round(last):
	"""
	Contains method for new round
	Clears LastPlay stack and resets pass counter
	
	Takes LastPlay struct

	"""
	print("Clearing stack....", "Starting new round...", sep="\n")

	pass_cnt = 0

	last.card.empty()

	return pass_cnt


def single_turn(last, player, turn, count):
	"""

	last is last play struct
	player is a stack in the list
	turn is player number
	count is the passed counter

	Clear screen
	"""
	
	# Asks if player is ready to begin turn
	ready = input("Is player{} ready? Y/N > ".format(turn))
	
	if ready.lower() == "n":

		# Returns to turn if player says no
		print("Well then, please prepare yourself...\n")
		count = single_turn(last, player, turn, count)
		
		return count

	elif ready.lower() == "y":
		
		# Displays result of last play for reference
		last.display() 
		
		# Reveals hand to player
		print("Now displaying your hand.\n", "\n")
		print(player) 

		# Does the game play
		count = choose_play(last, player, count)
		
		return count

	else:
		print("Please answer Y or N.")
		count = single_turn(last, player, turn, count)
		
		return count


def move_val():
	"""
	Stores the player's card value

	"""

	print("Please enter the card value and suit you want to play.",
		  "For example, Ace of Spades or 2 of Diamonds.", sep="\n")
	value = input("> ")

	if len(value.split()) > 2:
		return value
	else:
		print("Let us try this again.", 
			  "This time, please enter VALUE and SUIT.", 
			  "See above examples.", sep="\n")
		move_val()
		return


def game_end():
	"""
	Contains small blurb and exit to end game

	"""
	clear()
	print("You just won the game!!!!!",
		  "Congratulations!", "Have a cake!", sep="\n")
	cake = """
                 ,   ,   ,   ,             
               , |_,_|_,_|_,_| ,           
           _,-=|;  |,  |,  |,  |;=-_       
         .-_| , | , | , | , | , |  _-.     
         |:  -|:._|___|___|__.|:=-  :|     
         ||*:  :    .     .    :  |*||     
         || |  | *  |  *  |  * |  | ||     
     _.-=|:*|  |    |     |    |  |*:|=-._ 
    -    `._:  | *  |  *  |  * |  :_.'    -
     =_      -=:.___:_____|___.: =-     _= 
        - . _ __ ___  ___  ___ __ _ . -   
        
        """
	
	print(cake)
	print("Ending capitalism in 10 sec...")
	sleep(10)
	exit(0)


def choose_play(last, player, count):
	"""
	
	last is last play struct
	player is the hand in the list

	Holds method for player decisions in game

	"""

	playing = input("Do you wish to play this turn? Y/N > ")

	if playing.lower() == "n":
		count += 1
		return count
	
	elif playing.lower() == "y":
		# Questions for player's move
		value = move_val()

		# Checks move validity
		if legality.valid_move(last, value, player):
			
			# Removes played cards from hand
			removed = player.get(value)
			
			# Updates last play struct
			last.new_play(removed)
			
			# Checks if game is over
			if len(player) == 0:
				game_end()
				return count

			else:
				
				count = 0

				return count

		else:
			print("That's not a valid move. Let's try this again.")
			count = choose_play(last, player, count)
			return count
	else:
		print("Please answer Y or N.")
		count = choose_play(last, player, count)
		return count


### MAIN ###

def main():

	clear()

	print("*** DIET CAPITALISM ***\n".center(columns))
	print("I feel like diet capitalism is capitalism based on virtual goods.",
		  "Similar to how diet products replace real sugar with synthetic sugars,",
		  "the material goods capitalism was founded upon are replaced",
		  "by virtual ones in an increasingly internet-based economy.", sep="\n")
	print("- Tristan Kitch, a friend")
	sleep(10)
	clear()

	num = input("Are there 2 or 4 people playing? > ")
	clear()

	recent = LastPlay()
	hands = start_game(num)
	i = 0
	pass_cnt = 0
	while (i < int(num)):
		clear()
		pass_cnt = single_turn(recent, hands[i], i+1, pass_cnt)
		print(pass_cnt)
		if pass_cnt == int(num):
			pass_cnt = new_round(recent)
			i = -1
		if i == (int(num) - 1):
			i = -1

		i += 1


if __name__ == "__main__":
	main()
