#Basic email slicer
print("Welcome to this email Slicer")

var=input("Enter your email id: ").strip() #to input the email id and strip() is used to remove extra spaces

user=var[0:var.index("@")]  #Splitting values from start till @ 
dom=var[var.index("@")+1 : ] #Splitting valuie from charracter after @ till the end

print("Your Username is "+user)

print("Your domain is "+dom)