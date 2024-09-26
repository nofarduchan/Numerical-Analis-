import numpy as np
from numpy.linalg import norm
from matrix_utility import is_diagonally_dominant


def initialize_guess_vector(b):
    """
    Initializes the guess vector X0 to be the same size as b and filled with zeros.
    """
    return np.zeros_like(b, dtype=np.double)


def is_converged(x_new, x_old, tol):
    """
    Checks if the iterative process has converged based on the given tolerance.
    """
    return norm(x_new - x_old, np.inf) < tol


def print_iteration_header(A):
    """
    Prints the header for the iterations table.
    """
    print("Iteration" + "\t\t".join(["{:>12}".format(f"x{i}") for i in range(1, len(A) + 1)]))
    print("-----------------------------------------------------------------------------------------------")


def print_iteration_values(k, x):
    """
    Prints the values of x for the current iteration.
    """
    print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))


def jacobi_step(A, b, X0):
    """
    Performs one iteration step of the Jacobi method.
    """
    n = len(A)
    x = np.zeros(n, dtype=np.double)

    for i in range(n):
        sigma = sum(A[i][j] * X0[j] for j in range(n) if j != i)
        x[i] = (b[i] - sigma) / A[i][i]

    return x


def jacobi_iterative(A, b, X0=None, TOL=1e-16, N=200):
    """
    Performs Jacobi iterations to solve Ax = b, starting from an initial guess X0.
    """
    n = len(A)
    if X0 is None:
        X0 = initialize_guess_vector(b)

    if is_diagonally_dominant(A):
        print('Matrix is diagonally dominant - performing Jacobi algorithm\n')

    print_iteration_header(A)

    for k in range(1, N + 1):
        x_new = jacobi_step(A, b, X0)
        print_iteration_values(k, x_new)

        if is_converged(x_new, X0, TOL):
            return tuple(x_new)

        X0 = x_new.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x_new)


if __name__ == "__main__":
    A = np.array([[3, -1, 1], [0, 1, -1], [1, 1, -2]])
    b = np.array([4, -1, -3])

    solution = jacobi_iterative(A, b)

    print("\nApproximate solution:", solution)
