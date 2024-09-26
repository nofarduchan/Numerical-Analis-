import math


def trapezoidal_rule(f, a, b, n):
    """
    Computes the definite integral of a function using the Trapezoidal Rule.

    Parameters:
    f (function): The function to integrate.
    a (float): The start point of the interval.
    b (float): The end point of the interval.
    n (int): The number of subintervals.

    Returns:
    float: Approximate value of the integral.
    """
    h = compute_step_size(a, b, n)
    integral = initial_integral_value(f, a, b)

    for i in range(1, n):
        integral += compute_function_value(f, a, i, h)

    return finalize_integral(integral, h)


def compute_step_size(a, b, n):
    """
    Computes the step size for the trapezoidal rule.
    """
    return (b - a) / n


def initial_integral_value(f, a, b):
    """
    Computes the initial integral value using the endpoints.
    """
    return 0.5 * (f(a) + f(b))


def compute_function_value(f, a, i, h):
    """
    Computes the function value at the ith point.
    """
    return f(a + i * h)


def finalize_integral(integral, h):
    """
    Finalizes the integral by multiplying by the step size.
    """
    return integral * h


if __name__ == '__main__':
    f = lambda x: math.e ** (x ** 2)
    result = trapezoidal_rule(f, 0, 1, 2)
    print(f"Approximate integral: {result}")
