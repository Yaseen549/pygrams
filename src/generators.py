import random

# Function to generate a random hexadecimal color code
def generate_random_color():
    """
    Returns a hex color value with '#' symbol.
    Example: '#1A3F5C'
    """
    # Hexadecimal characters
    list_of_elements = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    six_digit_color_code = "#"  # Start with a '#'
    
    # Loop to select 6 random characters
    for _ in range(6):
        random_character = random.choice(list_of_elements)
        six_digit_color_code += random_character  # Add the character to the code
    
    return six_digit_color_code

# Function to generate odd numbers within a range
def generate_odd_numbers(start, end):
    """
    Returns a list of odd numbers in a given range.
    
    Parameters:
    - start: The starting number of the range (inclusive).
    - end: The ending number of the range (exclusive).
    
    Example:
    generate_odd_numbers(1, 10) -> [1, 3, 5, 7, 9]
    """
    odd_numbers = []  # Create an empty list to store odd numbers
    
    # Loop through the range
    for number in range(start, end):
        if number % 2 != 0:  # Check if the number is odd
            odd_numbers.append(number)  # Add to the list if odd
    
    return odd_numbers

# Function to generate even numbers within a range
def generate_even_numbers(start, end):
    """
    Returns a list of even numbers in a given range.
    
    Parameters:
    - start: The starting number of the range (inclusive).
    - end: The ending number of the range (exclusive).
    
    Example:
    generate_even_numbers(1, 10) -> [2, 4, 6, 8]
    """
    even_numbers = []  # Create an empty list to store even numbers
    
    # Loop through the range
    for number in range(start, end):
        if number % 2 == 0:  # Check if the number is even
            even_numbers.append(number)  # Add to the list if even
    
    return even_numbers

# Function to generate a single random number
def generate_random_number(start, end):
    """
    Returns a single random number within a given range.
    
    Parameters:
    - start: The starting number of the range (inclusive).
    - end: The ending number of the range (inclusive).
    
    Example:
    generate_random_number(1, 100) -> 57 (random value)
    """
    random_number = random.randint(start, end)  # Generate a random number
    return random_number

# Function to generate a list of random numbers
def generate_random_numbers(start, end, count):
    """
    Returns a list of random numbers within a given range.
    
    Parameters:
    - start: The starting number of the range (inclusive).
    - end: The ending number of the range (inclusive).
    - count: The number of random numbers to generate.
    
    Example:
    generate_random_numbers(1, 10, 3) -> [3, 7, 5] (random values)
    """
    random_list = []  # Create an empty list to store random numbers
    
    # Loop to generate 'count' random numbers
    for _ in range(count):
        random_number = random.randint(start, end)  # Generate a random number
        random_list.append(random_number)  # Add the number to the list
    
    return random_list
