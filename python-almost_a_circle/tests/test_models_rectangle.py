#!/usr/bin/python3
"""Unittest for Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_1_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_rectangle_1_2_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_1_2_3_4_5(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_neg1_2(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_1_neg2(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_0_2(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_1_0(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_1_2_neg3(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_1_2_3_neg4(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display_without_x_and_y(self):
        r = Rectangle(2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 1)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertIn("#", output.getvalue())

    def test_display(self):
        r = Rectangle(2, 2, 1, 1)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertIn("#", output.getvalue())

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89(self):
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        r = Rectangle(1, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_create_id_89(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_89_width_1(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_89_width_1_height_2(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_89_width_1_height_2_x_3(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_id_89_width_1_height_2_x_3_y_4(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        import os
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        import os
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_list(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        import os
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_no_file(self):
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result[0], Rectangle)


if __name__ == '__main__':
    unittest.main()
