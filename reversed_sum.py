try:
    num = int(input("Enter the numbers:"))
    if num>0 :
        reversed_num= int(str(abs(num))[::-1])
        print(reversed_num)
    else :
        reversed_num= -(int(str(abs(num))[::-1]))
        print(reversed_num)

    print(f"The reverse of {num} is {reversed_num}.")
except ValueError:
    print("Please enter a valid integer.")

