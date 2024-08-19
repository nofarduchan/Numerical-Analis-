"""
Yenkel Jaoui 324523075
Dan Yosef Avitan 203109996
Yarden Itah 315097527
Nofar Duchan 322599424

git_link: https://github.com/nofarduchan/Numerical-Analis-.git
"""


def linear_interpolation(points, x):
    """
    Perform linear interpolation between the two closest points to x.

    param points: List of points [(x0, y0), (x1, y1), ...]
    param x: x value for which to find the interpolated y value
    return: y value
    """
    # Sort points by x values
    points = sorted(points)

    # Find the two closest points
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    raise ValueError("x value is out of the range of provided points.")


def polynomial_interpolation(points, x):
    """
    Perform polynomial interpolation using the provided points.

    :param points: List of points [(x0, y0), (x1, y1), (x2, y2), ...]
    :param x: x value for which to find the interpolated y value
    :return: interpolated y value
    """
    n = len(points)
    result = 0

    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        result += term

    return result



def lagrange_interpolation(points, x):
    """
    param points: List of points [(x0, y0), (x1, y1), (x2, y2), ...]
    param x: x value for which to find the interpolated y value
    return: y value
    """
    total = 0
    n = len(points)
    # run on all the points
    for i in range(n):
        xi, yi = points[i]
        term = yi
        # run on all the points with point i
        for j in range(n):
            if j != i:
                # split the points[j] in xj,yj.
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        total += term
    return total




def main():
    # Defining the point pairs
    points =  [(0, 0), (1, 0.8415), (2, 0.9093)]

    # Getting the x value from the user
    x = 1.28

    # Asking the user for the interpolation method
    print("Choose interpolation method: ")
    print("0: Linear")
    print("1: Polynomial (3 points)")
    print("2: Lagrange (3 points)")

    method = int(input("Enter 0, 1, or 2: "))

    if method == 0:
        # if len(points) < 2:
        #     print("At least 2 points are required for linear interpolation.")
        # else:
            result = linear_interpolation(points, x)
            print(f"The estimated value of y for x = {x} using linear interpolation is: {result}")
    elif method == 1:
        # if len(points) < 3:
        #     print("At least 3 points are required for polynomial interpolation.")
        # else:
            result = polynomial_interpolation(points, x)
            print(f"The estimated value of y for x = {x} using polynomial interpolation is: {result}")
    elif method == 2:
        # if len(points) < 3:
        #     print("At least 3 points are required for polynomial interpolation.")
        # else:
            result = lagrange_interpolation(points, x)
            print(f"The estimated value of y for x = {x} using Lagrange interpolation is: {result}")
    else:
        print("Invalid method selection, please try again.")


if __name__ == "__main__":
    main()
