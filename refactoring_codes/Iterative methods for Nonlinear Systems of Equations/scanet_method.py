import math


def secant_method(f, x0, x1, TOL, N=50):
    def print_iteration(i, x0, x1, p):
        print("{:<10} {:<15} {:<15} {:<15}".format(i, x0, x1, p))

    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x0", "x1", "p"))

    for i in range(N):
        if f(x1) - f(x0) == 0:
            print("Method cannot continue due to division by zero.")
            return None

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully

        print_iteration(i, x0, x1, p)
        x0, x1 = x1, p

    return p


if __name__ == '__main__':
    f = lambda x: math.cos(x ** 2 + 5 * x + 6) / (2 * math.exp(-x))  # Example function
    TOL = 1e-6  # Tolerance
    N = 20  # Maximum number of iterations

    # Define the range and step size
    a = -3
    b = a + 0.1

    print("Checking for sign changes in the range [-3, 2]:")

    while b <= 2:
        if f(a) * f(b) < 0:  # A sign change is detected
            print(f"\nSign change detected between a = {a} and b = {b}")
            roots = secant_method(f, a, b, TOL, N)
            print(f"The equation f(x) has an approximate root at x = {roots:.6f}")

        a += 0.1  # Increment the lower bound
        b = a + 0.1  # Adjust the upper bound
