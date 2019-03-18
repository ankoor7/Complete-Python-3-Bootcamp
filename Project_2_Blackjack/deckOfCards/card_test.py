import unittest
from deckOfCards.card import Card
from deckOfCards import Constants


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.two_of_hearts = Card(Constants.HEARTS, 'Two')

    def test_card_has_suit(self):
        self.assertEqual('Two', self.two_of_hearts.rank)
        self.assertEqual('Hearts', self.two_of_hearts.suit)

    def test_card_has_a_value(self):
        self.assertEqual(2, self.two_of_hearts.value)

    def test_str_representation(self):
        self.assertEqual('Two of Hearts', str(self.two_of_hearts))


if __name__ == '__main__':
    unittest.main()
