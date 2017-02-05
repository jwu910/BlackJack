# Black Jack
# Create a Black Jack game in Python 2.7

import random as r # use for generating card values
import os , time # OS to clear screen, time to pause

# Built in python library for GUI development https://www.tutorialspoint.com/python/python_gui_programming.htm
# tink = Tkinter.Tk() 
# import Tkinter 
# tink.mainloop()	


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
		
	def has_ace(self, has_ace):
		'''
		boolean status to indicate if player is holding an ace.
		if they have an ace and their hand sum exceeds 21, change the value of the ace from 11 to 1.
		##Perhaps another way to check is 'if 11 in p.hand:'
		'''
		self.has_ace = has_ace

		
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
Players.append("Dealer")
	
# Assign class name per player	
for i in range(0,len(Players)):
	Players[i] = Player(Players[i])

	
for i in range(len(Players)):
	Players[i].status = "Playing"
	Players[i].has_ace = "False"


# This is the deck, use index value for card number, Boolean for status of card in deck.

Drawn = 0

Suit = {1:'H',2:'D',3:'S',4:'C'} 
DDeck = [[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True]]
Deck = [[True,True,True],
		[True,True,True],
		[True,True,True],
		[True,True,True]]



def draw_card(): # this function should draw card and return only card that was not previously drawn.
	Card_Suit = r.randint(1,4) # Generate card suit
	Card_Num = r.randint(1,3) # Generate card number
	card_val = 0
	while Deck[Card_Suit-1][Card_Num-1] == False:
		Card_Suit = r.randint(1,4) # Generate card suit
		Card_Num = r.randint(1,3) # Generate card number
	if Deck[Card_Suit-1][Card_Num-1] == True:
		Deck[Card_Suit-1][Card_Num-1] = False
	if Card_Num == 1: # Need or statement options for ace == 1 or ace == 11.
		card_val = 11
		p.has_ace = True
	elif Card_Num > 1 and Card_Num < 10:
		card_val = Card_Num
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

def hit_stand():
	while True:
		hit = raw_input("Hit or Stand? H/S = ")
		if hit.upper() == "H" or hit.upper() == "S":
			return hit.upper()
			break
		else:
			print "Invalid answer."
	return hit.upper()
		
valid_answers = ['H','S']
hit = ""

# Draw initial 2 cards for players
for player in Players:
	for i in range(len(Players)):
		p =	Players[i]
		if p.name == "Dealer" and len(p.hand) > 0:
			Card = draw_card()
			cardface = "***"
			hidden = str(Suit[Card[0]]) + str(Card[1])
			p.add_card(Card[2],cardface)
			if int(Card[1]) == 0:
				p.has_ace = "True"
		else:
			Card = draw_card()
			cardface = str(Suit[Card[0]]) + str(Card[1])
			
			if int(Card[1]) == 0:
				print "CARD[1] == 0 ---DEBUG"
				time.sleep(10)
				if p.has_ace == False:
					p.has_ace = True
				elif p.has_ace == True:
					Card[2] = 1

			p.add_card(Card[2],cardface)
		Drawn += 1
		
print_current()		
	
#quit()
# -----------------------------Deal---------------------------------------
print_current()
#
#	print p.name, p.status
for i in range(0,len(Players)):
	p = Players[i]
	if p.name != "Dealer": # Perform actions for players
		while sum(p.hand) <21:
			hit = hit_stand()
			if hit == "H":
				Card = draw_card()
				cardface = str(Suit[Card[0]]) + str(Card[1])
				# If statement to check for valid ace value
				if Card[2] == 11:
					if p.has_ace == False: # Player did not have ace, now marking ace.
						p.has_ace = True
					if sum(p.hand) + Card[2] > 21:
						Card[2] = 1
				else: # Check if player hand already has ace, if so, replace value of 11 with 1 if current card causes hand to exceed 21.
					if p.has_ace == True:
						if sum(p.hand) + Card[2] > 21:
							p.hand[p.hand.index(11)] = 1 # This line should search for value 11 in p.hand and change to 1

				p.add_card(Card[2],cardface)
				Drawn += 1
				print_current()
			elif hit == "S":
				p.status = "standing."
				print_current()
				break

		if sum(p.hand) > 21:
			p.status = "busted!"
			print_current()
			break
	 	
	elif p.name == "Dealer": # Perform Dealer actions
		while sum(p.hand) < 17:
			hit = "H"
			time.sleep(1)
			if hit == "H":
				Card = draw_card()
				cardface = str(Suit[Card[0]]) + str(Card[1])
				p.add_card(Card[2],cardface)
				p.card_faces[1] = hidden
				Drawn += 1
				print_current()
			elif hit == "S":
				p.status = "standing."
				p.card_faces[1] = hidden
				print_current()
				break
				
		if sum(p.hand) >= 17:
			p.status = "standing."
			p.card_faces[1] = hidden
			print_current()
		if sum(p.hand) > 21:
			p.status = "busted!"
			print_current()
			break
		
################################################# End player turns ########################################################
# Start results checking
index = 0
results = []

for i in Players[::]:
	p = Players[index]
	if sum(p.hand) < 22:
		results.append(sum(p.hand))
	else:
		results.append(0)
	index += 1
	

index = 0
for i in Players[::]:
	p = Players[index]
	if sum(p.hand) == max(results):
		print p.name, "wins!"
	if len(set(results)) == 1:
		print "Draw! Push!"
	index += 1

print Players[0].hand