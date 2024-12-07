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
