def has_armstrong(list_of_numbers):
    """
    Checks if the list has at least one Armstrong number.

    An Armstrong number is a number that is equal to the sum of its digits raised
    to the power of the number of digits.

    Parameters:
    ----------
    list_of_numbers : list of int
        A list of integers to check for Armstrong numbers.

    Returns:
    -------
    bool
        True if at least one Armstrong number exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> has_armstrong([153, 123])
    True

    >>> has_armstrong([10, 15])
    False
    """
    # Check input type
    if not isinstance(list_of_numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    for number in list_of_numbers:
        if not isinstance(number, int):
            raise TypeError("All elements in the list must be integers.")
        
        total = 0
        digits = str(number)
        num_digits = len(digits)
        
        for digit in digits:
            total += int(digit) ** num_digits
        
        if total == number:
            return True
    
    return False


def has_even_number(numbers):
    """
    Checks if a list contains at least one even number.

    Parameters:
    ----------
    numbers : list of int
        A list of integers to check for even numbers.

    Returns:
    -------
    bool
        True if an even number exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> has_even_number([1, 3, 4])
    True

    >>> has_even_number([1, 3, 5])
    False
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("All elements in the list must be integers.")
        if number % 2 == 0:
            return True
    return False



def has_odd_number(numbers):
    """
    Checks if a list contains at least one odd number.

    Parameters:
    ----------
    numbers : list of int
        A list of integers to check for odd numbers.

    Returns:
    -------
    bool
        True if an odd number exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> has_odd_number([2, 4, 5])
    True

    >>> has_odd_number([2, 4, 6])
    False
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("All elements in the list must be integers.")
        if number % 2 != 0:
            return True
    return False



def has_prime_number(numbers):
    """
    Checks if a list contains at least one prime number.

    Parameters:
    ----------
    numbers : list of int
        A list of integers to check for prime numbers.

    Returns:
    -------
    bool
        True if a prime number exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a list of integers.

    Examples:
    --------
    >>> has_prime_number([4, 5, 8])
    True

    >>> has_prime_number([4, 8, 9])
    False
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("All elements in the list must be integers.")
        
        if number > 1:
            is_prime = True
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                return True
    return False



def has_capital_letter(container):
    """
    Checks if the container contains at least one uppercase letter.
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for uppercase letters.

    Returns:
    -------
    bool
        True if there's at least one uppercase letter, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_capital_letter("Hello")
    True

    >>> has_capital_letter("hello")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    for item in container:
        if isinstance(item, str) and item.isupper():
            return True
    return False



def has_small_letter(container):
    """
    Checks if the container contains at least one lowercase letter.
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for lowercase letters.

    Returns:
    -------
    bool
        True if there's at least one lowercase letter, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_small_letter("Hello")
    True

    >>> has_small_letter("HELLO")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    for item in container:
        if isinstance(item, str) and item.islower():
            return True
    return False



def has_underscore(container):
    """
    Checks if the container contains an underscore (_).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for the underscore.

    Returns:
    -------
    bool
        True if there's an underscore, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_underscore("Hello_world")
    True

    >>> has_underscore("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return "_" in container



def has_white_space(container):
    """
    Checks if the container contains a white space ( ).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for white space.

    Returns:
    -------
    bool
        True if there's a white space, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_white_space("Hello world")
    True

    >>> has_white_space("Helloworld")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return " " in container



def has_period(container):
    """
    Checks if the container contains a period (.).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for the period.

    Returns:
    -------
    bool
        True if there's a period, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_period("Hello.")
    True

    >>> has_period("Hello")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return "." in container



def has_colon(container):
    """
    Checks if the container contains a colon (:).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for the colon.

    Returns:
    -------
    bool
        True if there's a colon, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_colon("Hello: world")
    True

    >>> has_colon("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return ":" in container



def has_semi_colon(container):
    """
    Checks if the container contains a semicolon (;).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for the semicolon.

    Returns:
    -------
    bool
        True if there's a semicolon, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_semi_colon("Hello; world")
    True

    >>> has_semi_colon("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return ";" in container



def has_comma(container):
    """
    Checks if the container contains a comma (,).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for the comma.

    Returns:
    -------
    bool
        True if there's a comma, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_comma("Hello, world")
    True

    >>> has_comma("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    return "," in container



def has_operator(container):
    """
    Checks if the container contains any of the operators (+, -, *, /, %).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for operators.

    Returns:
    -------
    bool
        True if any operator exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_operator("Hello + world")
    True

    >>> has_operator("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    operators = ["+", "-", "*", "/", "%"]
    for operator in operators:
        if operator in container:
            return True
    return False



def has_number(container):
    """
    Checks if the container contains a number (digit).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for digits.

    Returns:
    -------
    bool
        True if there's at least one digit, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_number("Hello123")
    True

    >>> has_number("Hello")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    for item in container:
        if str(item).isdigit():
            return True
    return False



def has_symbol(container):
    """
    Checks if the container contains any special symbol (e.g., @, #, $, etc.).
    
    Parameters:
    ----------
    container : str or list of str
        A string or list of characters to check for special symbols.

    Returns:
    -------
    bool
        True if any special symbol exists, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or a list of characters.

    Examples:
    --------
    >>> has_symbol("Hello@world")
    True

    >>> has_symbol("Hello world")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("Input must be a string or a list of characters.")
    
    symbols = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}", "{", "~", ":", "'", "\""]
    for symbol in symbols:
        if symbol in container:
            return True
    return False



def has_element(container, element):
    """
    Checks if the container (string or list) contains the specified element.
    
    Parameters:
    ----------
    container : str or list
        The container (string or list) to check.
    element : str or any
        The element to check for within the container.

    Returns:
    -------
    bool
        True if the element is found in the container, False otherwise.

    Raises:
    ------
    TypeError
        If the container is not a string or list.

    Examples:
    --------
    >>> has_element("Hello world", "world")
    True

    >>> has_element([1, 2, 3], 2)
    True

    >>> has_element("Hello world", "Python")
    False
    """
    # Check input type
    if not isinstance(container, (str, list)):
        raise TypeError("The container must be a string or a list.")
    
    return element in container
