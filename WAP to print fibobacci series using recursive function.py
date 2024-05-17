#WAP to print fibobacci series using recursive function



def fibonacci_recusive(n):
    if n<=1:
        return n
    else:
        return fibonacci_recusive(n-1)+ fibonacci_recusive(n-2)
terms=int(input("Enter the number :"))

#checking if the numberof terms is valid.
if terms<=0:
    print("Please enter a postive integer.")
else:
    print("Fibonacci series: ")
    for i in range(terms):
        print(fibonacci_recusive(i), end= " ")
    