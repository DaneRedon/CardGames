# Programmer: David Gordon
# Class CardGame
# Various CardGames in code form

from array import array
from pydoc import doc

#Card Arrays (separated to allow different card types for different games)
CardTypes = {1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"}
CardSuits = {"Hearts","Clubs","Diamonds","Spades"}

class CardGame:

    def __init__(self, cards:array):
        Cards = cards

    def creatBaseDeck52():
        # nil -> array of cards
        # {"CardName" : "Suit"}, allows for easy addition of more qualifiers
        newDeck = None
        for type in CardTypes:
            for suit in CardSuits:
                newDeck.append({"type": type, "suit": suit})
        return newDeck
            

#War = CardGame.new #not implemented yet