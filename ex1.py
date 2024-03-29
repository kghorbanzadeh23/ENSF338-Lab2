import timeit
import matplotlib.pyplot as plt

""""
1) This code resembles the Fibonacci Sequence
using recursion, you will enter a integer into the function and through
recursion it will produce a sequence of numbers where the two
terms added together produces the next third.

2) Divide-and-conquer algorithms involve breaking down a problem
into smaller sub-problems and then solving these sub-problems.
Recursion in this case is not considered a divide-and-conquer
algorithm because as the program runs there is no combination of results from sub-problems.

3) It looks like O(n) = O(2^(n-1)) + O(2^(n-1)) + O(2^(n-1)), which means O is going to be O(2^n).

"""


# Original Fibonacci function without memoization
def func_given(n):
    if n == 0 or n == 1:
        return n
    else:
        return func_given(n-1) + func_given(n-2)


# Fibonacci function with memoization
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n ==0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

""""
5) It looks like O(n) = O(n-1) + O(n-2) + O(1),
however with memorization the O is going to be O(n)
"""

# Create lists to store timing results
original_timings = []
improved_timings = []

for n in range(36):
    original_time = timeit.timeit(lambda: func_given(n), number=1)
    improved_time = timeit.timeit(lambda: fib_memo(n), number=1)
    original_timings.append(original_time)
    improved_timings.append(improved_time)

# Plot the results
plt.plot(range(36), original_timings, label="Original")
plt.xlabel("Input (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.title("Execution Time (Without Memorization)")
plt.savefig("ex1.6.1.jpg")

# Clear the figure
plt.clf()

# Plot the results for larger n values (0 to 35)
plt.plot(range(36), improved_timings, label="Improved (Memoization)")
plt.xlabel("Input (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.title("Execution Time (With Memorization)")
plt.savefig("ex1.6.2.jpg")