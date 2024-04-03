#!/usr/bin/python3
def safe_print_division(a, b):
    sub = 0
    try:
        sub = a / b
    except ZeroDivisionError:
        sub = None
    finally:
        print("Inside result: {}".format(sub))
        return sub
