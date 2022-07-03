def isArmstrong(number):
    """Returns True if the list contains an Armstrong Number

    :returns: bool
    """
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        return True
    else:
        return False

def isOddOrEven(number):
    """Checks whether the given number is Odd or Even

    :returns: String
    """
    if (number % 2) == 0:
        return "Even"
    else:
        return "Odd"


def isEven(number):
    """Checks whether the given number is Even else False

    :returns: bool
    """
    if number % 2 == 0:
        return True
    else:
        return False


def isOdd(number):
    """Checks whether the given number is Odd else False

    :returns: bool
    """
    if number % 2 != 0:
        return True
    else:
        return False


def isPrime(num):
    """Returns True if the list contains prime number else False

    :returns: bool
    """
    if num < 2:
        return False
    for n in range(2, num - 1):
        if num % n == 0:
            return False
    return True


def isLeapYear(year):
    """Returns boolean value based on the given year

    :returns: bool
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def isEvenNumberExist(list_of_numbers):
    """Returns True if Even number exist in a list else False

    :returns: bool
    """
    for num in list_of_numbers:
        if isEven(num):
            return True
    else:
        return False


def isOddNumberExist(list_of_numbers):
    """Returns True if Odd number exist in a list else False

    :returns: bool
    """
    for num in list_of_numbers:
        if isOdd(num):
            return True
    else:
        return False


def isPrimeNumberExist(list_of_numbers):
    """Returns True if prime number exist in a list else False

    :returns: bool
    """
    for number in list_of_numbers:
        if isPrime(number):
            return True
    else:
        return False


def isPositiveOrNegative(value):
    """Returns Positive else Negative
    :returns: String
    """
    if isPositive(value): return "Positive"
    if isNegative(value): return "Negative"
    if isZero(value): return "Zero"


def isPositive(value):
    """Returns 'True' if given value is positive(+) else 'False'

    :param value:
    :return: bool
    """
    if value > 0:
        return True
    else: return False


def isNegative(value):
    """Returns 'True' if given value is negative(-) else 'False'

    :param value:
    :return: bool
    """
    if value < 0:
        return True
    else: return False


def isZero(value):
    """Returns 'True' if given value is zero(0) else 'False'

    :param value:
    :return: bool
    """
    if value == 0:
        return True
    else: return False
