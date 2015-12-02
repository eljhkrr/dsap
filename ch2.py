import unittest

class Flower:
    """A botanical flower"""

    def __init__(self, name, petals, price):
        """Create new flower instance.

        name    the name of the flower
        petals  the number of petals that the flower has
        price   the price of the flower
        """
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        """Return name of the flower"""
        return self._name

    def get_petals(self):
        """Return number of petals that the flower has"""
        return self._petals

    def get_price(self):
        """Return the price of the flower"""
        return self._price

    def set_name(self, name):
        """Set the name of the flower"""
        self._name = name

    def set_petals(self, petals):
        """Set the number of petals for the flower"""
        self._petals = petals

    def set_price(self, price):
        """Set the price of the flower"""
        self._price = price

class TestCh2(unittest.TestCase):

    f = Flower("rose", 6, 100)

    def test_name(self):
        self.assertEqual(self.f.get_name(), "rose")
        self.f.set_name("cherry")
        self.assertEqual(self.f.get_name(), "cherry")

    def test_petals(self):
        self.assertEqual(self.f.get_petals(), 6)
        self.f.set_petals(10)
        self.assertEqual(self.f.get_petals(), 10)

    def test_price(self):
        self.assertEqual(self.f.get_price(), 100)
        self.f.set_price(200)
        self.assertEqual(self.f.get_price(), 200)

if __name__ == '__main__':
    unittest.main()
