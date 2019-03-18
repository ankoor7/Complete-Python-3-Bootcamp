from deckOfCards import Constants
from deckOfCards.card import Card

class Deck:
    def __init__(self):
        self.stack = [Card(suit, rank) for rank in Constants.ranks for suit in Constants.suits]


