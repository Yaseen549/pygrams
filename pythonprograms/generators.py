from pythonprograms.issers import *
import random


def generateRandomColor():
    """Returns a hexa color value with '#' symbol

    :return: string
    """
    listOfElements = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    six_digit_color_cde = "#"
    for elem in range(0,6):
        six_digit_color_cde += random.choice(listOfElements)
    return str(six_digit_color_cde)


def generateOddNumbers(start, end):
    """Returns odd numbers list

    :param start:
    :param end:
    :return: list
    """
    random_odd_numbers = []
    for nums in range(start, end):
        if isOdd(nums):
            random_odd_numbers.append(nums)
    return random_odd_numbers


def generateEvenNumbers(start, end):
    """Returns even numbers list

    :param start:
    :param end:
    :return: list
    """
    random_even_numbers = []
    for nums in range(start, end):
        if isEven(nums):
            random_even_numbers.append(nums)
    return random_even_numbers


def generateRandomNumber(start, end):
    """Returns a random Number

    :param start:
    :param end:
    :return: int
    """
    return random.randint(start, end)


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