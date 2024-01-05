from pythonprograms.issers import *
from datetime import datetime, date
import inspect

def getUniqueElements(value):
    """Returns list of unique elements

    :param value:
    :return:
    """
    return list(set(value))


def getCurrentTime(*args):
    """Returns current Time: time format hhmmss

    :param args:
    :return: dateTime
    """
    now = datetime.now()
    if len(args) <= 0:
        return now.strftime("%H:%M:%S")
    elif len(args) == 3:
        return now.strftime(f"%{args[0].upper()}:%{args[1].upper()}:%{args[2].upper()}")
    elif len(args) == 2:
        return now.strftime(f"%{args[0].upper()}:%{args[1].upper()}")
    elif len(args) == 1:
        return now.strftime(f"%{args[0].upper()}")


def getTodayDate(dateFormat="ddmmyy"):
    """Date formats: "ddmmyy", "mdyy", "mddy", "mdy"

    :param dateFormat:
    :return: string
    """
    today = date.today()

    if dateFormat == "ddmmyy":
        # dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        return d1
    elif dateFormat == "tmdyy":
        # Textual month, day and year
        d2 = today.strftime("%B %d, %Y")
        return d2
    elif dateFormat == "mddy":
        # mm/dd/y
        d3 = today.strftime("%m/%d/%y")
        return d3
    elif dateFormat == "mdy":
        # Month abbreviation, day and year
        d4 = today.strftime("%b-%d-%Y")
        return d4
    else:
        d1 = today.strftime("%d/%m/%Y")
        return d1


def getSourceCode(program):
    """Returns a source code of a function or program

    :param program:
    :return: string, paragraph
    """
    lines = inspect.getsource(program)
    return lines



def getEvenNumbers(list_of_numbers):
    """Returns a list of Even Numbers in a list

    :returns: list
    """
    even_list = []
    for num in list_of_numbers:
        if isEven(num):
            even_list.append(num)
    return even_list


def getOddNumbers(list_of_numbers):
    """Returns a list of Odd Numbers in a list

    :returns: list
    """
    odd_list = []
    for num in list_of_numbers:
        if isOdd(num):
            odd_list.append(num)
    return odd_list


def getPrimeNumbers(list_of_numbers):
    """Returns a list of prime numbers from a list

    :returns: list
    """
    list_of_prime_numbers = []
    for number in list_of_numbers:
        if isPrime(number):
            list_of_prime_numbers.append(number)
    return list_of_prime_numbers


def getEvenNumbersInRange(start, end):
    """Returns a list of Even Numbers in range

    :returns: list
    """
    even_list = []
    for num in range(start, end):
        if isEven(num):
            even_list.append(num)
    return even_list


def getOddNumbersInRange(start, end):
    """Returns a list of Odd Numbers in range

    :returns: list
    """
    odd_list = []
    for num in range(start, end):
        if isOdd(num):
            odd_list.append(num)
    return odd_list


def getPrimeNumbersInRange(lower_value, upper_value):
    """Returns a list of prime numbers between range

    :returns: list
    """
    list_of_prime_numbers = []
    for number in range(lower_value, upper_value + 1):
        if isPrime(number):
            list_of_prime_numbers.append(number)
    return list_of_prime_numbers


def getEvenValues(a_list):
    """Returns even values from a list

    :returns: list
    """
    string_list = []
    if a_list == str(a_list):
        for eachString in a_list:
            if isOdd(a_list.index(eachString)):
                string_list.append(eachString)
        return string_list
    even_position = []
    even_values = []
    for position in range(0, len(a_list)):
        if isOdd(position):
            even_position.append(position)
    for even_position_value in even_position:
        even_values.append(a_list[even_position_value])
    return even_values


def getOddValues(a_list):
    """Returns odd values from a list

    :returns: list
    """
    string_list = []
    if a_list == str(a_list):
        for eachString in a_list:
            if isEven(a_list.index(eachString)):
                string_list.append(eachString)
        return string_list
    odd_position = []
    odd_values = []
    for position in range(0, len(a_list)):
        if isEven(position):
            odd_position.append(position)
    for odd_position_value in odd_position:
        odd_values.append(a_list[odd_position_value])
    return odd_values



def getPrimeValues(a_list):
    """Returns Prime values from a list

    :returns: list
    """
    string_list = []
    if a_list == str(a_list):
        for eachString in a_list:
            if isPrime(a_list.index(eachString)):
                string_list.append(eachString)
        return string_list
    prime_position = []
    prime_values = []
    for position in range(0, len(a_list)):
        if isPrime(position):
            prime_position.append(position-1)
    for prime_position_value in prime_position:
        prime_values.append(a_list[prime_position_value])
    return prime_values

