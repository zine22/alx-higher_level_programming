#!/usr/bin/python
str = ""
for i in "abcdefghijklmnopqrstuvwxyz":
    if (i == 'e') or (i == 'q'):
        pass
    else:
        str += 1
print("{}".format(str), end="")
