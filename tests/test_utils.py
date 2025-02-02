import unittest
from codewars_solutions.utils import odd_count, is_isogram, find_outlier, tribonacci

class TestOddCount(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(odd_count(10), 5)
        self.assertEqual(odd_count(15), 7)
        self.assertEqual(odd_count(1), 0)
        self.assertEqual(odd_count(100), 50)

class TestIsIsogram(unittest.TestCase):
    def test_is_isogram(self):
        self.assertTrue(is_isogram("Dermatoglyphics"))
        self.assertFalse(is_isogram("aba"))
        self.assertFalse(is_isogram("moOse"))
        self.assertTrue(is_isogram(""))
        self.assertTrue(is_isogram("isogram"))
        self.assertFalse(is_isogram("hello"))
        self.assertFalse(is_isogram("Alphabet"))

class TestFindOutlier(unittest.TestCase):
    def test_find_outlier(self):
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
        self.assertEqual(find_outlier([10, 8, 6, 4, 2, 7]), 7)
        self.assertEqual(find_outlier([-21, -3, -7, 2, -9, -11]), 2)
        self.assertEqual(find_outlier([1, 3, 5, 7, 9, 2]), 2)



class TestTribonacci(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
        self.assertEqual(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])

    def test_edge_cases(self):
        self.assertEqual(tribonacci([1, 1, 1], 1), [1])
        self.assertEqual(tribonacci([1, 1, 1], 2), [1, 1])
        self.assertEqual(tribonacci([1, 1, 1], 3), [1, 1, 1])
        self.assertEqual(tribonacci([1, 1, 1], 0), [])
        self.assertEqual(tribonacci([5, 5, 5], 6), [5, 5, 5, 15, 25, 45])









if __name__ == "__main__":
    unittest.main()
