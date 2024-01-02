#!/usr/bin/python3
def appercase(str):
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ord(str) == ord (i):
            return True
        else:
            return False
        
