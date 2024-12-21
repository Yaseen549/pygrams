def remove_duplicates(arr):
    """
    Removes duplicate elements from an array or list.

    Parameters:
    ----------
    arr : list
        The list from which duplicates should be removed.

    Returns:
    -------
    list
        A new list with duplicates removed.

    Examples:
    --------
    >>> remove_duplicates([1, 2, 3, 4, 4, 5])
    [1, 2, 3, 4, 5]
    >>> remove_duplicates(['apple', 'banana', 'apple'])
    ['apple', 'banana']
    """
    return list(set(arr))


def merge_arrays(arr1, arr2):
    """
    Merges two arrays or lists into a single list.

    Parameters:
    ----------
    arr1 : list
        The first list to merge.
    arr2 : list
        The second list to merge.

    Returns:
    -------
    list
        A new list containing all elements from arr1 and arr2.

    Examples:
    --------
    >>> merge_arrays([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_arrays(['a', 'b'], ['c', 'd'])
    ['a', 'b', 'c', 'd']
    """
    return arr1 + arr2


def flatten_array(arr):
    """
    Flattens a multi-dimensional array into a single list.

    Parameters:
    ----------
    arr : list
        The multi-dimensional list to flatten.

    Returns:
    -------
    list
        A single flat list containing all elements from the nested arrays.

    Examples:
    --------
    >>> flatten_array([[1, 2], [3, 4], [5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten_array([['apple', 'banana'], ['cherry', 'date']])
    ['apple', 'banana', 'cherry', 'date']
    """
    result = []
    for sublist in arr:
        if isinstance(sublist, list):
            result.extend(flatten_array(sublist))  # Recursively flatten the sublist
        else:
            result.append(sublist)
    return result


def find_duplicates(arr):
    """
    Finds duplicate values in a list.

    Parameters:
    ----------
    arr : list
        The list to find duplicates in.

    Returns:
    -------
    list
        A list containing the duplicate values.

    Examples:
    --------
    >>> find_duplicates([1, 2, 3, 4, 4, 5])
    [4]
    >>> find_duplicates(['apple', 'banana', 'apple', 'cherry', 'banana'])
    ['apple', 'banana']
    """
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

