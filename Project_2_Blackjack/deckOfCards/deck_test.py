import unittest
from deckOfCards.deck import Deck

class MyTestCase(unittest.TestCase):
    def test_deck_size(self):
        this_deck = Deck()
        self.assertEqual(this_deck.stack, False)


if __name__ == '__main__':
    unittest.main()
