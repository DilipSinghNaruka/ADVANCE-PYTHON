#Write a program to calculate addition, subtraction by using lambda function.

#define lambda fuction for add and sub.
add=lambda x,y: x+y
sub=lambda x,y: x-y

num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
print("Addition: ",add(num1,num2))
print("Subtraction: ",sub(num1,num2))