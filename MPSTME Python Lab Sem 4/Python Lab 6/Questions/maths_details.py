'''
Develop a module called math_details. This module should have different functions
for
Calculating Permutation and combinations
Factorial of a number
Armstrong Number
Reverse of a number
'''
def factorial(num):
    prod = 1
    for i in range(1, num+1):
        prod = prod*i
    return prod


def permutation(r, n):
    return (factorial(n)//factorial(n-r))


def combination(r, n):
    return (factorial(n)//(factorial(r)*factorial(n-r)))


def armstrong(num):
    prod = 0
    temp = num
    while num != 0:
        digit = num % 10
        prod += digit**3
        num //= 10
    if temp == prod:
        return True
    else:
        return False


