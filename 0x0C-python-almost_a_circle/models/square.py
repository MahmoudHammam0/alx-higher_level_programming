#!/usr/bin/python3
'''class Square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square inherits from Rectnagle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialization'''
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update values of class attributes'''
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.size = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        '''overrides the Rectangle str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def to_dictionary(self):
        '''returns a dictionary representation of Square'''
        the_dict = {'id': self.id, 'x': self.x,
                    'size': self.size, 'y': self.y}
        return the_dict
