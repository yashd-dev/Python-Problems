'''You are responsible for writing a program that will calculate the hypotenuse and area of a right
triangle given its two bases. Your program will round all calculations to a precision of three
decimal places and provide a summary of the mathematical results.'''

# Importing math function
import math
#Printing Welcome Statement
print("Welcome to the Right Triangle Solver App")
#Getting usr input
sidea=float(input("Enter the first leg of triangle: "))
sideb=float(input("Enter the second leg of triangle: "))
# Calculations
sidec=round(math.sqrt((sidea**2)+(sideb**2)),3) # For Hypotenuse
area=round(0.5*sidea*sideb,3) # For Area
#
print(f"For the given triangle of sides {sidea} & {sideb}, the Hypotenuse is {sidec} and Area is {area}")


