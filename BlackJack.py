# Black Jack
# Create a Black Jack game in Python 2.7

import random as r # use for generating card values
import os # to clear screen

# Create a class of Player with Name and Hand
class Player(object):

	def __init__(self, name):
		self.name = name
		self.hand = []
		self.card_faces = []
		
	def add_card(self, card, cardface):
		self.hand.append(card)
		self.card_faces.append(cardface)
		
	def status(self, status):
		self.status = status

Player_Num = 2
		
# User input for number of players
#try: # Need to learn how to add a loop on exception errors to request num 
#	 # of players again instead of quit
#	Player_Num = input("Number of Players = ") #Max 6 Players
#except NameError:
#	print "Invalid data type, must be number 1-6."
#	quit()
#except SyntaxError:
#	print "Invalid data! Must enter number of players!"
#	quit()

# Check if number of players is valid	
#if Player_Num < 1:
#	print "Need at least 1 player!"
#	quit()
#elif Player_Num+1 > 7:
#	print "Too many players! Max 6 players."
#	quit()


# Assign player names - create player objects
Players = []
#for i in range(0,Player_Num):
Players.append(raw_input("Enter player name = "))
print Players
Players.append("Dealer")
print Players
	
# Assign class name per player	
for i in range(0,len(Players)):
	Players[i] = Player(Players[i])

	
for i in range(len(Players)):
	Players[i].status = "Playing"
	
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
	if Card_Num == 0: # Need or statement options for ace == 1 or ace == 11.
		card_val = 11
	elif Card_Num > 0 and Card_Num < 10:
		card_val = Card_Num + 1
	elif Card_Num > 9:
		card_val = 10
	return [Card_Suit, Card_Num, card_val]


# Keeps list of current players and their hands on top of terminal
def print_current():
	try:
		os.system('clear')
	#except:
		os.system('cls')
	finally:
		print "Current Players = "
		for i in range(0,len(Players)):
			p = Players[i]
			print p.name, "is", p.status
			print p.card_faces, sum(p.hand)
		print "---------------------------------------------"
		print "Total Cards on Table = ", Drawn
		print "---------------------------------------------"


Drawn = 0
valid_answers = ['H','S']


# Draw initial 2 cards for players
for player in Players:
	for i in range(len(Players)):
		p =	Players[i]
		if p.name == "Dealer" and len(p.hand) > 0:
			Card = draw_card()
			cardface = "***"
			p.add_card(Card[2],cardface)
		else:
			Card = draw_card()
			cardface = str(Suit[Card[0]]) + str(Card[1])
			p.add_card(Card[2],cardface)
		Drawn += 1
		
		
		
		
# -----------------------------Deal---------------------------------------
print_current()
for i in range(0,len(Players)):
	p = Players[i]
	while p.name != "Dealer" and p.status == "Playing":
		print_current()
		print 'Current player is =',p.name
		while True:
			hit = raw_input("Hit or Stay? H/S = ")
			if hit.upper == answer.upper() in valid_answers:
				if hit.upper == "H":
					Card = draw_card()
					cardface = str(Suit[Card[0]]) + str(Card[1])
					p.add_card(Card[2],cardface)
					Drawn += 1
					print_current()
					if sum(p.hand) > 21:
						p.status = "busted!"
						print_current()
						continue
						break
					print_current()
				elif hit.upper == "S":
					p.status = "standing."
					print_current()
					break
				else:
					print "this is where we're stuck"
	if sum(p.hand) > 21:
		p.status = "busted!"
	