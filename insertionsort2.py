y = int(input("Enter the amount of numbers you want to enter into the program. "))
myarray = [0]*y

for z in range(y):
    myarray[z] = float(input("Enter your number | "))

for x in range(1,y):
    var1 = myarray[x]
    j = x-1
    while j >= 0 and myarray[j] > var1:
        myarray[j+1] = myarray[j]
        j -= 1
    myarray[j+1] = var1

    
print(myarray)