#Q9) Write a program to convert decimal to binary, octal to hexadecimal.
def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num)[2:]
    return binary_num

def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    hexadecimal_num = hex(decimal_num)[2:].upper()
    return hexadecimal_num

# Decimal to Binary Conversion
decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"Binary equivalent: {binary_output}")

# Octal to Hexadecimal Conversion
octal_input = input("Enter an octal number: ")
hexadecimal_output = octal_to_hexadecimal(octal_input)
print(f"Hexadecimal equivalent: {hexadecimal_output}")