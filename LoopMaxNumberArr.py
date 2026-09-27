y = int(input("Enter the amount of numbers you want to enter into the program : "))
myarray = [0]*y
highest = 0
secondhighest = 0
for x in range(y):
    myarray[x] = float(input("Enter your number | "))
    
for z in range(y):
    if(highest<myarray[z]):
        secondhighest = highest
        highest = myarray[z]
    elif(secondhighest<myarray[z]):
        secondhighest = myarray[z]

            
print(myarray)
print("The greatest number is", highest, "and the second greatest is", secondhighest)


