#!/usr/bin/python3
'''

5-Text indentation module

'''


def text_indentation(text):
    '''print text with new lines in cases of .,? and :

    Args:
        text: must be string of text

    Return:
        Nothing

    Raises:
        TypeError: if text arg not a string
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')
    marker = 0
    for char in text:
        if marker == 0:
            if char == ' ':
                continue
            else:
                marker = 1
        if marker == 1:
            if char in ['.', '?', ':']:
                print(char)
                print()
                marker = 0
            else:
                print(char, end='')
