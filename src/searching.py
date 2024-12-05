# Searching

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

