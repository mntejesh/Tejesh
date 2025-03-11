try:
    n = int(input("Enter the number of n for the Fibonacci series: "))
    if n <= 0:
        print("Number of n must be a positive integer.") 
    elif n == 1:
        print(0)
    elif n == 2:
        print(0, 1)
    else:
        series = [0, 1]
        for i in range(2, n):
            series.append(series[-1] + series[-2])
            
    print(f"The Fibonacci series with {n} n is: {series}")
except ValueError:
    print("Please enter a valid integer.")
