class Hand():
    def __init__(self):
        self.cards = []

    def take_cards(self, new_cards):
        self.cards.extend(new_cards)

    def hand_value(self):
        return sum([card.value for card in self.cards])

    def is_bust(self):
        return self.hand_value() > 21

    def show(self):
        return [str(card) for card in self.cards]

