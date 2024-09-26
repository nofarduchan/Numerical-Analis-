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
    f = lambda x: x ** 2 - 5 * x + 2
    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20
    roots = secant_method(f, x0, x1, TOL, N)

    print(f"\nThe equation f(x) has an approximate root at x = {roots:.6f}")
