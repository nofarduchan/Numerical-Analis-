
def machine_epsilon():
    """
    Calculate the machine epsilon, the smallest value that can be added to 1 
    and still result in a number different from 1 in floating point arithmetic.
    """
    eps = 1.0
    while (1 + eps) > 1:
        eps /= 2  # Keep dividing epsilon by 2 until 1 + eps is indistinguishable from 1

    return eps * 2  # Return the smallest value that caused a change


def calculate_expression():
    """
    Compute the expression abs(3.0 * (4.0 / 3.0 - 1) - 1), 
    which demonstrates loss of precision in floating-point arithmetic.
    """
    return abs(3.0 * (4.0 / 3.0 - 1) - 1)


def apply_epsilon_correction(value, epsilon):
    """
    Correct the floating-point error by subtracting machine epsilon.

    :param value: The original floating-point result.
    :param epsilon: The machine epsilon value.
    :return: The corrected value after subtracting machine epsilon.
    """
    return value - epsilon


def display_results(expression, corrected_expression, epsilon):
    """
    Display the results of the calculation before and after applying epsilon correction.
    """
    print("Machine Precision  : ", epsilon)
    print("\nResult of abs(3.0 * (4.0 / 3.0 - 1) - 1) :")
    print("Before using machine epsilon: {}".format(expression))
    print("After correcting with machine epsilon: {}".format(corrected_expression))


if __name__ == '__main__':
    # Calculate machine epsilon
    m_eps = machine_epsilon()

    # Calculate the expression that suffers from floating-point precision issues
    expression = calculate_expression()

    # Correct the expression using machine epsilon
    corrected_expression = apply_epsilon_correction(expression, m_eps)

    # Display the results
    display_results(expression, corrected_expression, m_eps)

"""
machine_epsilon: הפונקציה מחשבת את הערך הקטן ביותר שניתן להוסיף ל-1 ועדיין לראות שינוי בתוצאה במערכת הנקודה הצפה.
calculate_expression: הפונקציה מחשבת את הביטוי שמדגים את בעיית הדיוק באריתמטיקה של נקודה צפה.
apply_epsilon_correction: פונקציה זו מתקנת את השגיאה במספר הנקודה הצפה על ידי הפחתת ה-epsilon המיוחס למכונה.
display_results: אחראית להדפסת התוצאות לפני ואחרי השימוש ב-epsilon לתיקון הביטוי.
"""
