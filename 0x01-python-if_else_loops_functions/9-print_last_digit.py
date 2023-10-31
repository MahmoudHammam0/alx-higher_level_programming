#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        n = number % 10
    else:
        n = number % -10
    if n < 0:
        n *= -1
    print(n, end='')
    return (n)
