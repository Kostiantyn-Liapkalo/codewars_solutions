import unittest
from codewars_solutions.utils import odd_count, is_isogram, find_outlier

class TestOddCount(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(odd_count(10), 5)
        self.assertEqual(odd_count(15), 7)
        self.assertEqual(odd_count(1), 0)
        self.assertEqual(odd_count(100), 50)

class TestIsIsogram(unittest.TestCase):
    def test_is_isogram(self):
        self.assertTrue(is_isogram("Dermatoglyphics"))  # Усі символи унікальні
        self.assertFalse(is_isogram("aba"))  # 'a' повторюється
        self.assertFalse(is_isogram("moOse"))  # 'o' повторюється (нечутливе до регістру)
        self.assertTrue(is_isogram(""))  # Порожній рядок - ізограма
        self.assertTrue(is_isogram("isogram"))  # Усі символи унікальні
        self.assertFalse(is_isogram("hello"))  # 'l' повторюється
        self.assertFalse(is_isogram("Alphabet"))  # 'a' повторюється

class TestFindOutlier(unittest.TestCase):
    def test_find_outlier(self):
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)  # Один непарний
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)  # Один парний
        self.assertEqual(find_outlier([10, 8, 6, 4, 2, 7]), 7)  # Один непарний
        self.assertEqual(find_outlier([-21, -3, -7, 2, -9, -11]), 2)  # Один парний
        self.assertEqual(find_outlier([1, 3, 5, 7, 9, 2]), 2)  # Один парний


if __name__ == "__main__":
    unittest.main()
