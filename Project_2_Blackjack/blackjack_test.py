import unittest
from deckOfCards.stack_test import StackTest
from deckOfCards.dealer_test import DealerTest


suite = unittest.TestSuite()
suite.addTests([StackTest()])

unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
