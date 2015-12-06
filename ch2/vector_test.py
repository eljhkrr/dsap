import unittest
from vector import Vector

class TestVetor(unittest.TestCase):

    def setUp(self):
        self.v = Vector([1, 2, 3, 4, 5])
        self.u = Vector([6, 7, 8, 9, 10])

    def test_len(self):
        self.assertEqual(len(self.v), 5)
        self.assertEqual(len(self.v), 5)

    def test_setget_item(self):
        self.assertEqual(self.v[0], 1)
        self.assertEqual(self.u[0], 6)
        self.v[1] = 20
        self.assertEqual(self.v[1], 20)
        self.u[3] = 40
        self.assertEqual(self.u[3], 40)

    def test_add(self):
        result = self.v + self.u
        self.assertEqual(str(result), "<7, 9, 11, 13, 15>")

    def test_sub(self):
        result = self.v - self.u
        self.assertEqual(str(result), "<-5, -5, -5, -5, -5>")
        result = self.u - self.v
        self.assertEqual(str(result), "<5, 5, 5, 5, 5>")

    def test_str(self):
        self.assertEqual(str(self.v), "<1, 2, 3, 4, 5>")
        self.assertEqual(str(self.u), "<6, 7, 8, 9, 10>")

    def test_neg(self):
        self.assertEqual(str(-self.v), "<-1, -2, -3, -4, -5>")
        self.assertEqual(str(-self.u), "<-6, -7, -8, -9, -10>")

    def test_mul(self):
        # scalar multiplication
        result = self.v * 4
        self.assertEqual(str(result), "<4, 8, 12, 16, 20>")
        # test dot product
        result = self.u * self.v
        self.assertEqual(result, 130)

if __name__ == "__main__":
    unittest.main()
