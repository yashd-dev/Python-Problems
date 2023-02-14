'''You are responsible for writing a program that will convert a given temperature in degrees
Fahrenheit to degrees Celsius and degrees Kelvin. Your program will round all conversions to a
precision of four decimal places. Lastly, your program will display the results in a convenient
table style format.'''

#Printing Welcome Statement
print("Welcome to The Temperature Counter App ! \n")

tempf=float(input("Enter the Temperature in Fahrenheit: "))
#Getting usr input
tempc=round((tempf-32)*5/9,3)
#Calculations
tempk=tempc+273.5
#Printing output
print("Temperature in Celsius is {} \nTemperature in Kelvin is {}".format(tempc,tempk))
