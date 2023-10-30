# Searching
# Binary Search
def binarySearch(arr, element):
    """Iterative binary search

    :param arr:
    :param element:
    :return: element, int
    """
    low = 0
    high = len(arr) - 1
    mid = 0
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
def linearSearch(arr, element):
    """Iterative linear search

    :param arr:
    :param element:
    :return: element, int
    """
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

# Credits to GeeksforGeeks & TutorialsPoint