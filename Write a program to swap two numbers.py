#Q5) Write a program to swap two numbers.
def swap_numbers(a, b):
    print("Before swapping:")
    print("a =", a)
    print("b =", b)

    # Swapping logic using a temporary variable
    temp = a
    a = b
    b = temp

    print("\nAfter swapping:")
    print("a =", a)
    print("b =", b)


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function to swap the numbers
swap_numbers(num1, num2)
