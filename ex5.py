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

# Function to measure the time it takes to find a random element in the vector
def measure_search_time(search_func, arr, iterations=1000):
    total_time = 0
    for _ in range(iterations):
        target = random.choice(arr)  # Randomly select an element in the vector
        search_code = f"{search_func}(arr, {target})"
        time_taken = timeit.timeit(search_code, globals=globals(), number=100)
        total_time += time_taken
    return total_time / iterations  # Average time over the specified iterations

# Vector sizes to test
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

# Measure performance for each vector size using both linear and binary search
for size in vector_sizes:
    arr = sorted([random.randint(1, size*10) for _ in range(size)])  # Create a sorted vector
    avg_linear_time = measure_search_time("linear_search", arr, iterations=1000)
    avg_binary_time = measure_search_time("binary_search", arr, iterations=1000)
    print(f"Vector Size: {size}, Average Linear Search Time: {avg_linear_time:.8f} seconds")
    print(f"Vector Size: {size}, Average Binary Search Time: {avg_binary_time:.8f} seconds")
    print()


