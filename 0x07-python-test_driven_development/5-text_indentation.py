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
    new_str = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            new_str += text[i] + "\n"
            if i == len(text) - 1 or text[i + 1] != ' ':
                new_str += "\n"
            continue
        if text[i] == ' ':
            if i == 0 or text[i - 1] == "\n":
                continue
            if text[i - 1] in ['.', '?', ':']:
                new_str += "\n"
                continue
            if text[i - 1] == ' ':
                continue
        new_str += text[i]
    print(new_str, end='')
