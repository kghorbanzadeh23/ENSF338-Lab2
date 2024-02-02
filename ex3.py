import timeit
import cProfile
import re
def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data
def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

def main():
    test_function()
    third_function()


cProfile.run('main()')


#1. A profile is a set of statistics that describe how often and for how long various parts of the program executed.

#2. A profile is to describe how the program behaviour is while a benchmark you are looking at one thing and seeing how effecient it is.

#3. 23.558

#4. Execution time goes to mostly the list comprehension in third_function() taking 23.062.
#And then main function where it took 0.495