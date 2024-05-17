# # WAP to sum of series 1^2 + 1/2^2 _ _ _ _ _ +1/n^2.


def sum_series(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / (i ** 2)
    return result 
def main():
    n = int(input("Enter the value of n: "))
    if n <= 0:
        print("Please enter a positive number.")
        return
    series_sum = sum_series(n) 
    print("Sum of the series is:", series_sum)  
if __name__ == "__main__":  
    main() 
