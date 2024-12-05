# Insertion Sort in Python
def insertion_sort(array):
    """Sort an array using Insertion Sort"""
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
    """Sort an array using Bubble Sort"""
    for i in range(len(array)):
        # Last i elements are already sorted
        for j in range(0, len(array) - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Selection Sort in Python
def selection_sort(array):
    """Sort an array using Selection Sort"""
    size = len(array)
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
    """Sort an array using Merge Sort"""
    if len(array) > 1:
        mid = len(array) // 2  # Find the middle of the array
        left_half = array[:mid]  # Split into left half
        right_half = array[mid:]  # Split into right half

        merge_sort(left_half)  # Sort the left half
        merge_sort(right_half)  # Sort the right half

        i = j = k = 0
        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        
        # If any elements are left in left_half, add them
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        
        # If any elements are left in right_half, add them
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

# Quick Sort in Python
def quick_sort(array):
    """Sort an array using Quick Sort"""
    
    def partition(arr, low, high):
        """Helper function to partition the array"""
        pivot = arr[high]  # Pivot is the last element
        i = low - 1  # Pointer to the smaller element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
        return i + 1
    
    def qsort(arr, low, high):
        """Recursive function to perform quicksort"""
        if low < high:
            pi = partition(arr, low, high)  # Partitioning index
            qsort(arr, low, pi - 1)  # Sort left half
            qsort(arr, pi + 1, high)  # Sort right half

    qsort(array, 0, len(array) - 1)

# Counting Sort in Python
def counting_sort(array):
    """Sort an array using Counting Sort"""
    max_value = max(array)  # Find the maximum element
    count_array = [0] * (max_value + 1)  # Create a count array
    
    # Count occurrences of each element
    for num in array:
        count_array[num] += 1
    
    # Rebuild the sorted array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i] * count_array[i])
    
    return sorted_array

# Radix Sort in Python
def radix_sort(array):
    """Sort an array using Radix Sort"""
    
    def counting_sort_radix(array, place):
        """Helper function to perform counting sort based on place"""
        size = len(array)
        output = [0] * size
        count = [0] * 10  # There are 10 possible digits (0-9)

        # Count occurrences of digits at 'place' value
        for i in range(size):
            index = array[i] // place
            count[index % 10] += 1

        # Update count to get the actual positions
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        for i in range(size - 1, -1, -1):
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1

        # Copy the sorted array back to the original array
        for i in range(size):
            array[i] = output[i]
    
    max_element = max(array)
    place = 1
    # Perform counting sort for every digit
    while max_element // place > 0:
        counting_sort_radix(array, place)
        place *= 10

# Bucket Sort in Python
def bucket_sort(array):
    """Sort an array using Bucket Sort"""
    # Create empty buckets
    buckets = [[] for _ in range(len(array))]

    # Distribute input array elements into buckets
    for num in array:
        index = int(len(array) * num)  # Bucket index
        buckets[index].append(num)
    
    # Sort each bucket and combine them
    array.clear()
    for bucket in buckets:
        array.extend(sorted(bucket))
    
    return array

# Heap Sort in Python
def heap_sort(arr):
    """Sort an array using Heap Sort"""
    
    def heapify(arr, n, i):
        """Helper function to ensure the heap property is maintained"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # Build the heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root and the last element
        heapify(arr, i, 0)  # Restore heap property for the reduced heap
    
    return arr

# Shell Sort in Python
def shell_sort(array):
    """Sort an array using Shell Sort"""
    n = len(array)
    gap = n // 2  # Initial gap size
    
    while gap > 0:
        # Perform insertion sort on elements with a gap
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2  # Reduce gap size
    
    return array
