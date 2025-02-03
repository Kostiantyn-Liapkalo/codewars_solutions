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




