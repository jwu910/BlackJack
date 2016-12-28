# Black Jack
# Create a Black Jack game in Python 2.7

import random as r #use for generating card values

# Create a class of Player with Name and Hand
class Player(object):

	def __init__(self, name):
		self.name = name
		self.hand = []
		
	def add_card(self, card):
		self.hand.append(card)
		
# User input for number of players
try: # Need to learn how to add a loop on exception errors to request num 
	 # of players again instead of quit
	Player_Num = input("Number of Players = ") #Max 6 Players
except NameError:
	print "Invalid data type, must be number 1-6."
	quit()
except SyntaxError:
	print "Invalid data! Must enter number of players!"
	quit()

# Check if number of players is valid	
if Player_Num < 1:
	print "Need at least 1 player!"
	quit()
elif Player_Num+1 > 7:
	print "Too many players! Max 6 players."
	quit()


# Assign player names - create player objects
Players = []
for i in range(0,Player_Num):
	Players.append(raw_input("Enter player names = "))
Players.append("Dealer")
	
# Assign class name per player	
for i in range(len(Players)):
	Players[i] = Player(Players[i])
	print Players[i].name
	

	
# This is the deck, use index value for card number, Boolean for status of card in deck.	
Suit = {1:'H',2:'D',3:'S',4:'C'} 
Deck = [[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True]]

def draw_card(): # this function should draw card and return only card that was not previously drawn.
	Card_Suit = r.randint(1,4) # Generate card suit
	Card_Num = r.randint(1,13) # Generate card number
	card_val = 0
	while Deck[Card_Suit-1][Card_Num-1] == False: 
		Card_Suit = r.randint(1,4) # Generate card suit
		Card_Num = r.randint(1,13) # Generate card number
	if Deck[Card_Suit-1][Card_Num-1] == True:
		Deck[Card_Suit-1][Card_Num-1] = False
	#Card = str(Suit[Card_Suit]) + str(Card_Num)
	if Card_Num == 0:
		card_val = 11
	elif Card_Num > 0 and Card_Num < 10:
		card_val = Card_Num + 1
	elif Card_Num > 9:
		card_val = 10
	return [Card_Suit, Card_Num, card_val]


# Hand cards out for players
Drawn = 0
cont = False


while Drawn < 52:
	print "Total Cards on Table = ", Drawn
	#for i in #######################
	
	cont = raw_input("Continue? Y/N = ")
	if cont == "Y":
		if Drawn >= 52:
				for i in range(0,len(Players)):
					p = Players[i]
					print p.name, p.hand, "Hand total = ", sum(p.hand)
					quit()
		elif 52 - Drawn < Player_Num+1:
			print "Not enough cards."
			print 52-Drawn, " Cards left"
			quit()
		else:
			for i in range(0,Player_Num+1):
				p = Players[i]
				Card = draw_card()
				cardface = str(Suit[Card[0]]) + str(Card[1])
				p.add_card(Card[2]) # Need to add card as card value
				Drawn += 1 # Count number of cards drawn
				print "Player = ", p.name, "Card Drawn = ", cardface
				print "Hand total = ", sum(p.hand)# Print cards dealt this round
	else:
		print "Paused, enter 'Y' to continue."

