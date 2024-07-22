"""
Yenkel Jaoui 324523075
Dan Yosef Avitan 203109996
Yarden Itah 315097527
Nofar Duchan 322599424

git_link: https://github.com/nofarduchan/Numerical-Analis-.git
"""
import numpy as np

arr = []

def row_addition_elementary_matrix(n, target_row, source_row, scalar=1.0):
    """
    Creates an elementary matrix for adding a multiple of one row to another.

    Parameters:
    n (int): Size of the matrix (number of rows/columns).
    target_row (int): The index of the row to which the multiple is added.
    source_row (int): The index of the row which is multiplied and added.
    scalar (float, optional): The scalar to multiply the source row. Default is 1.0.

    Returns:
    np.array: An elementary matrix for row addition.
    """
    if target_row < 0 or source_row < 0 or target_row >= n or source_row >= n:
        raise ValueError("Invalid row indices.")

    if target_row == source_row:
        raise ValueError("Source and target rows cannot be the same.")

    elementary_matrix = np.identity(n)
    elementary_matrix[target_row, source_row] = scalar

    return np.array(elementary_matrix)

def scalar_multiplication_elementary_matrix(n, row_index, scalar):
    """
    Creates an elementary matrix for multiplying a row by a scalar.

    Parameters:
    n (int): Size of the matrix (number of rows/columns).
    row_index (int): The index of the row to be multiplied.
    scalar (float): The scalar to multiply the row.

    Returns:
    np.array: An elementary matrix for row multiplication.
    """
    if row_index < 0 or row_index >= n:
        raise ValueError("Invalid row index.")

    if scalar == 0:
        raise ValueError("Scalar cannot be zero for row multiplication.")

    elementary_matrix = np.identity(n)
    elementary_matrix[row_index, row_index] = scalar

    return np.array(elementary_matrix)

def reverse_matrix(matrix):
    """
    Performs the Gauss-Jordan elimination process to find the inverse of a matrix.

    Parameters:
    matrix (np.array): The matrix to be inverted.

    Returns:
    np.array: The inverted matrix.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)

    return identity

def matrix_L(matrix):
    """
    Performs LU decomposition to find the lower triangular matrix L.

    Parameters:
    matrix (np.array): The matrix to be decomposed.

    Returns:
    np.array: The lower triangular matrix L.
    """
    i = 0
    j = 0
    for i in range(3):
        if i != j:
            x = float(-matrix[i][j] / matrix[j][j])
            identity_matrix = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
            identity_matrix[i][j] = x
            arr.append(identity_matrix)
            matrix = np.dot(identity_matrix, matrix)
    j += 1
    x = float(-matrix[i][j] / matrix[j][j])
    identity_matrix = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    identity_matrix[i][j] = x
    arr.append(identity_matrix)
    matrix = np.dot(identity_matrix, matrix)
    return matrix

def matrix_U():
    """
    Constructs the upper triangular matrix U from the elementary row operations stored in arr.

    Returns:
    np.array: The upper triangular matrix U.
    """
    matrixU = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    for elem in arr:
        rev_elem = reverse_matrix(elem)
        matrixU = np.dot(matrixU, rev_elem)
    return matrixU

if __name__ == '__main__':
    matrix = np.array([[1, 4, -3], [-2, 1, 5], [3, 2, 1]])
    matrixL = matrix_L(matrix)
    matrixU = matrix_U()
    matrix_A = np.dot(matrixU, matrixL)
    print(f' L: \n {matrixL}\n')
    print(f' U: \n {matrixU}\n')
    print(f' A: \n {matrix_A}\n')
    vector_b = np.array([[1], [2], [3]])
    rev_matrix_l = reverse_matrix(matrixL)
    rev_matrix_u = reverse_matrix(matrixU)
    print(f' Reverse L: \n {rev_matrix_l}\n')
    print(f' Reverse U: \n {rev_matrix_u}\n')
    vector_y = np.dot(reverse_matrix(matrixU), vector_b)
    print(f' Vector y: \n {vector_y}\n')
    vector_x = np.dot(reverse_matrix(matrixL), vector_y)
    print(f' Vector x: \n {vector_x}\n')
