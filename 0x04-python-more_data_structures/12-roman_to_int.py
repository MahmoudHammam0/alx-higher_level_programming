#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dictionary = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return (0)
    else:
        num = 0
        for x in range(len(roman_string)):
            for key, value in my_dictionary.items():
                if roman_string[x] == key:
                    num += value - 2 * my_dictionary[roman_string[x - 1]]
                else:
                    num += value
        return (num)
