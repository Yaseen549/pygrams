# Insertion Sort in Python
def insertion_sort(array):
    """
    Sorts an array using the Insertion Sort algorithm.

    The Insertion Sort algorithm builds the final sorted array one item at a time. 
    It is much like sorting a hand of playing cards, where you pick up one card 
    at a time and insert it into its correct position.

    Parameters:
    ----------
    array : list of int or float
        The input array to be sorted. It can contain integers or floating point numbers.

    Returns:
    -------
    list of int or float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.

    Examples:
    --------
    >>> insertion_sort([12, 11, 13, 5, 6])
    [5, 6, 11, 12, 13]

    >>> insertion_sort([3.2, 2.1, 4.7, 1.8])
    [1.8, 2.1, 3.2, 4.7]

    >>> insertion_sort([10, -1, 3, 0, -5])
    [-5, -1, 0, 3, 10]
    """
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("The list must contain only numeric values (int or float).")

    # Insertion Sort algorithm
    for step in range(1, len(array)):
        key = array[step]  # Current element to insert
        j = step - 1  # Start comparing with the previous element

        # Move elements of array[0..step-1] that are greater than key
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]  # Shift element to the right
            j -= 1  # Move the index leftwards
        array[j + 1] = key  # Insert the key in its correct position

    return array


# Bubble Sort in Python
def bubble_sort(array):
    """
    Sorts an array using the Bubble Sort algorithm.

    Bubble Sort repeatedly steps through the list, compares adjacent elements, 
    and swaps them if they are in the wrong order. The pass through the list is 
    repeated until the list is sorted. It is called "bubble" sort because smaller 
    elements "bubble" to the top (beginning of the list) with each iteration.

    Parameters:
    ----------
    array : list of int or float
        The input array to be sorted. It can contain integers or floating point numbers.

    Returns:
    -------
    list of int or float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.

    Examples:
    --------
    >>> bubble_sort([12, 11, 13, 5, 6])
    [5, 6, 11, 12, 13]

    >>> bubble_sort([3.2, 2.1, 4.7, 1.8])
    [1.8, 2.1, 3.2, 4.7]

    >>> bubble_sort([10, -1, 3, 0, -5])
    [-5, -1, 0, 3, 10]
    """
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("The list must contain only numeric values (int or float).")
    
    n = len(array)
    
    # Bubble Sort algorithm
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array


# Selection Sort in Python
def selection_sort(array):
    """
    Sorts an array using the Selection Sort algorithm.

    Selection Sort repeatedly finds the minimum element from the unsorted part of 
    the list and swaps it with the element at the current position. It iterates 
    through the entire list, placing the smallest element in the sorted portion 
    of the list at each step.

    Parameters:
    ----------
    array : list of int or float
        The input array to be sorted. It can contain integers or floating point numbers.

    Returns:
    -------
    list of int or float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.

    Examples:
    --------
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> selection_sort([3.5, 1.2, 5.7, 2.8])
    [1.2, 2.8, 3.5, 5.7]

    >>> selection_sort([10, -5, 0, 3, -2])
    [-5, -2, 0, 3, 10]
    """
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("The list must contain only numeric values (int or float).")
    
    size = len(array)
    
    # Selection Sort algorithm
    for step in range(size):
        min_idx = step  # Start with the first element as minimum
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:  # Find the minimum element
                min_idx = i
        # Swap the found minimum element with the element at 'step'
        array[step], array[min_idx] = array[min_idx], array[step]
    
    return array

# Merge Sort in Python
def merge_sort(array):
    """
    Sorts an array using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm that splits the array into halves,
    recursively sorts them, and then merges the sorted halves into a single sorted array.

    Parameters:
    ----------
    array : list of int or float
        The input array to be sorted. It can contain integers or floating point numbers.

    Returns:
    -------
    list of int or float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.

    Examples:
    --------
    >>> merge_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> merge_sort([3.5, 1.2, 5.7, 2.8])
    [1.2, 2.8, 3.5, 5.7]

    >>> merge_sort([10, -5, 0, 3, -2])
    [-5, -2, 0, 3, 10]
    """
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("The list must contain only numeric values (int or float).")
    
    # Base case: If the list has one or zero elements, it's already sorted
    if len(array) <= 1:
        return array

    # Find the middle index
    mid = len(array) // 2

    # Split the array into two halves
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    merged = []
    i = j = 0

    # Merge the two lists by comparing the elements
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Add remaining elements from left or right, if any
    merged.extend(left_half[i:])
    merged.extend(right_half[j:])
    
    return merged


# Merging two lists and sort
def merge_and_sort(left, right):
    """
    Merges two lists into one sorted list.

    Parameters:
    ----------
    left : list of int or float
        The first sorted list.
    right : list of int or float
        The second sorted list.

    Returns:
    -------
    list of int or float
        A merged and sorted list containing all elements from `left` and `right`.

    Examples:
    --------
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    merged = []
    i = j = 0

    # Merge the two lists by comparing the elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left or right, if any
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# Quick Sort in Python
def quick_sort(array):
    """
    Sorts an array using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that works by selecting a pivot element 
    and partitioning the array into two sub-arrays, according to whether each element 
    is less than or greater than the pivot. The sub-arrays are then sorted recursively.

    Parameters:
    ----------
    array : list of int or float
        The input array to be sorted. It can contain integers or floating point numbers.

    Returns:
    -------
    list of int or float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.

    Examples:
    --------
    >>> quick_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]

    >>> quick_sort([3.5, 1.2, 5.7, 2.8])
    [1.2, 2.8, 3.5, 5.7]

    >>> quick_sort([10, -5, 0, 3, -2])
    [-5, -2, 0, 3, 10]
    """
    
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    # Check if all elements in the list are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("The list must contain only numeric values (int or float).")
    
    # Helper function to partition the array based on the pivot
    def partition(arr, low, high):
        pivot = arr[high]  # Pivot is the last element
        i = low - 1  # Pointer to the smaller element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements
        
        # Swap pivot to its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  
        return i + 1

    # Helper function to sort the array recursively
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)  # Partitioning index
            quick_sort_recursive(arr, low, pi - 1)  # Sort left half
            quick_sort_recursive(arr, pi + 1, high)  # Sort right half

    # Call the recursive quick_sort function to sort the entire array
    quick_sort_recursive(array, 0, len(array) - 1)

    return array


# Counting Sort in Python
def counting_sort(array):
    """
    Sorts an array using the Counting Sort algorithm.

    Counting Sort is an integer sorting algorithm that counts the number of occurrences of each distinct value in the array.
    It uses this count to determine the position of each element in the sorted array.

    Parameters:
    ----------
    array : list of int
        A list of integers to be sorted. All elements must be non-negative integers.

    Returns:
    -------
    list of int
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-integer elements.
    ValueError
        If the input array contains negative integers, as Counting Sort requires non-negative integers.

    Examples:
    --------
    >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
    [1, 2, 2, 3, 3, 4, 8]

    >>> counting_sort([10, 9, 10, 8, 7, 6, 5])
    [5, 6, 7, 8, 9, 10, 10]
    """
    
    # Check if the input is a list
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")

    # Check if all elements in the array are integers
    if not all(isinstance(x, int) for x in array):
        raise TypeError("All elements in the array must be integers.")

    # Check if all elements are non-negative integers
    if any(x < 0 for x in array):
        raise ValueError("All elements in the array must be non-negative integers.")

    if not array:  # Return an empty array if the input is empty
        return []

    # Find the maximum element in the array
    max_value = max(array)

    # Create a count array to store the frequency of each element
    count_array = [0] * (max_value + 1)

    # Count occurrences of each element in the input array
    for num in array:
        count_array[num] += 1

    # Rebuild the sorted array based on the count array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i] * count_array[i])

    return sorted_array


# Radix Sort in Python
def radix_sort(array):
    """
    Sorts an array using the Radix Sort algorithm.

    Radix Sort is a non-comparative sorting algorithm that sorts numbers by processing 
    individual digits. It works by sorting the input elements by each digit, starting 
    from the least significant digit (LSD) to the most significant digit (MSD).

    Parameters:
    ----------
    array : list of int
        A list of non-negative integers to be sorted.

    Returns:
    -------
    list of int
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-integer elements.
    ValueError
        If the input array contains negative integers.

    Examples:
    --------
    >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
    [2, 24, 45, 66, 75, 90, 170, 802]
    """

    # Validate input
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    if not all(isinstance(x, int) for x in array):
        raise TypeError("All elements in the array must be integers.")
    
    if any(x < 0 for x in array):
        raise ValueError("All elements in the array must be non-negative integers.")
    
    # Handle edge case of empty array
    if not array:
        return []

    def counting_sort_radix(array, place):
        """
        A stable counting sort function used as a subroutine for Radix Sort.
        
        Sorts the array based on the digit at the given 'place' (exponent of 10).

        Parameters:
        ----------
        array : list of int
            A list of non-negative integers to be sorted.
        
        place : int
            The place value (1s, 10s, 100s, etc.) to sort by.
        """
        size = len(array)
        output = [0] * size  # Output array to store sorted values
        count = [0] * 10  # Count array to store the frequency of digits (0-9)

        # Count occurrences of digits at 'place' value
        for num in array:
            index = num // place
            count[index % 10] += 1

        # Update count array to contain actual positions
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array using the count array
        for i in range(size - 1, -1, -1):
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1

        # Copy the output array back into the original array
        for i in range(size):
            array[i] = output[i]

    # Find the maximum element to determine the number of digits
    max_element = max(array)
    place = 1  # Start sorting by the least significant digit (1s place)

    # Perform counting sort for each digit (place)
    while max_element // place > 0:
        counting_sort_radix(array, place)
        place *= 10  # Move to the next place value (10s, 100s, etc.)

    return array


# Bucket Sort in Python
def bucket_sort(array):
    """
    Sorts an array using the Bucket Sort algorithm.

    Bucket Sort divides the array into a number of smaller buckets, sorts each bucket individually, 
    and then combines the sorted buckets to obtain the final sorted array.

    This algorithm is particularly useful for uniformly distributed data over a range.

    Parameters:
    ----------
    array : list of float
        A list of floats in the range [0, 1) to be sorted.

    Returns:
    -------
    list of float
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-numeric elements.
    ValueError
        If any element in the array is outside the range [0, 1).

    Examples:
    --------
    >>> bucket_sort([0.42, 0.32, 0.53, 0.12, 0.45, 0.24])
    [0.12, 0.24, 0.32, 0.42, 0.45, 0.53]

    >>> bucket_sort([0.9, 0.7, 0.3, 0.5, 0.1])
    [0.1, 0.3, 0.5, 0.7, 0.9]
    """

    # Validate input
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    if not all(isinstance(x, (int, float)) for x in array):
        raise TypeError("All elements in the array must be numeric.")
    
    if any(x < 0 or x >= 1 for x in array):
        raise ValueError("All elements in the array must be in the range [0, 1).")

    # Handle edge case of empty array
    if not array:
        return []

    # Create empty buckets
    n = len(array)
    buckets = [[] for _ in range(n)]

    # Distribute input array elements into buckets
    for num in array:
        index = int(n * num)  # Bucket index calculation
        buckets[index].append(num)

    # Sort each bucket and combine them
    array.clear()
    for bucket in buckets:
        array.extend(sorted(bucket))

    return array

# Heap Sort in Python
def heap_sort(arr):
    """
    Sorts an array using the Heap Sort algorithm.

    Heap Sort is a comparison-based sorting algorithm that works by first
    converting the array into a heap (a binary tree structure) and then
    repeatedly extracting the maximum element from the heap and rebuilding
    the heap.

    Parameters:
    ----------
    arr : list of int
        A list of integers to be sorted.

    Returns:
    -------
    list of int
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-integer elements.
    
    Examples:
    --------
    >>> heap_sort([3, 5, 1, 10, 2])
    [1, 2, 3, 5, 10]

    >>> heap_sort([12, 11, 13, 5, 6, 7])
    [5, 6, 7, 11, 12, 13]
    """

    # Validate input
    if not isinstance(arr, list):
        raise TypeError("The input must be a list.")
    
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements in the array must be integers.")

    # Handle edge case for an empty list
    if len(arr) == 0:
        return []

    # Helper function to maintain the heap property
    def heapify(arr, n, i):
        """
        Maintains the heap property by ensuring the subtree rooted at index i is a max heap.
        
        Parameters:
        ----------
        arr : list of int
            The array to heapify.
        n : int
            The size of the heap.
        i : int
            The index of the current node in the heap.
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # If left child is larger than root
        if left < n and arr[i] < arr[left]:
            largest = left
        
        # If right child is larger than the largest so far
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)  # Recursively heapify the affected subtree

    n = len(arr)

    # Build the heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]
        
        # Restore heap property for the reduced heap
        heapify(arr, i, 0)

    return arr

# Shell Sort in Python
def shell_sort(array):
    """
    Sorts an array using the Shell Sort algorithm.

    Shell Sort is an in-place comparison-based sorting algorithm that generalizes 
    insertion sort to allow the exchange of items that are far apart. It starts by sorting 
    elements that are far apart and progressively reduces the gap between the elements to be compared.

    Parameters:
    ----------
    array : list of int
        A list of integers to be sorted.

    Returns:
    -------
    list of int
        A new list that is sorted in ascending order.

    Raises:
    ------
    TypeError
        If the input is not a list or contains non-integer elements.
    
    Examples:
    --------
    >>> shell_sort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]

    >>> shell_sort([12, 34, 54, 2, 3])
    [2, 3, 12, 34, 54]
    """
    
    # Validate input
    if not isinstance(array, list):
        raise TypeError("The input must be a list.")
    
    if not all(isinstance(x, int) for x in array):
        raise TypeError("All elements in the array must be integers.")

    # Handle edge case for an empty list
    if len(array) == 0:
        return []

    n = len(array)
    gap = n // 2  # Initial gap size

    # Perform the sorting using the Shell Sort method
    while gap > 0:
        # Perform insertion sort on elements with the current gap
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2  # Reduce the gap size (half the current gap)

    return array
