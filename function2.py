msg = "Greatest is; "

def max_of_three(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>c):
        return b
    elif(a==b and b==c):
        return 0
    else:
        return c

num1 = float(input("Enter a number. "))
num2 = float(input("Enter a second number. "))
num3 = float(input("Enter a third number. "))
ans = max_of_three(num1, num2, num3)

if(ans==0):
    print("All are Equal")
else:
    print(msg, ans)