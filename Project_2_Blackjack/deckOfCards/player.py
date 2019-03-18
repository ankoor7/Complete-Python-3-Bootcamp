from deckOfCards.hand import Hand


class Player(Hand):
    def __init__(self, cash=0, cards=[]):
        Hand.__init__(self, cards)

        if not isinstance(cash, int) or cash <= 0:
            raise Exception('a player needs cash to play the game')

        self.cash = cash

    def bet(self, amount):
        if self.cash < amount:
            raise Exception('Cannot bet more than you own')

        self.cash -= amount
        return {
            "bet": amount,
            "stack_value": self.cash
        }

    def collect(self, amount):
        self.cash += amount
        return {
            "stack_value": self.cash
        }





