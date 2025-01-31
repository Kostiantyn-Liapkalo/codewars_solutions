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