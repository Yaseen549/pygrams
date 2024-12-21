import re


def is_armstrong(number):
    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its digits 
    raised to the power of the number of digits. For example:
      - 153 is an Armstrong number because 1³ + 5³ + 3³ = 153
      - 9474 is an Armstrong number because 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474

    Parameters:
    - number (int or float): The number to check.

    Returns:
    - bool: True if the number is an Armstrong number, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_armstrong(153)
    True
    >>> is_armstrong(9474)
    True
    >>> is_armstrong(123)
    False
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    
    digits = str(abs(int(number)))  # Convert to integer and handle negative values
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == number


def is_even(number):
    """
    Checks if a number is even.

    An even number is an integer divisible by 2 without a remainder.

    Parameters:
    - number (int or float): The number to check.

    Returns:
    - bool: True if the number is even, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_even(4)
    True
    >>> is_even(7)
    False
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    
    return number % 2 == 0


def is_odd(number):
    """
    Checks if a number is odd.

    An odd number is an integer that is not divisible by 2.

    Parameters:
    - number (int or float): The number to check.

    Returns:
    - bool: True if the number is odd, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_odd(7)
    True
    >>> is_odd(4)
    False
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number.")
    
    return number % 2 != 0


def is_prime(number):
    """
    Checks if a number is prime.

    A prime number is greater than 1 and divisible only by 1 and itself.

    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.

    Raises:
    - TypeError: If the input is not an integer.

    Example:
    >>> is_prime(29)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True


def is_leap_year(year):
    """
    Checks if a year is a leap year.

    A leap year occurs every 4 years, except for years divisible by 100,
    unless the year is also divisible by 400.

    Parameters:
    - year (int): The year to check.

    Returns:
    - bool: True if the year is a leap year, False otherwise.

    Raises:
    - TypeError: If the input is not an integer.

    Example:
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    if not isinstance(year, int):
        raise TypeError("Input must be an integer.")
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_positive(value):
    """
    Checks if a number is positive.

    A positive number is greater than zero.

    Parameters:
    - value (int or float): The number to check.

    Returns:
    - bool: True if the number is positive, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_positive(5)
    True
    >>> is_positive(-3)
    False
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    
    return value > 0


def is_negative(value):
    """
    Checks if a number is negative.

    A negative number is less than zero.

    Parameters:
    - value (int or float): The number to check.

    Returns:
    - bool: True if the number is negative, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_negative(-5)
    True
    >>> is_negative(3)
    False
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    
    return value < 0


def is_zero(value):
    """
    Checks if a number is zero.

    Parameters:
    - value (int or float): The number to check.

    Returns:
    - bool: True if the number is zero, False otherwise.

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> is_zero(0)
    True
    >>> is_zero(3)
    False
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    
    return value == 0


def describe_number(value):
    """
    Describes a number as Positive, Negative, or Zero.

    Parameters:
    - value (int or float): The number to describe.

    Returns:
    - str: "Positive", "Negative", or "Zero".

    Raises:
    - TypeError: If the input is not a number.

    Example:
    >>> describe_number(5)
    'Positive'
    >>> describe_number(-3)
    'Negative'
    >>> describe_number(0)
    'Zero'
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a number.")
    
    if is_positive(value):
        return "Positive"
    if is_negative(value):
        return "Negative"
    return "Zero"


def is_anagram(string1, string2):
    """
    Checks if two strings are anagrams.

    Parameters:
    ----------
    string1 : str
        The first string to check.
    string2 : str
        The second string to check.

    Returns:
    -------
    bool
        True if the strings are anagrams, False otherwise.

    Raises:
    ------
    TypeError
        If the inputs are not strings.

    Examples:
    --------
    >>> is_anagram("listen", "silent")
    True

    >>> is_anagram("hello", "world")
    False
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Both inputs must be strings.")
    
    return sorted(string1) == sorted(string2)


def is_palindrome(string_or_number):
    """
    Determines if a string or number is a palindrome.

    Parameters:
    ----------
    string_or_number : str or int
        The string or number to check.

    Returns:
    -------
    bool
        True if the string or number is a palindrome, False otherwise.

    Raises:
    ------
    TypeError
        If the input is neither a string nor an integer.

    Examples:
    --------
    >>> is_palindrome("madam")
    True

    >>> is_palindrome(121)
    True

    >>> is_palindrome("hello")
    False
    """
    if not isinstance(string_or_number, (str, int)):
        raise TypeError("Input must be a string or an integer.")
    
    str_value = str(string_or_number)  # Convert number to string for uniformity
    return str_value == str_value[::-1]


def is_happy_number(number):
    """
    Checks if a number is a "happy number."

    Parameters:
    ----------
    number : int
        The number to check.

    Returns:
    -------
    bool
        True if the number is a happy number, False otherwise.

    Raises:
    ------
    ValueError
        If the number is not a positive integer.

    Examples:
    --------
    >>> is_happy_number(19)
    True

    >>> is_happy_number(4)
    False
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")
    
    def sum_of_squares(n):
        return sum(int(digit) ** 2 for digit in str(n))
    
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum_of_squares(number)
    
    return number == 1


def is_valid_email(email):
    """
    Validates an email address format.

    Parameters:
    ----------
    email : str
        The email address to validate.

    Returns:
    -------
    bool
        True if the email address is valid, False otherwise.

    Raises:
    ------
    TypeError
        If the email is not a string.

    Examples:
    --------
    >>> is_valid_email("test@example.com")
    True

    >>> is_valid_email("invalid-email")
    False
    """
    if not isinstance(email, str):
        raise TypeError("Input must be a string.")
    
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None

