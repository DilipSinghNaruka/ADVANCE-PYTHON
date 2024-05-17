#implementing real time/ technical application using exception handling(divide by zero error, veteran age validity).


# Function to calculate division with error handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Function to check if a person is a veteran (age must be at least 18 to join the military)
def is_veteran(age):
    if not isinstance(age, (int, float)):
        raise ValueError("Age must be a numeric value.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age >= 18

# Testing divide-by-zero exception handling
print("Testing divide-by-zero:")
result = safe_divide(10, 2)  # Valid division
print("10 divided by 2 is:", result)

result = safe_divide(10, 0)  # Division by zero
print("10 divided by 0 is:", result)

# Testing veteran age validity with exception handling
def check_veteran_status(age):
    try:
        if is_veteran(age):
            return "The person is eligible to be a veteran."
        else:
            return "The person is not eligible to be a veteran."
    except ValueError as ve:
        return f"Error: {ve}"

print("\nTesting age validation:")
print("Checking if 25-year-old is a veteran:", check_veteran_status(25))
print("Checking if 17-year-old is a veteran:", check_veteran_status(17))
print("Checking if -5-year-old is a veteran:", check_veteran_status(-5))
print("Checking if 'thirty' is a veteran:", check_veteran_status("thirty"))
