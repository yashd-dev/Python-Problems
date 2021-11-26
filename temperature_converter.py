'''You are responsible for writing a program that will convert a given temperature in degrees
Fahrenheit to degrees Celsius and degrees Kelvin. Your program will round all conversions to a
precision of four decimal places. Lastly, your program will display the results in a convenient
table style format.'''


print("Welcome to The Temperature Counter App ! \n")

tempf=float(input("Enter the Temperature in Fahrenheit: "))

tempc=round((tempf-32)*5/9,3)

tempk=tempc+273.5

print("Temperature in Celsius is {} \nTemperature in Kelvin is {}".format(tempc,tempk))