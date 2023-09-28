#!/usr/bin/python3
"""
Prints pascal triangle
"""
import itertools


def compute_trianlge_seq(seq):
    yield 1

    for idx, x in enumerate(seq):
        if idx == 0:
            continue
        yield (x + seq[idx - 1])

    yield 1

def pascal_triangle(n):
    """
    Returns a list of integers representing pascal's  triangle of size 'n'
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for _ in range(n - 1):
        pre_row = triangle[-1]
        cur_row = compute_trianlge_seq(pre_row)
        triangle.append(list(cur_row))
    
    return triangle
