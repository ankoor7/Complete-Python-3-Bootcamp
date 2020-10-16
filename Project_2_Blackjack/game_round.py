from .deckOfCards.player import Player
from .deckOfCards.dealer import Dealer

class GameRound():
    def __init__(self, players, dealer):
        if not isinstance(players, list) or not isinstance(players[0], Player):
            raise Exception('players need to be in a game')

        if not isinstance(dealer, Dealer):
            raise Exception('a game needs a dealer')

        self.players = players
        self.dealer = dealer

    def play_round(self):
        self.dealer.play_turn()

        [player.play_turn() for player in self.players if not player.is_bust]

    def deal_initial_cards(self):
        [player.make_bet() for player in self.players]
        self.dealer.play_turn()
        [player.play_turn() for player in self.players]
        self.dealer.play_turn()
        [player.play_turn() for player in self.players]

