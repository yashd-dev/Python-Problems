import itertools # For easily getting all the permutations 
c2=0
print("Welcome to my 4=10 Solver!\n")
while 1:
    if c2!=0:
        ask=input("\nDo You wish to continue y/n? ")
        if (ask.lower()).strip()=="y":
            pass
        elif (ask.lower()).strip()=="n":
            print("Thank You for Using My App :)")
            break
        else:
            print("Input other than yes detected, exiting...\n\nThank You for Using My App :)")
            break
    c2=0
    while 1:
        c3=0
        inp=input("Plesae Enter 4 Numbers in the following manner: 1 2 3 4\n")
        nums = inp.split()
        if len(nums)==4:
            for i in nums:
                if len(i)==1 and i.isdigit():
                    pass
                else:
                    c3+=1
            if c3>0:
                print("\nEnter single digit numbers only, Restaring...")
            else:
                break
            
        else:
            print("\nPlease enter 4 numbers only, Restarting...")

    operators = ['+', '-', '*', '/']
    list_operator = list(itertools.product(operators, repeat = 3))
    list_numbers = list(itertools.permutations(nums)) # Permutations are arrangements of things that preserve the order.
    for n in list_numbers:
        for o in list_operator:

            eq=''
            for i in range(len(n)-1):
                eq+=n[i]+o[i]
            eq+=n[-1]
            try:
                solution=eval(eq)
            except:
                pass
            if solution==10:
                print(f"{eq}=10")
                c2+=1
                break  
        if c2>=5:
            break
    if c2==0:
        print("No Posible Solutions are Found :(\n")
        ask=input("Do You wish to continue y/n? ")
        if ask.lower()=="y":
            pass
        elif ask.lower()=="n":
            print("\nThank You for Using My App :)")
            break
        else:
            print("\nInput other than yes detected, exiting...\nThank You for Using My App :)")
            break
