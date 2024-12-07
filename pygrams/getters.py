from datetime import datetime, date
import inspect


# Function to get unique elements from str, list/tuple, dict
def get_unique_elements(value):
    """
    Returns a list or string of unique elements from a string, list, or tuple.

    Removes duplicates while preserving the original order of elements.

    Parameters:
    ----------
    value : str, list, or tuple
        The input value from which to extract unique elements.

    Returns:
    -------
    str or list or tuple
        A string of unique characters if the input is a string.
        A list or tuple of unique elements if the input is a list or tuple.

    Raises:
    ------
    TypeError
        If the input is not a string, list, or tuple.

    Examples:
    --------
    >>> get_unique_elements("hello")
    'helo'

    >>> get_unique_elements([1, 2, 2, 3, 4, 4])
    [1, 2, 3, 4]

    >>> get_unique_elements((1, 2, 2, 3, 4, 4))
    (1, 2, 3, 4)

    >>> get_unique_elements(123)  # Invalid input
    Traceback (most recent call last):
      ...
    TypeError: Input must be a string, list, or tuple.
    """
    if isinstance(value, str):
        # Remove duplicate characters while preserving order
        return ''.join(sorted(set(value), key=value.index))
    elif isinstance(value, (list, tuple)):
        # Remove duplicate elements while preserving order
        return type(value)(sorted(set(value), key=value.index))
    else:
        raise TypeError("Input must be a string, list, or tuple.")


# Function to get the current time in a specified format
def get_current_time(*args):
    """
    Returns the current time in the format hh:mm:ss by default or in a custom format 
    based on the input arguments.

    Parameters:
    ----------
    *args : str
        Optional arguments specifying custom time format components.
        Valid options include:
        - 'h' or 'H': Hours (12-hour or 24-hour format)
        - 'm': Minutes
        - 's': Seconds
        - 'p': AM/PM marker (for 12-hour format)

    Returns:
    -------
    str
        The current time formatted as hh:mm:ss by default, or a custom format 
        based on the provided arguments.

    Raises:
    ------
    ValueError
        If invalid arguments are provided.

    Examples:
    --------
    >>> get_current_time()
    '14:35:42'  # Example output (depends on current time)

    >>> get_current_time('h', 'm', 's')
    '02:35:42'  # Example output in 12-hour format

    >>> get_current_time('h', 'm', 'p')
    '02:35 PM'  # Example output with AM/PM marker

    >>> get_current_time('H', 'm', 's')
    '14:35:42'  # Example output in 24-hour format

    >>> get_current_time('x')  # Invalid format
    Traceback (most recent call last):
      ...
    ValueError: Invalid time format argument: 'x'. Valid options are: 'h', 'H', 'm', 's', 'p'.
    """
    # Define valid format options
    valid_formats = {'h': '%I', 'H': '%H', 'm': '%M', 's': '%S', 'p': '%p'}
    
    # If no arguments are provided, return time in default format
    if not args:
        return datetime.now().strftime("%H:%M:%S")
    
    # Build the format string based on arguments
    format_string = []
    for arg in args:
        if arg.lower() not in valid_formats:
            raise ValueError(f"Invalid time format argument: '{arg}'. "
                             "Valid options are: 'h', 'H', 'm', 's', 'p'.")
        format_string.append(valid_formats[arg.lower()])
    
    # Join the format components and format the current time
    return datetime.now().strftime(":".join(format_string))


# Function to get today's date in a specified format
def get_today_date(date_format="ddmmyy"):
    """
    Returns the current date in various formats, based on the specified format string.

    Parameters:
    ----------
    date_format : str, optional
        A string representing the desired date format. Valid options include:
        - "ddmmyy": Day/Month/Year (default) -> e.g., 07/12/2024
        - "tmdyy": Full Month Day, Year -> e.g., December 7, 2024
        - "mddy": Month/Day/Year (two-digit year) -> e.g., 12/07/24
        - "mdy": Abbreviated Month-Day-Year -> e.g., Dec-07-2024

    Returns:
    -------
    str
        A string representing the current date in the specified format.

    Raises:
    ------
    ValueError
        If an invalid date format is provided.

    Examples:
    --------
    >>> get_today_date()
    '07/12/2024'  # Example output (depends on today's date)

    >>> get_today_date("tmdyy")
    'December 7, 2024'

    >>> get_today_date("mddy")
    '12/07/24'

    >>> get_today_date("mdy")
    'Dec-07-2024'

    >>> get_today_date("xyz")  # Invalid format
    Traceback (most recent call last):
      ...
    ValueError: Invalid date format: 'xyz'. Valid options are: 'ddmmyy', 'tmdyy', 'mddy', 'mdy'.
    """
    # Define valid formats
    valid_formats = {
        "ddmmyy": "%d/%m/%Y",  # Day/Month/Year
        "tmdyy": "%B %d, %Y",  # Full Month Day, Year
        "mddy": "%m/%d/%y",    # Month/Day/Year (two digits)
        "mdy": "%b-%d-%Y"      # Abbreviated Month-Day-Year
    }

    # Validate the date_format input
    if date_format not in valid_formats:
        raise ValueError(f"Invalid date format: '{date_format}'. "
                         "Valid options are: 'ddmmyy', 'tmdyy', 'mddy', 'mdy'.")

    # Return the formatted date based on the chosen format
    return date.today().strftime(valid_formats[date_format])


# Function to get the source code of a given program or function
def get_source_code(program):
    """
    Returns the source code of a given function, method, or program as a string.

    Parameters:
    ----------
    program : function or method
        The function or method whose source code is to be retrieved.

    Returns:
    -------
    str
        The source code of the given function or method.

    Raises:
    ------
    TypeError
        If the provided argument is not a function or method.

    Examples:
    --------
    >>> def example_function():
    >>>     return "Hello, World!"
    >>> get_source_code(example_function)
    'def example_function():\n    return "Hello, World!"\n'

    >>> get_source_code(print)
    'def print(...):\n    ...  # Built-in function in Python\n'

    >>> get_source_code(123)  # Invalid input
    Traceback (most recent call last):
      ...
    TypeError: The provided argument must be a function or method.
    """
    
    # Check if the input is a function or method
    if not callable(program):
        raise TypeError("The provided argument must be a function or method.")
    
    # Return the source code of the function or method
    return inspect.getsource(program)


# Function to get even numbers from a string, list, tuple, or dictionary.
def get_even_numbers(value):
    """
    Returns a list of even numbers from a string, list, tuple, or dictionary.
    For strings, checks if the Unicode values of the characters are even.

    Parameters:
    ----------
    value : str, list, tuple, or dict
        The input value from which even numbers are extracted.
        - For lists and tuples, checks for even integers or floats.
        - For strings, checks the Unicode values of characters.
        - For dictionaries, checks the values for even numbers.

    Returns:
    -------
    list
        A list of even numbers (or characters for strings) from the input.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_even_numbers([1, 2, 3, 4])
    [2, 4]

    >>> get_even_numbers("abc")
    ['a']

    >>> get_even_numbers({"a": 2, "b": 3})
    [2]
    """
    even_list = []

    if isinstance(value, (list, tuple)):
        for num in value:
            if isinstance(num, (int, float)) and num % 2 == 0:
                even_list.append(num)
    elif isinstance(value, str):
        for char in value:
            if ord(char) % 2 == 0:
                even_list.append(char)
    elif isinstance(value, dict):
        for val in value.values():
            if isinstance(val, (int, float)) and val % 2 == 0:
                even_list.append(val)
    else:
        raise TypeError("Input must be a string, list, tuple, or dictionary.")

    return even_list


# Function to get odd numbers from a string, list, tuple, or dictionary.
def get_odd_numbers(value):
    """
    Returns a list of odd numbers from a string, list, tuple, or dictionary.
    For strings, checks if the Unicode values of the characters are odd.

    Parameters:
    ----------
    value : str, list, tuple, or dict
        The input value from which odd numbers are extracted.
        - For lists and tuples, checks for odd integers or floats.
        - For strings, checks the Unicode values of characters.
        - For dictionaries, checks the values for odd numbers.

    Returns:
    -------
    list
        A list of odd numbers (or characters for strings) from the input.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_odd_numbers([1, 2, 3, 4])
    [1, 3]

    >>> get_odd_numbers("abc")
    ['b']

    >>> get_odd_numbers({"a": 2, "b": 3})
    [3]
    """
    odd_list = []

    if isinstance(value, (list, tuple)):
        for num in value:
            if isinstance(num, (int, float)) and num % 2 != 0:
                odd_list.append(num)
    elif isinstance(value, str):
        for char in value:
            if ord(char) % 2 != 0:
                odd_list.append(char)
    elif isinstance(value, dict):
        for val in value.values():
            if isinstance(val, (int, float)) and val % 2 != 0:
                odd_list.append(val)
    else:
        raise TypeError("Input must be a string, list, tuple, or dictionary.")

    return odd_list


# Function to get prime numbers from a string, list, tuple, or dictionary
def get_prime_numbers(value):
    """
    Returns a list of prime numbers from a string, list, tuple, or dictionary.
    For strings, checks if the Unicode values of the characters are prime.

    Parameters:
    ----------
    value : str, list, tuple, or dict
        The input value from which prime numbers are extracted.
        - For lists and tuples, checks for prime integers or floats.
        - For strings, checks the Unicode values of characters.
        - For dictionaries, checks the values for prime numbers.

    Returns:
    -------
    list
        A list of prime numbers (or characters for strings) from the input.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_prime_numbers([2, 3, 4, 5])
    [2, 3, 5]

    >>> get_prime_numbers("abc")
    ['a']

    >>> get_prime_numbers({"a": 2, "b": 3})
    [2, 3]
    """
    prime_list = []

    if isinstance(value, (list, tuple)):
        for num in value:
            if isinstance(num, (int, float)) and num > 1:
                # Check if num is prime
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    prime_list.append(num)

    elif isinstance(value, str):
        for char in value:
            num = ord(char)
            if num > 1:
                # Check if the Unicode value is prime
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    prime_list.append(char)

    elif isinstance(value, dict):
        for val in value.values():
            if isinstance(val, (int, float)) and val > 1:
                # Check if val is prime
                for i in range(2, int(val ** 0.5) + 1):
                    if val % i == 0:
                        break
                else:
                    prime_list.append(val)

    else:
        raise TypeError("Input must be a string, list, tuple, or dictionary.")

    return prime_list


# Function to get even values and keys from a dictionary, string, list, or tuple based on their positions
def get_even_values(container):
    """
    Returns the values and keys located at even positions in the container (string, list, tuple, or dictionary).
    
    Parameters:
    ----------
    container : str, list, tuple, or dict
        The container from which values/keys at even positions will be extracted. 
        - For strings, lists, and tuples, positions are based on index (0, 2, 4, ...).
        - For dictionaries, the even positions are based on the insertion order of the key-value pairs.

    Returns:
    -------
    list
        A list of values or key-value pairs (for dictionaries) from even positions.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_even_values([10, 20, 30, 40])
    [10, 30]

    >>> get_even_values("hello")
    ['h', 'l', 'o']

    >>> get_even_values({"a": 1, "b": 2, "c": 3})
    [('a', 1), ('c', 3)]
    """
    # Validate input type
    if not isinstance(container, (str, list, tuple, dict)):
        raise TypeError("Input must be a string, list, tuple, or dictionary.")
    
    even_values = []
    
    if isinstance(container, (str, list, tuple)):
        for i in range(0, len(container), 2):  # Even index positions: 0, 2, 4, ...
            even_values.append(container[i])
    
    elif isinstance(container, dict):
        for i, (key, value) in enumerate(container.items()):
            if i % 2 == 0:  # Even position
                even_values.append((key, value))  # Add key-value pair
    
    return even_values


# Function to get odd values and keys from a dictionary, string, list, or tuple based on their positions
def get_odd_values(container):
    """
    Returns the values and keys located at odd positions in the container (string, list, tuple, or dictionary).
    
    Parameters:
    ----------
    container : str, list, tuple, or dict
        The container from which values/keys at odd positions will be extracted. 
        - For strings, lists, and tuples, positions are based on index (1, 3, 5, ...).
        - For dictionaries, the odd positions are based on the insertion order of the key-value pairs.

    Returns:
    -------
    list
        A list of values or key-value pairs (for dictionaries) from odd positions.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_odd_values([10, 20, 30, 40])
    [20, 40]

    >>> get_odd_values("hello")
    ['e', 'l']

    >>> get_odd_values({"a": 1, "b": 2, "c": 3})
    [('b', 2)]
    """
    # Validate input type
    if not isinstance(container, (str, list, tuple, dict)):
        raise TypeError("Input must be a string, list, tuple, or dictionary.")
    
    odd_values = []
    
    if isinstance(container, (str, list, tuple)):
        for i in range(1, len(container), 2):  # Odd index positions: 1, 3, 5, ...
            odd_values.append(container[i])
    
    elif isinstance(container, dict):
        for i, (key, value) in enumerate(container.items()):
            if i % 2 != 0:  # Odd position
                odd_values.append((key, value))  # Add key-value pair
    
    return odd_values



# Function to get prime values and keys from a dictionary, string, list, or tuple based on prime positions
def get_prime_values(container):
    """
    Returns values and keys at positions that are prime numbers (indices) from string, list, tuple, or dictionary.
    
    Parameters:
    ----------
    container : str, list, tuple, or dict
        The container from which values/keys at prime-numbered positions will be extracted.
        - For strings, lists, and tuples, positions are based on index (prime indices such as 2, 3, 5, 7, ...).
        - For dictionaries, the prime positions are based on the insertion order of the key-value pairs.

    Returns:
    -------
    list
        A list of values or key-value pairs (for dictionaries) from prime-numbered positions.

    Raises:
    ------
    TypeError
        If the input is not a string, list, tuple, or dictionary.

    Examples:
    --------
    >>> get_prime_values([10, 20, 30, 40, 50, 60])
    [30, 50]

    >>> get_prime_values("hello")
    ['l']

    >>> get_prime_values({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
    [('b', 2), ('d', 4)]
    """
    # Validate input type
    if not isinstance(container, (str, list, tuple, dict)):
        raise TypeError("Input must be a string, list, tuple, or dictionary.")
    
    prime_values = []

    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    if isinstance(container, (str, list, tuple)):
        for i in range(len(container)):
            if is_prime(i):  # Check if the index is prime
                prime_values.append(container[i])
    
    elif isinstance(container, dict):
        for i, (key, value) in enumerate(container.items()):
            if is_prime(i):  # Check if the position is prime
                prime_values.append((key, value))  # Add key-value pair
    
    return prime_values
