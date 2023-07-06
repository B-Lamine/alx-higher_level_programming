#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integerList(self):
        """Test a list of integers.
        """
        self.assertEqual(max_integer([10, 2, 30, 4]), 30)

    def test_emptyList(self):
        """Test an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_oneElementList(self):
        """Test list of one element.
        """
        self.assertEqual(max_integer([0]), 0)

    def test_mixedList(self):
        """Test a list with mixed types elements.
        """
        self.assertRaises(TypeError, max_integer, ['a', 2])

    def test_stringList(self):
        """Test a list of strings.
        """
        self.assertEqual(max_integer(['abc', 'c', 'bb']), 'c')

    def test_noneList(self):
        """Test none list argument.
        """
        self.assertRaises(TypeError, max_integer, 123)
