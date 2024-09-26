import numpy as np
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix


def check_square_matrix(matrix):
    """
    Check if the matrix is square.
    Raise ValueError if not.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")


def check_singular_matrix(matrix, i):
    """
    Check if the matrix is singular at index i.
    Raise ValueError if singular.
    """
    if matrix[i, i] == 0:
        raise ValueError("Matrix is singular, cannot find its inverse.")


def scale_row(matrix, identity, i):
    """
    Scale row i so that the diagonal element becomes 1.
    Apply the same transformation to the identity matrix.
    """
    scalar = 1.0 / matrix[i, i]
    elementary_matrix = scalar_multiplication_elementary_matrix(matrix.shape[0], i, scalar)
    matrix = np.dot(elementary_matrix, matrix)
    identity = np.dot(elementary_matrix, identity)
    return matrix, identity


def eliminate_off_diagonal(matrix, identity, i, j):
    """
    Eliminate the element at matrix[j, i] by row addition.
    Apply the same transformation to the identity matrix.
    """
    scalar = -matrix[j, i]
    elementary_matrix = row_addition_elementary_matrix(matrix.shape[0], j, i, scalar)
    matrix = np.dot(elementary_matrix, matrix)
    identity = np.dot(elementary_matrix, identity)
    return matrix, identity


def matrix_inverse(matrix):
    """
    Find the inverse of a non-singular matrix using elementary row operations.
    """
    print(
        f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n{matrix}\n")

    check_square_matrix(matrix)  # Verify that the matrix is square
    n = matrix.shape[0]
    identity = np.identity(n)

    for i in range(n):
        check_singular_matrix(matrix, i)  # Check if the matrix is singular at the diagonal

        if matrix[i, i] != 1:
            matrix, identity = scale_row(matrix, identity, i)
            print(f"Matrix after scaling row {i + 1}:\n{matrix}\n")

        # Eliminate elements above and below the diagonal
        for j in range(n):
            if i != j:
                matrix, identity = eliminate_off_diagonal(matrix, identity, i, j)
                print(f"Matrix after eliminating element in row {j + 1}:\n{matrix}\n")

    return identity


if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 6]])

    try:
        A_inverse = matrix_inverse(A)
        print("\nInverse of matrix A: \n", A_inverse)

    except ValueError as e:
        print(str(e))
