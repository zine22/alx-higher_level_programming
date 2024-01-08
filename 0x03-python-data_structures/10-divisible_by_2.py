#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tt = []
    for i in my_list:
        if i % 2 == 0:
            tt.append(True)
        else:
            tt.append(False)
    return tt
