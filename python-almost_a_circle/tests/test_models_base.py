#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_to_json_string_value(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_value(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])


if __name__ == '__main__':
    unittest.main()
