# Programmer: David Gordon
# Class CardGame
# Various CardGames in code form

# DESC: 
# base class for variouscard games
# full game details are determined by derived classes

# NOTES:
# further adaptation to specifics in derived classes

from array import array
from pydoc import doc

# GLOBAL VARS
# card arrays (separated to allow different card types for different games)
CardTypes = {2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"} #Ordered *typical* lowest to highest suit value
CardSuits = {"Clubs","Diamonds","Hearts","Spades"} #Ordered lowest to highest suit value

class CardGame:
    # base class for various card games
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
        return newDeck


War = CardGame("War")