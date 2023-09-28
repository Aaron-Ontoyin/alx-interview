#!/usr/bin/python3
"""
Prints pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing pascal's  triangle of size 'n'
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(n - 1):
        pre_row = triangle[-1]
        cur_row = [1]
        for idx, x in enumerate(pre_row):
            if idx == 0:
                continue
            cur_row.append(x + pre_row[idx - 1])
        cur_row.append(1)
        triangle.append(cur_row)
    
    return triangle
