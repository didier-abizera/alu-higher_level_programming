#!/usr/bin/python3
"""Unittest for Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_default_x_y(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(3, 4, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 3/4")

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 4)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "b")

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4)

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, "x")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 0, "y")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -1)

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 0, -1)

    def test_update_args(self):
        r = Rectangle(3, 4)
        r.update(5, 6, 7)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)

    def test_update_kwargs(self):
        r = Rectangle(3, 4)
        r.update(width=10, height=20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_to_dictionary(self):
        r = Rectangle(3, 4, 0, 0, 1)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 3)
        self.assertEqual(d['height'], 4)


if __name__ == '__main__':
    unittest.main()
