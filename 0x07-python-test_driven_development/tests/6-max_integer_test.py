#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''subclass of unittest class to test max_integer'''
    def test_func(self):
        '''test different valid args for max_integer function'''
        self.assertAlmostEqual(max_integer([4, 2, 3, 0]), 4)

    def test_floats(self):
        '''float args for max_integer'''
        self.assertAlmostEqual(max_integer([2.5, 3.5, 4.5]), 4.5)

    def test_negative(self):
        '''negative ints args'''
        self.assertAlmostEqual(max_integer([-20, -10, -90]), -10)

    def test_mixed(self):
        '''mixed floats and ints args'''
        self.assertAlmostEqual(max_integer([1, 2.5, -20, - 3.8]), 2.5)

    def test_type_float(self):
        '''tests invalid args for max_integer function'''
        self.assertRaises(TypeError, max_integer, 2.5)

    def test_type_None(self):
        '''None arg'''
        self.assertRaises(TypeError, max_integer, None)

    def test_type_int(self):
        '''int arg'''
        self.assertRaises(TypeError, max_integer, 5)

    def test_empty(self):
        '''test empty list'''
        self.assertIsNone(max_integer([]))

    def test_type_str(self):
        '''test str arg'''
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "Not Number"])

    def test_no_arg(self):
        '''no args passed'''
        self.assertIsNone(max_integer())

    def test_one_arg(self):
        '''list with one element passed'''
        self.assertAlmostEqual(max_integer([-1]), -1)

    def test_strings(self):
        '''list of strings'''
        self.assertEqual(max_integer(["say", "my", "name"]), "say")


if __name__ == "__main__":
    unittest.main()
