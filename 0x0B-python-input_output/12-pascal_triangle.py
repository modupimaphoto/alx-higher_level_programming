#!/usr/bin/python3
"""Defines Pascal’s triangle"""


def pascal_triangle(n):
    """pascal_triangle function
     returns a list of lists of integers
     representing the Pascal’s triangle of n:
     """
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return
