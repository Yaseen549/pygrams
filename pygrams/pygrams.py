from pygrams.getters import *
from pygrams.generators import *
from pygrams.haselements import *
from pygrams.issers import *
from pygrams.searching import *
from pygrams.sorting import *


def daysInMonth(year, month):
    """Returns number of days in a given year and month

    :returns: int
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) and month == 2:
        return 29
    return month_days[month - 1]


def bmi(height_in_meter, weight_in_kg):
    """Returns a Body Mass Index (BMI) value

    :returns: float or int
    """
    bmi_value = round(weight_in_kg / (height_in_meter * height_in_meter))
    return bmi_value


def fizzBuzz(start, end):
    """Returns a list of fizzBuzz

    :returns: list
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
            fizz_buzz_values.append(number)
    return fizz_buzz_values


def fibonacci(upto_n):
    """Returns a list of Fibonacci Sequence

    :returns: list
    """
    n1, n2 = 0, 1
    fibonacci_numbers = [n1, n2]
    for i in range(2, upto_n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        fibonacci_numbers.append(n3)
    return fibonacci_numbers


def factorial(n):
    """Returns a list of factorial numbers up to N

    :returns: int
    """
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)



def swap(value1, value2):
    """Swap two values eg: a=10, b=20 | a, b = swap(a, b) | print(a, b)

    :returns: Integer
    """
    temp = value1
    value1 = value2
    value2 = temp
    return value1, value2


def count(a_list, element):
    """Returns a number of occurrence of the given 'number' in 'a_list'

    :param a_list:
    :param element:
    :return: count, int
    """
    count = 0
    for ele in a_list:
        if (ele == element):
            count = count + 1
    return count


def reverse(param):
    """Reversing the given String or List

    :param param:
    :return: List
    """
    return param[::-1]


def charList(param):
    """returns all characters from a string of paragraph

    :param param:
    :return: list
    """
    a = param.replace(" ", "")
    return list(a)


def wordList(param):
    """Returns all the words as a list from a string of paragraph

    :param param:
    :return: list
    """
    return param.split(' ')


def joinList(list_of_words):
    """joins the list of words

    :param list_of_words:
    :return: list
    """
    return " ".join(list_of_words)

