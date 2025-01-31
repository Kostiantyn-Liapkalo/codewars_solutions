import unittest
from codewars_solutions.utils import odd_count, is_isogram

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

if __name__ == "__main__":
    unittest.main()
