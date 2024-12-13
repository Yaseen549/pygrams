def normalize_data(data):
    """
    Normalizes a list of numbers to a range of [0, 1].

    Parameters:
    ----------
    data : list of float or int
        A list of numbers to normalize.

    Returns:
    -------
    list of float
        The normalized list of numbers.

    Raises:
    ------
    ValueError
        If the list is empty or all elements are the same.

    Examples:
    --------
    >>> normalize_data([10, 20, 30])
    [0.0, 0.5, 1.0]
    """
    if not data:
        raise ValueError("The data list cannot be empty.")
    
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        raise ValueError("Cannot normalize when all elements are the same.")

    return [(x - min_val) / (max_val - min_val) for x in data]


def filter_odd_numbers(numbers):
    """
    Filters and returns only the odd numbers from a list.

    Parameters:
    ----------
    numbers : list of int
        A list of integers.

    Returns:
    -------
    list of int
        A list containing only the odd numbers.

    Examples:
    --------
    >>> filter_odd_numbers([1, 2, 3, 4])
    [1, 3]
    """
    return [num for num in numbers if num % 2 != 0]


def filter_even_numbers(numbers):
    """
    Filters and returns only the even numbers from a list.

    Parameters:
    ----------
    numbers : list of int
        A list of integers.

    Returns:
    -------
    list of int
        A list containing only the even numbers.

    Examples:
    --------
    >>> filter_even_numbers([1, 2, 3, 4])
    [2, 4]
    """
    return [num for num in numbers if num % 2 == 0]


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.

    Parameters:
    ----------
    nested_list : list
        A nested list to flatten.

    Returns:
    -------
    list
        A single flattened list.

    Examples:
    --------
    >>> flatten_list([[1, 2], [3, 4], [5]])
    [1, 2, 3, 4, 5]
    """
    return [item for sublist in nested_list for item in sublist]
