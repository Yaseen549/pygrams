def find_median(numbers):
    """
    Finds the median of a list of numbers.

    Parameters:
    ----------
    numbers : list of int or float
        A list of numbers.

    Returns:
    -------
    float
        The median value.

    Raises:
    ------
    ValueError
        If the list is empty.

    Examples:
    --------
    >>> find_median([1, 2, 3, 4, 5])
    3
    >>> find_median([1, 2, 3, 4])
    2.5
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


def find_mode(numbers):
    """
    Finds the mode (most frequent value) in a list of numbers.

    Parameters:
    ----------
    numbers : list of int or float
        A list of numbers.

    Returns:
    -------
    list
        A list of the most frequent values (in case of ties).

    Raises:
    ------
    ValueError
        If the list is empty.

    Examples:
    --------
    >>> find_mode([1, 2, 2, 3])
    [2]
    >>> find_mode([1, 2, 2, 3, 3])
    [2, 3]
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    from collections import Counter
    freq = Counter(numbers)
    max_count = max(freq.values())
    return [key for key, count in freq.items() if count == max_count]


def find_range(numbers):
    """
    Returns the range (difference between max and min) of a list of numbers.

    Parameters:
    ----------
    numbers : list of int or float
        A list of numbers.

    Returns:
    -------
    float
        The range of the numbers.

    Raises:
    ------
    ValueError
        If the list is empty.

    Examples:
    --------
    >>> find_range([1, 2, 3, 4, 5])
    4
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    return max(numbers) - min(numbers)


def binary_search_recursive(sorted_list, target, low=0, high=None):
    """
    A recursive implementation of binary search.

    Parameters:
    ----------
    sorted_list : list
        A sorted list to search in.
    target : int or float
        The value to search for.
    low : int, optional
        The starting index (default is 0).
    high : int, optional
        The ending index (default is None, which sets it to the length of the list).

    Returns:
    -------
    int
        The index of the target if found, else -1.

    Examples:
    --------
    >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
    2
    >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
    -1
    """
    if high is None:
        high = len(sorted_list) - 1
    
    if low > high:
        return -1

    mid = (low + high) // 2
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] > target:
        return binary_search_recursive(sorted_list, target, low, mid - 1)
    else:
        return binary_search_recursive(sorted_list, target, mid + 1, high)
