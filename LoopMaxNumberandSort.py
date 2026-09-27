def sort(a:int, arr:list):
    for x in range(a):
        for y in range(a-1):
            if(arr[y]<arr[y+1]):
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp

y = int(input("Enter the amount of numbers you want to enter into the program. "))
myarray = [0]*y
high = 0
secondhigh = 1
for x in range(y):

    myarray[x] = float(input("Enter your number | "))

    for z in range(y-1):
        if(myarray[high]<myarray[z+1]):
            secondhigh = high
            high = z+1
        elif(myarray[secondhigh]<myarray[z+1]):
            secondhigh = z+1

print("The greatest number is", myarray[high], "and the second greatest is", myarray[secondhigh])

sort(y, myarray)

print(myarray)


