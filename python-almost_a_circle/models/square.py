#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        attrs = ['id', 'size', 'x', 'y']
        for i, val in enumerate(args):
            setattr(self, attrs[i], val)
        if not args:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y
        }
