import math

def lcm(a, b):
    """
    Finds the least common multiple (LCM) of two integers.

    Parameters:
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns:
    -------
    int
        The LCM of the two integers.

    Raises:
    ------
    ValueError
        If a or b is not a positive integer.

    Examples:
    --------
    >>> lcm(4, 6)
    12
    """
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)


def lcm_of_list(numbers):
    """
    Computes the least common multiple (LCM) of a list of numbers.

    Parameters:
    ----------
    numbers : list of int
        A list of integers to compute the LCM.

    Returns:
    -------
    int
        The LCM of the list of numbers.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> lcm_of_list([4, 5, 6])
    60

    >>> lcm_of_list([15, 20, 25])
    300
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = lcm(lcm_result, num)
    
    return lcm_result


def gcd(a, b):
    """
    Finds the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns:
    -------
    int
        The GCD of the two integers.

    Raises:
    ------
    ValueError
        If a or b is not a positive integer.

    Examples:
    --------
    >>> gcd(48, 18)
    6

    >>> gcd(7, 5)
    1
    """
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers.")

    while b:
        a, b = b, a % b
    return a


def gcd_of_list(numbers):
    """
    Computes the greatest common divisor (GCD) of a list of numbers.

    Parameters:
    ----------
    numbers : list of int
        A list of integers to compute the GCD.

    Returns:
    -------
    int
        The GCD of the list of numbers.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> gcd_of_list([12, 15, 21])
    3

    >>> gcd_of_list([48, 180, 240])
    12
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    gcd_result = numbers[0]
    for num in numbers[1:]:
        gcd_result = math.gcd(gcd_result, num)
    
    return gcd_result


def power(base, exponent):
    """
    Calculates the power of a base raised to a given exponent.

    Parameters:
    ----------
    base : int or float
        The base number to be raised.
    exponent : int
        The exponent to raise the base to.

    Returns:
    -------
    int or float
        The result of raising the base to the given exponent.

    Raises:
    ------
    TypeError
        If the base or exponent is not a number.
    ValueError
        If the exponent is negative and the base is zero.

    Examples:
    --------
    >>> power(2, 3)
    8

    >>> power(5, 0)
    1

    >>> power(3, -2)
    0.1111111111111111
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, int):
        raise TypeError("Base must be a number, and exponent must be an integer.")
    
    if base == 0 and exponent < 0:
        raise ValueError("Base 0 cannot have a negative exponent.")
    
    return base ** exponent
