#Q) Write a program to print the sum the series 1+1/2 _ _ _ _ _ +1/n.



n = int (input("Enter the number of terms :" ))
sum1 = 0
for i in range(1, n+1):
    sum1 = sum1 + (1/i)

    print("The sum of series is ", round(sum1,2))