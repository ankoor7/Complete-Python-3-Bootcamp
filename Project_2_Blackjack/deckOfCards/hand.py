class Hand():
    def __init__(self, new_cards=[]):
        self.cards = []
        self.take_cards(new_cards)

    def take_cards(self, new_cards):
        self.cards.extend(new_cards)

    def total(self):
        return sum([card.value for card in self.cards])

    def is_bust(self):
        return self.total() > 21

    def show(self):
        return [str(card) for card in self.cards]

