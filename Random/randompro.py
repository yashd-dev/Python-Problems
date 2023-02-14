#This is a random number guesser game, idea taken from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
#This is made by Yash D , https://github.com/yashd-dev
import random
import sys

while True:
     num=random.randint(1,30)
     print("Welcome To My Random Number Guessing Game from 1 to 30")
     c=0
     while True:
     
          print("Enter a value ")
          if c==4:
               if num%2==0:
                    print("Hint the above number is a Even Number")
               else:
                    print("Hint the above number is a Odd Number")

          user=int(input())
          if user==num:
               print("Congratulations you got it correct in "+str(c)+" tries")
               print("Do You Wish to continue? Y for yes and N for no")
               inp=input()
               if(inp=="Y" or inp=="y"):
                    break
               elif(inp=="N" or inp=="n"):
                    print("Thank You For Playing 😁")
                    sys.exit()
                    
               else:
                    print("Incorrect Value Has been entered😒,Terminating program")
                    sys.exit()
                   
          elif user<num:
               print("Incorrect value🙄🙄,you have predicted the number lower than whats given")
               c=c+1
          elif user>num:
               print("Incorrect value🙄🙄,you have predicted the number higher than whats given")
               c=c+1



