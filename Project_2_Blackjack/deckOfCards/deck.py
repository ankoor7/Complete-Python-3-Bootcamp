from random import shuffle
from deckOfCards import constants
from deckOfCards.card import Card
from itertools import islice


class Deck:
    def __init__(self):
        self.stack = [Card(suit, rank) for rank in constants.ranks for suit in constants.suits]

    def shuffle(self):
        shuffle(self.stack)

    def deal(self, n=1):
        cards = self.stack[0:n]
        self.stack = self.stack[n:]
        return cards

    def number_of_cards_left(self):
        return len(self.stack)

