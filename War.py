# Programmer: David Gordon
# Class War
# Allows two players to play the card game "War"

# WAR instructions:
# Each player is shuffled half of the deck
# Each player then takes turns taking a card off the top of their deck
# The cards are compared and the one with the higher value takes both cards
# Whoever has more collected cards at the end wins the game

# Notes:

from random import random
import CardGame

Player1Default = "Player1"
Player2Default = "Player2"


class War(CardGame):
    # CardGame(self, name, cards=False)
    def __init__(self, player1 = False, player2 = False):

        self.timesPlayed = 0
        self.player1 = player1 or Player1Default
        self.liveDeck = self.cards

        # cards in live game deck
        self.player1Cards 
        self.player2Cards

        #
        self.player1WinCardPile
        self.player2WinCardPile
        
        # assigns player names - ensures no duplicate names
        if (self.player1 != player2 and self.player1 != Player2Default):
            self.player2 = player2 or Player2Default
        else:
            self.player2 = (player2 + "A") or (Player2Default + "A")

    def Shuffle(self):
        # nil -> nil
        # shuffles the live deck (only happens when the deck is fully used up in war)
        cardsCopy = self.cards.copy()
        shuffledDeck = []
        
        l = len(cardsCopy)
        while (l > 0):
            randNum = random.rangRange(0,(len(cardsCopy)-1))
            randCard = cardsCopy[randNum].pop(randNum)
            shuffledDeck.append(randCard)
            l -= 1

        return(shuffledDeck)

    def FindHighCardOf2(self, card1, card2):
        # card1 : dict, card2 : dict -> highercard : dict
        # finds the higher card of 2 given cards
        pass
    
    def GetTopCardFromPlayer(self, playerDeck):
        # playerDeck : array -> topCard : dict
        # pops the card from the top of a given deck
        pass

    def PlayRound(self):
        # nil -> nil
        # takes top card from each players live deck 
        # compares the two top cards
        # gives player with highcard both cards 
        pass

    def CalculateResult(self):
        # nil -> nil
        pass
