def oddOrEven(number):
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
    for n in range(2, (num) - 1):
        if num % n == 0:
            return False
    return True


def isEvenNumberExist(listOfNumbers):
    """Returns True if Even number exist in a list else False
    :returns: bool
    """
    for num in listOfNumbers:
        if isEven(num):
            return True
    else:
        return False


def isOddNumberExist(listOfNumbers):
    """Returns True if Odd number exist in a list else False
    :returns: bool
    """
    for num in listOfNumbers:
        if isOdd(num):
            return True
    else:
        return False


def isPrimeNumberExist(listOfNumbers):
    """Returns True if prime number exist in a list else False
    :returns: bool
    """
    for number in listOfNumbers:
        if isPrime(number):
            return True
    else:
        return False



def getEvenNumbers(listOfNums):
    """Returns a list of Even Numbers in a list
    :returns: list
    """
    evenList = []
    for num in listOfNums:
        if isEven(num):
            evenList.append(num)
    return evenList


def getOddNumbers(listOfNums):
    """Returns a list of Odd Numbers in a list
    :returns: list
    """
    oddList = []
    for num in listOfNums:
        if isOdd(num):
            oddList.append(num)
    return oddList


def getPrimeNumbers(listOfNumbers):
    """Returns a list of prime numbers from a list
    :returns: list
    """
    listOfPrimeNumbers = []
    for number in listOfNumbers:
        if isPrime(number):
            listOfPrimeNumbers.append(number)
    return listOfPrimeNumbers




def getEvenNumbersInRange(start, end):
    """Returns a list of Even Numbers in range
    :returns: list
    """
    evenList = []
    for num in range(start, end):
        if isEven(num):
            evenList.append(num)
    return evenList



def getOddNumbersInRange(start, end):
    """Returns a list of Odd Numbers in range
    :returns: list
    """
    evenList = []
    for num in range(start, end):
        if isOdd(num):
            evenList.append(num)
    return evenList


def getPrimeNumbersInRange(lower_value, upper_value):
    """Returns a list of prime numbers between range
    :returns: list
    """
    listOfPrimeNumbers = []
    for number in range(lower_value, upper_value + 1):
        if isPrime(number):
            listOfPrimeNumbers.append(number)
    return listOfPrimeNumbers




def getEvenValues(alist):
    """Returns even values from a list
    :returns: list
    """
    evenPosition = []
    evenValues = []
    for nums in range(0, len(alist)):
        if isOdd(nums):
            evenPosition.append(nums)
    for numbs in evenPosition:
        evenValues.append(alist[numbs])
    return evenValues


def getOddValues(alist):
    """Returns odd values from a list
    :returns: list
    """
    oddPosition = []
    oddValues = []
    for nums in range(0, len(alist)):
        if isEven(nums):
            oddPosition.append(nums)
    for numbs in oddPosition:
        oddValues.append(alist[numbs])
    return oddValues



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


def bmi(height_in_cm, weight_in_kg):
    """Returns a Body Mass Index (BMI) value
    :returns: float or int
    """
    bmi_value = round(weight_in_kg / (height_in_cm * height_in_cm))
    return bmi_value


def fizzBuzz(start, end):
    """Returns a list of fizzBuzz
    :returns: list
    """
    fizzBuzzValues = []
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            fizzBuzzValues.append("FizzBuzz")
        elif number % 3 == 0:
            fizzBuzzValues.append("Fizz")
        elif number % 5 == 0:
            fizzBuzzValues.append("Buzz")
        else:
            fizzBuzzValues.append(number)
    return fizzBuzzValues


def fibonacci(upto_n):
    """Returns a list of Fibonacci Sequence
    :returns: list
    """
    n1, n2 = 0, 1
    fibonacci_nums = [n1, n2]
    for i in range(2, upto_n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        fibonacci_nums.append(n3)
    return fibonacci_nums


def factorial(n):
    """Returns a list of factorial numbers up to N
    :returns: int
    """
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def isArmstrong(num):
    """Returns True if the list contains an Armstrong Number
    :returns: bool
    """
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if num == sum:
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

