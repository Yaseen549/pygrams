def is_armstrong(number):
    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number equal to the sum of its digits raised
    to the power of the number of digits.
    For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 153,
    and 9474 is an Armstrong number because 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474.

    :param number: int - The number to check.
    :return: bool - True if Armstrong, False otherwise.
    """
    # Convert the number to a string to count digits
    digits = str(number)
    num_digits = len(digits)
    
    total = 0
    temp = number
    
    # Loop over each digit and raise it to the power of num_digits
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits  # Raise digit to the power of num_digits
        temp //= 10  # Remove the last digit
    
    return total == number  # Compare sum with the original number


def is_even(number):
    """
    Checks if a number is even.

    :param number: int - The number to check.
    :return: bool - True if even, False otherwise.
    """
    return number % 2 == 0


def is_odd(number):
    """
    Checks if a number is odd.

    :param number: int - The number to check.
    :return: bool - True if odd, False otherwise.
    """
    return number % 2 != 0


def is_prime(number):
    """
    Checks if a number is prime.

    A prime number is greater than 1 and divisible only by 1 and itself.

    :param number: int - The number to check.
    :return: bool - True if prime, False otherwise.
    """
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):  # Check divisors up to square root of the number.
        if number % i == 0:
            return False
    
    return True


def is_leap_year(year):
    """
    Checks if a year is a leap year.

    A leap year is divisible by 4, but not divisible by 100 unless also divisible by 400.

    :param year: int - The year to check.
    :return: bool - True if leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


def has_even_number(numbers):
    """
    Checks if a list contains at least one even number.

    :param numbers: list - List of integers.
    :return: bool - True if an even number exists, False otherwise.
    """
    for number in numbers:
        if is_even(number):
            return True
    return False


def has_odd_number(numbers):
    """
    Checks if a list contains at least one odd number.

    :param numbers: list - List of integers.
    :return: bool - True if an odd number exists, False otherwise.
    """
    for number in numbers:
        if is_odd(number):
            return True
    return False


def has_prime_number(numbers):
    """
    Checks if a list contains at least one prime number.

    :param numbers: list - List of integers.
    :return: bool - True if a prime number exists, False otherwise.
    """
    for number in numbers:
        if is_prime(number):
            return True
    return False


def is_positive(value):
    """
    Checks if a value is positive.

    :param value: int - The value to check.
    :return: bool - True if positive, False otherwise.
    """
    return value > 0


def is_negative(value):
    """
    Checks if a value is negative.

    :param value: int - The value to check.
    :return: bool - True if negative, False otherwise.
    """
    return value < 0


def is_zero(value):
    """
    Checks if a value is zero.

    :param value: int - The value to check.
    :return: bool - True if zero, False otherwise.
    """
    return value == 0


def describe_number(value):
    """
    Describes a number as Positive, Negative, or Zero.

    :param value: int - The number to describe.
    :return: str - A string describing the number.
    """
    if is_positive(value):
        return "Positive"
    if is_negative(value):
        return "Negative"
    return "Zero"
