def min_of_three(n1, n2, n3):
    if(n1<n2):
        if(n1<n3):
            return n1
        else:
            return n3
    elif(n2<n3):
        return n2
    elif(n1==n2 and n2==n3):
        return 0
    else: 
        return n3

print("This program will have you enter 3 numbers and will (hopefully) return the smallest number back.")


var1 = float(input("Enter your first number. "))
var2 = float(input("Enter your second number. "))
var3 = float(input("Enter your third and final number. "))

ans = min_of_three(var1, var2, var3)

if(ans!=0):
    print(ans, "is the smallest number")
else:
    print("All numbers are equal.")
