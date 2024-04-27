import random
import time
from functools import wraps

# Time measuring function:

def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper


# Merge sort:

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort_helper(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_helper(left_half)
        merge_sort_helper(right_half)

        merge(arr, left_half, right_half)

@measure_execution_time
def merge_sort(arr):
    merge_sort_helper(arr)


# Insertion sort:

@measure_execution_time
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort_helper(arr, p, q - 1)
        quick_sort_helper(arr, q + 1, r)

@measure_execution_time
def quick_sort(arr, p, r):
    quick_sort_helper(arr, p, r)



# Count sort:

@measure_execution_time
def count_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr


# Bubble sort:

@measure_execution_time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
if __name__ == "__main__":
    unsorted_array=[random.randint(1,1000) for _ in range(10000)]
    print('array unsorted')

    bubble_sort(unsorted_array.copy())
    quick_sort(unsorted_array.copy(),0,len(unsorted_array)-1)
    
    merge_sort(unsorted_array.copy())
    insertion_sort(unsorted_array.copy())
    count_sort(unsorted_array.copy())


    