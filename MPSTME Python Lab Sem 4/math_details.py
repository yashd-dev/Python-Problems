'''
Develop a module called math_details. This module should have different functions
for
Calculating Permutation and combinations
Factorial of a number
Armstrong Number
Reverse of a number
'''
import math

def factorial(num):
    prod = 1
    if type(num) is int:
        for i in range(1, num+1):
            prod = prod*i
        return prod
    else:
        print("Enter a Integer please! ")
        raise Exception


def permutation(n,k):
    if n>0 and k >0 and type(n) is int and type(k) is int:
        return (math.perm(n,k))
    else:
        raise Exception
        

def combination(n, k):
    if n>0 and k >0 and type(n) is int and type(k) is int:
        return (math.comb(n,k))
    else:
        raise Exception 


def armstrong(num):
    if type (num) is int:
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
    else:
        raise Exception


if __name__ == "__main__":
    facto = factorial(int(input("Enter A Number to find its factorial ")))
    print("The factorial is ", facto)
    if armstrong(int(input("Enter a Number to check for Armstrong"))):
        print("It is a armstrong")
    else:
        print("It is not a armstrong")
    print(permutation(1,2))
    print(combination(5,9))
