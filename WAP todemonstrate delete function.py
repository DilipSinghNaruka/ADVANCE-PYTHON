#Wrtie a program to demonstrate delete function.

import os

# Check if the file exists
if os.path.exists("file.txt"):  
    os.remove("file.txt")  
    print("Deleted successfully!")  
else:  
    print("File not available")  
