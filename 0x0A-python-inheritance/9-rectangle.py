#!/usr/bin/python3

"""
==============================
    ,jfgilfytudfjydrrydgjh
==============================
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ghfiehassfhbslfj"""
    def __init__(self, width, height):
        """lkjsdfizxzvasdfj"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """jkaflshafje"""
        return self.__height * self.__width
    def __str__(self):
        """jfklsdilejwasl"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
