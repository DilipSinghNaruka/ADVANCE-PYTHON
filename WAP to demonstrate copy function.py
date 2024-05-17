#Write a program to demonstrate copy function 1.


# Opening the file in write mode (lowercase 'w')
f = open("file.txt", "w")

f.write("Hello Avinash")
f.close()

# Using a try-except block for error handling
try:
    with open("file.txt") as f2:
        with open("file1.txt", "w") as f3:
            for line in f2:
                f3.write(line)

    print("File has been copied!")

except FileNotFoundError:
    print("File is not available")

finally:
    if 'f2' in locals() and not f2.closed:
        f2.close()
        print("File closed")
