import numpy as np

def romberg_integration(func, a, b, n):
    """
    Romberg Integration

    Parameters:
    func (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of iterations (higher value leads to better accuracy).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    h = compute_initial_h(a, b)
    R = initialize_romberg_table(n, func, a, b, h)

    for i in range(1, n):
        h = update_step_size(h)
        sum_term = compute_sum_term(func, a, h, i)

        R[i, 0] = compute_first_column(R, i, h, sum_term)
        update_romberg_table(R, i)

    return R[n - 1, n - 1]

def compute_initial_h(a, b):
    """
    Computes the initial step size (h).
    """
    return b - a

def initialize_romberg_table(n, func, a, b, h):
    """
    Initializes the Romberg table with the first estimate.
    """
    R = np.zeros((n, n), dtype=float)
    R[0, 0] = 0.5 * h * (func(a) + func(b))
    return R

def update_step_size(h):
    """
    Halves the step size for each iteration.
    """
    return h / 2

def compute_sum_term(func, a, h, i):
    """
    Computes the summation term for Romberg integration.
    """
    sum_term = 0
    for k in range(1, 2 ** i, 2):
        sum_term += func(a + k * h)
    return sum_term

def compute_first_column(R, i, h, sum_term):
    """
    Computes the first column of the Romberg table for the current iteration.
    """
    return 0.5 * R[i - 1, 0] + h * sum_term

def update_romberg_table(R, i):
    """
    Updates the Romberg table for the current row using extrapolation.
    """
    for j in range(1, i + 1):
        R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / ((4 ** j) - 1)

def f(x):
    """
    The function to be integrated.
    """
    return 1 / (2 + x ** 4)

if __name__ == '__main__':
    a = 0
    b = 1
    n = 5
    integral = romberg_integration(f, a, b, n)

    print(f"Division into n = {n} sections")
    print(f"Approximate integral in range [{a}, {b}] is {integral}")
