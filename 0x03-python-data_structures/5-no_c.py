#!/usr/bin/python3
def no_c(my_string):
    noc = ""
    for i in my_string:
        if (i == "c") or (i =="C"):
            noc += ""
        else:
            noc += i
            return noc
