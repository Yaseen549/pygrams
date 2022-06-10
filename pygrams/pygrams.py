from pygrams.haselements import *
from pygrams.sorting import *
from pygrams.searching import *
from datetime import datetime, date
import inspect
import random


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


def daysInMonth(year, month):
    """Returns number of days in a given year and month

    :returns: int
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) and month == 2:
        return 29
    return month_days[month - 1]


def bmi(height_in_inch, weight_in_kg):
    """Returns a Body Mass Index (BMI) value

    :returns: float or int
    """
    bmi_value = round(weight_in_kg / (height_in_inch * height_in_inch))
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


def getUniqueElements(value):
    """Returns list of unique elements

    :param value:
    :return:
    """
    return list(set(value))


def generateRandomNumbers(start, end):
    """Returns a list of random numbers

    :param start:
    :param end:
    :return: list
    """
    randomList = []
    for nums in range(start, end):
        randomNumbers = random.randint(start, end)
        randomList.append(randomNumbers)
    return randomList


def generateRandomNumber(start, end):
    """Returns a random Number

    :param start:
    :param end:
    :return: int
    """
    return random.randint(start, end)


def getCurrentTime(*args):
    """Returns current Time:

    :param args:
    :return: dateTime
    """
    now = datetime.now()
    if len(args) == 3 or len(args) < 1 or len(args) == 0:
        return now.strftime("%H:%M:%S")
    elif len(args) == 2:
        return now.strftime("%H:%M")
    elif len(args) == 1:
        return now.strftime("%H")


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


def generateRandomColor():
    """Returns a hexa color value with '#' symbol

    :return: string
    """
    listOfElements = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    six_digit_color_cde = "#"
    for elem in range(0,6):
        six_digit_color_cde += random.choice(listOfElements)
    return str(six_digit_color_cde)


def reverse(param):
    """Reversing the given String or List

    :param param:
    :return: List
    """
    return param[::-1]


def getSourceCode(program):
    """Returns a source code of a function or program

    :param program:
    :return: string, paragraph
    """
    lines = inspect.getsource(program)
    return lines


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

