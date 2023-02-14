''' You are responsible for writing a program that will convert any given speed in miles per hour to
a more metric friendly unit of meters per second. All calculations should be rounded to a set
decimal precision of 2 decimal places.'''

#Printing Welcome Statement
print("Welcome to The Miles Per Hour to Kilometer Per Hour or Meter Per Seconds and  Counter App ! \n")
#Getting usr input
choice=int(input("Enter 1 to Convert The Miles Per Hour to Kilometer Per Hour \nEnter 2 to Convert Miles Per Hour to Meter Per Seconds \n"))
# Calculations & Printing̥
if choice==1:
    miles=int(input("Enter Speed in Miles: "))
    kilometers=round(miles*1.60,2)
    print("{} mph = {} km/h ".format(miles,kilometers))
elif choice==2:
    miles=int(input("Enter Speed in Miles: "))
    meters=round(miles*0.447,2)
    print("{} mph = {} m/s ".format(miles,meters))
else:
    print("Wrong Value entered, please try again")