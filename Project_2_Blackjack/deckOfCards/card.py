from deckOfCards import Constants


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Constants.values[self.rank]
        return

    def __str__(self):
        return f'{self.rank} of {self.suit}'
