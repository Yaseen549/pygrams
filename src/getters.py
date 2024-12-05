from datetime import datetime, date
import inspect

# Function to get unique elements from a list
def get_unique_elements(value):
    """Returns a list of unique elements from the input list."""
    return list(set(value))


# Function to get the current time in a specified format
def get_current_time(*args):
    """Returns the current time in the format hh:mm:ss or custom format based on input arguments."""
    # Get the current time
    now = datetime.now()
    
    # If no arguments, return time in hh:mm:ss format
    if len(args) == 0:
        return now.strftime("%H:%M:%S")
    
    # If arguments are provided, return time in custom format
    format_string = ":".join([f"%{arg.upper()}" for arg in args])
    return now.strftime(format_string)


# Function to get today's date in a specified format
def get_today_date(date_format="ddmmyy"):
    """Returns the current date in various formats like dd/mm/yy, mm/dd/yy, etc."""
    today = date.today()
    
    if date_format == "ddmmyy":
        return today.strftime("%d/%m/%Y")  # Format: day/month/year
    elif date_format == "tmdyy":
        return today.strftime("%B %d, %Y")  # Format: Month day, year
    elif date_format == "mddy":
        return today.strftime("%m/%d/%y")  # Format: month/day/year (two digits)
    elif date_format == "mdy":
        return today.strftime("%b-%d-%Y")  # Format: month abbreviation-day-year
    else:
        return today.strftime("%d/%m/%Y")  # Default format


# Function to get the source code of a given program or function
def get_source_code(program):
    """Returns the source code of a function or program as a string."""
    return inspect.getsource(program)


# Function to get even numbers from a list of numbers
def get_even_numbers(list_of_numbers):
    """Returns a list of even numbers from the input list."""
    even_list = []
    for num in list_of_numbers:
        if num % 2 == 0:  # Check if the number is even
            even_list.append(num)
    return even_list


# Function to get odd numbers from a list of numbers
def get_odd_numbers(list_of_numbers):
    """Returns a list of odd numbers from the input list."""
    odd_list = []
    for num in list_of_numbers:
        if num % 2 != 0:  # Check if the number is odd
            odd_list.append(num)
    return odd_list


# Function to get prime numbers from a list of numbers
def get_prime_numbers(list_of_numbers):
    """Returns a list of prime numbers from the input list."""
    prime_list = []
    for num in list_of_numbers:
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, num):
                if num % i == 0:  # If divisible by any number, it's not prime
                    break
            else:
                prime_list.append(num)  # If no divisor is found, it's prime
    return prime_list


# Function to get even numbers in a specific range
def get_even_numbers_in_range(start, end):
    """Returns a list of even numbers within a given range."""
    even_list = []
    for num in range(start, end):
        if num % 2 == 0:  # Check if the number is even
            even_list.append(num)
    return even_list


# Function to get odd numbers in a specific range
def get_odd_numbers_in_range(start, end):
    """Returns a list of odd numbers within a given range."""
    odd_list = []
    for num in range(start, end):
        if num % 2 != 0:  # Check if the number is odd
            odd_list.append(num)
    return odd_list


# Function to get prime numbers in a specific range
def get_prime_numbers_in_range(lower_value, upper_value):
    """Returns a list of prime numbers within a given range."""
    prime_list = []
    for num in range(lower_value, upper_value + 1):
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, num):
                if num % i == 0:  # If divisible by any number, it's not prime
                    break
            else:
                prime_list.append(num)  # If no divisor is found, it's prime
    return prime_list


# Function to get even values from a list based on their positions
def get_even_values(a_list):
    """Returns the values located at even positions in the list."""
    even_values = []
    for i in range(0, len(a_list), 2):  # Iterate over even positions (0, 2, 4, ...)
        even_values.append(a_list[i])
    return even_values


# Function to get odd values from a list based on their positions
def get_odd_values(a_list):
    """Returns the values located at odd positions in the list."""
    odd_values = []
    for i in range(1, len(a_list), 2):  # Iterate over odd positions (1, 3, 5, ...)
        odd_values.append(a_list[i])
    return odd_values


# Function to get prime values from a list based on prime positions
def get_prime_values(a_list):
    """Returns values at positions that are prime numbers."""
    prime_values = []
    for i in range(len(a_list)):
        if i > 1:  # Start checking from position 2 (since 0 and 1 are not prime)
            for j in range(2, i):
                if i % j == 0:  # If the index is divisible by any number, it's not prime
                    break
            else:
                prime_values.append(a_list[i])  # If index is prime, add the value to the list
    return prime_values
