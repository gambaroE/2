import unittest

from somma import somma, check

class TestSommaFunction(unittest.TestCase):

    def test_somma(self):
        # Test with positive integers
        self.assertEqual(somma([1, 2, 3]), 6)
        # Test with negative integers
        self.assertEqual(somma([-1, -2, -3]), -6)
        # Test with a mix of positive and negative integers
        self.assertEqual(somma([1, -2, 3]), 2)
        # Test with an empty list
        self.assertEqual(somma([]), 0)

    def test_check_valid_input(self):
        # Test with valid input
        self.assertEqual(check("1,2,3"), [1, 2, 3])
        # Test with a single integer
        self.assertEqual(check("5"), [5])
        # Test with negative integers
        self.assertEqual(check("-1,-2,-3"), [-1, -2, -3])
        # Test with spaces around integers
        self.assertEqual(check(" 1 ,  2,3 "), [1, 2, 3])

    def test_check_invalid_input(self):
        # Test with non-integer input
        with self.assertRaises(ValueError):
            check("1,2,3a")
        # Test with empty input
        with self.assertRaises(ValueError):
            check("")
        # Test with input containing non-integer characters
        with self.assertRaises(ValueError):
            check("1,2,3,4.5")

if __name__ == '__main__':
    unittest.main()
