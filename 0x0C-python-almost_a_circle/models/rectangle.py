#!/usr/bin/python3
'''Rectangle class module'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter for x'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter for y'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''return area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''print the rectangle to stdout'''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        '''overrides the str method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''update values of attributes of Rectangle class'''
        for i in range(len(args)):
            if i == 0:
                if args[i] is None:
                    continue
                else:
                    self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        continue
                    else:
                        self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value
