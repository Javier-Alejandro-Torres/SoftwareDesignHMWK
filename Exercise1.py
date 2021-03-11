import unittest
import math

class TestStringMethods(unittest.TestCase):

    def test_rounding_UP(self):
        self.assertEqual(math.ceil(3.6), 4)

    def test_rounding_DOWN(self):
        self.assertEqual(math.ceil(3.2), 4)

    def test_rounding_negatives(self):
        self.assertEqual(math.ceil(-76.8), -76)

    def test_Decimals(self):
        self.assertEqual(math.ceil(0.8543),1)

    def test_Cero(self):
        self.assertEqual(math.ceil(0), 0)

    def test_Caracter_false(self):
        self.assertFalse(math.ceil(0), "a")

    def test_Caracter_true(self):
        self.assertTrue(math.ceil(1), 1)

    def test_Operations(self):
        self.assertEqual(math.ceil(4.4+3.9), 9)
        self.assertEqual(math.ceil(4.4 - 3.9), 1)
        self.assertEqual(math.ceil(4 * 3.2), 13)
        self.assertEqual(math.ceil(4 / 3.2), 2)
        self.assertEqual(math.ceil(math.sqrt(2)), 2)


if __name__ == '__main__':
    unittest.main()