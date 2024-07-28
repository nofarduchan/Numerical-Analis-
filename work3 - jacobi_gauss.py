"""
Yenkel Jaoui 324523075
Dan Yosef Avitan 203109996
Yarden Itah 315097527
Nofar Duchan 322599424

git_link: https://github.com/nofarduchan/Numerical-Analis-.git
"""
import numpy as np

def is_diagonally_dominant(A):
    """
    Checks if a matrix is diagonally dominant.

    Parameters:
    A (ndarray): The input matrix.

    Returns:
    bool: True if the matrix is diagonally dominant, False otherwise.
    """
    n = len(A)
    for i in range(n):
        diagonal_element = abs(A[i][i])
        off_diagonal_sum = sum(abs(A[i][j]) for j in range(n) if i != j)

        if diagonal_element < off_diagonal_sum:
            return False
    return True


def jacobi(A, b, tol=0.001, max_iterations=1000):
    """
    Solves the system of linear equations using the Jacobi method.

    Parameters:
    A (ndarray): The coefficient matrix.
    b (ndarray): The constant terms.
    tol (float): The tolerance for convergence.
    max_iterations (int): The maximum number of iterations.

    Returns:
    ndarray or str: The solution vector if the matrix is diagonally dominant,
                    otherwise an error message.
    """
    if not is_diagonally_dominant(A):
        return "Matrix is not diagonally dominant"

    print("\njacobi: [Xr+1  Yr+1  Zr+1]")
    x = np.zeros_like(b, dtype=np.double)  # Initialize the solution vector with zeros
    print(x)
    for _ in range(max_iterations):
        x_new = np.zeros_like(x)  # Create a new vector to store the current iteration solution
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x[:i])  # Sum of the previous coefficients
            s2 = np.dot(A[i, i + 1:], x[i + 1:])  # Sum of the next coefficients
            x_new[i] = (b[i] - s1 - s2) / A[i, i]  # Update the current variable value

        if np.allclose(x, x_new, atol=tol):  # Check if the difference is within the allowed tolerance
            print(f'{x_new}')
            return x_new
        x = x_new  # Update the solution vector
        print(f'{x}')

    return x


def gauss_seidel(A, b, tol=0.001, max_iterations=1000):
    """
    Solves the system of linear equations using the Gauss-Seidel method.

    Parameters:
    A (ndarray): The coefficient matrix.
    b (ndarray): The constant terms.
    tol (float): The tolerance for convergence.
    max_iterations (int): The maximum number of iterations.

    Returns:
    ndarray or str: The solution vector if the matrix is diagonally dominant,
                    otherwise an error message.
    """
    if not is_diagonally_dominant(A):
        return "Matrix is not diagonally dominant"

    print("\ngauss seidel: [Xr+1  Yr+1  Zr+1]")
    x = np.zeros_like(b, dtype=np.double)  # Initialize the solution vector with zeros
    print(x)
    for _ in range(max_iterations):
        x_new = np.copy(x)  # Create a new vector to store the current iteration solution
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])  # Sum of the previous coefficients
            s2 = np.dot(A[i, i + 1:], x[i + 1:])  # Sum of the next coefficients
            x_new[i] = (b[i] - s1 - s2) / A[i, i]  # Update the current variable value

        if np.allclose(x, x_new, atol=tol):  # Check if the difference is within the allowed tolerance
            print(f'{x_new}')
            return x_new
        x = x_new  # Update the solution vector
        print(f'{x}')

    return x


def main():
    """
    Main function to test the Jacobi and Gauss-Seidel methods on a 3x3 matrix.
    """

    A = np.array([[5, 2, 1], [2, 6, 3], [1, 2, 7]], dtype=np.double)  # Define the coefficient matrix
    b = np.array([1, 0, 4], dtype=np.double)  # Define the constant terms vector

    # A = np.array([[4, 2, 0], [2, 10, 4], [0, 4, 5]], dtype=np.double)  # Define the coefficient matrix
    # b = np.array([2, 6, 5], dtype=np.double)  # Define the constant terms vector

    jacobi_solution = jacobi(A, b)  # Solve using the Jacobi method
    gauss_seidel_solution = gauss_seidel(A, b)  # Solve using the Gauss-Seidel method

    print("\n")
    print("Jacobi Solution:", jacobi_solution)
    print("Gauss-Seidel Solution:", gauss_seidel_solution)


if __name__ == "__main__":
    main()
