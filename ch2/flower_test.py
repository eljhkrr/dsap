from flower import Flower
import unittest

class TestFlower(unittest.TestCase):

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
