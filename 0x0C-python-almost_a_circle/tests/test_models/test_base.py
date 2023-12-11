#!/usr/bin/python3
'''unittest module for base.py'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''unittest class for base class'''
    def test_no_args(self):
        '''test class base without args'''
        t = Base()
        self.assertEqual(t.id, 1)

    def test_int_arg(self):
        '''test class base with one int arg'''
        x = Base(10)
        self.assertEqual(x.id, 10)

    def test_several_instances(self):
        '''several instances of class base'''
        a = Base()
        b = Base()
        c = Base()
        d = Base()
        self.assertEqual(d.id, 5)

    def test_more_args(self):
        '''test class base with more args'''
        self.assertRaises(TypeError, Base, 3, 5)

    def test_neg_int(self):
        '''test Base with negative integer'''
        h = Base(-20)
        self.assertEqual(h.id, -20)

    def test_zero_arg(self):
        '''test Base with 0 as arg'''
        m = Base(0)
        self.assertEqual(m.id, 0)

    def test_str(self):
        '''test Base with string'''
        v = Base("Hello")
        self.assertEqual(v.id, "Hello")

    def test_float(self):
        '''test Base with float'''
        v = Base(2.5)
        self.assertEqual(v.id, 2.5)

    def test_dict(self):
        '''test Base with dictionary'''
        v = Base({'a': 0, 'b': 1, 'c': 2})
        self.assertEqual(v.id, {'a': 0, 'b': 1, 'c': 2})

    def test_list(self):
        '''test Base with list'''
        v = Base([0, 1, 2, 3])
        self.assertEqual(v.id, [0, 1, 2, 3])

    def test_tuple(self):
        '''test Base with tuple'''
        v = Base((2, 5))
        self.assertEqual(v.id, (2, 5))

if __name__ == '__main__':
    unittest.main()
