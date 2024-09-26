import numpy as np
from matrix_utility import swap_rows_elementary_matrix, row_addition_elementary_matrix

def pivot_row_selection(A, current_row):
    """
    Select the pivot row with the largest absolute value in the current column.
    """
    pivot_row = current_row
    v_max = A[pivot_row][current_row]
    N = len(A)
    for j in range(current_row + 1, N):
        if abs(A[j][current_row]) > v_max:
            v_max = A[j][current_row]
            pivot_row = j
    return pivot_row

def apply_row_swap(A, L, i, pivot_row, N):
    """
    Apply row swapping if necessary and update matrix A and L.
    """
    if pivot_row != i:
        e_matrix = swap_rows_elementary_matrix(N, i, pivot_row)
        print(f"Elementary matrix for swapping row {i} with row {pivot_row}:\n{e_matrix}\n")
        A = np.dot(e_matrix, A)
        print(f"Matrix after row swap:\n{A}\n")
    return A

def eliminate_column_below_pivot(A, L, i):
    """
    Eliminate the elements below the pivot in column i and update matrices A and L.
    """
    N = len(A)
    for j in range(i + 1, N):
        m = -A[j][i] / A[i][i]
        e_matrix = row_addition_elementary_matrix(N, j, i, m)
        e_inverse = np.linalg.inv(e_matrix)
        L = np.dot(L, e_inverse)
        A = np.dot(e_matrix, A)
        print(f"Elementary matrix to eliminate element in row {j} below pivot in column {i}:\n{e_matrix}\n")
        print(f"Matrix after elimination:\n{A}\n")
    return A, L

def lu_decomposition(A):
    """
    Perform LU decomposition on matrix A and return matrices L and U.
    """
    N = len(A)
    L = np.eye(N)  # Create an identity matrix for L

    for i in range(N):
        pivot_row = pivot_row_selection(A, i)
        if A[i][pivot_row] == 0:
            raise ValueError("LU Decomposition cannot be performed (singular matrix).")
        A = apply_row_swap(A, L, i, pivot_row, N)
        A, L = eliminate_column_below_pivot(A, L, i)

    U = A
    return L, U

def backward_substitution(U):
    """
    Solve the system using backward substitution.
    """
    N = len(U)
    x = np.zeros(N)
    for i in range(N - 1, -1, -1):
        x[i] = U[i][N]
        for j in range(i + 1, N):
            x[i] -= U[i][j] * x[j]
        x[i] = x[i] / U[i][i]
    return x

def lu_solve(A_b):
    """
    Solve the system Ax = b using LU decomposition.
    """
    L, U = lu_decomposition(A_b)
    print("Lower triangular matrix L:\n", L)
    print("Upper triangular matrix U:\n", U)
    result = backward_substitution(U)
    print_solution(result)

def print_solution(solution):
    """
    Print the solution of the system.
    """
    print("\nSolution for the system:")
    for x in solution:
        print("{:.6f}".format(x))

if __name__ == '__main__':
    A_b = [[1, -1, 2, -1, -8],
           [2, -2, 3, -3, -20],
           [1, 1, 1, 0, -2],
           [1, -1, 4, 3, 4]]

    lu_solve(A_b)
