import random

ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        return f"{self.rank[0]} of {self.suit}"

class Deck:
    def __init__(self):
        self.full_deck = []
        for s in suits:
            for r in ranks:
                self.full_deck.append(Card((r, ranks.get(r)), s))

    def shuffle_deck(self):
        random.shuffle(self.full_deck)

    def give_card(self):
        self.full_deck.pop(-1)

    def give_start_hand(self):
        return [self.full_deck.pop(-1), self.full_deck.pop(-1)]
