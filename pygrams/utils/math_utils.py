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


def modulo(a, b):
    """
    Calculates the modulo (remainder) of two numbers.

    Parameters:
    ----------
    a : int or float
        The dividend.
    b : int or float
        The divisor.

    Returns:
    -------
    int or float
        The remainder when 'a' is divided by 'b'.

    Raises:
    ------
    ZeroDivisionError
        If 'b' is zero.

    Examples:
    --------
    >>> modulo(10, 3)
    1
    >>> modulo(7.5, 2)
    1.5
    """
    if b == 0:
        raise ZeroDivisionError("The divisor cannot be zero.")
    return a % b


def is_perfect_square(n):
    """
    Checks if a number is a perfect square.

    Parameters:
    ----------
    n : int
        The number to be checked.

    Returns:
    -------
    bool
        True if 'n' is a perfect square, otherwise False.

    Examples:
    --------
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(14)
    False
    """
    if n < 0:
        return False
    return math.isqrt(n) ** 2 == n


def prime_factors(n):
    """
    Finds the prime factors of a number.

    Parameters:
    ----------
    n : int
        The number to find the prime factors of.

    Returns:
    -------
    list
        A list of prime factors of 'n'.

    Examples:
    --------
    >>> prime_factors(18)
    [2, 3, 3]
    >>> prime_factors(29)
    [29]
    """
    factors = []
    if n <= 1:
        return factors

    # Find the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # n must be odd at this point, so we can check for odd factors starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


