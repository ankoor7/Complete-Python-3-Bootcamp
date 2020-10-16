from deckOfCards.hand import Hand


class Dealer(Hand):
    def __init__(self, deck):
        self.hidden_card = []
        Hand.__init__(self)
        self.deck = deck

    def take_cards(self, card):
        if len(self.hidden_card) is 1:
            super().take_cards(card)
        else:
            self.hidden_card.extend(card[0:1])
            super().take_cards(card[1:])

    def reveal(self):
        self.cards.extend(self.hidden_card)
        self.hidden_card = []
        return self.is_bust()

    def play_turn(self):
        if not self.is_bust():
            self.take_cards(self.deck.deal())
