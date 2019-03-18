from deckOfCards.player import Player


class Dealer(Player):
    def __init__(self, cards):
        self.hidden_card = cards[0:1]
        Player.__init__(self, cards[1:])

    def reveal(self):
        self.cards.append(self.hidden_card)
        return self.total()