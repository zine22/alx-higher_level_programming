#!/usr/bin/python3
def safe_print_division(a, b):
    re = 0
    try:
        re = a / b
    except ZeroDivisionError:
        re = None
    finally:
        print('inside resault: {}'.format(re))
        return re
