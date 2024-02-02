import timeit 
import random


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not in the list

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Return the index of the target if found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Return -1 if the target is not in the list

# Function to measure average performance
def measure_performance(search_func, arr_size):
    setup_code = f"""
import random
from __main__ import {search_func}
arr = sorted([random.randint(1, {arr_size*10}) for _ in range({arr_size})])
target = random.randint(1, {arr_size*10})
"""
    search_code = f"{search_func}(arr, target)"
    time_taken = timeit.timeit(search_code, setup=setup_code, number=1000)
    return time_taken / 1000  # Average time taken for 1000 searches

# Vector sizes to test
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]


