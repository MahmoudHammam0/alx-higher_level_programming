#!/usr/bin/python3
'''Square class unittest module'''
from models.square import Square
from models.rectangle import Rectangle
import unittest


class TestSquare(unittest.TestCase):
    '''unittest class for square class'''
    def test_Rectangle_subclass(self):
        '''check is square inherits from Rectangle'''
        self.assertTrue(issubclass(Square, Rectangle))

    def test_no_args(self):
        '''test Square without arguments'''
        self.assertRaises(TypeError, Square)

    def test_one_arg(self):
        '''test square with one argument'''
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_attr_x(self):
        '''test square attribue x'''
        s1 = Square(2, 5)
        self.assertEqual(s1.x, 5)

    def test_attr_y(self):
        '''test square attribute y'''
        s1 = Square(1, 3, 5)
        self.assertEqual(s1.y, 5)

    def test_Rectangle_attr(self):
        '''test Rectangle attributes from square'''
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.id, 4)

    def test_area_method(self):
        '''test area from Square class'''
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_str_method(self):
        '''test str method of Square'''
        s1 = Square(3, 5, 9, 120)
        s = "[Square] (120) 5/9 - 3"
        x = str(s1)
        self.assertEqual(x, s)

    def test_square_size(self):
        '''test attribute size of Square class'''
        s1 = Square(8, 5, 3, 4)
        self.assertEqual(s1.size, 8)
        self.assertRaises(TypeError, Square, "h")
        self.assertRaises(TypeError, Square, (1, 1))
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(ValueError, Square, -20)
        self.assertRaises(TypeError, Square, 2.5)
        self.assertRaises(TypeError, Square, {'a', 'b'})
        self.assertRaises(TypeError, Square, [])
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)

    def test_square_update_args(self):
        '''test class Square with non keyworded args'''
        s1 = Square(1)
        up = [89, 1, 2, 3]
        s1.update(*up)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_square_update_kwargs(self):
        '''test square class with keyworded args'''
        s1 = Square(5)
        up = {"y": 6, "id": 20, "x": 5, "size": 7}
        s1.update(**up)
        self.assertEqual(s1.id, 20)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.size, 7)

    def test_to_dictionary_method(self):
        '''test Square to dictionary method'''
        s1 = Square(5, 1, 2, 89)
        s1_dict = s1.to_dictionary()
        x = {'x': 1, 'y': 2, 'id': 89, 'size': 5}
        self.assertEqual(s1_dict, x)
        self.assertTrue(type(s1_dict) is dict)

if __name__ == '__main__':
    unittest.main()
