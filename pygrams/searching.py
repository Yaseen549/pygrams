# Searching
import math

# Binary Search
def binary_search(arr, element):
    """
    Performs an iterative binary search to find the index of a specified element in a sorted array.

    Binary Search works by repeatedly dividing the search interval in half. If the value of the element
    is less than the item in the middle of the interval, it searches the left half, otherwise, it searches
    the right half. This process continues until the element is found or the search interval is empty.

    Args:
    arr (list): A sorted list of elements where the search is to be performed.
    element: The element to search for in the array.

    Returns:
    int: The index of the element if found, otherwise -1 indicating the element is not present in the array.

    Example:
    >>> binary_search([1, 2, 3, 4, 5, 6], 4)
    3
    >>> binary_search([1, 2, 3, 4, 5], 10)
    -1
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid - 1
        else:
            return mid
    return -1


# Linear Search
def linear_search(arr, element):
    """
    Performs an iterative linear search to find the index of a specified element in an array.

    In Linear Search, the function checks each element of the array in order, starting from the first element.
    It continues until the element is found or the entire array is traversed. It is efficient for unsorted data
    or small arrays but has a time complexity of O(n).

    Args:
    arr (list): A list of elements to search through.
    element: The element to search for in the array.

    Returns:
    int: The index of the element if found, otherwise -1 indicating the element is not present in the array.

    Example:
    >>> linear_search([10, 20, 30, 40], 30)
    2
    >>> linear_search([10, 20, 30], 100)
    -1
    """
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


def ternary_search(sorted_list, target):
    """
    A more efficient search algorithm for sorted data by dividing the list into three parts.

    Parameters:
    ----------
    sorted_list : list
        A sorted list of elements.
    target : int
        The element to search for.

    Returns:
    -------
    int
        The index of the target element if found, otherwise -1.

    Raises:
    ------
    ValueError
        If the sorted_list is not a list.

    Examples:
    --------
    >>> ternary_search([1, 4, 5, 7, 9, 12], 7)
    3

    >>> ternary_search([1, 4, 5, 7, 9, 12], 10)
    -1
    """
    if not isinstance(sorted_list, list):
        raise ValueError("The first argument must be a list.")
    
    low, high = 0, len(sorted_list) - 1
    
    while high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        
        if sorted_list[mid1] == target:
            return mid1
        if sorted_list[mid2] == target:
            return mid2
        
        if target < sorted_list[mid1]:
            high = mid1 - 1
        elif target > sorted_list[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    
    return -1


def jump_search(sorted_list, target):
    """
    A search algorithm that works by jumping ahead by a fixed block size and performing a linear search.

    Parameters:
    ----------
    sorted_list : list
        A sorted list of elements.
    target : int
        The element to search for.

    Returns:
    -------
    int
        The index of the target element if found, otherwise -1.

    Raises:
    ------
    ValueError
        If the sorted_list is not a list.

    Examples:
    --------
    >>> jump_search([1, 4, 5, 7, 9, 12], 7)
    3

    >>> jump_search([1, 4, 5, 7, 9, 12], 10)
    -1
    """
    if not isinstance(sorted_list, list):
        raise ValueError("The first argument must be a list.")
    
    n = len(sorted_list)
    step = int(math.sqrt(n))  # Step size
    
    prev = 0
    while sorted_list[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    for i in range(prev, min(step, n)):
        if sorted_list[i] == target:
            return i
    
    return -1
