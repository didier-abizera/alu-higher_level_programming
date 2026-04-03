#!/usr/bin/python3
"""Unittest for Square class."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_1(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_str1(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_1_str2(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_1_2_str3(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_neg1(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_1_neg2(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_1_2_neg3(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_0(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update(self):
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89(self):
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id_89_size_1_x_2(self):
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_id_89_size_1_x_2_y_3(self):
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id_89(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_89_size_1(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_89_size_1_x_2(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_id_89_size_1_x_2_y_3(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_list(self):
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_exists(self):
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()
        self.assertIsInstance(result[0], Square)


if __name__ == '__main__':
    unittest.main()
