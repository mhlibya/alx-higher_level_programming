#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    decimal = 0
    prev = 0
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for symbol in reversed(roman_string):
        if symbol in symbols:
            value = symbols.get(symbol)
            if value < prev:
                decimal -= value
            else:
                decimal += value
        else:
            return 0
        prev = value
    return decimal
