# Black Jack
# Create a Black Jack game in Python 2.7

import random as r #use for generating card values


# User input for number of players
Player_Num = input("Number of Players = ") #Max 6 Players

Player_Names = []
for player in range(Player_Num):
	Player_Names.append(raw_input("Enter player names = "))

print Player_Names
Card_Suit = r.randint(1,4) # Generate card suit
Card_Num = r.randint(1,13) # Generate card number

print Card_Suit, Card_Num

# This is the deck, use index value for card number, Boolean for status of card in deck.
Deck = [[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True],
		[True,True,True,True,True,True,True,True,True,True,True,True,True]]
		
print Deck[Card_Suit-1][Card_Num-1]
Suit = ['H', 'D', 'S', 'C'] 
