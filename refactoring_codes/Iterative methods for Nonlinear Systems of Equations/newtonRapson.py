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
    f = lambda x: x ** 3 - 3 * x ** 2
    df = lambda x: 3 * x ** 2 - 6 * x
    p0 = -5
    TOL = 1e-6
    N = 100
    root = newton_raphson(f, df, p0, TOL, N)

    print(f"\nThe equation f(x) has an approximate root at x = {root:<15.9f}")
