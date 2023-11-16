#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D square matrix inplace in 90 degress clockwise"""
    matrix90 = []
    mlen = len(matrix)
    for i in range(mlen):
        matrix90.append([m[i] for m in matrix][::-1])
    for i in range(mlen):
        matrix[i] = matrix90[i]
