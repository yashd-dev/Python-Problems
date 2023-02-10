"""1
Develop a module called math_details. This module should have different functions for 
Calculating Permutation and combinations
Factorial of a number 
Armstrong Number 
Reverse of a number. 
"""
from maths_details import *
from calculator import *

facto = factorial(int(input("Enter A NUmber to find its factorial ")))
print("The facto is ", facto)

if armstrong(int(input("Enter a Number to check for Armstrong"))):
    print("It is a armstrong")
else:
    print("It is not armstrong")

print(permutation(1, 2))
print(combination(5, 9))

fibonacci(10)
