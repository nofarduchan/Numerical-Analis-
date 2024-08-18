"""
Yenkel Jaoui 324523075
Dan Yosef Avitan 203109996
Yarden Itah 315097527
Nofar Duchan 322599424

git_link: https://github.com/nofarduchan/Numerical-Analis-.git
"""

# השתמשנו בפונקציות מקובץ עזר נוסף, כדי שהקובץ יתקמפל יש להוריד קובץ זה מהגיט
from matrix_utility import *

def linearInterpolation(table_points, point):
    p = []
    result = 0
    flag = 1
    for i in range(len(table_points)):
        p.append(table_points[i][0])
    for i in range(len(p) - 1):
        if i <= point <= i + 1:
            x1 = table_points[i][0]
            x2 = table_points[i + 1][0]
            y1 = table_points[i][1]
            y2 = table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print("\nThe approximation (interpolation) of the point ", point, " is: ", round(result, 4))
            flag = 0
    if flag:
        x1 = table_points[0][0]
        x2 = table_points[1][0]
        y1 = table_points[0][1]
        y2 = table_points[1][1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print( "\nThe approximation (extrapolation) of the point ", point, " is: ", round(result, 4))




def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result

def GaussJordanElimination(matrix, vector):
    """
    Function for solving a linear equation using gauss's elimination method
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Solve Ax=b -> x=A(-1)b
    """
    # Pivoting process
    matrix, vector = RowXchange(matrix, vector)
    # Inverse matrix calculation
    invert = InverseMatrix(matrix, vector)
    return MulMatrixVector(invert, vector)




def UMatrix(matrix,vector):
    """
    :param matrix: Matrix nxn
    :return:Disassembly into a  U matrix
    """
    # result matrix initialized as singularity matrix
    U = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i])/matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)
    # U matrix is a doubling of elementary matrices that we used to reset organs under the pivot
    U = MultiplyMatrix(U, matrix)
    return U


def LMatrix(matrix, vector):
    """
       :param matrix: Matrix nxn
       :return:Disassembly into a  L matrix
       """
    # Initialize the result matrix
    L = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # pivoting process
        matrix, vector = RowXchageZero(matrix, vector)
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            # Finding the M(ij) to reset the organs under the pivot
            elementary[j][i] = -(matrix[j][i])/matrix[i][i]
            # L matrix is a doubling of inverse elementary matrices
            L[j][i] = (matrix[j][i]) / matrix[i][i]
            matrix = MultiplyMatrix(elementary, matrix)

    return L


def SolveLU(matrix, vector):
    """
    Function for deconstructing a linear equation by ungrouping LU
    :param matrix: Matrix nxn
    :param vector: Vector n
    :return: Solve Ax=b -> x=U(-1)L(-1)b
    """
    matrixU = UMatrix(matrix)
    matrixL = LMatrix(matrix)
    return MultiplyMatrix(InverseMatrix(matrixU), MultiplyMatrix(InverseMatrix(matrixL), vector))


def solveMatrix(matrixA,vectorb):
    detA = Determinant(matrixA, 1)
    # print( "\nDET(A) = ", detA)

    if detA != 0:
        # print("CondA = ", Cond(matrixA, InverseMatrix(matrixA, vectorb)))
        # print("\nnon-Singular Matrix - Perform GaussJordanElimination")
        result = GaussJordanElimination(matrixA, vectorb)
        # print(np.array(result))
        return result
    else:
        # print("Singular Matrix - Perform LU Decomposition\n")
        # print("Matrix U: \n")
        print(np.array(UMatrix(matrixA, vectorb)))
        # print("\nMatrix L: \n")
        print(np.array(LMatrix(matrixA, vectorb)))
        # print("\nMatrix A=LU: \n")
        result = MultiplyMatrix(LMatrix(matrixA, vectorb), UMatrix(matrixA, vectorb))
        # print(np.array(result))
        return result


def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix

    b = [[point[1]] for point in table_points]

    # print("The matrix obtained from the points: ", '\n', np.array(matrix))
    # print("\nb vector: ", '\n',np.array(b))
    matrixSol = solveMatrix(matrix, b)

    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    print("\nThe polynom:")
    print('P(X) = '+'+'.join([ '('+str(matrixSol[i][0])+') * x^' + str(i) + ' ' for i in range(len(matrixSol))])  )
    print(f"\nThe Result of P(X={x}) is:")
    print(result)
    return result


if __name__ == '__main__':

    # Defining the point pairs
    points = [(0, 0), (1, 0.8415), (2, 0.9093)]

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
        result = linearInterpolation(points, x)
    elif method == 1:
        # if len(points) < 3:
        #     print("At least 3 points are required for polynomial interpolation.")
        # else:
        result = polynomialInterpolation(points, x)
    elif method == 2:
        # if len(points) < 3:
        #     print("At least 3 points are required for polynomial interpolation.")
        # else:
        x_data = [point[0] for point in points]
        y_data = [point[1] for point in points]
        result = lagrange_interpolation(x_data, y_data, x)
        print(f"The approximation (extrapolation) of x = {x} using Lagrange interpolation is: {result}")
    else:
        print("Invalid method selection, please try again.")