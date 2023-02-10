def triangle(num):
    for i in range(num+1,0,-1):
        for j in range(1,i):
            print("*",end=" ")
        print()
