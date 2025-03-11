try:
    number = int(input("Enter a number to find its factorial: "))

    # Check if the number is negative, zero, or positive
    if number < 0:
        print("Factorial does not exist for negative numbers.")
    elif number == 0 or number == 1:
        print(f"The factorial of {number} is 1.")
    else:
        fact = 1
        for i in range(2, number + 1):
            fact *= i
        print(f"The factorial of {number} is {fact}.")
except ValueError:
    print("Please enter a valid integer.")
