y = int(input("Enter the amount of numbers you want to enter into the program. "))
myarray = [0]*y
flag = False
for x in range(y):

    var1 = float(input("Enter your number | "))

    if(x==0):
        myarray[x] = var1
    else:
        index = 0
        flag = False

        while (flag == False) and (index<x):
            if(myarray[index]>var1):
                flag = True
                LoopEnd = index
            index += 1

        if(flag == True):
            print(LoopEnd)
            for i in range(x,LoopEnd,-1):
                myarray[i] = myarray[i-1]
                print(myarray)
            
            myarray[LoopEnd] = var1

        else:
            myarray[x] = var1

            
    
    print(myarray)