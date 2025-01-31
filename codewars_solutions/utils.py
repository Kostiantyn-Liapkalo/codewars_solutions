def odd_count(n: int) -> int:
    return n // 2

def is_isogram(string):
    string = string.lower()#ignor
    return len(string) == len(set(string))#unique symbol