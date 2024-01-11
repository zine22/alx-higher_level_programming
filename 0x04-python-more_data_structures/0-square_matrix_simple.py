#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = [[] for y in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x[i].append(matrix[i][j] ** 2)
    return x
