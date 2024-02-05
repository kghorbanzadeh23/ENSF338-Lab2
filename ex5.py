import timeit 
import random
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

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
avg_Linear = []
avg_Binary = []
sizes =[]
# Measure performance for each vector size using both linear and binary search
for size in vector_sizes:
    arr = sorted([random.randint(1, size*10) for _ in range(size)])  # Create a sorted vector
    avg_linear_time = measure_search_time("linear_search", arr, iterations=1000)
    avg_binary_time = measure_search_time("binary_search", arr, iterations=1000)
    print(f"Vector Size: {size}, Average Linear Search Time: {avg_linear_time:.8f} seconds")
    print(f"Vector Size: {size}, Average Binary Search Time: {avg_binary_time:.8f} seconds")
    print()
    avg_Linear.append(avg_linear_time)
    avg_Binary.append(avg_binary_time)
    sizes.append(size)


#Produce a linear regression plot
def linear(x, a, b):
    return a*x+b
constants = curve_fit(linear, sizes, avg_Linear)
plt.scatter(sizes, avg_Linear)
linevalues = [constants[0][0] * x + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.3.2.png
plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Linear Regression: Number of Records vs. Average Processing Time')
plt.savefig('output.5.3.1.png')

#Produce a linear regression plot
plt.clf()
def logs(x,a,b):
    return a*np.log(x) + b
constants = curve_fit(logs, sizes, avg_Binary)
plt.scatter(sizes, avg_Binary)
linevalues = [constants[0][0] * np.log(x) + constants[0][1] for x in vector_sizes]
plt.plot(vector_sizes, linevalues, 'r')

# Save the plot to a file named output.3.2.png
plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time (seconds)')
plt.title('Log Regression: Number of Records vs. Average Processing Time')
plt.savefig('output.5.3.2.png')

'''
Discuss the results. For each interpolating function, describe the type of function?

For linear search the function turns out to be linear, which makes senses because the
requires going through the entire list to find said 'target'. The parameters are the
number of records as x and average processing time as y.

For binary search the function turns out to be a log function, this is because
this search requires dividing the search in half until the target is found. The
parameters are the number of records a and average processing time as y.

Are the results what you expected?
Yes both graph were expected as the result, because the time complexity of the search
and the function directly correlates with each other.
'''
