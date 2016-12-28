# Black Jack
# Create a Black Jack game in Python 2.7

import random as r #use for generating card values

# Create a class of Player with Name and Hand
def Class Player(Object):
	def __init__(self, Name, Hand):
		Player.Name = Name
		Player.Hand = []

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
elif Player_Num > 6:
	print "Too many players! Max 6 players."
	quit()


	
	
	

# Assign player names
Player_Names = []
for player in range(Player_Num):
	Player_Names.append(raw_input("Enter player names = "))	
	
# This is the deck, use index value for card number, Boolean for status of card in deck.	
Suit = {1:'H',2:'D',3:'S',4:'C'} 
Deck = [[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True]]

def draw_card(): # this function should draw card and return only card that was not previously drawn.
	Card_Suit = r.randint(1,4) # Generate card suit
	Card_Num = r.randint(1,13) # Generate card number
	while Deck[Card_Suit-1][Card_Num-1] == False: 
		Card_Suit = r.randint(1,4) # Generate card suit
		Card_Num = r.randint(1,13) # Generate card number
	if Deck[Card_Suit-1][Card_Num-1] == True:
		Deck[Card_Suit-1][Card_Num-1] = False
	#Card = str(Suit[Card_Suit]) + str(Card_Num)
	return [Card_Suit, Card_Num]


# Hand cards out for players
Drawn = 0
while Drawn < 52:
	for i in range(0,Player_Num):
		Card = draw_card()
		Drawn += 1 # Count number of cards drawn
		print str(Suit[Card[0]]) + str(Card[1]), Drawn
		
print Player_Names
print Deck[0]
print Deck[1]
print Deck[2]
print Deck[3]

