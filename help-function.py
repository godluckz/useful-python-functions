# This will give summary of the function and what rapameters it takes
# help(print)

print("-------------------------")

#Can be used for personal functions as long as they have function string
def _multiply(p_num1 : float, p_num2 : float) -> float:
    """"
    p_num1: value 1 - float
    p_num2: value 2 - float

    returns: float

    function will multiply the given two numbers and return the result.
    """

    return p_num1 * p_num2

help(_multiply)