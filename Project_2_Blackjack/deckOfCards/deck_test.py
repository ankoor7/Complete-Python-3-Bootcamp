import unittest
from deckOfCards.deck import Deck


class DeckTest(unittest.TestCase):
    def test_deck_size(self):
        this_deck = Deck()
        self.assertEqual(len(this_deck.stack), 52)

    def test_shuffle_deck(self):
        this_deck = Deck()
        initial_order = [str(card) for card in this_deck.stack]

        this_deck.shuffle()

        final_order = [str(card) for card in this_deck.stack]
        self.assertNotEqual(initial_order, final_order, 'Deck is not shuffled')
        self.assertTrue(len(this_deck.stack), 52)

    def test_deal(self):
        this_deck = Deck()

        hand = this_deck.deal(4)
        self.assertEqual(48, len(this_deck.stack))
        self.assertEqual(4, len(hand))

        hand = this_deck.deal(3)
        self.assertEqual(45, len(this_deck.stack))
        self.assertEqual(3, len(hand))

        hand = this_deck.deal(10000000)
        self.assertEqual(0, len(this_deck.stack))
        self.assertEqual(45, len(hand))

        hand = this_deck.deal(10000000)
        self.assertEqual(0, len(this_deck.stack))
        self.assertEqual(0, len(hand))


if __name__ == '__main__':
    unittest.main()
