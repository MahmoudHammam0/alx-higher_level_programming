#!/usr/bin/python3
'''My list class module which inherits from class list'''


class MyList(list):
    '''class mylist inherits from class list'''
    def __init__(self):
        '''initialization'''
        super().__init__

    def print_sorted(self):
        '''sort the list in ascending order'''
        print(sorted(self))
