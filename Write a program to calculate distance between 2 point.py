#Q6) Write a program to calculate distance between 2 point.
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Prompt the user to enter coordinates of two points
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate distance between the two points
distance = calculate_distance(x1, y1, x2, y2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}.")
