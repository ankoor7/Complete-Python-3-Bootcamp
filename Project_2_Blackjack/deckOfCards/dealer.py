from deckOfCards.hand import Hand


class Dealer(Hand):
    def __init__(self, cards):
        self.hidden_card = cards[0:1]
        Hand.__init__(self, cards[1:])

    def reveal(self):
        self.cards.extend(self.hidden_card)
        self.hidden_card = []
        return self.is_bust()

