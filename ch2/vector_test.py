import unittest
from vector import Vector

class TestVetor(unittest.TestCase):

    def setUp(self):
        self.v = Vector(5)

    def test_len(self):
        self.assertEqual(len(self.v), 5)

    def test_setget_item(self):
        self.v[1] = 20
        self.assertEqual(self.v[1], 20)
        self.v[3] = 40
        self.assertEqual(self.v[3], 40)

    def test_add(self):
        self.v[0] = 45
        self.v[4] = 32
        u = Vector(5)
        u[0] = 12
        u[1] = 76
        result = self.v + u
        self.assertEqual(str(result), "<57, 76, 0, 0, 32>")

    def test_sub(self):
        u = Vector(5)
        u[0] = 23
        u[3] = 43
        result = self.v - u
        self.assertEqual(str(result), "<-23, 0, 0, -43, 0>")

    def test_str(self):
        self.assertEqual(str(self.v), "<0, 0, 0, 0, 0>")
        

if __name__ == "__main__":
    unittest.main()
