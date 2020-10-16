class Stack():
    def __init__(self, cash=0):
        if not isinstance(cash, int) or cash <= 0:
            raise Exception('a stack needs cash')

        self.reserve = cash
        self.stake = 0

    def bet(self, amount):
        if self.has_cash(amount):
            self.increase_bet(amount)
            return True

        return False

    def increase_bet(self, amount):
        self.reserve -= amount
        self.stake += amount

    def collect(self, amount):
        self.reserve += amount

    def take_stake(self):
        amount = self.stake
        self.stake = 0
        return amount

    def has_cash(self, amount):
        return self.reserve >= amount
