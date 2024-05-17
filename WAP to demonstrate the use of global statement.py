# Write a program to demonstrate the use of global statement.



global_var = 10
def modify_global():
    global global_var 
    global_var = 20  

def print_global():
    print("Global variable inside function:", global_var)  

print("Global variable before modification:", global_var)
modify_global()

print("Global variable after modification:", global_var)

print_global();;;

