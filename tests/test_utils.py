import unittest
from codewars_solutions.utils import odd_count, is_isogram, find_outlier, tribonacci, create_phone_number, filter_list, encode_morse, decode_morse, narcissistic, alphabet_position, delete_nth, generate_hashtag,solution




class TestRangeExtraction(unittest.TestCase):

    def test_example(self):
        args = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
        expected = "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
        self.assertEqual(solution(args), expected)

    def test_single_number(self):
        # Test for the case where there is only one number in the list.
        args = [1]
        expected = "1"
        self.assertEqual(solution(args), expected)

    def test_two_consecutive_numbers(self):
        # If the sequence consists of only 2 numbers,
        # # they do not form a range, so "1,2" is expected, not "1-2".
        args = [1, 2]
        expected = "1,2"
        self.assertEqual(solution(args), expected)

    def test_simple_range(self):
        # If the sequence has 3 or more numbers, it must form a range.
        args = [1, 2, 3, 4, 5]
        expected = "1-5"
        self.assertEqual(solution(args), expected)

    def test_mixed_ranges(self):
        # Mixed sequence test with individual numbers and ranges.
        args = [1, 2, 4, 5, 6, 8, 9, 10, 11, 13]
        expected = "1,2,4-6,8-11,13"
        self.assertEqual(solution(args), expected)

    def test_non_consecutive(self):
        # Test for a list where there are no consecutive numbers at all.
        args = [1, 3, 5, 7]
        expected = "1,3,5,7"
        self.assertEqual(solution(args), expected)



class GenerateHashtag(unittest.TestCase):
    def test_generate_hashtag(self):
        self.assertEqual(generate_hashtag("Hello there thanks for trying my Kata"), "#HelloThereThanksForTryingMyKata")
        self.assertEqual(generate_hashtag("    Hello     World   "), "#HelloWorld")
        self.assertEqual(generate_hashtag(""), False)
        self.assertEqual(generate_hashtag("a" * 140), False)
        self.assertEqual(generate_hashtag("code wars"), "#CodeWars")
        self.assertEqual(generate_hashtag("  "), False)
        self.assertEqual(generate_hashtag("test"), "#Test")


class DeleteNth(unittest.TestCase):

    def test_delete_nth(self):
        self.assertEqual(delete_nth([1,2,3,4,5,5,5,4,9,8,7], 2), [1,2,3,4,5,5,4,9,8,7])
        self.assertEqual(delete_nth([1, 2, 3, 4, 5], 2), [1,2,3,4,5])
        self.assertEqual(delete_nth([], 2), [])
        self.assertEqual(delete_nth([1, 2, 3, 4, 5, 5, 5, 4, 9, 8, 7], 4), [1, 2, 3, 4, 5, 5, 5, 4, 9, 8, 7])
        self.assertEqual(delete_nth([1, 2, 7, 7, 5, 5, 5, 8, 8, 8, 7], 2), [1, 2, 7, 7, 5, 5, 8, 8])



class AlphabetPosition(unittest.TestCase):

    def test_alphabet_position(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("Hello, World!"), "8 5 12 12 15 23 15 18 12 4")
        self.assertEqual(alphabet_position("12345"), "")
        self.assertEqual(alphabet_position("abcXYZ"), "1 2 3 24 25 26")



class Narcissistic(unittest.TestCase):

    def test_narcissistic_tests(self):
        self.assertEqual(narcissistic(7), True, '7 is narcissistic')
        self.assertEqual(narcissistic(371), True, '371 is narcissistic')

    def test_not_narcissistic_tests(self):
        self.assertEqual(narcissistic(122), False, '122 is not narcissistic')
        self.assertEqual(narcissistic(4887), False, '4887 is not narcissistic')


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
