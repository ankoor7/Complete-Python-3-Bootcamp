from deckOfCards.hand import Hand
from deckOfCards.stack import Stack
from blackjack import get_input, number_validator


class Player(Hand):
    def __init__(self, deck, cash=0):
        Hand.__init__(self)
        self.stack = Stack(cash)
        self.deck = deck

    def play_turn(self):
        if not self.is_bust():
            self.take_cards([self.deck.deal()])

    def make_bet(self):
        amount = get_input('Make a bet: ', number_validator)
        self.stack.bet(amount)
