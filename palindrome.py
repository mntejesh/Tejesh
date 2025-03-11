def count_digits(num):
    try:
        num = abs(int(num))  # Ensure the number is positive
        return len(str(num))
    except ValueError:
        return "Invalid input. Please enter a valid integer."

def is_palindrome(num):
    try:
        num = int(num)
        original_num = str(num)
        reversed_num = original_num[::-1]
        return original_num == reversed_num
    except ValueError:
        return "Invalid input. Please enter a valid integer."

def main():
    # Input from the user
    try:
        number = int(input("Enter a number: "))
        digit_count = count_digits(number)
        print(f"The number {number} has {digit_count} digits.")
        if is_palindrome(number):
            print(f"The number {number} is a palindrome.")
        else:
            print(f"The number {number} is not a palindrome.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
