#Write a program to calulate factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
num = int(input("Enter a number:"))
#checking if the number is negative or positive.
if num<0:
    print("Factorial is not defined for negative numbers. ")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ",num,"is",factorial(num))