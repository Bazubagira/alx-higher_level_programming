#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute square value."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
