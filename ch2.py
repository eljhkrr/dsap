import unittest

class Flower:

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
        self._price = price

class TestCh2(unittest.TestCase):

    f = Flower("rose", 6, 100)

    def test_name(self):
        self.assertEqual(self.f.get_name(), "rose")

    def test_petals(self):
        self.assertEqual(self.f.get_petals(), 6)

    def test_price(self):
        self.assertEqual(self.f.get_price(), 100)

if __name__ == '__main__':
    unittest.main()
