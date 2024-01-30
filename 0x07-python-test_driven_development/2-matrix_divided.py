#!/usr/bin/python3
"""
Module that contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Arguments:
        matrix: matrix to be divided
        div: value to divide all elements in the matrix
    """
    if type(div) not in [int, float]:
        """
        check if div is of type 'int' or 'float'
        else: TypeError is raised
        >>> matrix_divided([[2, 7, 6], [1, 8, 5]], "2")
        Traceback (most recent call last):
            ...
        TypeError: div must be a number
        """
        raise TypeError("div must be a number")
    elif div == 0:
        """
        check is div equals 0
        if true: ZeroDivisionError is raised
        >>> matrix_divided([[3, 5, 7], [2, 9, 5]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
        """
        raise ZeroDivisionError("division by zero")
    elif (div == float("inf")) or (div == float("-inf")):
        raise OverflowError("cannot convert float infinity \
to integer or float")

    if not (isinstance(matrix[0], list)):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    else:
        """
        checks if the firat element in matrix is of type 'list'
        """
        for i in matrix:
            for j in i:
                if type(j) not in [int, float]:
                    """
                    if element[j] in matrix is not 'int' or 'float'
                    TypeError is raised
                    """
                    raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
                    break

    if isinstance(matrix[0], list):
        len_calc = matrix[0]
        for i in matrix:
            if len(len_calc) != len(i):
                raise TypeError("Each row of the matrix \
must have the same size")
                break
        main_lst = []
        for i in matrix:
            sub_lst = []
            for j in i:
                sub_lst.append(round(j/div, 2))
            main_lst.append(sub_lst)
        return main_lst
