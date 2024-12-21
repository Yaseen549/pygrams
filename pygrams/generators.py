import random
import uuid
import string


def generate_random_color(format='hex'):
    """
    Generates a random color code in the specified format ('hex' or 'rgb').

    Parameters:
    - format (str): The desired format of the color code. Options are:
        - 'hex': Returns a hexadecimal color code (e.g., "#1A2B3C").
        - 'rgb': Returns an RGB color code as a string (e.g., "rgb(123, 45, 67)").
      Defaults to 'hex'.

    Returns:
    - str: A random color code in the specified format.

    Raises:
    - ValueError: If the format is not 'hex' or 'rgb'.

    Examples:
    >>> generate_random_color('hex')
    '#A3F2B4' (random value)
    >>> generate_random_color('rgb')
    'rgb(45, 123, 89)' (random value)
    """
    if not isinstance(format, str):
        raise TypeError("Format must be a string.")
    
    if format.lower() == 'hex':
        color_code = '#' + ''.join(random.choice("0123456789ABCDEF") for _ in range(6))
        return color_code

    elif format.lower() == 'rgb':
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        return f"rgb({r}, {g}, {b})"

    else:
        raise ValueError("Invalid format. Use 'hex' or 'rgb'.")


def generate_odd_numbers(start, end, inclusive_end=False):
    """
    Generates a list of odd numbers within a specified range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range.
    - inclusive_end (bool): If True, includes the end number in the range; otherwise, it is exclusive.
      Defaults to False.

    Returns:
    - list[int]: A list of odd numbers within the specified range.

    Raises:
    - ValueError: If start is greater than end.

    Examples:
    >>> generate_odd_numbers(1, 10)
    [1, 3, 5, 7, 9]
    >>> generate_odd_numbers(1, 10, inclusive_end=True)
    [1, 3, 5, 7, 9]
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end values must be integers.")
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")

    if inclusive_end:
        end += 1
    return [num for num in range(start, end) if num % 2 != 0]


def generate_even_numbers(start, end, inclusive_end=False):
    """
    Generates a list of even numbers within a specified range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range.
    - inclusive_end (bool): If True, includes the end number in the range; otherwise, it is exclusive.
      Defaults to False.

    Returns:
    - list[int]: A list of even numbers within the specified range.

    Raises:
    - ValueError: If start is greater than end.

    Examples:
    >>> generate_even_numbers(1, 10)
    [2, 4, 6, 8]
    >>> generate_even_numbers(1, 10, inclusive_end=True)
    [2, 4, 6, 8, 10]
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end values must be integers.")
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")

    if inclusive_end:
        end += 1
    return [num for num in range(start, end) if num % 2 == 0]


def generate_prime_numbers(start, end, count):
    """
    Generates a specified number of prime numbers within a range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range (inclusive).
    - count (int): The maximum number of prime numbers to return.

    Returns:
    - list[int]: A list of prime numbers within the specified range.

    Raises:
    - ValueError: If start is greater than end or count is not positive.

    Examples:
    >>> generate_prime_numbers(10, 50, 5)
    [11, 13, 17, 19, 23]
    """
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(count, int):
        raise TypeError("Start, end, and count must be integers.")
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")
    if count <= 0:
        raise ValueError("Count must be a positive integer.")

    primes = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
        if len(primes) == count:
            break
    return primes


def generate_random_number(start, end):
    """
    Generates a random number within a specified range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range (inclusive).

    Returns:
    - int: A random number within the specified range.

    Raises:
    - ValueError: If start is greater than end.

    Examples:
    >>> generate_random_number(1, 10)
    7 (random value)
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers.")
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")

    return random.randint(start, end)


def generate_random_numbers(start, end, count):
    """
    Generates a list of random numbers within a specified range.

    Parameters:
    - start (int): The starting number of the range (inclusive).
    - end (int): The ending number of the range (inclusive).
    - count (int): The number of random numbers to generate.

    Returns:
    - list[int]: A list of random numbers within the specified range.

    Raises:
    - ValueError: If start is greater than end or count is not positive.

    Examples:
    >>> generate_random_numbers(1, 10, 3)
    [3, 7, 5] (random values)
    """
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(count, int):
        raise TypeError("Start, end, and count must be integers.")
    if start > end:
        raise ValueError("Start value cannot be greater than end value.")
    if count <= 0:
        raise ValueError("Count must be a positive integer.")

    return [random.randint(start, end) for _ in range(count)]


def generate_fibonacci_numbers(n):
    """
    Generates the first n Fibonacci numbers.

    Parameters:
    ----------
    n : int
        The number of Fibonacci numbers to generate.

    Returns:
    -------
    list
        A list containing the first n Fibonacci numbers.

    Raises:
    ------
    ValueError
        If n is not a positive integer.

    Examples:
    --------
    >>> generate_fibonacci_numbers(5)
    [0, 1, 1, 2, 3]

    >>> generate_fibonacci_numbers(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci


def generate_uuid():
    """
    Generates a unique identifier (UUID).

    Returns:
    -------
    str
        A UUID string.

    Examples:
    --------
    >>> generate_uuid()
    'e7b9b1f4-e0e7-47d6-9b84-2d60b34d0c44'
    """
    return str(uuid.uuid4())


def generate_password(length, options=None):
    """
    Creates a random password based on provided length and options.

    Parameters:
    ----------
    length : int
        The length of the password to generate.
    options : dict, optional
        Options for the password generation (e.g., include special chars, digits).

    Returns:
    -------
    str
        A randomly generated password string.

    Raises:
    ------
    ValueError
        If the length is not a positive integer.

    Examples:
    --------
    >>> generate_password(8)
    'D$2h6b8r'

    >>> generate_password(12, {'digits': True, 'special_chars': True})
    'K8!rO3$H2j#L'
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Default options if none provided
    if options is None:
        options = {}

    # Start with a base character set
    char_set = lowercase + uppercase
    if options.get('digits', False):
        char_set += digits
    if options.get('special_chars', False):
        char_set += special_chars
    
    # Randomly generate password
    return ''.join(random.choice(char_set) for _ in range(length))

