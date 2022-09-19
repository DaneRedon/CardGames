# Programmer: David Gordon
# Class CardGame
# Various CardGames in code form

from array import array
from pydoc import doc


#Card Arrays (separated to allow different card types for different games)
CardTypes = {1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"}
CardSuits = {"Hearts","Clubs","Diamonds","Spades"}

class CardGame:

    def __init__(self, name, cards=False):
        self.cards = cards or self.CreateBaseDeck52()
        self.name = name

    def CreateBaseDeck52(self):
        # nil -> array of cards
        # {"CardName" : "Suit"}, allows for easy addition of more qualifiers
        newDeck = []
        for type in CardTypes:
            for suit in CardSuits:
                newDeck.append({"type": type, "suit": suit})
                # print(newDeck[len(newDeck)-1])
        return newDeck
            
War = CardGame("War")