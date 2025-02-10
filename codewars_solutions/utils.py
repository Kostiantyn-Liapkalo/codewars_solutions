'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
'''

def alphabet_position(text):
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())

# Description:
# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#
# For example, take 153 (3 digits), which is narcissistic:
#
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:
#
#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

def narcissistic( value ):
    digits = [int(d) for d in str(value)]
    num_digits = len(digits)
    total = sum(d ** num_digits for d in digits)
    return total == value

#(2) def narcissistic(value):
#       return value == sum(int(x) ** len(str(value)) for x in str(value))

#(3) def narcissistic(value):
#       return value == sum(list(map(lambda x:int(x)**len(str(value)),str(value))))


# from preloaded import MORSE_CODE
#
# def decode_morse(morse_code):
#
#     morse_code = morse_code.strip()
#     words = morse_code.split('   ')
#
#     decoded_words = []
#     for word in words:
#         letters = word.split()
#         decoded_word = ''.join(MORSE_CODE[letter] for letter in letters)
#         decoded_words.append(decoded_word)
#
#     return ' '.join(decoded_words)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def encode_morse(text):

    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)


def decode_morse(morse_code):

    reversed_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    words = morse_code.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join(reversed_dict.get(letter, '') for letter in letters)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))


# def decodeMorse(morse_sequence):
#     words = []
#     for morse_word in morse_sequence.split('   '):
#         word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
#         if word:
#             words.append(word)
#     return ' '.join(words)
# _____________________________________

def odd_count(n: int) -> int:
    return n // 2

def is_isogram(string):
    string = string.lower()#ignor
    return len(string) == len(set(string))#unique symbol

#You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
    evens = [num for num in integers if num % 2 == 0]
    odds = [num for num in integers if num % 2 != 0]

    return evens[0] if len(evens) == 1 else odds[0]
#or
# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
#  or
# def find_outlier(nums):
#     base_parity = sum(x % 2 for x in nums[:3]) // 2
#
#     for i in range(len(nums)):
#         if nums[i] % 2 != base_parity:
#             return nums[i]



"""
    Generates a Tribonacci sequence based on the sum of the previous three numbers.

    :param signature: A list of three initial numbers
    :param n: Number of numbers in the output list
    :return: The first n numbers of the sequence
"""
"""
If n == 0, we return an empty list.
If n ≤ 3, we return the first n elements of the initial list (signature).
For n > 3:
Copy the signature to the result.
We add new numbers that are the sum of the last three in result.
We repeat until the length of result is equal to n.
"""
def tribonacci(signature, n):
    if n == 0:
        return []
    if n <= 3:
        return signature[:n]

    result = signature[:]

    while len(result) < n:
        result.append(sum(result[-3:]))

    return result

"""
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
"""

"""
def tribonacci(signature,n):
    return signature[:n] if n<=len(signature) else tribonacci(signature + [sum(signature[-3:])],n)
"""

"""
def tribonacci(signature,n):
    return signature[:1] + tribonacci(signature[1:] + [sum(signature)], n - 1) if n > 0 else []
"""


"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!
"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}" .format(*n)

# def create_phone_number(n):
#   return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

# create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

# def create_phone_number(n):
#     num = ''.join(str(h) for h in n);
#     return f'({num[0:3]}) {num[3:6]}-{num[6:]}'

"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
def filter_list(l):
    return list(filter(lambda x: isinstance(x, int), l))

# def filter_list(l):
#     return [x for x in l if isinstance(x, int)]



"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

selfEqual('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
"""




