import numpy as np

def gaussian_elimination(mat):
    """
    Perform Gaussian Elimination to solve a system of linear equations.
    """
    singular_flag = forward_substitution(mat)

    if singular_flag != -1:
        return handle_singular_matrix(mat, singular_flag)

    return backward_substitution(mat)

def handle_singular_matrix(mat, singular_flag):
    """
    Handle cases where the matrix is singular.
    """
    N = len(mat)
    if mat[singular_flag][N]:
        return "Singular Matrix (Inconsistent System)"
    else:
        return "Singular Matrix (May have infinitely many solutions)"

def swap_rows(mat, i, j):
    """
    Swap rows i and j in the matrix.
    """
    mat[i], mat[j] = mat[j], mat[i]

def forward_substitution(mat):
    """
    Perform forward substitution to reduce the matrix to upper triangular form.
    Returns the index of the row where the matrix is singular, or -1 if the matrix is non-singular.
    """
    N = len(mat)
    for k in range(N):
        pivot_row = find_pivot_row(mat, k)
        if mat[pivot_row][k] == 0:
            return k  # Matrix is singular

        if pivot_row != k:
            swap_rows(mat, k, pivot_row)

        eliminate_column(mat, k)

    return -1

def find_pivot_row(mat, k):
    """
    Find the row with the largest pivot in column k.
    """
    N = len(mat)
    pivot_row = k
    for i in range(k + 1, N):
        if abs(mat[i][k]) > abs(mat[pivot_row][k]):
            pivot_row = i
    return pivot_row

def eliminate_column(mat, k):
    """
    Eliminate the elements in column k below the diagonal.
    """
    N = len(mat)
    for i in range(k + 1, N):
        multiplier = mat[i][k] / mat[k][k]
        for j in range(k + 1, N + 1):
            mat[i][j] -= mat[k][j] * multiplier
        mat[i][k] = 0

def backward_substitution(mat):
    """
    Perform backward substitution to solve for the unknowns.
    """
    N = len(mat)
    x = np.zeros(N)

    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N]
        for j in range(i + 1, N):
            x[i] -= mat[i][j] * x[j]
        x[i] /= mat[i][i]

    return x

if __name__ == '__main__':
    A_b = [
        [1, -1, 2, -1, -8],
        [2, -2, 3, -3, -20],
        [1, 1, 1, 0, -2],
        [1, -1, 4, 3, 4]
    ]

    result = gaussian_elimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print("\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
