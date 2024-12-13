import re


def char_list(param):
    """
    Returns all characters from a string (excluding spaces).

    Parameters:
    ----------
    param : str
        The input string from which characters will be extracted (spaces will be excluded).

    Returns:
    -------
    list of str
        A list of characters from the string, excluding spaces.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> char_list("Hello world")
    ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

    >>> char_list("Python programming")
    ['P', 'y', 't', 'h', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
    """
    # Check if the input is a string
    if not isinstance(param, str):
        raise TypeError("The input must be a string.")
    
    # Return list of characters excluding spaces
    return list(param.replace(" ", ""))



def word_list(param):
    """
    Returns all the words as a list from a string (paragraph).

    Parameters:
    ----------
    param : str
        The input string (paragraph) from which words will be extracted.

    Returns:
    -------
    list of str
        A list of words from the string.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> word_list("Hello world! This is Python.")
    ['Hello', 'world!', 'This', 'is', 'Python.']

    >>> word_list("One two three")
    ['One', 'two', 'three']
    """
    # Check if the input is a string
    if not isinstance(param, str):
        raise TypeError("The input must be a string.")
    
    # Split the string into words
    return param.split()



def join_list(list_of_words):
    """
    Joins a list of words into a single string.

    Parameters:
    ----------
    list_of_words : list of str
        The list of words to be joined.

    Returns:
    -------
    str
        A single string with words joined by a space.

    Raises:
    ------
    TypeError
        If the input is not a list of strings.

    Examples:
    --------
    >>> join_list(['Hello', 'world'])
    'Hello world'

    >>> join_list(['Python', 'is', 'awesome'])
    'Python is awesome'
    """
    # Check if the input is a list of strings
    if not isinstance(list_of_words, list):
        raise TypeError("The input must be a list.")
    
    if not all(isinstance(word, str) for word in list_of_words):
        raise TypeError("Each element of the list must be a string.")
    
    # Join the list of words into a single string
    return " ".join(list_of_words)


def slugify(string):
    """
    Converts a string into a slug format for URLs.

    Parameters:
    ----------
    string : str
        The string to convert into a slug.

    Returns:
    -------
    str
        The converted slug in lowercase with words separated by hyphens.

    Examples:
    --------
    >>> slugify("Hello World!")
    'hello-world'

    >>> slugify("This is a test.")
    'this-is-a-test'
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    # Convert to lowercase, remove non-alphanumeric characters (except spaces), and replace spaces with hyphens
    string = string.lower()
    string = re.sub(r'[^a-z0-9\s]', '', string)  # Remove special characters
    string = string.strip().replace(' ', '-')  # Replace spaces with hyphens
    
    return string


def camel_to_snake_case(string):
    """
    Converts a camelCase string to snake_case.

    Parameters:
    ----------
    string : str
        The string to convert from camelCase to snake_case.

    Returns:
    -------
    str
        The converted string in snake_case.

    Examples:
    --------
    >>> camel_to_snake_case("camelCaseExample")
    'camel_case_example'

    >>> camel_to_snake_case("myVariable")
    'my_variable'
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    # Use regular expression to find capital letters and replace them with an underscore followed by lowercase letter
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', string).lower()


def snake_to_camel_case(string):
    """
    Converts a snake_case string to camelCase.

    Parameters:
    ----------
    string : str
        The string to convert from snake_case to camelCase.

    Returns:
    -------
    str
        The converted string in camelCase.

    Examples:
    --------
    >>> snake_to_camel_case("snake_case_example")
    'snakeCaseExample'

    >>> snake_to_camel_case("my_variable_name")
    'myVariableName'
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    # Split the string by underscores and capitalize each word except the first one
    parts = string.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


def word_count(text):
    """
    Returns the count of words in a text.

    Parameters:
    ----------
    text : str
        The text to count words in.

    Returns:
    -------
    int
        The count of words in the text.

    Examples:
    --------
    >>> word_count("Hello world!")
    2

    >>> word_count("This is a test sentence.")
    5
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Split the text into words based on whitespace and count the number of words
    return len(text.split())
