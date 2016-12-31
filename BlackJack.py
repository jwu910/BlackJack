# Black Jack
# Create a Black Jack game in Python 2.7

import random as r # use for generating card values
import os # to clear screen
# Create a class of Player with Name and Hand
class Player(object):

	def __init__(self, name):
		self.name = name
		self.hand = []
		
	def add_card(self, card):
		self.hand.append(card)
		
	def status(self, status):
		self.status = status
	# def fold(self, p):
		# self.hand.pop(p)
		
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
	if Card_Num == 0:
		card_val = 11
	elif Card_Num > 0 and Card_Num < 10:
		card_val = Card_Num + 1
	elif Card_Num > 9:
		card_val = 10
	return [Card_Suit, Card_Num, card_val]


# Keeps list of current players and their hands on top of console
def print_current():
	os.system('clear')
	print "Current Players = "
	for i in range(len(Players)):
		if sum(p.hand) > 21:
			continue
		else:
			print Players[i].name, "is", Players[i].status
			print Players[i].hand, sum(Players[i].hand)
	print "---------------------------------------------"
	print "Total Cards on Table = ", Drawn
	print "---------------------------------------------"
	
	
# Hand cards out for players
Drawn = 0

while sum(Players[len(Players)-1].hand) < 21:
	for i in range(0,len(Players)): # Cycle through all players
		p = Players[i]
		index = 0
		# Check if player is still playing
		
		############################################# WORKING #########################################
		if all(Players[i].status == "busted!" for Player in Players):
			print "Dealer wins!!!!!!!!!"
			quit()
		
		# need to add winning conditions for dealer as well as winning conditions for players.
		
		
		if p.status == "Playing" and sum(p.hand) < 21:
			print_current()
			print "Current Player is", p.name
			hit = raw_input("Hit or Stay? H/S = ")
			if hit == "H" or hit == "h":
				Card = draw_card()
				p.add_card(Card[2])
			elif hit == "S" or hit == "s":
				continue
		if sum(p.hand) > 21:
			p.status = "busted!"
			continue
if sum(Players[len(Players)-1].hand) > 21:
	print_current()
	print "Dealer has busted!"
	print "Remaining payers win!"
	
	
	
	
	
#	while p.status == "Playing" and index == i:
#		if sum(p.hand) < 21:
#			print_current()
#			print "Current Player is", p.name
#			hit = raw_input("Hit or Stay? H/S = ")
#			if hit == "H" or hit == "h":
#				Card = draw_card()
#				p.add_card(Card[2])
#				Drawn += 1
#				print "next"
#			continue
#		else:
#			print p.name, "has busted!"
#			p.status = "Folded!"
#	index += 1
#	continue	


					   
					   
					   
#while Drawn < 52:
#	print_current()
#	
#	for i in range(0,len(Players)):
#		if sum(Players[len(Players)-1].hand) > 21:
#			print sum(Players[len(Players)-1].hand)
#			print "Dealer Busted! Players win!"
#			print "Next Round!, Play Again?"
#			quit()
#		elif sum(Players[i-1].hand) > 21:
#			Players[i-1].status = "Busted!"
#			next
#		try:
#			if sum(Players[i-1].hand) > 21:
#				p = Players[i-1]
#				print p.name, "'s hand is over 21! Bust!!"
#				Players.pop(i-1)
#				p.status = "Busted!"
#
#		except IndexError:
#			print i
#			print Players
#			
#	if Drawn >= 52:
#			for i in range(0,len(Players)):
#				print p.name, p.hand, "Hand total = ", sum(Players[i].hand)
#				quit()
#	
#	elif 52 - Drawn < len(Players):
#		print "Not enough cards."
#		print 52-Drawn, " Cards left"
#		quit()
#	
#	else:
#		for i in range(0,len(Players)):
#			p = Players[i]
#			if p.status == "Playing":
#			# Add sum(p.hand) and see if player would like to hit or stay
#				print "Current Player: ", p.name
#				print "Hand total: ", sum(p.hand)
#				if p.name == "Dealer":
#					hit = "H"
#				else:
#					hit = raw_input("Hit or Stay? H/S = ")
#				if hit == "H":
#					Card = draw_card()
#					cardface = str(Suit[Card[0]]) + str(Card[1])
#					p.add_card(Card[2]) # Need to add card as card value
#					Drawn += 1 # Count number of cards drawn
#					print_current()
#					print "Player: ", p.name, "Card Drawn: ", cardface
#					print "Hand total: ", sum(p.hand)# Print cards dealt this round
#					print "---------------------------------------------"
#				elif hit == "S":
#					continue
#			elif p.status == "Folded!":
#				next
#	
#
#