import math

import numpy as np


def print_iteration_header():
    """
    Prints the header for the Newton-Raphson iteration table.
    """
    print("{:<10} {:<15} {:<15}".format("Iteration", "p0", "p1"))


def print_iteration_values(i, p0, p):
    """
    Prints the values for each iteration of the Newton-Raphson method.
    """
    print("{:<10} {:<15.9f} {:<15.9f}".format(i, p0, p))


def newton_raphson(f, df, p0, TOL, N=50):
    """
    Performs the Newton-Raphson method to find the root of the function f.

    Parameters:
        f: The function for which we want to find the root.
        df: The derivative of the function f.
        p0: Initial guess for the root.
        TOL: Tolerance for stopping criteria.
        N: Maximum number of iterations.

    Returns:
        The approximate root of the function f.
    """
    print_iteration_header()

    for i in range(N):
        derivative_value = df(p0)
        if derivative_value == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / derivative_value

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully

        print_iteration_values(i, p0, p)
        p0 = p

    return p


if __name__ == '__main__':
    f = lambda x: (2*x*np.exp(-x) + np.log(2*x**2)) * (2*x**4 + 2*x**2 - 3*x - 5)
    df = lambda x: ((2*np.exp(-x) - 2*x*np.exp(-x) + (1/x)) * (2*x**4 + 2*x**2 - 3*x - 5)) + \
               ((2*x*np.exp(-x) + np.log(2*x**2)) * (8*x**3 + 4*x - 3))

    TOL = 1e-6
    N = 100

    # Check for sign changes in the range [-3, 2] with steps of 0.1
    a = -3
    b = a + 0.1
    while b <= 2:
        if f(a) * f(b) < 0:  # Sign change detected
            p0 = (a + b) / 2  # Midpoint as initial guess
            print(f"\nSign change detected between {a} and {b}")
            root = newton_raphson(f, df, p0, TOL, N)
            print(f"The equation f(x) has an approximate root at x = {root:<15.9f}")
        a += 0.1
        b = a + 0.1
