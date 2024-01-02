#!/usr/bin/python3
str = ""
for i in "abcdefghijklmnopqrstuvwxyz":
    if (i == 'e') or (i == 'q'):
        pass
    else:
        str += i
print("{}".format(str), end="")
