# 1. Write a function that gets an amount as input and returns that amount increased by 20%.
# def func_20_percent(amount):
#     increased = 20/100*amount
#     return amount + increased
#
# print(func_20_percent(10))

# 2. Write a function that gets a value for x as input and returns the value in x
# of the function f(x) = x^3 − 3x^2 + 7x − 6

# def func(value):
#     return value**3 - 3*value**2 + 7*value - 6
# (a) Evaluate the above function for the values 0, 1, 4, -3.
# print(func(0))
# print(func(1))
# print(func(4))
# print(func(-3))

# 3. Write a function that gets a value for x as input and returns the value in x of the function
import math
import numpy
def func(x):
    return (numpy.cbrt(x**2 - 5*x) - (math.sqrt((1 - x**3 + 2*x**2) / (3*x**2 - 1)) ** (1/5)))

# (a) Evaluate the above function for the values -2, 1, 75, 3.
print(func(-2))

