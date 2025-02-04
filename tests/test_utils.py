import unittest
from codewars_solutions.utils import odd_count, is_isogram, find_outlier, tribonacci, create_phone_number, filter_list, encode_morse, decode_morse



class TestMorseCode(unittest.TestCase):

    def test_encode_morse(self):
        self.assertEqual(encode_morse("SOS"), "... --- ...")
        self.assertEqual(encode_morse("Hello"), ".... . .-.. .-.. ---")
        self.assertEqual(encode_morse("Morse Code"), "-- --- .-. ... . / -.-. --- -.. .")

    def test_decode_morse(self):
        self.assertEqual(decode_morse("... --- ..."), "SOS")
        self.assertEqual(decode_morse(".... . .-.. .-.. ---"), "HELLO")
        self.assertEqual(decode_morse("-- --- .-. ... . / -.-. --- -.. ."), "MORSE CODE")


class TestOddCount(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(odd_count(10), 5)
        self.assertEqual(odd_count(15), 7)
        self.assertEqual(odd_count(1), 0)
        self.assertEqual(odd_count(100), 50)

class TestIsIsogram(unittest.TestCase):
    def test_is_isogram(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)
        self.assertEqual(is_isogram("aba"), False)
        self.assertEqual(is_isogram("moOse"), False)
        self.assertEqual(is_isogram(""), True)
        self.assertEqual(is_isogram("isogram"), True)
        self.assertEqual(is_isogram("hello"), False)
        self.assertEqual(is_isogram("Alphabet"), False)

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


class CreatePhoneNumber(unittest.TestCase):
    def basic_test_case(self):
        self.assertEqual(create_phone_number([1,2,3,4,5,6,7,8,9,0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


class FilterList(unittest.TestCase):
    def basic_test_case(self):
        self.assertEqual(filter_list([1,2,'a','b']),"1,2")
        self.assertEqual(filter_list([1,'a','b',0,15]), "1,0,15")
        self.assertEqual(filter_list([1,2,'aasf','1','123',123]), "1,2,123")



# class DecodeMorse(unittest.TestCase):
#     def test_morse_hey_jude(self):
#         self.assertEqual(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
#
#     def test_morse_basic_examples(self):
#         self.assertEqual(decode_morse('.-'), 'A')
#         self.assertEqual(decode_morse('--...'), '7')
#         self.assertEqual(decode_morse('...-..-'), '$')
#         self.assertEqual(decode_morse('.'), 'E')
#         self.assertEqual(decode_morse('..'), 'I')
#         self.assertEqual(decode_morse('. .'), 'EE')
#         self.assertEqual(decode_morse('.   .'), 'E E')
#         self.assertEqual(decode_morse('...-..- ...-..- ...-..-'), '$$$')
#         self.assertEqual(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
#         self.assertEqual(decode_morse('.-... ---...   -..-. --...'), '&: /7')
#         self.assertEqual(decode_morse('...---...'), 'SOS')
#         self.assertEqual(decode_morse('... --- ...'), 'SOS')
#         self.assertEqual(decode_morse('...   ---   ...'), 'S O S')
#
#     def test_morse_extra_spaces(self):
#         self.assertEqual(decode_morse(' . '), 'E')
#         self.assertEqual(decode_morse('   .   . '), 'E E')
#
#     def test_morse_complex_example(self):
#         self.assertEqual(
#             decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
#             'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
#         )








if __name__ == "__main__":
    unittest.main()
