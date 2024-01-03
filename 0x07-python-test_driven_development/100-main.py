#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

print(matrix_mul([[4, 2], [4, 8 ]], [[7, 14], [2, 6]]))
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 8, 4]]))
print(matrix_mul([[], []], [[5, 6], [1, 2]]))
