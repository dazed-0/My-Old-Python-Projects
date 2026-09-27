def calculator(n1, n2, opt):
    if(opt=="+"):
        return n1+n2
    elif(opt=="-"):
        return n1-n2
    elif(opt=="/"):
        return n1/n2
    elif(opt=="*"):
        return n1*n2
    else:
        return "Err"

num1 = float(input("Input the first number "))
num2 = float(input("Input the second number "))
operator = str(input("Enter operator "))

if("Err"==(calculator(num1, num2, operator))):
    print("Invalid Operator.")
else:
    print("The answer is:", calculator(num1, num2, operator))

msg = "Greatest is; "

def max_of_three(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>c):
        return b
    else:
        return c

num1 = float(input("Enter a number. "))
num2 = float(input("Enter a second number. "))
num3 = float(input("Enter a third number. "))
ans = max_of_three(num1, num2, num3)

print(msg, ans)