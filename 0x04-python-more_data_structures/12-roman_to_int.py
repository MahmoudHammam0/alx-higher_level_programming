#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for x in range(len(roman_string)):
        if x > 0 and my_dict[roman_string[x]] > my_dict[roman_string[x - 1]]:
            num += my_dict[roman_string[x]] - 2 * my_dict[roman_string[x - 1]]
        else:
            num += my_dict[roman_string[x]]
    return num
