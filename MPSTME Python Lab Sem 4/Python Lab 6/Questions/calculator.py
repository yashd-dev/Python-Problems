'''
Develop a module named calculator.py in Python, which contain two function 
factorial(n) : to find factorial of a number, 
Fibonacci(n): to find Fibonacci series up to given number, n. 
Perform following tasks: 
a) Import the developed module 
b) call the functions available in the module 
i) to generate Fibonacci series upto a number, and 
ii) to determine factorial of a number entered by user

'''

def fibonacci(n):
    num1=0
    num2=1
    summ=0
    for i in range(n):
        print(num1,end=" ")
        summ=num1+num2
        num2=num1
        num1=summ

def factorial(num):
    prod = 1
    for i in range(1, num+1):
        prod = prod*i
    return prod
    