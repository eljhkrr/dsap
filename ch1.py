import unittest

def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False

def is_even(k):
    while k > 0:
        k -= 2
    return True if k == 0 else False

class TestCh1(unittest.TestCase):

    def test_ismultiple(self):
        self.assertTrue(is_multiple(2, 4))
        self.assertFalse(is_multiple(3, 4))
        self.assertFalse(is_multiple(4, 2))
        with self.assertRaises(ZeroDivisionError):
            is_multiple(0, 10)
            

if __name__ == '__main__':
    unittest.main()
