#!/usr/bin/python3
'''My integer module'''


class MyInt(int):
    '''class MyInt inherits from int class'''
    def __eq__(self, other):
        '''implements behaviour of == operator'''
        return False

    def __ne__(self, other):
        '''implements behaviour of != operator'''
        return True
