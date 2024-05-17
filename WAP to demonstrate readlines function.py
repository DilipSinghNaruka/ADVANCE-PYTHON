#Write a program to demonstrate readlines function.

# Open the file in write mode
with open("file.txt", "w") as f:
    f.write("Hello avinash")

# Open the file in read mode
with open("file.txt", "r") as f:
    print(f.read(10))
    
    f.seek(0)  
    print(f.readlines())

print("File read successfully!")
