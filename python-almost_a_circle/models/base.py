#!/usr/bin/python3
"""Module for Base class."""
import json
import os


class Base:
    """Base class for managing id attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list from JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list of instances to file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as f:
            f.write(cls.to_json_string(
                [o.to_dictionary() for o in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Loads list of instances from file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            return [cls.create(**d)
                    for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """Creates instance with attributes from dictionary."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
