#Write a  programt to calculate power (x, n).


def power (x, n):
    result = 1
    for i in range (n):
        result *= x
    return result

x = float(input("Enter base of (x): "))
n = int(input("Enter exponent of (n): "))
result = power(x,n)
print(f"{x} raised to the power {n} is : ",result)

