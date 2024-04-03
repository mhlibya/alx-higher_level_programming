#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        num = 8 - "laster"
    except:
        print(message)
        raise
