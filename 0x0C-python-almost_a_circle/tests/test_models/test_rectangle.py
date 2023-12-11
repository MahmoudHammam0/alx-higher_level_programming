#!/usr/bin/python3
'''Rectangle unittest module'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''unittest for Rectangle class'''
    def test_no_args(self):
        '''test Rectangle class with no args'''
        self.assertRaises(TypeError, Rectangle)

    def test_one_arg(self):
        '''test Rectangle with one argument'''
        self.assertRaises(TypeError, Rectangle, 5)

    def test_two_valid_args(self):
        '''test Rectangle with width and height'''
        r1 = Rectangle(3, 5)
        self.assertIsInstance(r1, Rectangle)

    def test_str_args(self):
        '''test Rectangle with string argument'''
        self.assertRaises(TypeError, Rectangle, "hi", 5)

    def test_float_arg(self):
        '''test Rectangle with floats'''
        self.assertRaises(TypeError, Rectangle, 2.5, 5)

    def test_list_arg(self):
        '''test Rectangle with list'''
        self.assertRaises(TypeError, Rectangle, [1, 2], 2)

    def test_set_arg(self):
        '''test Rectangle with set'''
        self.assertRaises(TypeError, Rectangle, {1, 5}, 5)

    def test_negative_width(self):
        '''test Rectangle with negative width'''
        self.assertRaises(ValueError, Rectangle, -2, 1)

    def test_negative_height(self):
        '''test Rectangle with negative height'''
        self.assertRaises(ValueError, Rectangle, 2, -1)

    def test_negative_x(self):
        '''test REctangle with negative x'''
        self.assertRaises(ValueError, Rectangle, 2, 1, -2)

    def test_negative_y(self):
        '''test Rectangle with negative y'''
        self.assertRaises(ValueError, Rectangle, 2, 1, 2, -5)

    def test_dictionary(self):
        '''test Rectangle with dictionary argument'''
        self.assertRaises(TypeError, Rectangle, {'a': 1, 'b': 2}, 1)

    def test_attr_width(self):
        '''test attribute width of Rectangle'''
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.width, 5)

    def test_attr_height(self):
        '''test attribute height of Rectangle'''
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.height, 10)

    def test_attr_x(self):
        '''test attribute x of Rectangle'''
        r1 = Rectangle(5, 10, 6)
        self.assertEqual(r1.x, 6)

    def test_attr_y(self):
        '''test attribute y of rectangle'''
        r1 = Rectangle(5, 10, 6, 7)
        self.assertEqual(r1.y, 7)

    def test_attr_id(self):
        '''test attribute id of Rectangle'''
        r1 = Rectangle(5, 10, 6, 7, 12)
        self.assertEqual(r1.id, 12)

    def test_zero_width(self):
        '''test Rectangle with zero as width'''
        self.assertRaises(ValueError, Rectangle, 0, 1)

    def test_zero_height(self):
        '''test Rectangle with zero as height'''
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_zero_x(self):
        '''test Rectangle with zero as x'''
        r1 = Rectangle(5, 6, 0)
        self.assertEqual(r1.x, 0)

    def test_zero_y(self):
        '''test Rectangle with zero as y'''
        r1 = Rectangle(5, 6, 1, 0)
        self.assertEqual(r1.y, 0)

    def test_area(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_display(self):
