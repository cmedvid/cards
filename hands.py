"""
This module creates the hands for players
"""



### IMPORTS ###

import pydealer as pyd


deck = pyd.Deck()
deck.shuffle()

### HAND CREATION ###

def hand_size(player):
	"""
	Depending on player number (2 or 4), assigns 
	hand sizes and creates and then 
	populates empty stacks for decks
	
	"""
	
	if player == str(2):
		cards = 26
	elif player == str(4):
		cards = 13
	else:
		print("Warning. There are too many or too little people here.")
		return
		
		
	hands = [pyd.Stack()] * int(player) # create empty stacks
	for i in range(int(player)):
		
		dealt = deck.deal(cards) # select hand size of  cards
		
		hands[i] += dealt # place cards into hand
		
		hands[i].sort() # sorts cards for player
	
	return hands



