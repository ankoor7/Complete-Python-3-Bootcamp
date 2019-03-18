import unittest
from .deck import Deck
from .hand import Hand
from .card import Card
from deckOfCards import constants


class HandTest(unittest.TestCase):
    def test_instantiation(self):
        this_hand = Hand()
        this_hand.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertEqual(2, len(this_hand.cards))

    def test_take_cards(self):
        this_deck = Deck()
        this_hand = Hand()
        this_hand.take_cards(this_deck.deal(4))

        self.assertEqual(48, len(this_deck.stack))
        self.assertEqual(4, len(this_hand.cards))

    def test_total(self):
        this_hand = Hand()
        this_hand.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertEqual(5, this_hand.total())

        this_hand.take_cards([Card(constants.HEARTS, 'Four')])
        self.assertEqual(9, this_hand.total())

    def test_is_bust(self):
        this_hand = Hand()
        this_hand.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertFalse(this_hand.is_bust())

        this_hand.take_cards([Card(constants.HEARTS, 'Queen'), Card(constants.HEARTS, 'King')])
        self.assertTrue(this_hand.is_bust())

    def test_show_hand(self):
        this_hand = Hand()
        this_hand.take_cards([Card(constants.HEARTS, 'Two'), Card(constants.HEARTS, 'Three')])
        self.assertSequenceEqual(['Two of Hearts', 'Three of Hearts'], this_hand.show())


if __name__ == '__main__':
    unittest.main()
