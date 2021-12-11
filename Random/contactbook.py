`#This is a Comandline python contact book with MongoDb as its Backend Storage for the contacts
import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/") #

mydb = myclient["Contacts"]  #Making the Database

mycol=mydb["Users"]  #Name of the collections inside the Contacts database


#Contents of the database
mylist=[{"Name":"Suresh","Phone No":"1473529684"},
{"Name":"Hola","Phone No":"9182763198"},
{"Name":"Raju","Phone No":"6483029354"},
{"Name":"Hodda","Phone No":"1475369524"},
{"Name":"Himesh","Phone No":"5793549635"},
{"Name":"Kunal","Phone No":"5279374512"},
{"Name":"Kalam","Phone No":"2654793514"},
{"Name":"Sachin","Phone No":"1756314789"},
]

# mydoc=mycol.insert_many(mylist)  Run this only once on a new device   

print("Welcome TO my Comandline contact book")
condition=True

while condition==True: #for continuous opperaton of the program

  #Now performing CRUD(Create,Read,Update,Delete) operations
  print("To Find any contacts press 1\n")
  print("To Add any contacts press 2\n")
  print("To Delete any contacts press 3\n")
  print("To Change any contacts press 4\n")#This function is still work in progress
  print("To exit , enter any key\n")

  var=int(input("Enter your choice: "))

  if var==1:
    print("You can Find here contacts\n")
    print("To view contacts name in Ascending order press 1\n")
    print("To view contacts name in Decending order press 2\n")
    print("To get any Phone Number Enter 3\n") 
    va=int(input("Enter your choice: "))
    if va==1:
      mydoc = mycol.find({}, {'_id': False}).sort("Name", 1) #
      for x in mydoc:
        print(x)
    elif va==2:
      mydoc = mycol.find({}, {'_id': False}).sort("Name", -1)
      for x in mydoc:
        print(x)
    elif va==3:
      name=input("Enter name to search ")
      name=name.capitalize()
      print(name)
      mydoc=mycol.find( { "Name": {"$regex": name } } ,{'_id': False}) 
      for x in mydoc:
        print(x)

  elif var==2:
    name=input("Enter the name to add in the contact book: ").capitalize()
    phoneno=input("Enter the phone of that person to add in the contact book: ")
    mydoc=mycol.insert_one({"Name": name , "Phone No" : phoneno})
    mydoc = mycol.find({}, {'_id': False}).sort("Name", -1)
    for x in mydoc:
      print(x)

  elif var==3:
    try:
      name=input("Enter name of the contact to delete : ").capitalize()
      phoneno=input("Enter Phone Number of the contact to delete : ")
      mydoc=mycol.delete_one({"Name" : name , "Phone No": phoneno})
      mydoc = mycol.find({}, {'_id': False}).sort("Name", -1)
      for x in mydoc:
        print(x)
    except:
      print("Error occured: Values entered by you are not matching with values in contact book")

  else :
    print("Thank you for using this program")
    sys.exit()

  choice=input("Do you wish to continue ? press enter for yes or any other key for no" )
  if(choice==' '):
    print("Thank you for using this program")
    sys.exit()

  


   








    


