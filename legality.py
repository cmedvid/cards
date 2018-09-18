import pydealer as pyd

def valid_move(last, value, player):
	"""
	From LastPlay struct, compares the previous 
	played card's value to the proposed play.
	Must follow the rules.

	last is LastPlay struct
	value is card
	player is the hand attributed to that player

	returns Boolean

	"""

	# Turn string value into card type
	new_card = player.get(str(value))
	
	# Return card to hand after looking at it
	player.add(new_card)

	player.sort()

	if len(new_card) == 0:
		return False
	
	else:
		# First play is always valid
		if len(last.card) == 0:
			return True
		
		# If not the first play
		else:

			new_card_stack = pyd.Stack()   #  For comparison, both must be in a stack
			new_card_stack.add(new_card)
			if new_card[0] > last.card[0]:
				return True
			else:
				return False


