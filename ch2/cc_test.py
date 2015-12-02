from cc import CreditCard
import unittest

class TestCreditCard(unittest.TestCase):

    def test_charge(self):
        card = CreditCard("Mr. Test", "TBank Inc", "20 677 880", 1000)
        with self.assertRaises(ValueError):
            card.charge("abcd")

    def test_make_payment(self):
        card = CreditCard("Mr. Test", "TBank Inc", 200, 1000)
        with self.assertRaises(ValueError):
            card.make_payment("a")

            
if __name__ == '__main__':
    unittest.main()
