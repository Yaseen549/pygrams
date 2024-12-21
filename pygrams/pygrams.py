from pygrams.generators import *
from pygrams.getters import *
from pygrams.has_elements import *
from pygrams.is_elements import *
from pygrams.others import *
from pygrams.searching import *
from pygrams.sorting import *

from pygrams.data_manipulation.data_processing import *
from pygrams.data_manipulation.data_viz import *

from pygrams.utils.algorithmic_utils import *
from pygrams.utils.date_and_time_utils import *
from pygrams.utils.default_utils import *
from pygrams.utils.file_utils import *
from pygrams.utils.math_utils import *
from pygrams.utils.network_utils import *
from pygrams.utils.string_utils import *


def days_in_a_month(year, month):
    """
    Returns the number of days in a given month of a particular year.

    This function accounts for leap years and adjusts the number of days
    in February accordingly. For example, if the month is February (2)
    and the year is a leap year, it will return 29. Otherwise, it returns
    the standard number of days for that month.

    Args:
    year (int): The year to check.
    month (int): The month number (1 for January, 2 for February, etc.).

    Returns:
    int: The number of days in the specified month of the given year.

    Example:
    >>> days_in_a_month(2024, 2)
    29
    >>> days_in_a_month(2023, 2)
    28
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year manually
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if month == 2:
            return 29
    return month_days[month - 1]


def bmi(height_in_meter, weight_in_kg):
    """
    Calculates the Body Mass Index (BMI) based on height and weight.

    The BMI is calculated using the formula: BMI = weight(kg) / (height(m))^2.
    The result is rounded to two decimal places for easier interpretation.

    Args:
    height_in_meter (float): The height of the individual in meters.
    weight_in_kg (float): The weight of the individual in kilograms.

    Returns:
    float: The calculated BMI value rounded to two decimal places.

    Example:
    >>> bmi(1.75, 70)
    22.86
    """
    # Custom BMI calculation
    bmi_value = weight_in_kg / (height_in_meter * height_in_meter)
    return round(bmi_value, 2)


def fizz_buzz(start, end):
    """
    Returns a list of values from start to end, replacing multiples of 3 and 5
    with 'Fizz' and 'Buzz', respectively. If a number is divisible by both 3 and 5,
    it is replaced with 'FizzBuzz'.

    Args:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    list: A list of integers and strings ('Fizz', 'Buzz', 'FizzBuzz') based on the criteria.

    Example:
    >>> fizz_buzz(1, 10)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
    """
    fizz_buzz_values = []
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            fizz_buzz_values.append("FizzBuzz")
        elif number % 3 == 0:
            fizz_buzz_values.append("Fizz")
        elif number % 5 == 0:
            fizz_buzz_values.append("Buzz")
        else:
            fizz_buzz_values.append(str(number))
    return fizz_buzz_values


def fibonacci(upto_n):
    """
    Generates a list of Fibonacci numbers up to the nth value.

    The Fibonacci sequence is generated by adding the previous two numbers
    in the sequence to get the next number. The sequence starts with 0 and 1.

    Args:
    upto_n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    list: A list containing the Fibonacci sequence up to the specified number.

    Example:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    """
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < upto_n:
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)
    return fibonacci_numbers


def factorial(n):
    """
    Calculates the factorial of a given number using a loop.

    The factorial of a number n is the product of all positive integers
    less than or equal to n. For example, the factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120.

    Args:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.

    Example:
    >>> factorial(5)
    120
    """
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def swap(value1, value2):
    """
    Swaps two values and returns them in reversed order.

    This function manually swaps the values of two variables by using a
    temporary variable to hold one value during the process.

    Args:
    value1: The first value to swap.
    value2: The second value to swap.

    Returns:
    tuple: A tuple containing the swapped values.

    Example:
    >>> swap(10, 20)
    (20, 10)
    """
    # Simple manual swap using a temporary variable
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2


def count(a_list, element):
    """
    Counts the number of occurrences of a specified element in a list.

    This function iterates through the list and increments a counter each
    time the specified element is found.

    Args:
    a_list (list): The list to search.
    element: The element whose occurrences are to be counted.

    Returns:
    int: The number of times the element appears in the list.

    Example:
    >>> count([1, 2, 2, 3, 4], 2)
    2
    """
    count = 0
    for ele in a_list:
        if ele == element:
            count += 1
    return count


def reverse(param):
    """
    Reverses the given string or list.

    This function manually reverses the input by iterating backwards
    through the elements and collecting them in a new list.

    Args:
    param (str or list): The string or list to reverse.

    Returns:
    list or str: The reversed string or list.

    Example:
    >>> reverse('hello')
    ['o', 'l', 'l', 'e', 'h']
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    """
    reversed_param = []
    # Loop backwards through the list or string
    for i in range(len(param) - 1, -1, -1):
        reversed_param.append(param[i])
    return reversed_param


def leap_years_in_range(start, end):
    """
    Returns all leap years within a given range.

    Parameters:
    ----------
    start : int
        The start year of the range.
    end : int
        The end year of the range.

    Returns:
    -------
    list of int
        List of leap years within the range.

    Raises:
    ------
    ValueError
        If start year is greater than end year.

    Examples:
    --------
    >>> leap_years_in_range(2000, 2020)
    [2000, 2004, 2008, 2012, 2016, 2020]
    """
    if start > end:
        raise ValueError("Start year must not be greater than end year.")
    
    leap_years = []
    for year in range(start, end + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years.append(year)
    return leap_years


def nth_root(number, n):
    """
    Calculates the nth root of a number.

    Parameters:
    ----------
    number : float
        The number to find the nth root of.
    n : int
        The degree of the root.

    Returns:
    -------
    float
        The nth root of the number.

    Raises:
    ------
    ValueError
        If n is less than or equal to 0.

    Examples:
    --------
    >>> nth_root(27, 3)
    3.0
    """
    if n <= 0:
        raise ValueError("The root degree must be greater than 0.")
    return number ** (1 / n)


def palindrome(string_or_number):
    """
    Checks if a string or number is a palindrome.

    Parameters:
    ----------
    string_or_number : str or int
        The string or number to check.

    Returns:
    -------
    bool
        True if it is a palindrome, False otherwise.

    Examples:
    --------
    >>> palindrome("radar")
    True

    >>> palindrome(12321)
    True

    >>> palindrome("hello")
    False
    """
    s = str(string_or_number)
    return s == s[::-1]

