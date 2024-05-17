#Write a program to append a text in existing file.

f = open("file.txt", "w")

f.write("Hello king ")
f.close()

file = open("file.txt", "a")
file.write("How are you?")

file.close()
print("File appended successfully!")