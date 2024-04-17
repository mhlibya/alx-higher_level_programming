#!/usr/bin/python3
"""
====================
   jklasfdjfsdhfe
====================
"""

def add_attribute(cls, attr_name, attr_value):
    """jlkfsdjfansehfasrg"""
    if not hasattr(cls, attr_name):
        setattr(cls, attr_name, attr_value)
    else:
        raise ValueError("can't add new attribute")
