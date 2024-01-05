#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    if number == 0:
        print("0 args")
    elif number == 1:
        print(" 1 arg")
    else:
        print("{} args".format(number))
    for i in range(number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
