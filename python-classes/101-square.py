#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """Class that defines a square with print instance"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # character"""
        if self.__size == 0:
            print("")
        else:
            for j in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

cat > 101-square.py << 'EOF'
#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """Class that defines a square with print instance"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # character"""
        if self.__size == 0:
            print("")
        else:
            for j in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation same as my_print"""
        result = ""
        if self.__size == 0:
            return ""
        for j in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
