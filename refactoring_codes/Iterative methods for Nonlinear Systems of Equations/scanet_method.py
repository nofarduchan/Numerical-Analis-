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
    # f = lambda x: x ** 2 - 5 * x + 2  # הפונקציה שלך
    f = lambda x: math.cos(x ** 2 + 5 * x + 6) / (2 * math.exp(-x))
    TOL = 1e-6
    N = 20

    # הגדרת הטווח והקפיצות
    a = -3
    b = a + 0.1

    print("Checking for sign changes in the range [-3, 2]:")

    while b <= 2:
        if f(a) * f(b) < 0:  # שינוי סימן נמצא
            print(f"\nSign change detected between a = {a} and b = {b}")
            roots = secant_method(f, a, b, TOL, N)
            print(f"The equation f(x) has an approximate root at x = {roots:.6f}")

        a += 0.1  # הגדלת הקצה התחתון
        b = a + 0.1  # התאמת הקצה העליון
