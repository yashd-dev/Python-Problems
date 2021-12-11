#Simple python script for a comandline rolling dice
import random
import sys
from tqdm import tqdm
print("Welcome to the rolling dice simulator\n")
var=""
while var=="":
    num=random.randint(1,6)
    print("The dice is currently rolling\n")
    for i in tqdm (range (10), desc="Loading..."):
        pass
    print("The dice has presents the number: "+str(num)+"\n")
    var=input("To continue just press enter")
    var=var.strip()
    print("\n")
    if var != "" :
        print("Thankyou for using this program")
        sys.exit()
        
