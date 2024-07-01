"""
Yenkel Jaoui 324523075
Dan Yosef Avitan 203109996
Yarden Itah 315097527
Nofar Duchan 322599424

git_link:
"""


import numpy as np
def reverse_matrix(matrix):
    """
     This function performs the Gauss-Jordan elimination process to find the inverse of a matrix.

     Parameters:
     matrix (np.array): The matrix to be inverted.

      Returns:
      np.array: The inverted matrix.
      """
    rows, columns = matrix.shape
    i = 0
    j = 0
    elementary = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    while True:
        if j == 1:
            if i != j:
                x = int(-matrix[i][j] / matrix[j][j])
                identity_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
                identity_matrix[i][j] = x
                matrix = np.dot(identity_matrix, matrix)
                elementary = np.dot(identity_matrix, elementary)
                if i == 0:
                    break
                else:
                    i -= 1
            else:
                j += 1
        elif i != j:
            x = int(-matrix[i][j]/matrix[j][j])
            identity_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            identity_matrix[i][j] = x
            matrix = np.dot(identity_matrix, matrix)
            elementary = np.dot(identity_matrix, elementary)
            if i == rows-1:
                j += 1
            elif i == 0 and j == columns-1:
                j -= 1
            elif i == rows-2 and j == columns-1:
                i -= 1
            else:
                i += 1
        else:
            if i != rows - 1:
                i += 1

    return elementary

def func_norma(matrix):
    """
    This function calculates the maximum row sum norm (also known as infinity norm) of a matrix.

    Parameters:
    matrix (np.array): The matrix for which the norm is to be calculated.

    Returns:
    float: The maximum row sum norm of the matrix.
    """
    rows, columns = matrix.shape
    arr = []
    sum = 0
    for i in range(rows):
        for j in range(columns):
            x = abs(matrix[i, j])
            sum = sum + x
        arr.append(sum)
        sum = 0

    return max(arr)


def show_factor(matrix_A):
    """
    This function calculates and prints various factors related to the given matrix,
    including the inverted matrix, its norm, and the condition number.

    Parameters:
    matrix_A (np.array): The matrix for which the factors are to be calculated.

    Returns:
    float: The condition number of the matrix.
    """
    print("Matrix A:")
    print(matrix_A)
    if np.linalg.det(matrix_A) != 0:
        matrix_B = reverse_matrix(matrix_A)
    print("Matrix B:")
    print(matrix_B)
    norma_A = func_norma(matrix_A)
    print("Norma A = ")
    print(norma_A)
    norma_B = func_norma(matrix_B)
    print("Norma B = ")
    print(norma_B)
    COND = norma_A * norma_B
    return COND

if __name__ == '__main__':
    matrix_A = np.array([[1, -1, -2], [2, -3, -5], [-1, 3, 5]])
    COND = show_factor(matrix_A)
    print("COND = ")
    print(COND)
