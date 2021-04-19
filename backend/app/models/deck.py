# Deck Model.
# on init creates a deck in "frech pack" order.
# getMappedDeck returns the deck with the values of the cards.
# S = Spades
# D = Diamonds
# H = Hearts
# C = Clubs
# K = King
# Q = Queen
# J = Jack
# A = Ace
# Different shuffling techniques taken from https://www.wikihow.com/Shuffle-a-Deck-of-Playing-Cards
import random
from utils.spearmans import Spearman
class Deck:
    def __init__(self):
        self.history = []

        self.card_mapping = {
        0: "AS",1: "2S",2: "3S",3: "4S",4: "5S",5: "6S",6: "7S",7: "8S",8: "9S",9: "10S",10: "JS",11: "QS",
        12: "KS",13: "AD",14: "2D",15: "3D",16: "4D",17: "5D",18: "6D",19: "7D",20: "8D",21: "9D",22: "10D",23: "JD",
        24: "QD",25: "KD",26: "KC",27: "QC",28: "JC",29: "10C",30: "9C",31: "8C",32: "7C",33: "6C",34: "5C",35: "4C",
        36: "3C",37: "2C",38: "AC",39: "KH",40: "QH",41: "JH",42: "10H",43: "9H",44: "8H",45: "7H",46: "6H",47: "5H",
        48: "4H",49: "3H",50: "2H",51: "1H",52: "AH",
        }

        self.deck = [0, 1, 2, 3, 4, 5, 6, 7, 8,
       9, 10, 11, 12, 13, 14, 15,
       16, 17, 18, 19, 20, 21, 22, 
       23, 24, 25, 26, 27, 28, 29,
       30, 31, 32, 33, 34, 35, 36,
       37, 38, 39, 40, 41, 42, 43, 
       44, 45, 46, 47, 48, 49, 50,
       51]


    def getMappedDeck(self):
        return [self.card_mapping[x] for x in self.deck]
    
    def getUnMappedDeck(self):
        return self.deck

    def get_shuffle_history(self):
        return self.history

    def shuffle_riffle(self, times: int = 1):
        """ This i an implementation of a "perfect" riffle """
        for j in range(0,times):
            deck = self.deck.copy()
            first_half = deck[0:len(deck)//2][::-1]
            second_half = deck[len(deck)//2::][::-1]
            new_deck = []
            for i in range(len(first_half)):
                new_deck.append(first_half[i])
                new_deck.append(second_half[i])
            self.deck = new_deck.copy()
            self.history.append([self.card_mapping[x] for x in self.deck])


        
    def shuffle_overhand(self, times: int = 1):
        for j in range(0,times):
            deck = self.deck.copy()
            start = random.randrange(13,23)
            stop = random.randrange(27,37)
            third = deck[start:stop]
            new_deck = deck[0:start]
            new_deck.extend(deck[stop::])
            new_deck =  third + new_deck
            self.deck = new_deck.copy()
            self.history.append([self.card_mapping[x] for x in self.deck])

    def shuffle_hindu(self,times: int = 1):
        for j in range(0,times):
            deck = self.deck.copy()
            new_deck = []
            while deck:
                stop = random.randrange(5,10)
                new_deck = deck[0:stop] + new_deck
                deck = deck[stop::]
            self.deck = new_deck.copy()
            self.history.append([self.card_mapping[x] for x in self.deck])


    def calculate_difference(self,a: list):
        spearman = Spearman()

        return spearman.calculate(a,self.getUnMappedDeck())


