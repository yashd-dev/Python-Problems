'''You are responsible for writing a program that displays a multiplication table and exponentiation
table for any given number. Each table should show mathematical results for operations
performed with the given number and integers from 1 to 9. The program will then print a series
of messages to the user describing how cool mathematics truly is.'''
#Printing Welcome Statement
print("Welcome to The Multiplication/Exponent Table App!\n")

#Taking usr input 
name=input("Enter Your Name: ").title().strip() 

num=float(input(f"Welcome {name} what number would you like to work with: "))

#Calculations and Printing
print(f"Multiplication Table for {num}")

x=1

while x <= 10:
    ans=round(x*num,3)
    print(f"\t {x} * {num} = {ans}")
    x=x+1
    
y=1
print(f"Exponential Table for {num}")
while y <= 10:
    ans=round(num**y,3)
    print(f"\t {y} ^ {num} = {ans}")
    y=y+1
