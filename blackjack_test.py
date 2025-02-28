import unittest
import deck
import player


class MyTestCase(unittest.TestCase):
    test_deck = deck.Deck()

    def test_cards(self):
        self.assertEqual(52, len(self.test_deck.full_deck))

    def test_give_card(self):
        test = deck.Deck()
        card = test.give_card()
        self.assertEqual(51, len(test.full_deck))
        self.assertFalse(card in test.full_deck)

    def test_shuffle(self):
        test = self.test_deck.full_deck.copy()
        self.assertEqual(test, self.test_deck.full_deck)
        self.test_deck.shuffle_deck()
        self.assertNotEqual(test, self.test_deck.full_deck)

    def test_give_start_hand(self):
        test = deck.Deck()
        hand = test.give_start_hand()
        self.assertEqual(2, len(hand))

    def test_sum_hand(self):
        test_cards = [deck.Card(('Ace',11), 's'), deck.Card(('Ace',11), 's')]
        p = player.Player(False, 100, test_cards)
        self.assertEqual(12, p.sum_hand())

if __name__ == '__main__':
    unittest.main()
