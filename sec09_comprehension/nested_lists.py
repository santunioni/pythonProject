"""
Aligned lists are lists inside lists

In other programming languages (C/Java) there are data structures called arrays:
 - One-dimensional: Arrays/Vectors
 - 2-dimensional: Matrices
 - N-dimensional: Tensors/N-vectors

In python we have only lists. However, lists can be put inside other list to mimic structures
like matrices.
"""

# Each list inside the list represent a line in a matrix
# numpy package is better for treating matrices
matrix = [[23, 123, 5], [12, 54, 98], [12, 65, 312]]
print(f"The matrix is {matrix}")


def get_element(line, column, _matrix):
    return _matrix[line][column]


# Comprehension for aligned list
# Create a flat list
matrix_flat = [_element for lines in matrix for _element in lines]
print(f"The flat matrix is {matrix_flat}")


# This will return the same matrix
matrix = [[_element for _element in lines] for lines in matrix]
print(f"The           matrix is {matrix}")


# 'Transpose the matrix': for each line of the matrix I get the column
# and transform it to a line of the transpose matrix
lines, columns = len(matrix), len(matrix[0])
matrix_T = [[matrix[_column][_line] for _column in range(columns)] for _line in range(lines)]
print(f"The transpose matrix is {matrix_T}")
