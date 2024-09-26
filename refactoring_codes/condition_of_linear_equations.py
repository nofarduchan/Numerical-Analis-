"""
טיב ההצגה ונורמת המקסימום
"""
import numpy as np
from inverse_matrix import matrix_inverse
from matrix_utility import print_matrix

def calculate_row_sum(matrix, row):
    """
    Calculate the sum of absolute values in a specific row.
    """
    return sum(abs(matrix[row][col]) for col in range(len(matrix)))

def matrix_norm(matrix):
    """
    Calculate the infinity norm (max row sum) of a matrix.
    """
    return max(calculate_row_sum(matrix, row) for row in range(len(matrix)))

def condition_number(A):
    """
    Compute the condition number of matrix A based on its infinity norm.
    """
    norm_A = matrix_norm(A)
    A_inv = matrix_inverse(A)
    norm_A_inv = matrix_norm(A_inv)
    return norm_A * norm_A_inv

def display_matrix_info(A, A_inv, norm_A, norm_A_inv):
    """
    Display information about the matrix, its inverse, and norms.
    """
    print("Matrix A:")
    print_matrix(A)
    print("Inverse of A:")
    print_matrix(A_inv)
    print("Max Norm of A:", norm_A)
    print("Max Norm of the inverse of A:", norm_A_inv)

if __name__ == '__main__':
    A = np.array([[2, 1.7, -2.5],
                  [1.24, -2, -0.5],
                  [3, 0.2, 1]])

    norm_A = matrix_norm(A)
    A_inv = matrix_inverse(A)
    norm_A_inv = matrix_norm(A_inv)
    cond = condition_number(A)

    display_matrix_info(A, A_inv, norm_A, norm_A_inv)
    print("\nCondition number:", cond)
