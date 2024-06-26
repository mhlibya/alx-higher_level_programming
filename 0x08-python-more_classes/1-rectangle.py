#!/usr/bin/python3

class Rectangle:
    def __init__(self, width, height):
        self.wedth = width
        self.height = height

    
    @property
    def width(self):
        return self.width

    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    
    @property
    def height(self):
        return self.height
    
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
