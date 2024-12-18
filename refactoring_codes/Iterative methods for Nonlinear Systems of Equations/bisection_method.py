"""
שיטת החציה - bisection_method
"""

import math
import numpy as np


def max_steps(a, b, err):
    """
    Calculates the maximum number of iterations required to reach the desired accuracy.
    """
    return int(np.floor(-np.log2(err / (b - a)) / np.log2(2) - 1))


def print_iteration_header():
    """
    Prints the header for the bisection iteration table.
    """
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))


def print_iteration_values(k, a, b, f_a, f_b, c, f_c):
    """
    Prints the values for each iteration of the bisection method.
    """
    print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f_a, f_b, c, f_c))


def is_converged(a, b, tol):
    """
    Checks if the method has converged based on the tolerable error.
    """
    return abs(b - a) <= tol


def bisection_step(f, a, b):
    """
    Performs a single step of the bisection method and returns the new midpoint c and updated interval [a, b].
    """
    c = (a + b) / 2
    if f(c) == 0:
        return c, a, b  # Found the exact root

    if f(c) * f(a) < 0:
        return c, a, c  # Update b to c
    else:
        return c, c, b  # Update a to c

def find_sign_changes_and_solve(f, start, end, step):
    a = start
    while a < end:
        b = a + step
        # בדיקה אם יש שינוי סימן
        if f(a) * f(b) < 0:
            print(f"Sign change found between a = {a} and b = {b}")
            # קריאה לפונקציית bisection_method עבור תחום זה
            root = bisection_method(f, a, b)
            print(f"The equation f(x) has an approximate root at x = {root}\n")
        a += step

def bisection_method(f, a, b, tol=1e-6):
    """
    Performs the bisection method to find the root of the given function f in the interval [a, b].
    """
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("The scalars a and b do not bound a root")

    steps = max_steps(a, b, tol)
    print_iteration_header()

    for k in range(steps):
        c, a, b = bisection_step(f, a, b)
        print_iteration_values(k, a, b, f(a), f(b), c, f(c))

        if is_converged(a, b, tol):
            return c

    return c  # Return the last approximation of the root


if __name__ == '__main__':
    # f = lambda x: x ** 4 + x ** 3 - 3 * x ** 2
    f = lambda x: math.cos(x ** 2 + 5 * x + 6) / (2 * math.exp(-x))
    # f_prime = lambda x: ((-math.sin(x ** 2 + 5 * x + 6) * (2 * x + 5) * 2 * math.exp(-x)) +
    #                             (math.cos(x ** 2 + 5 * x + 6) * (-2 * math.exp(-x)))
    #                     ) / (4 * math.exp(-2 * x))
    start = -3
    end = 2
    step = 0.1
    # קריאה לפונקציה שתבדוק ותמצא שורשים
    find_sign_changes_and_solve(f, start, end, step)
