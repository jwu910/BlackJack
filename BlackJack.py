# Black Jack
# Create a Black Jack game in Python 2.7

import random as r #use for generating card values


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

print Player_Names # Print just for testing

def draw_card():
	Suit = {1:'H',2:'D',3:'S',4:'C'} 
	Card_Suit = r.randint(1,4) # Generate card suit
	Card_Num = r.randint(1,13) # Generate card number
	Card = str(Suit[Card_Suit]) + str(Card_Num)
	return(Card)

# This is the deck, use index value for card number, Boolean for status of card in deck.

Deck = [[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True]]
		

#print Deck[Card_Suit-1][Card_Num-1] # Print just for testing



#print Card_Suit, Card_Num # Print just for testing
print draw_card()
# Hand cards out for players
