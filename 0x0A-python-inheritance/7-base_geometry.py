#!/usr/bin/python3
"""
=======================
   gjkfkuftjtydfhdtr
=======================
"""
class BaseGeometry:
    """jhfrsszzcrdyuf"""
    def area(self):
        """qiufhdovzx"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """azjfauohqpjfisef"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass
