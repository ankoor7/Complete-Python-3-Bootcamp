import unittest
from deckOfCards.stack import Stack


class StackTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.cash = 400
        self.stack = Stack(self.cash)

    def runTest(self):
        self.test_bet()
        self.test_collect()
        self.test_has()
        self.test_instantiation()
        self.test_take_stake()

    def test_instantiation(self):
        this_stack = Stack(self.cash)
        self.assertEqual(400, this_stack.reserve)

    def test_collect(self):
        self.stack.collect(100)
        self.assertEqual(500, self.stack.reserve)

    def test_bet(self):
        self.assertFalse(self.stack.bet(401))
        self.assertEqual(400, self.stack.reserve)
        self.assertEqual(0, self.stack.stake)

        self.assertTrue(self.stack.bet(400))
        self.assertEqual(0, self.stack.reserve)
        self.assertEqual(400, self.stack.stake)

    def test_take_stake(self):
        self.assertTrue(self.stack.bet(400))
        self.assertEqual(400, self.stack.take_stake())
        self.assertEqual(0, self.stack.stake)

    def test_has(self):
        self.assertTrue(self.stack.has_cash(400))
        self.assertTrue(self.stack.has_cash(300))
        self.assertFalse(self.stack.has_cash(401))


if __name__ == '__main__':
    unittest.main()
